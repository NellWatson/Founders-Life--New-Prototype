init python:

    class SuperBar():

        def __init__(self, base, inc, dec, var, **kwargs):
            self.base = base
            self.inc = inc
            self.dec = dec
            self.var = var
            self.properties = kwargs

            self.last_st = 0
            self.last_value = getattr(store, var)
            self.delta = 0
            self.review_step = 0

        def displayable(self, st):
            current = getattr(store, self.var)

            # Check to see if the variable value has changed
            if current != self.last_value:
                self.delta += self.last_value - current
                self.review_step = self.delta / 30.0

            # If the variable value decreased
            if self.delta > 0.001:
                d = self.dec
                v = current + self.delta
                self.delta -= self.review_step

            # If the variable value increased
            elif self.delta < -0.001:
                d = self.inc
                v = self.last_value + self.delta
                self.delta -= self.review_step
            else:
                d = self.base
                v = current
                self.delta = 0
                self.review_step = 0

            self.last_value = current

            if self.delta or current <= 10:
                return At(Bar(value=v, range=100, left_bar=Solid(d), right_bar=Color(d).shade(0.75), **self.properties), flash)
            else:
                return Bar(value=v, range=100, left_bar=Solid(d), right_bar=Color(d).shade(0.75), **self.properties)

    class ReviewB():

        def __init__(self):
            self.founder_level = 1
            self.founder_status = "founder_status"
            self.colour = "#00ff00"

            self.updated_fl = False

            # The current money player has earned
            self.money = 0

            # The money player had before this sprint
            self.old_money = 0

            # The step by which the bar should update
            self.review_step = 0

            # Th value of the bar
            self.bar_value = 0

            # The range of the bar
            self.bar_range = 1

            # Check to see if we can show bar

        def valuation(self, st, limit):
            header = "Startup Valuation: "

            if store.current_sprint > 0:
                tag = "{color=#00ff00}$"
            else:
                tag = "{color=#ff0000}$"

            symbol = " (+$" if store.current_sprint > 0 else " (-$"

            return Text(tag + "{:,}".format(store.money) + symbol + "{:,}".format(store.current_sprint) + "){/color}")

        def fl(self, st, limit):
            # If enough time had not passed, don't show the text
            if st < limit:
                return Text("")

            if self.updated_fl:
                return Text("{color=#00ff00}" + str(self.founder_level) + "{/color}")
            else:
                return Text(str(last_founder_level), color="#000000")

        def bar(self, st, limit):
            if st < limit:
                return Bar(range=FOUNDER_INDEX[self.founder_level][1], value=store.money - store.current_sprint, height=20)

            if self.money != store.money:
                self.money = store.money

                # Find the money Founder had before this sprint
                self.old_money = store.money - store.current_sprint

                # Set the Bar range to the current Founder Level milestone
                self.bar_range = FOUNDER_INDEX[self.founder_level][1]
                self.bar_value = self.old_money

                # Find the last money milestone
                last_money_milestone = FOUNDER_INDEX[self.founder_level-1][1]

                # Find the steps by which the bar will be updated
                self.review_step = store.current_sprint * 3000 / self.bar_range

            # If the bar is full, check to see if we can update the bar to a new one
            if self.bar_value >= self.bar_range:
                self.updated_fl = True
                self.founder_level += 1
                self.bar_value = 0
                self.bar_range = FOUNDER_INDEX[self.founder_level][1] - self.bar_range

            # Update the bar
            if self.old_money < self.money:
                self.bar_value += self.review_step
                self.old_money += self.review_step

            if self.updated_fl:
                status = "Founder Status: {color=#00ff00}" + FOUNDER_INDEX[self.founder_level][0] + "{/color}"
            else:
                status = "Founder Status: " + FOUNDER_INDEX[self.founder_level][0]

            return VBox(Bar(range=self.bar_range, value=self.bar_value, height=10), Text(str(self.old_money) + "/" + str(FOUNDER_INDEX[self.founder_level][1]), color="#000000", xalign=0.5), Text(status, xalign=0.5, color="#000000"), spacing=10, xalign=0.5)

    def dynamic_bar(st, at, bar):
        return bar.displayable(st), 0.1

    def dynamic_review(st, at, d, limit):
        return d(st, limit), 0.1
