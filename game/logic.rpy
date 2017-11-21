init python:
    check = {
        "money": ""
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
        if new_value > maximum and name != "money":
            new_value = maximum
        
        check["money"] = ""
        if name == "money":
            if value < 0:
                store.check[name] = "{color=#ff0000}$" + format(new_value, ",") + "{/color}"
            else:
                store.check[name] = "{color=#00ff00}$" + format(new_value, ",") + "{/color}"

        setattr(store, name, new_value)

    def find_event():
        _available_buckets = events_pool.keys()

        # On turn 5 and 7 check if any event bucket hasn't been used yet
        if not turn_no % 5 or not turn_no % 7:
            if len(week_event_bucket_type) < 4:
                _available_buckets = [i for i in _available_buckets if i not in week_event_bucket_type]
        else:
            # For regular days, just make sure that two types of events are not repeated
            if store.last_event_bucket:
                _available_buckets.remove(last_event_bucket)

        current_bucket = renpy.random.choice(_available_buckets)
        week_event_bucket_type.add(current_bucket)
    
        event = renpy.random.choice( events_pool[current_bucket] )
        store.last_event_bucket = event.split("_")[0]
        events_pool[last_event_bucket].remove(event)

        return event
