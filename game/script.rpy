label start:

    scene bg lounge
    show screen hud

    ""
    "This is Mr. X's lounge."

    show mr x at center with dissolve

label checkpoint:
    if turn_no and not (turn_no % 4):
        $ month += 1

    if energy > 0 and morale > 0 and money > 0:
        $ turn_no += 1

        "And here comes another turning point in Mr. X's life."
        
        jump expression find_event()
    elif energy > 0:
        "You are out of Energy."
    elif morale > 0:
        "You are out of Morale."
    elif money > 0:
        "You are out of Cash."

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

        "Choose A":
            "Some time in the future..."

            $ variable("energy", 10)
            $ variable("morale", -10)
            $ variable("money", 10000)

            "Awesome. You earned money"

        "Choose B":
            "Some time in the future..."

            $ variable("energy", -10)
            $ variable("morale", 10)
            $ variable("money", 10000)

            "Fantastic. Money and Morale; that's an M&M I like (aside from the regular ones)."

        "Choose C":
            "Some time in the future..."

            $ variable("energy", 10)
            $ variable("morale", -10)
            $ variable("money", -10000)

            "Well on the plus side, you have some extra energy."

    jump checkpoint

label minor_event_2:
    $ event_name = "Minor Event 2"

    "He is sitting motionlessly in a corner, mulling over one of the easiest decision of his life. Make X's mind for him please because... reasons!"

    menu:
        "What should he do?"

        "Choose A":
            "Some time in the future..."

            $ variable("energy", 5)
            $ variable("morale", -5)
            $ variable("money", 5000)

            "Awesome. You earned money"

        "Choose B":
            "Some time in the future..."

            $ variable("energy", -5)
            $ variable("morale", 5)
            $ variable("money", 5000)

            "Fantastic. Money and Morale; that's an M&M I like (aside from the regular ones)."

        "Choose C":
            "Some time in the future..."

            $ variable("energy", 5)
            $ variable("morale", -5)
            $ variable("money", -5000)

            "Well on the plus side, you have some extra energy."

    jump checkpoint

label minor_event_3:
    $ event_name = "Minor Event 3"

    "He is sitting motionlessly in a corner, mulling over one of the easiest decision of his life. Make X's mind for him please because... reasons!"

    menu:
        "What should he do?"

        "Choose A":
            "Some time in the future..."

            $ variable("energy", 10)
            $ variable("morale", -10)
            $ variable("money", 10000)

            "Awesome. You earned money"

        "Choose B":
            "Some time in the future..."

            $ variable("energy", -10)
            $ variable("morale", 10)
            $ variable("money", 10000)

            "Fantastic. Money and Morale; that's an M&M I like (aside from the regular ones)."

        "Choose C":
            "Some time in the future..."

            $ variable("energy", -10)
            $ variable("morale", -10)
            $ variable("money", 10000)

            "Well on the plus side, you have some extra energy."

    jump checkpoint

label minor_event_4:
    $ event_name = "Minor Event 4"

    "He is sitting motionlessly in a corner, mulling over one of the easiest decision of his life. Make X's mind for him please because... reasons!"

    menu:
        "What should he do?"

        "Choose A":
            "Some time in the future..."

            $ variable("energy", 5)
            $ variable("morale", 5)
            $ variable("money", -10000)

            "Awesome. You are a bit more energetic."

        "Choose B":
            "Some time in the future..."

            $ variable("energy", -5)
            $ variable("morale", 5)
            $ variable("money", 5000)

            "Fantastic. Money and Morale; that's an M&M I like (aside from the regular ones)."

        "Choose C":
            "Some time in the future..."

            $ variable("energy", 5)
            $ variable("morale", -5)
            $ variable("money", +5000)

            "Well you have some extra money and energy."

    jump checkpoint

label major_event:
    $ event_name = "Major Event 1"

    "He is sitting motionlessly in a corner, mulling over one of the hardest decision of his life."

    menu:
        "What should he do?"

        "Choose Major A":
            "Some time in the future..."

            $ variable("energy", 50)
            $ variable("morale", -50)
            $ variable("money", 50000)

            "Awesome. You earned money"

        "Choose Major B":
            "Some time in the future..."

            $ variable("energy", -50)
            $ variable("morale", 50)
            $ variable("money", 50000)

            "Fantastic. Money and Morale; that's an M&M I like (aside from the regular ones)."

        "Choose Major C":
            "Some time in the future..."

            $ variable("energy", 50)
            $ variable("morale", -50)
            $ variable("money", -50000)

            "Well on the plus side, you have some extra energy."

    jump checkpoint
