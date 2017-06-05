init python:
    check = {
        "energy": "",
        "morale": "",
        "confirm": False,
    }

    events_pool = {
        9999: ["ux_research", "delegation", "equity", "beta"],
        1: ["cloud", "day_one_pr", "conference", "key_messaging", "premature_launch"],
        2: ["nda", "micro_managing"]
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

    def find_event():
        actual_pool = events_pool[founder_level] + events_pool[9999]
        return renpy.random.choice( events_pool[actual_pool] )
