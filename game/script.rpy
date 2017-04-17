label start:

    scene bg lounge
    show screen hud

    ""
    "This is Mr. Grey's lounge."

    show mr grey at center with dissolve

    "He is sitting motionlessly in a corner, mulling over one of the hardest decision of his life."
    "He was recently given a tempting offer by one of his rival's employee."
    "The said employee was ready to hand over his rival's user data, for a price of course."

    menu:
        g "What should I do?"

        "Pay $$$ to secretly acquire it":
            "Some time in the future..."

            $ variable("energy", 20)
            $ variable("morale", -50)
            $ variable("money", 10000)

            "Awesome. You’ve saved time AND made your startup more valuable! ...But key staff have lost respect for you."

        "Publicly expose employee":
            "Some time in the future..."

            $ variable("energy", -50)
            $ variable("morale", 20)
            $ variable("money", -10000)

            "You did the right thing, even Hacker News thinks so. Unfortunately, the PR fallout costs you a lot of energy and stalled progress."

        "Privately reject offer":
            "Some time in the future..."

            $ variable("morale", 20)
            $ variable("money", 5000)

            "You did the right thing. You’ve won the respect of your key staff and caught the attention of investors."

    "Done"

    return
