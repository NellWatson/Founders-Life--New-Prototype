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

        def __init__(self, radius, colour, width=0, pos=None, internal_circle=None, internal_radius=0, **kwargs):
            super(Circle, self).__init__(**kwargs)

            self.radius = radius
            self.colour = colour
            self.width = width
            self.internal_circle = internal_circle
            self.internal_radius = internal_radius

            if not pos:
                self.pos = (radius, radius)
            else:
                self.pos = pos

            self.area = radius * 2 + 1

        def render(self, width, height, st, at):

            r = renpy.Render(self.area, self.area)

            c = r.canvas()
            c.circle(self.colour, self.pos, self.radius, self.width)

            if self.internal_circle:
                c.circle(self.internal_circle, self.pos, self.internal_radius, self.width)

            renpy.redraw(self, 0)
            return r

    def circular_buttons(radius, colour, image_path):
        """
        Returns a circular displayable which has a centered image.
        """
        
        return Fixed(Circle(radius, colour), Image(image_path, xalign=0.5, yalign=0.5), xsize=radius*2, ysize=radius*2)

    def clear_user_data(fully=False):
        renpy.unlink_save("custom")
        if fully:
            persistent._clear(progress=True)
            renpy.transition(Dissolve(0.25))
            renpy.show_screen("success_msg", message="Game was successfully reset.", width=600, show_button="Okay")

            create_leaderboard_data()
        else:
            renpy.transition(Dissolve(0.25))
            renpy.show_screen("success_msg", message="Save file was deleted.", width=600, show_button="Okay")

    def meets_condition(var, value, condition):
        """
        Checks if the condition is satisfied or not.

        var : Name of the variable.
        value : The value of the variable.
        condition: Can be either "greater", "lesser", "equal", "greater_equal", "lesser_equal".
        """

        if ":chapter" in var:
            _seen, _chosen = chapter_manager.seen_event(var.split(":")[0], value)

            if not _seen:
                return False

            if condition == "chose:any":
                return _seen
            else:
                return _chosen == condition.split(":")[1]
            
        if var == "mindfulness":
            var = "morale"

        if ":affection" in var:
            stored_value = characters_roster.get_affection(var.split(":")[0])
        elif ":money" in var:
            money_month = var.split(":")[0]
            if money_month == "current":
                money_month = store.month
            elif money_month == "last":
                money_month = store.month - 1
            else:
                money_month = int(money_month)
                
            stored_value = int(money_manager.get_monthly_earning(money_month))
        else:
            stored_value = getattr(store, var)

        if condition == "equal":
            if stored_value == value:
                return True
        elif condition == "greater":
            if stored_value > value:
                return True
        elif condition == "lesser":
            if stored_value < value:
                return True
        elif condition == "greater_equal":
            if stored_value >= value:
                return True
        elif condition == "lesser_equal":
            if stored_value <= value:
                return True
        elif condition == "not":
            if stored_value != value:
                return True
        return False

label after_load():
    $ telemetry.resume()
