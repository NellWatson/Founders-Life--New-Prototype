init python:
    check = {
        "energy": "",
        "morale": "",
        "confirm": False,
    }

    def calculate_pool():
        top_level = ["productivity", "energy", "morale", "money"]
        mid_level = ["major", "minor"]
        low_level = ["01", "02", "03", "04", "05"]

        for i in top_level:
            events_pool[i] = []
            for j in mid_level:
                for k in low_level:
                    events_pool[i].append( i + "_" + j + "_" + k )

    def variable(name, value, maximum=100):
        old_value = getattr(store, name)
        new_value = old_value + value
        if new_value > maximum:
            new_value = maximum
        
        if value < 0:
            store.check[name] = "{color=#ff0000}" + str(value) + "{/color}"
        else:
            store.check[name] = "{color=#00ff00}+" + str(value) + "{/color}"
        store.check["confirm"] = True

        setattr(store, name, new_value)

    def find_event():
        _available_buckets = events_pool.keys()

        if store.last_event_bucket:
            _available_buckets.remove(last_event_bucket)
        current_bucket = renpy.random.choice(_available_buckets)
    
        event = renpy.random.choice( events_pool[current_bucket] )
        store.last_event_bucket = event.split("_")[0]
        events_pool[last_event_bucket].remove(event)

        return event
