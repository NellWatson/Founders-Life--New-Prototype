label start:
    scene bg bedroom
    # print renpy.display.core.scene_lists().get_all_displayables()
    
    show screen hud
    call screen founder_map

    jump event_intro

screen game_screen():
    modal True
    default b = ReviewB()
    
    add DynamicDisplayable(dynamic_review, b)

label checkpoint:
    $ event_name = ""

    if energy > 100:
        $ energy = 100

    if morale > 100:
        $ morale = 100
    
    if turn_no and not (turn_no % 5):
        # current_sprint = energy * morale * turn_no * founder_level
        # money += current_sprint
        $ founder_score = energy + morale + (money * turn_no)
        $ level_up = False
        $ last_founder_level = founder_level

        call screen sprint_review(current_bg)
        call screen startup_review(current_bg)

        if turn_no > 19:
            call screen err_msg(message="End of Episode. More coming soon.", title="game over")
            return

        while money > FOUNDER_INDEX[founder_level][1]:
            $ founder_level += 1
            $ level_up = True

            if founder_level > 10:
                $ founder_level = 10

        #call screen level_up(current_bg)
        if energy < 30:
            call screen warn_msg(message="Being a founder is physically tough, you need to pro-actively manage your energy.", title="warning")

        if morale < 30:
            call screen warn_msg(message="Being a founder is mentally exhausting, you need to be mindful of your mental well-being.", title="warning")

        if money < 30:
            call screen warn_msg(message="Being a founder is financially draining, you need to strike a balance between investing in your dreams and being frugal with your cash reserves.", title="warning")

    if energy > 0 and morale > 0:
        $ turn_no += 1
        $ current_bg = "bg " + BACKGROUNDS[founder_level - 1]

        scene expression current_bg with dissolve
        jump expression find_event()

    elif energy < 0:
        call screen err_msg(message="You are out of Energy.", title="game over")
    elif morale < 0:
        call screen err_msg(message="You are out of Morale.", title="game over")

    "You survived [turn_no] days."

    return

label cloud:
    menu:
        "Your lead programmer wants us build and run our own servers. Do it?"

        "$_YES":
            $ variable("energy", -20)
            $ variable("morale", 20)

        "$_NO":
            $ variable("energy", 20)
            $ variable("morale", -20)

    jump checkpoint

label day_one_pr:
    menu:
        "Send out a press release to announce your new venture?"

        "$_YES":
            $ variable("energy", -5)
            $ variable("morale", -10)

        "$_NO":
            $ variable("energy", 20)
            $ variable("morale", 20)

    jump checkpoint

label conference:
    menu:
        "There’s a conference coming up that looks interesting. Buy a ticket for $5,000?"

        "$_YES":
            $ variable("energy", -50)
            $ variable("morale", -10)

        "$_NO":
            $ variable("energy", 50)
            $ variable("morale", 50)

    jump checkpoint

label key_messaging:
    menu:
        "Figuring out the key messaging for your startup is distracting you from product development. Should you hire a PR firm?"

        "$_YES":
            $ variable("energy", 20)
            $ variable("morale", -20)

        "$_NO":
            $ variable("energy", -30)
            $ variable("morale", 50)

    jump checkpoint

label premature_launch:
    menu:
        "We have a very basic working version. Should we roll out a public beta?"

        "$_YES":
            $ variable("energy", 0)
            $ variable("morale", -20)

        "$_NO":
            $ variable("morale", 20)

    jump checkpoint

label ux_research:
    menu:
        "Your designer thinks you should run some UX Research before we continue building out the product?"

        "$_YES":
            $ variable("energy", -20)
            $ variable("morale", 20)

        "$_NO":
            $ variable("energy", 30)
            $ variable("morale", -30)

    jump checkpoint

label delegation:
    menu:
        "Your workload is becoming distracting. Should you take a week out to train up your team to handle key tasks?"

        "$_YES":
            $ variable("energy", -20)
            $ variable("morale", 30)

        "$_NO":
            $ variable("energy", -40)
            $ variable("morale", -40)

    jump checkpoint

label equity:
    menu:
        "You have finally found your perfect designer but she wants 10% equity to join. Should you agree to her terms?"

        "$_YES":
            $ variable("energy", 30)
            $ variable("morale", 30)

        "$_NO":
            $ variable("energy", -30)
            $ variable("morale", -30)

    jump checkpoint

