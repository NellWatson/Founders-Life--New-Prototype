init python:

    class ResumeLastGame(Action):

        def __init__(self, slot):
            self.slot = slot

        def __call__(self):
            if renpy.can_load(self.slot):
                renpy.load(self.slot)
            else:
                renpy.jump_out_of_context("start")

    class Circle(renpy.Displayable):

        def __init__(self, radius, colour, width=0, pos=None, **kwargs):
            super(Circle, self).__init__(**kwargs)

            self.radius = radius
            self.colour = colour
            self.width = width

            if not pos:
                self.pos = (radius, radius)
            else:
                self.pos = pos

            self.area = radius * 2 + 1

        def render(self, width, height, st, at):

            r = renpy.Render(self.area, self.area)

            c = r.canvas()
            c.circle(self.colour, self.pos, self.radius, self.width)

            renpy.redraw(self, 0)
            return r

    def circular_buttons(radius, colour, image_path):
        """
        Returns a circular displayable which has a centered image.
        """
        
        return Fixed(Circle(radius, colour), Image(image_path, xalign=0.5, yalign=0.5), xsize=radius*2, ysize=radius*2)

    def clear_user_data():
        renpy.unlink_save("custom")
        renpy.show_screen("inform", message="Game was successfully reset.")

label after_load():
    $ telemetry.resume()

screen inform(message):
    modal True
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Okay") action Hide("inform")
