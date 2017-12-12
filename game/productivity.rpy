label productivity_major_01:
    $ event_code = "ch01e04"
    show player e at center
    menu:
        e "The visual design isn't quite right, it needs more iteration. Push back the MVP launch deadline?"

        "$_YES":
            $ variable("productivity", -20)
            $ variable("energy", -20)
            $ variable("money", -1000)

        "$_NO":
            $ variable("productivity", 20)
            $ variable("morale", 20)

    jump checkpoint

label productivity_major_02:
    $ event_code = "ch01e05"
    show player e at center
    menu:
        e "Maybe you can't be both a founder and a maker every day, it's burning you out? Better portion your maker/manager schedules and hire a freelancer to pick up some of the lower level slack?"

        "$_YES":
            $ variable("productivity", 20)
            $ variable("energy", 20)
            $ variable("morale", 20)
            $ variable("money", -1000)

        "$_NO":
            $ variable("productivity", -20)
            $ variable("energy", -20)
            $ variable("morale", -20)

    jump checkpoint

label productivity_major_03:
    $ event_code = "ch01e31"
    show player e at center
    menu:
        e "Your 'maker' schedule is distracting from your 'manager' value. Should you clear the schedule and train up the team to assume responsibility for some key tasks?"

        "$_YES":
            $ variable("productivity", 20)
            $ variable("energy", 20)
            $ variable("morale", 20)
            $ variable("money", -500)

        "$_NO":
            $ variable("productivity", -20)
            $ variable("energy", -20)
            $ variable("morale", -20)

    jump checkpoint

label productivity_minor_01:
    $ event_code = "ch01e10"
    show player e at center
    menu:
        e "Administrative duties are killing your attention and impact, hire a virtual assistant from Upwork to finish some urgent but unimportant admin tasks?"

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

label productivity_minor_02:
    $ event_code = "ch01e18"
    show player r at center
    menu:
        r "Hey, [founder_name], since you are just starting out, Rocca here is going to offer you a once-in-a-lifetime deal. I'll you provide legal counsel for the rest of the month for just $1,000...that's a small price to pay for a more productive, protected startup! What do you say?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", 10)
            $ variable("money", -1000)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", -10)

    jump checkpoint

label productivity_minor_03:
    $ event_code = "ch01e18"
    show player e at center
    menu:
        e "Your phone won't stop buzzing. Turn off notifications and get some focus?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", 10)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", -10)

    jump checkpoint

label productivity_minor_04:
    $ event_code = "ch01e26"
    show player e at center
    menu:
        e "A super smart peer sends you some really good feedback, pivot this week's objectives to factor in their insights?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", -10)
            $ variable("morale", 10)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", 10)
            $ variable("morale", -10)

    jump checkpoint

label productivity_minor_05:
    $ event_code = "ch01e33"
    show player e at center
    menu:
        e "Everyone is hitting their goals but [startup_name] is no nearer product/market fit. Time for the difficult conversation about sandbagging objectives?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", -10)
            $ variable("morale", 10)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", 10)
            $ variable("morale", -10)

    jump checkpoint
