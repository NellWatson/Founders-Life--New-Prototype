init python:

    class VarTracker():

        def __init__(self):
            self.store = {}
            self.final_value = {}

        def add_value(self, name, value):
            if name in self.store:
                self.store[name].append(value)
                self.final_value[name] += value
            else:
                self.store[name] = [value]
                self.final_value[name] = value

        def get_value(self, name):
            return sum(self.store[name])

        def get_modifier(self, name):
            if name not in self.store:
                return 1

            if sum(self.store[name]) >= 0:
                return (self.final_value[name] % 10 * 0.01) + 1
            else:
                return 1 - (self.final_value[name] % 10 * 0.01)

    check = {
        "money": ""
    }

    def variable(name, value, maximum=100):
        old_value = getattr(store, name)
        new_value = old_value + value

        if name != "money":
            modifier = var_tracker.get_modifier(name)
        else:
            modifier = 1

        new_value *= modifier

        if new_value > maximum and name != "money":
            new_value = maximum
        
        check["money"] = ""
        if name == "money":
            if value < 0:
                store.check[name] = "{color=#ff0000}$" + format(new_value, ",") + "{/color}"
            else:
                store.check[name] = "{color=#00ff00}$" + format(new_value, ",") + "{/color}"

        _final = int(new_value)
        setattr(store, name, _final)
        var_tracker.add_value(name, value)
