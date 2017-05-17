label start:

    scene bg lounge
    show screen hud

    jump set_startup

label checkpoint:
    $ event_name = ""
    
    if turn_no and not (turn_no % 4):
        $ month += 1

        call screen startup_review("bg lounge")
        
        $ founder_level += 1

        if founder_level > 10:
            $ founder_level = 10

        call screen level_up("bg lounge")
        call screen startup_preview("bg lounge")

    if energy > 0 and morale > 0 and money > 0:
        $ turn_no += 1
        "And here comes another turning point in Mr. X's life."
        
        jump expression find_event()

    elif energy < 0:
        $ print energy
        call screen err_msg(message="You are out of Energy.", title="game over")
    elif morale < 0:
        $ print morale
        call screen err_msg(message="You are out of Morale.", title="game over")
    elif money < 0:
        $ print money
        call screen err_msg(message="You are out of Cash.", title="game over")

    if month > 1:
        "You survived [month] months."
    else:
        "You survived [month] month."

    return

label minor_event_1:
    $ event_name = "Minor Event 1"

    "He is sitting motionlessly in a corner, mulling over one of the easiest decision of his life. Make X's mind for him please because... reasons!"

    menu:
        "What should he do?"

        "$_YES":
            "Some time in the future..."

            $ variable("energy", 10)
            $ variable("morale", -10)
            $ variable("money", 10000)

            "Awesome. You earned money"

        "$_NO":
            "Some time in the future..."

            $ variable("energy", -10)
            $ variable("morale", 10)
            $ variable("money", 10000)

            "Fantastic. Money and Morale; that's an M&M I like (aside from the regular ones)."

    jump checkpoint

label minor_event_2:
    $ event_name = "Minor Event 2"

    "He is sitting motionlessly in a corner, mulling over one of the easiest decision of his life. Make X's mind for him please because... reasons!"

    menu:
        "What should he do?"

        "$_YES":
            "Some time in the future..."

            $ variable("energy", 5)
            $ variable("morale", -5)
            $ variable("money", 5000)

            "Awesome. You earned money"

        "$_NO":
            "Some time in the future..."

            $ variable("energy", -5)
            $ variable("morale", 5)
            $ variable("money", 5000)

            "Fantastic. Money and Morale; that's an M&M I like (aside from the regular ones)."

    jump checkpoint

label minor_event_3:
    $ event_name = "Minor Event 3"

    "He is sitting motionlessly in a corner, mulling over one of the easiest decision of his life. Make X's mind for him please because... reasons!"

    menu:
        "What should he do?"

        "$_YES":
            "Some time in the future..."

            $ variable("energy", 10)
            $ variable("morale", -10)
            $ variable("money", 10000)

            "Awesome. You earned money"

        "$_NO":
            "Some time in the future..."

            $ variable("energy", -10)
            $ variable("morale", 10)
            $ variable("money", 10000)

            "Fantastic. Money and Morale; that's an M&M I like (aside from the regular ones)."

    jump checkpoint

label minor_event_4:
    $ event_name = "Minor Event 4"

    "He is sitting motionlessly in a corner, mulling over one of the easiest decision of his life. Make X's mind for him please because... reasons!"

    menu:
        "What should he do?"

        "$_YES":
            "Some time in the future..."

            $ variable("energy", 5)
            $ variable("morale", 5)
            $ variable("money", -10000)

            "Awesome. You are a bit more energetic."

        "$_NO":
            "Some time in the future..."

            $ variable("energy", -5)
            $ variable("morale", 5)
            $ variable("money", 5000)

            "Fantastic. Money and Morale; that's an M&M I like (aside from the regular ones)."

    jump checkpoint

label major_event:
    $ event_name = "Major Event 1"

    "He is sitting motionlessly in a corner, mulling over one of the hardest decision of his life."

    menu:
        "What should he do?"

        "$_YES":
            "Some time in the future..."

            $ variable("energy", 50)
            $ variable("morale", -50)
            $ variable("money", 50000)

            "Awesome. You earned money"

        "$_NO":
            "Some time in the future..."

            $ variable("energy", -50)
            $ variable("morale", 50)
            $ variable("money", 50000)

            "Fantastic. Money and Morale; that's an M&M I like (aside from the regular ones)."

    jump checkpoint
