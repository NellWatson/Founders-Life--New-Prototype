init python:

    def normalise_event_text(txt):
        return txt.replace("#NAME", store.founder_name).replace("#PLAYER:", "").replace("#MONEY_MONTH", money_manager.get_monthly_earning()).split("::")[-1]
    normalise = normalise_event_text

    class Event():

        def __init__(self, id, title, category, character, description, yes_action, no_action={}, yes_caption="Yes", no_caption="No", yes_description={}, no_description={}, condition=[], play_on=0, play_after="", bg=None, repeatable=False, version="1"):
            self.id = id
            self.title = title
            self.category = category
            self.character = characters_roster.get_character_object(character)
            self.condition = condition
            self._description = description
            self.yes_action = yes_action
            self.no_action = no_action
            self.yes_caption = yes_caption
            self.no_caption = no_caption
            self._yes_description = yes_description
            self._no_description = no_description
            self.play_on = play_on
            self.play_after = play_after
            self.bg = bg
            self.version = version
            self.repeatable = repeatable

            self.seen_on_day = -1
            self.chose_action = None
            self.last_description_no = -1
            self.choice_last_description_no = -1

            self.current_language = "en"
            self.positive_kpi = []
            self.negative_kpi = []

            self.positive_lean = 0
            self.negative_lean = 0

            self.determine_event_lean()

        def determine_event_lean(self):
            for name, value in self.yes_action.items():
                if value > 0:
                    if name in self.no_action:
                        self.positive_kpi.append(name)
                    self.positive_lean += 1
                elif value < 0:
                    if name in self.no_action:
                        self.negative_kpi.append(name)
                    self.positive_lean -= 1

            for name, value in self.no_action.items():
                if value > 0:
                    self.negative_lean += 1
                elif value < 0:
                    self.negative_lean += 1

        def mark_as_seen(self):
            self.seen_on_day = store.turn_no

        def run_action(self, action_list):
            self.mark_as_seen()
            for name, value in action_list.items():
                if "affection" in name:
                    if ":" in name:
                        character, affection = name.split(":")
                        characters_roster.update_affection(character, value)
                    else:
                        self.character.affection += value
                else:
                    if name == "mindfulness":
                        name = "morale"
                    variable(name, value)

            store.choice_effects = {}

        @property
        def overall_lean(self):
            return self.positive_lean - self.negative_lean
        
        @property
        def can_run(self):
            if self.play_on and self.play_on != store.turn_no:
                return False

            if self.has_seen:
                return False

            if not self.condition:
                return True

            for condition in self.condition:
                if meets_condition(*condition):
                    continue
                return False
            return True

        @property
        def yes(self):
            self.chose_action = "yes"
            self.run_action(self.yes_action)
            if self.positive_lean > 0:
                chapter_manager.record_choice_lean(1)
            else:
                chapter_manager.record_choice_lean(0)

        @property
        def no(self):
            self.chose_action = "no"
            self.run_action(self.no_action)
            if self.negative_lean > 0:
                chapter_manager.record_choice_lean(-1)
            else:
                chapter_manager.record_choice_lean(0)

        @property
        def is_yes(self):
            return self.yes_action != {}

        @property
        def is_no(self):
            return self.no_action != {}

        @property
        def has_seen(self):
            if self.repeatable:
                return self.seen_on_day > -1 and int(self.seen_on_day / 7) == int(store.turn_no / 7)
            else:
                return self.seen_on_day > -1

        @property
        def get_speaker(self):
            if not self.chose_action:
                current_description_no = self.last_description_no + 1
                description_list = self._description[self.current_language]
            else:
                if not self._yes_description and not self._no_description:
                    return self.character.get_character_object
                current_description_no = self.choice_last_description_no + 1
                if self.chose_action == "yes":
                    description_list = self._yes_description[self.current_language]
                if self.chose_action == "no":
                    description_list = self._no_description[self.current_language]

            if current_description_no == len(description_list):
                current_description_no -= 1

            if "#PLAYER:" in description_list[current_description_no]:
                return characters_roster.get_character_object("none").get_character_object
            else:
                if "::" in description_list[current_description_no]:
                    _char = description_list[current_description_no].split("::")[0]
                    return characters_roster.get_character_object(_char).get_character_object

                return self.character.get_character_object

        @property
        def description(self):
            self.last_description_no += 1
            return normalise(self._description[self.current_language][self.last_description_no])

        @property
        def last_description(self):
            if self.has_multiple_descriptions:
                return "{cps=0}" + normalise(self._description[self.current_language][-1]) + "{/cps}"
            else:
                return normalise(self._description[self.current_language][-1])

        @property
        def has_multiple_descriptions(self):
            return len(self._description[self.current_language]) > 1

        @property
        def seeing_last_description(self):
            return self.last_description_no + 1 == len(self._description[self.current_language])

        @property
        def choice_have_description(self):
            if self.chose_action == "yes":
                if self.current_language not in self._yes_description:
                    return False
                return len(self._yes_description[self.current_language])

            elif self.chose_action == "no":
                if self.current_language not in self._no_description:
                    return False
                return len(self._no_description[self.current_language])

        @property
        def choice_description(self):
            return self.yes_description if self.chose_action == "yes" else self.no_description

        @property
        def yes_description(self):
            self.choice_last_description_no += 1
            if self.choice_last_description_no == len(self._yes_description[self.current_language]):
                self.choice_last_description_no -= 1
            return normalise(self._yes_description[self.current_language][self.choice_last_description_no])
        
        @property
        def no_description(self):
            self.choice_last_description_no += 1
            if self.choice_last_description_no == len(self._no_description[self.current_language]):
                self.choice_last_description_no -= 1
            return normalise(self._no_description[self.current_language][self.choice_last_description_no])

        @property
        def seeing_choice_last_description(self):
            if self.chose_action == "yes":
                return self.choice_last_description_no + 1 == len(self._yes_description[self.current_language])
            elif self.chose_action == "no":
                return self.choice_last_description_no + 1 == len(self._no_description[self.current_language])

    class EventManager():

        def __init__(self, id):
            self.id = id
            self.store = {}

            self.events_seen = 0
            self.all_categories = []
            self.last_event_category = None
            self.last_event_played = ""
            self.last_version = ""

            self.event_choices_lean = []

        def load(self, filepath, extra_index_file=None):
            file_list = load(filepath, "index")

            for file, version in file_list:
                data = load(filepath, file)
                if "title" not in data:
                    data["title"] = "No Title"

                if file not in self.store:
                    self.store[data["id"]] = Event(version=version, **data)

        def get_event(self, event):
            return self.store[event]

        @property
        def run_event(self):
            available_events = self.available_events_this_week
            if len(available_events) == 1:
                chosen_event = available_events[0]
            elif len(available_events) == 0:
                chosen_event = "chapter_default"
            else:
                if len(self.event_choices_lean) > 6:
                    last_seven_lean = sum(self.event_choices_lean[-7:])
                    final_events = []
                    
                    if last_seven_lean <= 0:
                        for i in available_events:
                            if self.store[i].overall_lean >= 0:
                                final_events.append(i)

                    if len(final_events):
                        available_events = final_events

                chosen_event = renpy.random.choice(available_events)
                self.last_event_played = chosen_event

            if config.developer:
                store.dev_option__event_play.append(chosen_event)
            return self.store[chosen_event]

        @property
        def available_events_this_week(self):
            _temp_list = []
            for id in self.store:
                # If any event needs to be played this turn, play it.
                # Also makes sure that if there are any conditions, they are satisfied.

                if id == "chapter_default":
                    continue

                if self.store[id].can_run:
                    if self.last_event_played and self.store[id].play_after == self.last_event_played:
                        return [id]

                    if self.store[id].play_on == store.turn_no:
                        return [id]
                    _temp_list.append(id)
            return _temp_list

    class ChapterManager():

        def __init__(self):
            self.current_chapter = ""
            self.store = {}

        def load_chapter(self, id, filepath):
            self.store[id] = EventManager(id)
            self.store[id].load(filepath)

        def set_chapter(self, chapter):
            self.current_chapter = chapter

        def get_event(self):
            return self.store[self.current_chapter].run_event

        def seen_event(self, chapter, event):
            return ( self.store[chapter].get_event(event).has_seen, self.store[chapter].get_event(event).chose_action )

        def record_choice_lean(self, value):
            self.store[self.current_chapter].event_choices_lean.append(value)
