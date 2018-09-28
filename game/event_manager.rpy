init python:

    class Event():

        def __init__(self, id, category, character, description, yes_action, no_action, yes_caption="Yes", no_caption="No", condition=[], play_on=0, repeatable=False, version="1"):
            self.id = id
            self.category = category
            self.character = characters_roster.get_character_object(character)
            self.condition = condition
            self._description = description
            self.yes_action = yes_action
            self.no_action = no_action
            self.yes_caption = yes_caption
            self.no_caption = no_caption
            self.play_on = play_on
            self.version = version
            self.repeatable = repeatable

            self.seen_on_day = -1
            self.chose_action = None
            self.last_description_no = -1

            self.current_language = "en"

        def mark_as_seen(self):
            self.seen_on_day = store.turn_no

        def run_action(self, action_list):
            self.mark_as_seen()
            for name, value in action_list.items():
                if name == "mindfulness":
                    name = "morale"
                if name == "affection":
                    self.character.affection += value
                else:
                    variable(name, value)

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

        @property
        def no(self):
            self.chose_action = "no"
            self.run_action(self.no_action)

        @property
        def has_seen(self):
            if self.repeatable:
                return self.seen_on_day > -1 and int(self.seen_on_day / 7) == int(store.turn_no / 7)
            else:
                return self.seen_on_day > -1

        @property
        def description(self):
            self.last_description_no += 1
            return self._description[self.current_language][self.last_description_no].replace("#NAME", store.founder_name)

        @property
        def last_description(self):
            return self._description[self.current_language][-1].replace("#NAME", store.founder_name)

        @property
        def has_multiple_description(self):
            return len(self._description[self.current_language]) > 1

        @property
        def seeing_last_description(self):
            return self.last_description_no + 1 == len(self._description[self.current_language])

    class EventManager():

        def __init__(self, id):
            self.id = id
            self.store = {}

            self.events_seen = 0
            self.all_categories = []
            self.last_event_category = None
            self.last_version = ""

        def load(self, filepath, extra_index_file=None):
            file_list = load(filepath, "index")

            for file, version in file_list:
                data = load(filepath, file)

                if file not in self.store:
                    self.store[file] = Event(version=version, **data)

        @property
        def run_event(self):
            available_events = self.available_events_this_week
            if len(available_events) == 1:
                chosen_event = available_events[0]
            else:
                chosen_event = renpy.random.choice(available_events)
            return self.store[chosen_event]

        @property
        def available_events_this_week(self):
            _temp_list = []
            for id in self.store:
                # If any event needs to be played this turn, play it.
                # Also makes sure that if there are any conditions, they are satisfied.
                if self.store[id].can_run:
                    if self.store[id].play_on-1 == store.turn_no:
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
