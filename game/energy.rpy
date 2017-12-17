label energy_major_01:
    $ event_code = "ch01e01"
    show eileen at center
    menu:
        e "With your current pace, there is no way that the MVP is going to ship to the schedule you promised interested investors. Pressure the team to crunch some nights and weekends?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", -20)
            $ variable("morale", -20)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", 20)
            $ variable("morale", 20)

    jump checkpoint

label energy_major_02:
    $ event_code = "ch01e02"
    show eileen at center
    menu:
        e "It's clear that the team is not completely aligned with your vision. Put development on hold for a few days to go offsite to articulate a coherent mission and compelling vision to the team?"

        "$_YES":
            $ variable("productivity", -20)
            $ variable("energy", 20)
            $ variable("morale", 20)
            $ variable("money", -1000)

        "$_NO":
            $ variable("productivity", 20)
            $ variable("energy", -20)
            $ variable("morale", -20)

    jump checkpoint

label energy_minor_01:
    $ event_code = "ch01e03"
    show raquel at center
    menu:
        r "Hey, [founder_name], bookkeeping is a pain...a time-consuming pain. Do you want me to hook you up with a part-time accountant, they'll look after the books for $500 per month?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", 10)
            $ variable("money", -600)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", -10)

    jump checkpoint

label energy_minor_02:
    $ event_code = "ch01e04"
    show eileen at center
    menu:
        e "These financials projections won't model themselves and you can't move forward without them. Finish them tonight, whatever it takes?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", -10)
            $ variable("morale", -10)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", 10)
            $ variable("morale", 10)

    jump checkpoint

label energy_minor_03:
    $ event_code = "ch01e05"
    show eileen at center
    menu:
        e "A reminder email just came in about tonight's VC Mixer, confirm attendance?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", -10)
            $ variable("morale", 10)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", 10)
            $ variable("morale", -10)

    jump checkpoint

label energy_minor_04:
    $ event_code = "ch01e06"
    show eileen at center
    menu:
        e "How hard can it be to track down one stupid little bug? Delay today's release and go for a long walk?"

        "$_YES":
            $ variable("productivity", -10)
            $ variable("energy", 10)
            $ variable("morale", 10)

        "$_NO":
            $ variable("productivity", 10)
            $ variable("energy", -10)
            $ variable("morale", -10)

    jump checkpoint

label energy_minor_05:
    $ event_code = "ch01e07"
    show eileen at center
    menu:
        e "Everyone is busy but nothing productive seems to get down. Introduce the team to Objectives and Key Results (OKRs)?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", 10)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", -10)

    jump checkpoint
