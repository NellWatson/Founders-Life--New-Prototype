label start:

    scene bg lounge
    show screen hud

    ""
    "This is Mr. X's lounge."

    show mr x at center with dissolve

label checkpoint:
    if energy > 0 and morale > 0 and money > 0:
        jump expression find_event()

    pause 5.0

    return

label minor_event:
    $ turn_no += 1

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

label major_event:
    $ turn_no += 1

    "He is sitting motionlessly in a corner, mulling over one of the hardest decision of his life."

    menu:
        "What should he do?"

        "Pay $$$ to secretly acquire it":
            "Some time in the future..."

            $ variable("energy", 50)
            $ variable("morale", -50)
            $ variable("money", 50000)

            "Awesome. You’ve saved time AND made your startup more valuable! ...But key staff have lost respect for you."

        "Publicly expose employee":
            "Some time in the future..."

            $ variable("energy", -50)
            $ variable("morale", 50)
            $ variable("money", 50000)

            "You did the right thing, even Hacker News thinks so. Unfortunately, the PR fallout costs you a lot of energy and stalled progress."

        "Privately reject offer":
            "Some time in the future..."

            $ variable("energy", 50)
            $ variable("morale", -50)
            $ variable("money", -50000)

            "You did the right thing. You’ve won the respect of your key staff and caught the attention of investors."

    jump checkpoint
