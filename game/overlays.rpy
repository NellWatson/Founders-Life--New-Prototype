screen hud():
    frame:
        xsize 1920
        ysize 160

        background Solid("#d3d3d3")

        text "Days as Founder: {0:02d}".format(turn_no) size 30 color "#000000" xalign 0.05 yalign 0.15

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 8
            
            hbox:
                xalign 0.5
                yalign 0.5

                spacing 7

                add "images/gui/Productivity/rocket-32.png" yalign 0.5 xoffset -44
                add DynamicDisplayable(dynamic_bar, productivity_bar)
            hbox:
                xalign 0.5
                yalign 0.5

                spacing 7

                add "images/gui/Energy/charge_battery-32.png" yalign 0.5 xoffset -44
                add DynamicDisplayable(dynamic_bar, energy_bar)
            
            hbox:
                xalign 0.5
                yalign 0.5
                spacing 7

                add "images/gui/Mindfulness/meditation_guru-32.png" yalign 0.5 xoffset -44
                add DynamicDisplayable(dynamic_bar, morale_bar)
        
        hbox:
            xalign 0.95
            yalign 0.15
            
            text "Savings: " color "#000000"
            if check["money"]:
                text check["money"] color "#000000" at flash
            else:
                text "${:,}".format(money) color "#000000"

screen founder_map():
    add Solid("#ffffff")

    vbox:
        xalign 0.90
        ypos 100
        spacing 5

        text "                    Score: 0" size 45 color "#000000" text_align 1.0
        text "Weeks as Founder: 0" size 45 color "#000000" text_align 1.0

    vbox:
        xalign 0.10
        ypos 100
        spacing 5

        text "[founder_name]" size 45 color "#000000" text_align 1.0
        text "[startup_name]" size 45 color "#000000" text_align 1.0

    hbox:
        xalign 0.5
        yalign 0.5

        imagebutton:
            idle Fixed(Circle(100, "#00a1ff"), Text("1", color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)
            hover Fixed(Circle(100, "#00ff00"), Text("1", color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)

            action Return()

            at flash
        add Solid("#00a1ff", xysize=(200, 10)) yalign 0.5

        imagebutton:
            idle Fixed(Circle(100, "#00a1ff"), Text("2", color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)
            hover Fixed(Circle(100, "#00ff00"), Text("2", color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)

            action Show("warn_msg", message="Finish Chapter 1 first.", hide_anyway=True)
        add Solid("#00a1ff", xysize=(200, 10)) yalign 0.5

        imagebutton:
            idle Fixed(Circle(100, "#00a1ff"), Text("3", color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)
            hover Fixed(Circle(100, "#00ff00"), Text("3", color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)

            action Show("warn_msg", message="Finish Chapter 1 first.", hide_anyway=True)
        add Solid("#00a1ff", xysize=(200, 10)) yalign 0.5

        imagebutton:
            idle Fixed(Circle(100, "#00a1ff"), Text("4", color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)
            hover Fixed(Circle(100, "#00ff00"), Text("4", color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)

            action Show("warn_msg", message="Finish Chapter 1 first.", hide_anyway=True)
        add Solid("#00a1ff", xysize=(200, 10)) yalign 0.5

        imagebutton:
            idle Fixed(Circle(100, "#00a1ff"), Text("5", color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)
            hover Fixed(Circle(100, "#00ff00"), Text("5", color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)

            action Show("warn_msg", message="Finish Chapter 1 first.", hide_anyway=True)
