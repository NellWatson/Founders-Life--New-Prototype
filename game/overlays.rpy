init python:
    check = {

    "energy": 0,
    "morale": 0,
    "money": 0
    }

    def variable(name, value):
        old_value = getattr(store, name)
        new_value = old_value + value

        if old_value > new_value:
            store.check[name] = -1
        elif old_value < new_value:
            store.check[name] = 1
        else:
            store.check[name] = 0

        setattr(store, name, new_value)
        return

    def counter(name):
        value = getattr(store, name)

        if check[name] == -1:
            check[name] = 0
            return "{color=#ff0000}" + str(value) + "{/color}"
        elif check[name] == 1:
            check[name] = 0
            return "{color=#00ff00}" + str(value) + "{/color}"
        else:
            return str(value)

screen hud():
    frame:
        xpos 25
        yalign 0.5

        xsize 320
        ysize 960

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 100

            vbox:
                spacing 10
                text "ENERGY" xalign 0.5
                text counter("energy") xalign 0.5

            vbox:
                spacing 10
                text "MORALE" xalign 0.5
                text counter("morale") xalign 0.5

            vbox:
                spacing 10
                text "CASH" xalign 0.5
                text "[CURRENCY]" + counter("money") xalign 0.5
