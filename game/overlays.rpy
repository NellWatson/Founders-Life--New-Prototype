screen hud():
    if check["confirm"]:
        key "dismiss" action [SetDict(check, "energy", ""), SetDict(check, "morale", ""), SetDict(check, "money", ""), SetDict(check, "confirm", False), Function(renpy.IgnoreEvent)]

    if event_name:
        frame:
            xalign 0.5
            ypos -5

            xsize 300
            ysize 55

            text "[event_name]" xalign 0.5 yalign 0.6

    frame:
        xpos 25
        ypos 40

        xsize 320
        ysize 720

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 70

            text "Founder Weeks: {0:02d}".format(turn_no) size 30 xalign 0.5

            vbox:
                xalign 0.5
                spacing 10
                
                text "ENERGY" xalign 0.5
                text "[energy]" xalign 0.5

                if check["energy"]:
                    text check["energy"] xalign 0.5 at flash
                else:
                    null height 40

            vbox:
                xalign 0.5
                spacing 10
                
                text "MORALE" xalign 0.5
                text "[morale]" xalign 0.5

                if check["morale"]:
                    text check["morale"] xalign 0.5 at flash
                else:
                    null height 40

            vbox:
                xalign 0.5
                spacing 10
                
                text "CASH" xalign 0.5
                text "[CURRENCY]" + "[money]" xalign 0.5

                if check["money"]:
                    text check["money"] xalign 0.5 at flash
                else:
                    null height 40
