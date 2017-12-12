label money_major_01:
    $ event_code = "ch01e06"
    show player e at center
    menu:
        e "Hey, [founder_name], you really want to have a Non-Disclosure Agreement (NDA) in place before you speak to potential investors - they are sharks! I can draft you one for $2,000?"

        "$_YES":
            $ variable("productivity", 20)
            $ variable("morale", -20)
            $ variable("money", 2000)

        "$_NO":
            $ variable("morale", 20)

    jump checkpoint

label money_major_02:
    $ event_code = "ch01e11"
    show player e at center
    menu:
        e "A fellow startup wants you to perform code review for them. It pays $1,000 - block out time away from [startup_name] and do the work?"

        "$_YES":
            $ variable("productivity", -20)
            $ variable("energy", -20)
            $ variable("morale", -20)
            $ variable("money", 2000)

        "$_NO":
            $ variable("productivity", 20)
            $ variable("energy", 20)
            $ variable("morale", 20)

    jump checkpoint

label money_minor_01:
    $ event_code = "ch01e02"
    show player e at center
    menu:
        e "An old friend needs a day of technical writing done and thinks you'd be the perfect freelancer for the gig. It pays $500, take the day off from [startup_name] and do the work?"

        "$_YES":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", -10)
            $ variable("money", 500)

        "$_NO":
            $ variable("productivity", 10)
            $ variable("morale", 10)

    jump checkpoint

label money_minor_02:
    $ event_code = "ch01e03"
    show player e at center
    menu:
        e "There's a chance to run some UX research with some solid prospects. It will take a day and cost $500 in gift cards, stop making and start testing?"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", -10)
            $ variable("morale", -10)
            $ variable("money", -500)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("morale", 10)

    jump checkpoint

label money_minor_03:
    $ event_code = "ch01e14"
    show player e at center
    menu:
        e "The local community college would like you to speak to their students. It pays $500 but it would involve going out of town. Do it?"

        "$_YES":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", 10)
            $ variable("money", 500)

        "$_NO":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", -10)

    jump checkpoint

label money_minor_04:
    $ event_code = "ch01e16"
    show player e at center
    menu:
        e "Fast Company would like you to author an essay on Startup Mindfulness, they'll pay $500?"

        "$_YES":
            $ variable("productivity", -20)
            $ variable("energy", -10)
            $ variable("morale", 20)
            $ variable("money", 500)

        "$_NO":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", -20)

    jump checkpoint

label money_minor_05:
    $ event_code = "ch01e16"
    show player e at center
    menu:
        e "Your Uber bill is now $500 a month. Take the productivity hit, pocket the saving and start walking more?"

        "$_YES":
            $ variable("productivity", -20)
            $ variable("energy", -10)
            $ variable("morale", 10)
            $ variable("money", 500)

        "$_NO":
            $ variable("productivity", 20)
            $ variable("energy", 10)
            $ variable("morale", -10)

    jump checkpoint

label money_minor_06:
    $ event_code = "ch01e24"
    show player e at center
    menu:
        e "StartStars Incubator would like you to mentor at their Startup Weekend, they'll pay $500?"

        "$_YES":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", 10)
            $ variable("money", 500)

        "$_NO":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", -10)

    jump checkpoint
