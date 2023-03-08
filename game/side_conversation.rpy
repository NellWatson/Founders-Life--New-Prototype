init python:

    class SideConversation():

        def __init__(self, id, title, label, condition):
            self.id = id
            self.title = title
            self.label = label
            self.condition = condition

            self.has_seen = False

        def play(self):
            self.has_seen = True
            renpy.call_in_new_context(self.label)

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
            return True

    class SideConversationManager():

        def __init__(self):
            self.store = []

        def load(self, filepath="extra", filename="side_conversations"):
            sc_list = load(filepath, filename)

            for sc in sc_list:
                self.store.append(SideConversation(**sc))

        def find_and_play_event(self):
            for sc in self.store:
                if not sc.can_run:
                    continue
                
                sc.play()
                break
