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
            self.step = 0

        def displayable(self, st):
            current = getattr(store, self.var)

            # Check to see if the variable value has changed
            if current != self.last_value:
                self.delta += self.last_value - current
                self.step = self.delta / 30.0

            # If the variable value decreased
            if self.delta > 0.001:
                d = self.dec
                v = current + self.delta
                self.delta -= self.step

            # If the variable value increased
            elif self.delta < -0.001:
                d = self.inc
                v = self.last_value + self.delta
                self.delta -= self.step
            else:
                d = self.base
                v = current
                self.delta = 0
                self.step = 0

            self.last_value = current

            if self.delta or current <= 10:
                return At(Bar(value=v, range=100, left_bar=Solid(d), right_bar=Color(d).shade(0.75), **self.properties), flash)
            else:
                return Bar(value=v, range=100, left_bar=Solid(d), right_bar=Color(d).shade(0.75), **self.properties)

    def dynamic_bar(st, at, bar):
        return bar.displayable(st), 0.1