label beta:
    menu:
        "It is going to impossible to get to \"Feature Complete\" for the next scheduled Beta rollout. Should we push back the release date?"

        "$_YES":
            $ variable("morale", -10)

        "$_NO":
            $ variable("energy", -20)
            $ variable("morale", 30)

    jump checkpoint

label nda:
    menu:
        "Your lawyer wants to draw up an NDA for potential VCs to sign?"

        "$_YES":
            $ variable("energy", -20)
            $ variable("morale", -50)

        "$_NO":
            $ variable("energy", 5)
            $ variable("morale", 40)

    jump checkpoint

label micro_managing:
    menu:
        "Key team members want to own the tasks they have been delegated. Should you stop micro-managing key activities?"

        "$_YES":
            $ variable("energy", 40)
            $ variable("morale", 40)

        "$_NO":
            $ variable("energy", -40)
            $ variable("morale", -40)

    jump checkpoint

label tier_2_1:
    menu:
        "This is a Tier 2 Test Event (Yes = Morale, No = Energy)"

        "$_YES":
            $ variable("energy", -10)
            $ variable("morale", 20)

        "$_NO":
            $ variable("energy", 20)
            $ variable("morale", -10)

    jump checkpoint

label tier_3_1:
    menu:
        "This is a Tier 3 Test Event (Yes = Morale, No = Energy)"

        "$_YES":
            $ variable("energy", -10)
            $ variable("morale", 20)

        "$_NO":
            $ variable("energy", 20)
            $ variable("morale", -10)

    jump checkpoint

label tier_3_2:
    menu:
        "This is a Tier 3 Test Event (Yes = Morale, No = Energy)"

        "$_YES":
            $ variable("energy", 30)
            $ variable("morale", -20)

        "$_NO":
            $ variable("energy", -20)
            $ variable("morale", 30)

    jump checkpoint

label tier_4_1:
    menu:
        "This is a Tier 4 Test Event (Yes = Morale, No = Energy)"

        "$_YES":
            $ variable("energy", -10)
            $ variable("morale", 20)

        "$_NO":
            $ variable("energy", 20)
            $ variable("morale", -10)

    jump checkpoint

label tier_4_2:
    menu:
        "This is a Tier 4 Test Event (Yes = Morale, No = Energy)"

        "$_YES":
            $ variable("energy", 30)
            $ variable("morale", -20)

        "$_NO":
            $ variable("energy", -20)
            $ variable("morale", 30)

    jump checkpoint

label tier_5_1:
    menu:
        "This is a Tier 5 Test Event (Yes = Morale, No = Energy)"

        "$_YES":
            $ variable("energy", -10)
            $ variable("morale", 20)

        "$_NO":
            $ variable("energy", 20)
            $ variable("morale", -10)

    jump checkpoint

label tier_5_2:
    menu:
        "This is a Tier 5 Test Event (Yes = Morale, No = Energy)"

        "$_YES":
            $ variable("energy", 30)
            $ variable("morale", -20)

        "$_NO":
            $ variable("energy", -20)
            $ variable("morale", 30)

    jump checkpoint

label tier_6_1:
    menu:
        "This is a Tier 6 Test Event (Yes = Morale, No = Energy)"

        "$_YES":
            $ variable("energy", -10)
            $ variable("morale", 20)

        "$_NO":
            $ variable("energy", 20)
            $ variable("morale", -10)

    jump checkpoint

label tier_6_2:
    menu:
        "This is a Tier 6 Test Event (Yes = Morale, No = Energy)"

        "$_YES":
            $ variable("energy", 30)
            $ variable("morale", -20)

        "$_NO":
            $ variable("energy", -20)
            $ variable("morale", 30)

    jump checkpoint

label tier_7_1:
    menu:
        "This is a Tier 7 Test Event (Yes = Morale, No = Energy)"

        "$_YES":
            $ variable("energy", -10)
            $ variable("morale", 20)

        "$_NO":
            $ variable("energy", 20)
            $ variable("morale", -10)

    jump checkpoint

label tier_7_2:
    menu:
        "This is a Tier 7 Test Event (Yes = Morale, No = Energy)"

        "$_YES":
            $ variable("energy", 30)
            $ variable("morale", -20)

        "$_NO":
            $ variable("energy", -20)
            $ variable("morale", 30)

    jump checkpoint
