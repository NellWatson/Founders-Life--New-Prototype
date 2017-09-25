screen hud():
    frame:
        xsize 1920
        ysize 160

        text "Founder Days: {0:02d}".format(turn_no) size 30 xalign 0.05 yalign 0.5

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            
            hbox:
                xalign 0.5
                yalign 0.5

                spacing 20

                text "Energy" yalign 0.5 xoffset -44
                add DynamicDisplayable(dynamic_bar, energy_bar) xoffset 41
            
            hbox:
                xalign 0.5
                yalign 0.5
                spacing 20

                text "Mindfulness" yalign 0.5
                add DynamicDisplayable(dynamic_bar, morale_bar)
            
        hbox:
            xalign 0.95
            yalign 0.5
            spacing 20

            text "Money: $[money]" yalign 0.5
