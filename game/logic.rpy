init python:
    check = {
        "energy": "",
        "morale": "",
        "money": "",
        "confirm": False,
    }

    def variable(name, value):
        old_value = getattr(store, name)
        new_value = old_value + value
        
        if value < 0:
            store.check[name] = "{color=#ff0000}" + str(value) + "{/color}"
        else:
            store.check[name] = "{color=#00ff00}+" + str(value) + "{/color}"
        store.check["confirm"] = True

        setattr(store, name, new_value)

    def find_event(pool=["major_event", "minor_event"]):
        return renpy.random.choice(pool)
