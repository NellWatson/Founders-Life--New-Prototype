init python:

    class Event():

        def __init__(self, id, category, character, condition, description, yes_action, no_action, version="1"):
            self.id = id
            self.category = category
            self.character = characters_roster.get_character_object(character)
            self.condition = condition
            self.description = description
            self.yes_action = yes_action
            self.no_action = no_action
            self.version = version

            self.seen_on_day = -1
            self.chose_action = None

        def mark_as_seen(self):
            self.seen_on_day = store.turn_no

        def run_action(self, action_list):
            self.mark_as_seen()
            for name, value in action_list.items():
                if name == "affection":
                    self.character.affection += value
                else:
                    variable(name, value)

        @property
        def can_run(self):
            if self.has_seen:
                return False

            if not self.condition:
                return True

            for condition in self.condition:
                if meets_condition(*condition):
                    continue
                return False

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
            return self.seen_on_day > -1

    class EventManager():

        def __init__(self, id):
            self.id = id
            self.store = {}

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
            print available_events

            if len(available_events) == 1:
                chosen_event = available_events[0]
            else:
                chosen_event = renpy.random.choice(self.available_events_this_week)
            return self.store[chosen_event]

        @property
        def available_events_this_week(self):
            _temp_list = []
            for id in self.store:
                if self.store[id].can_run:
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