init python:
    check = {
        "money": ""
    }

    def calculate_pool():
        top_level = [
            ("productivity", "03", "05"),
            ("energy", "02", "05"),
            ("morale", "03", "05"),
            ("money", "02", "06")
            ]
        mid_level = ["major", "minor"]
        low_level = ["01", "02", "03", "04", "05", "06"]

        for i, major_limit, minor_limit in top_level:
            events_pool[i] = []
            for j in mid_level:
                for k in low_level:
                    if j == "major" and k > major_limit:
                        break
                    elif j == "minor" and k > minor_limit:
                        break
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

        if (events_pool) > 1:
            # On turn 5 and 7 check if any event bucket hasn't been used yet
            if not turn_no % 5 or not turn_no % 7:
                if len(week_event_bucket_type) < 4:
                    _available_buckets = [i for i in _available_buckets if i not in week_event_bucket_type]
            else:
                # For regular days, just make sure that two types of events are not repeated
                if store.last_event_bucket:
                    _available_buckets.remove(last_event_bucket)

        # Remove empty buckets from the que
        _available_buckets = [ x for x in _available_buckets if x in events_pool ]

        current_bucket = renpy.random.choice(_available_buckets)
        week_event_bucket_type.add(current_bucket)
    
        event = renpy.random.choice( events_pool[current_bucket] )
        store.last_event_bucket = event.split("_")[0]
        events_pool[last_event_bucket].remove(event)

        # If the event pool for an event is empty, rmeove it
        if not events_pool[current_bucket]:
            del events_pool[current_bucket]

        renpy.sound.play("sfx/fx002.wav")

        return event
