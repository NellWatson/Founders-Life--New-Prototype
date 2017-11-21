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
    add Solid("#dfdfdf")

    vbox:
        xalign 0.90
        ypos 100
        spacing 5

        text "Score: {:,}".format(founder_score) size 45 color "#000000" xalign 1.0
        text "Weeks as Founder: {}".format(week) size 45 color "#000000" xalign 1.0

    vbox:
        xalign 0.10
        ypos 100
        spacing 5

        text "[founder_name]" size 45 color "#000000" text_align 1.0
        text "[startup_name]" size 45 color "#000000" text_align 1.0

    hbox:
        xalign 0.5
        yalign 0.5

        for i in range(1, 6):
            if i < current_episode:
                add Fixed(Circle(100, "#00ff00"), Text(str(i), color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)
            elif i == current_episode:
                add Fixed(Circle(100, "#00a1ff"), Text(str(i), color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200) at flash
            else:
                add Fixed(Circle(100, "#00a1ff"), Text(str(i), color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)

            if i != 5:
                if i >= current_episode:
                    add Solid("#00a1ff", xysize=(200, 10)) yalign 0.5
                else:
                    add Solid("#00ff00", xysize=(200, 10)) yalign 0.5

    fixed:
        xalign 0.5
        ypos 360

        use fl_window("err_msg", "EPISODE " + str(current_episode), colour="#559fdd", width=600, height=100, show_button="Let's go!", underlay=False):
            vbox:
                xalign 0.5
                yalign 0.5

                text EPISODE_NAMES[current_episode-1] color "#000000"
