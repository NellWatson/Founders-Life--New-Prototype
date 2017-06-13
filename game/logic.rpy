init python:
    check = {
        "energy": "",
        "morale": "",
        "confirm": False,
    }

    events_pool = {
        9999: ["ux_research", "delegation", "beta"],
        1: ["cloud", "day_one_pr", "conference", "key_messaging", "premature_launch"],
        2: ["nda", "micro_managing", "tier_2_1"],
        3: ["tier_3_1", "tier_3_2"],
        4: ["tier_4_1", "tier_4_2"],
        5: ["tier_5_1", "tier_5_2"],
        6: ["tier_6_1", "tier_6_2"],
        7: ["tier_7_1", "tier_7_2"]
    }

    available_pool = {
        9999: ["ux_research", "delegation", "beta"],
        1: ["cloud", "day_one_pr", "conference", "key_messaging", "premature_launch"],
        2: ["nda", "micro_managing", "tier_2_1"],
        3: ["tier_3_1", "tier_3_2"],
        4: ["tier_4_1", "tier_4_2"],
        5: ["tier_5_1", "tier_5_2"],
        6: ["tier_6_1", "tier_6_2"],
        7: ["tier_7_1", "tier_7_2"]
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
        if not available_pool[founder_level]:
            available_pool[founder_level] = events_pool[founder_level]

        if not available_pool[9999]:
            available_pool[9999] = events_pool[9999]

        event = renpy.random.choice(available_pool[founder_level] + available_pool[9999])

        if event in available_pool[founder_level]:
            available_pool[founder_level].remove(event)
        elif event in available_pool[9999]:
            available_pool[9999].remove(event)

        return event
