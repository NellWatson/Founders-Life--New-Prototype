init python:

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
