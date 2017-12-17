init python:

    def return_random_ele(l, limit):
        _random_list = []

        for i in range(0, limit):
            ele = renpy.random.choice(l)

            while ele in _random_list:
                ele = renpy.random.choice(l)
            _random_list.append(ele)

        return _random_list

    def dynamic_show_text(st, at, req_st, value, effect=None, default="0"):
        if req_st > st:
            return Text(default, color="#000000"), .1
        else:
            if req_st < 4:
                renpy.sound.play("sfx/fx008.wav")
            if effect:
                if type(value) == int:
                    return At(Text("{:,}".format(value), color="#000000"), effect), None
                else:
                    return At(Text(value, color="#000000"), effect), None
            else:
                if type(value) == int:
                    return Text("{:,}".format(value), color="#000000"), None
                else:
                    return Text(value, color="#000000"), None

    def dynamic_show(st, at, req_st, d):
        if req_st > st:
            return Text(""), .1
        else:
            return d, None

screen startup_sector():
    modal True
    zorder 100

    default fields = return_random_ele(STARTUP_FIELDS, 6)

    for i in range(0, 6):
        button:
            xsize 400

            idle_background "#ffff00"
            hover_background "#00ff00"

            if len(fields[i]) > 20:
                text fields[i] size 27 color "#000000" xalign 0.5 yalign 0.5
            else:
                text fields[i] color "#000000" xalign 0.5 yalign 0.5

            action [SetVariable("startup_field", fields[i]), Hide("startup_sector")]

            xpos 440 + (i%3) * 450
            if i < 3:
                ypos 895
            else:
                ypos 965

screen startup_logo(_transient=True):
    modal True
    zorder 100

    default fields = return_random_ele(STARTUP_ICONS, 3)

    hbox:
        xpos 440
        ypos 887
        spacing 250

        for i in range(0, 3):
            button:
                xysize(128, 128)

                idle_background Solid("#559fdd")
                hover_background Solid( Color("#559fdd").shade(0.5) )
                selected_background Solid( Color("#559fdd").tint(0.5) )

                add "images/icons/" + fields[i] zoom 0.20 xalign 0.5 yalign 0.5

                action [SetVariable("startup_icon", fields[i]), Hide("startup_logo")]

screen sprint_review(bg):
    on "show":
        action Play("sound", "sfx/fx009.wav")
        
    add "bg review"

    default review = ReviewB()

    use fl_window("startup_preview", "WEEKLY SPRINT COMPLETED", colour="#559fdd", width=900, height=440, cross=False):
        vbox:
            xsize 800
            xalign 0.5
            spacing 10
            first_spacing 40

            text "[founder_name]" color "#000000" xalign 0.5
            text "Founder Points Earned: {:,}".format(founder_score) color "#000000" xalign 0.5

            null height 1.0
            add DynamicDisplayable(dynamic_review, review.bar, 0.25) xalign 0.5
            
            null height 16.0
            text "Total Founder Points: {:,}".format(total_founder_score) color "#000000" xalign 0.5

        textbutton _("Let's Go"):
            idle_background("#d3d3d3")
            hover_background Solid( Color("#d3d3d3").tint(0.5) )
            selected_background Solid( Color("#d3d3d3").shade(0.5) )

            action Return()

            xalign 0.5
            yalign 0.99

    if trophy_shelf.show_trophy_icon:
        imagebutton:
            idle circular_buttons(80, "#ffffff", "gui/achievements/achievement.png")
            hover circular_buttons(80, "#dfdfdf", "gui/achievements/achievement.png")

            action Show("achievement_screen", shelf=trophy_shelf)

            xalign 0.02
            yalign 0.02

            if trophy_shelf.unseen:
                at flash_zoom

screen startup_review(bg):
    add "bg review"

    use fl_window("startup_preview", "SPRINT REVIEW", colour="#559fdd", width=900, height=550, cross=False):
        vbox:
            xsize 800
            xalign 0.5
            spacing 10

            null height 1.0
            text "Another sprint completed [founder_name]" color "#000000" xalign 0.5
            null height 8.0

            grid 2 7:
                xpos 200
                spacing 10

                text "Productivity" color "#000000"
                text DynamicDisplayable(dynamic_show_text, 0.75, productivity)
                
                text "Energy" color "#000000"
                text DynamicDisplayable(dynamic_show_text, 1.5, energy)
                
                text "Mindfulness" color "#000000"
                text DynamicDisplayable(dynamic_show_text, 2.25, morale)
                
                text "Cashflow" color "#000000"
                hbox:
                    text "$" color "#000000"
                    text DynamicDisplayable(dynamic_show_text, 3, money)
                
                text "Days as Founder   " color "#000000"
                text DynamicDisplayable(dynamic_show_text, 3.75, turn_no)
                
                null height 1.0
                null height 1.0

                text "{b}Founder Points Earned{/b}" color "#000000"
                text DynamicDisplayable(dynamic_show_text, 4.5, founder_score)

        textbutton _("CONTINUE"):
            idle_background("#d3d3d3")
            hover_background Solid( Color("#d3d3d3").tint(0.5) )
            selected_background Solid( Color("#d3d3d3").shade(0.5) )

            action Return()

            xalign 0.5
            yalign 0.99

screen level_up(bg):

    on "hide":
        action With(dissolve)
        
    add bg
    add Solid("#00000050")

    default next_xp = FOUNDER_INDEX[founder_level+1][1] if founder_level < 11 else 100000000000
    default review = ReviewB()

    use fl_window("startup_preview", founder_name, colour="#559fdd", width=900, height=575, cross=False):
        vbox:
            xsize 900
            xalign 0.5
            spacing 10

            text "[startup_name]" color "#000000" xalign 0.5
            add "images/icons/" + startup_icon zoom 0.3 xalign 0.5

            grid 2 2:
                transpose True
                spacing 10

                xalign 0.5

                text "Startup Valuation: " color "#000000"
                text "Founder Level: " color "#000000"

                text DynamicDisplayable(dynamic_review, review.valuation, 0.0) xalign 0.5
                text DynamicDisplayable(dynamic_review, review.fl, 1.0) xalign 0.5

            text " " size 7
            add DynamicDisplayable(dynamic_review, review.bar, 2.0) xalign 0.5

        textbutton _("CONTINUE"):
            idle_background("#d3d3d3")
            hover_background Solid( Color("#d3d3d3").tint(0.5) )
            selected_background Solid( Color("#d3d3d3").shade(0.5) )

            action Return()

            xalign 0.5
            yalign 0.999
