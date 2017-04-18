screen hud():
    if check["confirm"]:
        key "dismiss" action [SetDict(check, "energy", ""), SetDict(check, "morale", ""), SetDict(check, "money", ""), SetDict(check, "confirm", False), Function(renpy.IgnoreEvent)]
    frame:
        xpos 25
        yalign 0.5

        xsize 320
        ysize 960

        text "Month: {0:02d}".format(divmod(turn_no, 4)[0] + 1) size 45 xalign 0.5 ypos 20

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 100

            vbox:
                spacing 10
                text "ENERGY" xalign 0.5
                text "[energy]" xalign 0.5

                if check["energy"]:
                    text check["energy"] xalign 0.5 at flash
                else:
                    null height 40

            vbox:
                spacing 10
                text "MORALE" xalign 0.5
                text "[morale]" xalign 0.5

                if check["morale"]:
                    text check["morale"] xalign 0.5 at flash
                else:
                    null height 40

            vbox:
                spacing 10
                text "CASH" xalign 0.5
                text "[CURRENCY]" + "[money]" xalign 0.5

                if check["money"]:
                    text check["money"] xalign 0.5 at flash
                else:
                    null height 40
