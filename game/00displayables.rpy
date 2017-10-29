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
            self.founder_level = last_founder_level
            self.founder_status = "founder_status"
            self.colour = "#00ff00"

            self.updated_fl = False

            # The current Founder Score of player
            self.total_founder_score = 0

            # The old Founder Score of player
            self.old_founder_score = 0

            # The step by which the bar should update
            self.review_step = 0

            # Th value of the bar
            self.bar_value = 0

            # The range of the bar
            self.bar_range = 1

        def valuation(self, st, limit):
            header = "Startup Valuation: "

            if store.current_sprint > 0:
                tag = "{color=#00ff00}$"
                symbol = "(+$"
                end_tag = "){/color}"

            elif store.current_sprint == 0:
                tag = "$"
                symbol = "(+$"
                end_tag = ")"

            else:
                tag = "{color=#ff0000}$"
                symbol = "(-$"
                end_tag = "){/color}"

            return Text(tag + "{:,}".format(store.money) + symbol + "{:,}".format(store.current_sprint) + end_tag, color="#000000")

        def fl(self, st, limit):
            # If enough time had not passed, don't show the text
            if st < limit:
                return Text("")

            if self.updated_fl:
                return Text("{color=#00ff00}" + str(self.founder_level) + "{/color}")
            else:
                return Text(str(last_founder_level), color="#000000")

        def bar(self, st, limit):
            # Wait for 'st' time before starting to update the bar
            if st < limit:
                return Bar(range=FOUNDER_INDEX[self.founder_level][1], value=store.total_founder_score - store.founder_score, height=20)

            # If the current Founder Score and stored Founder score don't match, update them before continuing
            if self.total_founder_score != store.total_founder_score:
                self.total_founder_score = store.total_founder_score

                # Find the Founder Score player had before this sprint
                self.founder_score = store.total_founder_score - store.founder_score

                # Set the Bar range to the current Founder Level milestone
                self.bar_range = FOUNDER_INDEX[self.founder_level][1]
                self.bar_value = self.founder_score

                # Find the steps by which the bar will be updated
                print store.founder_score, self.bar_range
                self.review_step = store.founder_score * 3000 / self.bar_range

            # If the bar is full, check to see if we can update the bar to a new one
            if self.bar_value >= self.bar_range:
                self.updated_fl = True
                self.founder_level += 1
                self.bar_value = 0
                self.bar_range = FOUNDER_INDEX[self.founder_level][1] - self.bar_range

            # Update the bar
            if self.founder_score < self.total_founder_score:
                self.bar_value += self.review_step
                self.founder_score += self.review_step
            else:
                self.founder_score = self.total_founder_score

            if self.updated_fl:
                status = "Founder Status: {color=#00ff00}" + FOUNDER_INDEX[self.founder_level][0] + "{/color}"
            else:
                status = "Founder Status: " + FOUNDER_INDEX[self.founder_level][0]

            return Bar(range=self.bar_range, value=self.bar_value, height=10)

    def dynamic_bar(st, at, bar):
        return bar.displayable(st), 0.1

    def dynamic_review(st, at, d, limit):
        return d(st, limit), 0.01
