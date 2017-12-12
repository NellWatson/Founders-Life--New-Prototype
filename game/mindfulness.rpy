label morale_major_01:
    $ event_code = "ch01e01"
    show player e at center
    menu:
        e "Danny is an incredible engineer but his arrogance and aloofness keeps the rest of the team. Fire him?"

        "$_YES":
            $ variable("productivity", -20)
            $ variable("energy", -10)
            $ variable("morale", 20)
            $ variable("money", 1000)

        "$_NO":
            $ variable("productivity", 20)
            $ variable("energy", 10)
            $ variable("morale", -20)

    jump checkpoint

label morale_major_02:
    $ event_code = "ch01e21"
    show player e at center
    menu:
        e "You are getting so much done today, that's the beauty of curating a no-distration environment. Cancel the team pizza lunch and continue the productivity streak?"

        "$_YES":
            $ variable("productivity", 20)
            $ variable("energy", -20)
            $ variable("morale", -20)

        "$_NO":
            $ variable("productivity", -20)
            $ variable("energy", 20)
            $ variable("morale", 20)

    jump checkpoint

label morale_major_03:
    $ event_code = "ch01e22"
    show player r at center
    menu:
        r "Hey, [founder_name], I know you enjoy your co-working space but a contact just told me of some great office space downtown going for $2,000 a month. Shall I prepare the lease?"

        "$_YES":
            $ variable("productivity", 20)
            $ variable("energy", 20)
            $ variable("morale", 20)
            $ variable("money", -2000)

        "$_NO":
            $ variable("productivity", -20)
            $ variable("energy", -20)
            $ variable("morale", -20)

    jump checkpoint

label morale_minor_01:
    $ event_code = "ch01e07"
    show player c at center
    menu:
        c "Hey, are you still on for the college reunion this weekend? I know things are hectic at [startup_name]?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", -10)
            $ variable("morale", -20)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", 10)
            $ variable("morale", 20)

    jump checkpoint

label morale_minor_02:
    $ event_code = "ch01e09"
    show player e at center
    menu:
        e "It's been a long day, skip the gym and grab takeout and beer?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", 10)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", -10)

    jump checkpoint

label morale_minor_03:
    $ event_code = "ch01e15"
    show player e at center
    menu:
        e "A Twitter acquaintance is in town and would like to meet for coffee today, go?"

        "$_YES":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", 10)

        "$_NO":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", -10)

    jump checkpoint

label morale_minor_04:
    $ event_code = "ch01e27"
    show player e at center
    menu:
        e "Your first free evening in a long time. Your friend, Mia, suggests you both settle down for a pizza and Netflix marathon. Politely decline and get an early night?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", -10)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", 10)

    jump checkpoint

label morale_minor_05:
    $ event_code = "ch01e28"
    show player r at center
    menu:
        r "Hey, [founder_name], my cousin's gym just opened. I can get you a lifetime membership for just $500. Shall I send over the papers?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", 10)
            $ variable("money", -500)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", -10)

    jump checkpoint
