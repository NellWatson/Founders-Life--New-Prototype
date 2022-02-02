init python:
    class FeedbackInputValue(InputValue):

        def __init__(self, key=None, mechanics=False):
            self.key = key

        def get_text(self):
            try:
                return store.feedback[self.key]
            except KeyError:
                return ""

        def set_text(self, s):
            store.feedback[self.key] = s

        def enter(self):
            renpy.run(self.Toggle())
            raise renpy.IgnoreEvent()

    class RoomInputValue(InputValue):

        def __init__(self, key=None, mechanics=False):
            self.key = key

        def get_text(self):
            return getattr(persistent, self.key)

        def set_text(self, s):
            setattr(persistent, self.key, s)

        def enter(self):
            renpy.run(self.Toggle())
            raise renpy.IgnoreEvent()

screen feedback_form_screen():
    modal True

    default page = 1
    default slide = 0
    default required_actions = 0

    default metrics = [
        ("OVERALL EXP.", "overall"),
        ("EASE OF USE", "ease"),
        ("GAMEPLAY", "gameplay"),
        ("STORY", "story"),
        ("GRAPHICS", "graphics"),
        ("SOUND", "sound")
        ]
    default scale = [ ("BAD", 0), ("AVERAGE", 1), ("GOOD", 2) ]

    add Solid("#559fdd")

    if page == 1:

        vbox:
            spacing 20
            xpos 800
            yalign 0.5

            for title, k in metrics:
                fixed:
                    ysize 112

                    text title style "feedback_text" xpos -660 yalign 0.5

                    for i, ind in scale:
                        button:
                            xsize 300
                            ysize 80

                            idle_background Solid("#ffffff")
                            hover_background Solid("#4cff4c")
                            selected_idle_background Solid("#4cff4c")

                            xpos 300*ind + 20*ind + 140
                            yalign 0.5

                            text i size 40 bold True color "#000000" xalign 0.5 yalign 0.5

                            action [ SetDict(feedback, k, ind), If(feedback.has_key(k), true=NullAction(), false=SetScreenVariable("required_actions", required_actions+1)) ]

                            at button_hover

                null height 1

        if required_actions >= 6:
            button:
                xysize (200, 1080)

                idle_background Solid("#559fdd", xysize=(200, 1080))
                hover_background Solid("#88bbe7", xysize=(200, 1080))

                text ">" color "#ffffff" size 100 bold True xalign 0.5 yalign 0.5

                action SetScreenVariable("page", page+1)

                xalign 1.0

    elif page == 2:
        if slide > 0:
            button:
                xysize (1250, 150)

                idle_background Solid("#559fdd", xysize=(1250, 150))
                hover_background Solid("#88bbe7", xysize=(1250, 150))

                text "Previous ( ^ )" color "#ffffff" size 60 bold True xalign 0.5 yalign 0.5

                action SetScreenVariable("slide", slide-1)

                xalign 0.5
                yalign 0.0

        if slide < 4:
            button:
                xysize (1250, 150)

                idle_background Solid("#559fdd", xysize=(1250, 150))
                hover_background Solid("#88bbe7", xysize=(1250, 150))

                text "Next ( v )" color "#ffffff" size 60 bold True xalign 0.5 yalign 0.5

                action SetScreenVariable("slide", slide+1)

                xalign 0.5
                yalign 1.0

        if slide == 0:

            vbox:
                xalign 0.5
                yalign 0.4
                spacing 40

                $ input = Input(value=FeedbackInputValue("liked"), size=40, color="#ffffff", font="fonts/Dyslexie_Regular_159164.ttf", pixel_width=3200)

                text "Question #01/05" style "feedback_text" size 50
                text "What did you like about Founder Life?" style "feedback_text" xmaximum 1400 xalign 0.5

                fixed:
                    fit_first True

                    add Solid("#4c8fc6", xysize=(1350, 160))
                    button:
                        xysize (1350, 200)
                        background "#00000000"

                        action input.enable
                        add input

        if slide == 1:

            vbox:
                xalign 0.5
                yalign 0.4
                spacing 40

                $ input = Input(value=FeedbackInputValue("not_liked"), size=40, color="#ffffff", font="fonts/Dyslexie_Regular_159164.ttf", pixel_width=3200)

                text "Question #02/05" style "feedback_text" size 50
                text "What did you dislike about Founder Life?" style "feedback_text" xmaximum 1400 xalign 0.5

                fixed:
                    fit_first True

                    add Solid("#4c8fc6", xysize=(1350, 160))
                    button:
                        xysize (1350, 200)
                        background "#00000000"

                        action input.enable
                        add input

        if slide == 2:

            vbox:
                xalign 0.5
                yalign 0.4
                spacing 40

                $ input = Input(value=FeedbackInputValue("more_of"), size=40, color="#ffffff", font="fonts/Dyslexie_Regular_159164.ttf", pixel_width=3200)

                text "Question #03/05" style "feedback_text" size 50
                text "Founder Life should have more..." style "feedback_text" xmaximum 1400 xalign 0.5

                fixed:
                    fit_first True

                    add Solid("#4c8fc6", xysize=(1350, 160))
                    button:
                        xysize (1350, 200)
                        background "#00000000"

                        action input.enable
                        add input

        elif slide == 3:

            vbox:
                xalign 0.5
                yalign 0.4
                spacing 40

                $ input = Input(value=FeedbackInputValue("less_of"), size=40, color="#ffffff", font="fonts/Dyslexie_Regular_159164.ttf", pixel_width=3200)

                text "Question #04/05" style "feedback_text" size 50
                text "Founder Life should have less..." style "feedback_text" xmaximum 1400 xalign 0.5

                fixed:
                    fit_first True

                    add Solid("#4c8fc6", xysize=(1350, 160))
                    button:
                        xysize (1350, 200)
                        background "#00000000"

                        action input.enable
                        add input

        elif slide == 4:
            vbox:
                xalign 0.5
                yalign 0.4
                spacing 40

                $ input = Input(value=FeedbackInputValue("one_change"), size=40, color="#ffffff", font="fonts/Dyslexie_Regular_159164.ttf", pixel_width=3200)

                text "Question #05/05" style "feedback_text" size 50
                text "If I was to only change one thing about the game, it would be..." style "feedback_text" xmaximum 1400 xalign 0.5

                fixed:
                    fit_first True

                    add Solid("#4c8fc6", xysize=(1350, 160))
                    button:
                        xysize (1350, 200)
                        background "#00000000"

                        action input.enable
                        add input

            button:
                xysize (200, 1080)

                idle_background Solid("#559fdd", xysize=(200, 1080))
                hover_background Solid("#88bbe7", xysize=(200, 1080))

                text ">" color "#ffffff" size 100 bold True xalign 0.5 yalign 0.5

                action SetScreenVariable("page", page+1)

                xalign 1.0

        button:
            xysize (200, 1080)

            idle_background Solid("#559fdd", xysize=(200, 1080))
            hover_background Solid("#88bbe7", xysize=(200, 1080))

            text "<" color "#ffffff" size 100 bold True xalign 0.5 yalign 0.5

            action SetScreenVariable("page", page-1)

            xalign 0.0

    elif page == 3:

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30

            text "Thanks for your feedback, it is really important to us." style "feedback_text"

            vbox:
                spacing 10
                xsize 1200
                xalign 0.5
                yalign 0.5

                $ input = Input(value=FeedbackInputValue("email"), size=30, color="#ffffff", font="fonts/Dyslexie_Regular_159164.ttf", pixel_width=580)

                text "If you are would enjoy chatting about the game some more, please leave your email address below." style "feedback_text" size 50 xalign 0.5 yalign 0.5

                fixed:
                    fit_first True
                    xalign 0.5
                    yalign 0.5

                    add Solid("#4c8fc6", xysize=(600, 70))

                    button:
                        xysize (550, 50)
                        background "#00000000"

                        action input.enable
                        add input

            button:
                style "fl_button"

                text "Okay" style "fl_button_text"

                action [ Function(telemetry.submit_form), SetField(persistent, "submitted_form", True), Return() ]

                xalign 0.5
