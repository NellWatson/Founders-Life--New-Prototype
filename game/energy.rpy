label energy_minor_01:
    menu:
        "So much work to do but so little time. Skip lunch and power through?"

        "$_YES":
            $ variable("energy", -5)

        "$_NO":
            $ variable("energy", 5)

    jump checkpoint

label energy_minor_02:
    menu:
        "Things are crazy today, more coffee?"

        "$_YES":
            $ variable("energy", -5)

        "$_NO":
            $ variable("energy", +5)

    jump checkpoint

label energy_minor_03:
    menu:
        "Skip gym?"

        "$_YES":
            $ variable("energy", 5)

        "$_NO":
            $ variable("energy", -5)

    jump checkpoint

label energy_minor_04:
    menu:
        "Your first free evening in a long time. Your friend Mia suggests you both settle down for a pizza and Netflix marathon. Decline and pre-prepare individual meals for the next week instead?"

        "$_YES":
            $ variable("energy", 5)

        "$_NO":
            $ variable("energy", -5)

    jump checkpoint

label energy_minor_05:
    menu:
        "You read a Fast Company article on successful founders and their exercise habits. Set the alarm for an hour early and hit the gym?"

        "$_YES":
            $ variable("energy", 5)

        "$_NO":
            $ variable("energy", -5)

    jump checkpoint

label energy_major_01:
    menu:
        "It's a sunny day but you are running a little late. Call ahead to let the team know when you'll arrive and then enjoy a leisurely stroll?"

        "$_YES":
            $ variable("energy", 10)

        "$_NO":
            $ variable("energy", -10)

    jump checkpoint

label energy_major_02:
    menu:
        "The deadline is getting closer but the backlog is not getting smaller. Rally the troops and pull and all-nighter?"

        "$_YES":
            $ variable("energy", -10)

        "$_NO":
            $ variable("energy", 10)

    jump checkpoint

label energy_major_03:
    menu:
        "Your 'maker' schedule is distracting from your 'manager' value. Should you clear a week in the schedule and train up the team to handle some key tasks?"

        "$_YES":
            $ variable("energy", 10)

        "$_NO":
            $ variable("energy", -10)

    jump checkpoint

label energy_major_04:
    menu:
        "You are getting buried under a mountain of paperwork. Hire a Virtual Assistant from Upwork?"

        "$_YES":
            $ variable("energy", 10)

        "$_NO":
            $ variable("energy", -10)

    jump checkpoint

label energy_major_05:
    menu:
        "The product feature you have been working on is holding up this week's release. Work all night to catch up instead of delegating?"

        "$_YES":
            $ variable("energy", -10)

        "$_NO":
            $ variable("energy", 10)

    jump checkpoint
