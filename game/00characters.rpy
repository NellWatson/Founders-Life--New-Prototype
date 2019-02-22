define character.n = Character("Nell", image="nell")
define character.e = Character("Eileen", image="eileen")
define character.s = Character("Skylar", image="skylar")
define character.t = Character("Takashi", image="takashi")
define character.r = Character("Roger", image="roger")
define character.d = Character("Dominique")
define character.none = Character(image="none")

init python:

    class CharacterRooster():

        def __init__(self):
            self.store = {}

        def add_character(self, id, name, ch_obj, sprite):
            self.store[id] = SingleCharacter(id, name, ch_obj, sprite)

        def get_character_object(self, id):
            return self.store.get(id.lower(), None)

        def get_character_by_name(self, name, one=False, all=True):
            _all_objects = []

            for i in self.store.values():
                if i.name == name:
                    if one:
                        return i
                    _all_objects.append(i)
            return _all_objects

        def change_affection(self, id, by):
            self.store[id].affection += by

        def get_affection(self, id):
            return self.store[id].affection

        def update_affection(self, id, value):
            self.store[id].affection += value

    class SingleCharacter():

        def __init__(self, id, name, ch_obj, sprite):
            self.id = id
            self.name = name
            self.ch_obj = ch_obj
            self.sprite = sprite

            self.affection = 0

        @property
        def get_character_object(self):
            return getattr(character, self.ch_obj)
