screen hud():
    frame:
        xsize 1920
        ysize 160

        background Solid("#ffffff")

        text "Days as Founder: {0:02d}".format(total_days) size 30 color "#000000" xalign 0.05 yalign 0.15
        if config.developer:
            hbox:
                xalign 0.05
                yalign 0.80
                spacing 5
                
                text "[event_code]" color "#000000" yalign 0.5

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 8
            
            hbox:
                xalign 0.5
                yalign 0.5

                spacing 7

                add "gui/hud/productivity.png" yalign 0.5 xoffset -44
                add DynamicDisplayable(dynamic_bar, productivity_bar)
            hbox:
                xalign 0.5
                yalign 0.5

                spacing 7

                add "gui/hud/energy.png" yalign 0.5 xoffset -44
                add DynamicDisplayable(dynamic_bar, energy_bar)
            
            hbox:
                xalign 0.5
                yalign 0.5
                spacing 7

                add "gui/hud/morale.png" yalign 0.5 xoffset -44
                add DynamicDisplayable(dynamic_bar, morale_bar)
        
        hbox:
            xalign 0.95
            yalign 0.15
            
            text "Savings: " color "#000000"
            if check["money"]:
                text check["money"] color "#000000" at flash
            else:
                text "${:,}".format(money) color "#000000"

        if config.developer:
            hbox:
                xalign 0.96
                yalign 0.70
                
                textbutton _("Event Play Order") action Show("event_play_list")

screen founder_map():
    add "bg review"

    vbox:
        xalign 0.90
        ypos 100
        spacing 5

        text "Founder Score: {:,}".format(total_founder_score) size 45 color "#000000" xalign 1.0
        text "Days as Founder: {}".format(turn_no) size 45 color "#000000" xalign 1.0

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
            if i < current_chapter:
                add Fixed(Circle(100, "#00ff00"), Text(str(i), color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)
            elif i == current_chapter:
                add Fixed(Circle(100, "#ffff00"), Text(str(i), color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200) at flash
            else:
                add Fixed(Circle(100, "#dfdfdf"), Text(str(i), color="#ffffff", size=52, xalign=0.5, yalign=0.5), xsize=200, ysize=200)

            if i != 5:
                if i >= current_chapter:
                    add Solid("#00a1ff", xysize=(200, 10)) yalign 0.5
                else:
                    add Solid("#00ff00", xysize=(200, 10)) yalign 0.5

    fixed:
        xalign 0.5
        ypos 360

        use fl_window("err_msg", "EPISODE " + str(current_chapter), colour="#559fdd", width=600, height=100, show_button="Let's go!", underlay=False):
            vbox:
                xalign 0.5
                yalign 0.5

                text EPISODE_NAMES[current_chapter-1] color "#000000"

screen character_intro():
    default character_list = ["skylar", "takashi", "roger"]
    add Solid("#00000000") alpha 0.5

    text "Who is with you?"  size 60 color "#000000" xalign 0.5 yalign 0.25

    hbox:
        xalign 0.5
        yalign 0.55
        spacing 40

        for i in character_list:
            button:
                xysize (309, 310)

                background "gui/who.png"
                add "images/contacts/" + i + ".png" xalign 0.5 yalign 0.5 xoffset 1 yoffset 4

                action Call(i + "_intro")

    textbutton _("Let's Start the Journey"):
        style "fl_button"

        action Jump("checkpoint")

        xalign 0.5
        yalign 0.85
