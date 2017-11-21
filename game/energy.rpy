label energy_minor_01:
    show player a at center
    menu:
        a "(energy_minor_01) So much work to do but so little time. Skip lunch and power through?"

        "$_YES":
            $ variable("energy", -10)

        "$_NO":
            $ variable("energy", 10)

    jump checkpoint

label energy_minor_02:
    show player b at center
    menu:
        b "(energy_minor_02) Things are crazy today, more coffee?"

        "$_YES":
            $ variable("energy", -10)

        "$_NO":
            $ variable("energy", +10)

    jump checkpoint

label energy_minor_03:
    show player c at center
    menu:
        c "(energy_minor_03) Skip gym?"

        "$_YES":
            $ variable("energy", 10)

        "$_NO":
            $ variable("energy", -10)

    jump checkpoint

label energy_minor_04:
    show player d at center
    menu:
        d "(energy_minor_04) Your first free evening in a long time. Your friend Mia suggests you both settle down for a pizza and Netflix marathon. Decline and pre-prepare individual meals for the next week instead?"

        "$_YES":
            $ variable("energy", 10)

        "$_NO":
            $ variable("energy", -10)

    jump checkpoint

label energy_minor_05:
    show player e at center
    menu:
        e "(energy_minor_010) You read a Fast Company article on successful founders and their exercise habits. Set the alarm for an hour early and hit the gym?"

        "$_YES":
            $ variable("energy", 10)

        "$_NO":
            $ variable("energy", -10)

    jump checkpoint

label energy_major_01:
    show player a at center
    menu:
        a "(energy_major_01) It's a sunny day but you are running a little late. Call ahead to let the team know when you'll arrive and then enjoy a leisurely stroll?"

        "$_YES":
            $ variable("energy", 20)

        "$_NO":
            $ variable("energy", -20)

    jump checkpoint

label energy_major_02:
    show player b at center
    menu:
        b "(energy_major_02) The deadline is getting closer but the backlog is not getting smaller. Rally the troops and pull and all-nighter?"

        "$_YES":
            $ variable("energy", -20)

        "$_NO":
            $ variable("energy", 20)

    jump checkpoint

label energy_major_03:
    show player c at center
    menu:
        c "(energy_major_03) Your 'maker' schedule is distracting from your 'manager' value. Should you clear a week in the schedule and train up the team to handle some key tasks?"

        "$_YES":
            $ variable("energy", 20)

        "$_NO":
            $ variable("energy", -20)

    jump checkpoint

label energy_major_04:
    show player d at center
    menu:
        d "(energy_major_04) You are getting buried under a mountain of paperwork. Hire a Virtual Assistant from Upwork?"

        "$_YES":
            $ variable("energy", 20)

        "$_NO":
            $ variable("energy", -20)

    jump checkpoint

label energy_major_05:
    show player e at center
    menu:
        e "(energy_major_010) The product feature you have been working on is holding up this week's release. Work all night to catch up instead of delegating?"

        "$_YES":
            $ variable("energy", -20)

        "$_NO":
            $ variable("energy", 20)

    jump checkpoint
