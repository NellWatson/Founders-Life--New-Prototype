define character.n = Character("Nell", image="nell")
define character.c = Character("Carla", image="carla")
define character.d = Character("Dominique", image="dominique")
define character.e = Character("Eileen", image="eileen")
define character.ra = Character("Raquel", image="raquel")
define character.s = Character("Skylar", image="carla")
define character.t = Character("Takashi", image="raquel")
define character.r = Character("Roger", image="dominique")
define character.none = Character(image="none")

init python:

    class CharacterRooster():

        def __init__(self):
            self.store = {}

        def add_character(self, id, name, ch_obj, sprite):
            self.store[id] = SingleCharacter(id, name, ch_obj, sprite)

        def get_character_object(self, id):
            return self.store.get(id, None)

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
