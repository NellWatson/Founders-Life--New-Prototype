init python:
    check = {
        "energy": "",
        "morale": "",
        "money": "",
        "confirm": False,
    }

    new_events_pool = {
        9999: ["ux_research", "equity", "beta"],
        1: ["cloud", "day_one_pr", "conference", "key_messaging", "premature_launch"],
        2: ["nda", "micro_managing"]
    }

    events_pool = {
        1: ["pr_vs_development", "hire_more", "late_night_sprint", "holiday", "bad_ui", "testing"],
        2: ["nda"]
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

    def startup_development(amount):
        if amount < 0:
            store.development -= amount

        mod = morale * 0.015
        store.development += (amount * dev_employees * mod)

    def startup_pr(amount):
        if amount < 0:
            store.pr -= amount
            
        mod = morale * 0.015
        store.pr += (amount * pr_employees * mod)

    def move_employees(old, new, number=1):
        old_dept = getattr(store, old)
        new_dept = getattr(store, new)

        # Check if there are emplyees in the department
        if old_dept <= 0:
            return

        setattr(store, old, old_dept-1)
        setattr(store, new, new_dept-1)

    def weekly_deductions():
        store.money -= (pr_employees + dev_employees + testing_employees) * 80 * 6
        store.energy += 10
        store.morale += 10

    def find_event():
        return renpy.random.choice( events_pool[founder_level] )

    def can_upgrade_startup():
        next_level = FOUNDER_INDEX[ founder_level + 1 ]

        if development < next_level["dev"] or pr < next_level["pr"] or testing < next_level["testing"]:
            return

        store.founder_level += 1
        renpy.call_screen("level_up", bg="bg lounge")
