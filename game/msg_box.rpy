init python:

    def find_height(message, width, gap=5, min_height=120, padding=20):
        """
        Returns the height of the Text displayable
        """

        if renpy.mobile:
            return 300

        w, h = Text(message).size()
        modifier, round_up = divmod(w, width)

        # Add +1 if the value is even a fraction bigger
        if round_up:
            modifier += 1

            # Add +1 for safety since there is no gurantee that the text will break perfectly.
            if round_up > width / 1.5:
                modifier += 1

        height = int( (h * modifier) + (gap * modifier) + padding )

        return height if height > min_height else min_height

screen fl_window(name, title, colour="#559fdd", width=600, height=400, _bar_height=90, cross=True, hide_anyway=False, show_button=None, underlay=True):

    default tinted = Color(colour).tint(0.5)
    default shaded = Color(colour).shade(0.5)

    if not hide_anyway:
        $ called = (renpy.game.context().info._current_interact_type == "screen")
    else:
        $ called = False

    if underlay:
        add Solid("#000000") alpha 0.60

    if len(title) > 20:
        default t_size = 46
    else:
        default t_size = 64

    vbox:
        xalign 0.5
        yalign 0.5

        fixed:
            xmaximum width
            ymaximum _bar_height

            add Solid(colour)
            text title.upper() size t_size color "#ffffff" font "fonts/Dyslexie_Bold_159164.ttf" yalign 0.5 xalign 0.5

            if cross and not show_button:
                button:
                    xysize _bar_height, _bar_height

                    idle_background Solid(colour)
                    hover_background Solid(tinted)
                    selected_background Solid(shaded)

                    text "X" font "fonts/Dyslexie_Regular_159164.ttf" size 60 color "#ffffff" yalign 0.5 xalign 0.52

                    action If(called, true=Return(), false=Hide(name, transition=Dissolve(0.25)))

                    xpos width+20

        frame:
            xsize width
            ysize height

            background Solid("#ffffff")

            transclude

        if show_button:
            button:
                xysize width, _bar_height-15
                yoffset 20

                idle_background Solid(colour)
                hover_background Solid(tinted)
                selected_background Solid(shaded)

                text show_button font "fonts/Dyslexie_Regular_159164.ttf" size 50 color "#ffffff" yalign 0.5 xalign 0.52

                action If(called, true=Return(), false=Hide(name, transition=Dissolve(0.25)))

screen success_msg(message, title="Success", width=600, height=0, hide_anyway=False, show_button=""):
    modal True
    add Solid("#00000050")

    default actual_height = height if height else find_height(message, width-20)

    use fl_window("success_msg", title, colour="#4BB543", width=width, height=actual_height, hide_anyway=hide_anyway, show_button=show_button):
        vbox:
            xalign 0.5
            yalign 0.5

            text message color "#000000"

screen warn_msg(message, title="Warning", width=600, height=0, hide_anyway=False, show_button=""):
    modal True
    add Solid("#00000050")

    default actual_height = height if height else find_height(message, width-20)

    use fl_window("warn_msg", title, colour="#ff8800", width=width, height=actual_height, hide_anyway=hide_anyway, show_button=show_button):
        vbox:
            xalign 0.5
            yalign 0.5

            text message size 30 color "#000000"

screen err_msg(message, title="Error", width=600, height=0, hide_anyway=False, show_button=""):
    modal True

    default actual_height = height if height else find_height(message, width-20)

    use fl_window("err_msg", title, colour="#ff0000", width=width, height=actual_height, hide_anyway=hide_anyway, show_button=show_button):
        vbox:
            xalign 0.5
            yalign 0.5

            text message color "#000000"

screen msg(message, title="Information", width=600, height=0, **kwargs):
    modal True

    default actual_height = height if height else find_height(message, width-20)

    use fl_window("err_msg", title, colour="#559fdd", width=width, height=actual_height, **kwargs):
        vbox:
            xalign 0.5
            yalign 0.5

            text message color "#000000"
