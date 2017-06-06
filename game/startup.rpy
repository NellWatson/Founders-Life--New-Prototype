init python:

    def return_random_ele(l, limit):
        _random_list = []

        for i in range(0, limit):
            ele = renpy.random.choice(l)

            while ele in _random_list:
                ele = renpy.random.choice(l)
            _random_list.append(ele)

        return _random_list

label set_startup:
    show nell bot at center with dissolve

    n "Welcome I'm Nell, your mentor.
    I'll be helping you out as you embark upon your exciting journey as a founder."

    $ founder_name = renpy.input("What's your name:") or "Founder"
    $ startup_name = renpy.input("What's your startup name:") or "StartUP Inc"

    show screen startup_sector
    n "What's your startup sector?"

    show screen startup_logo
    n "What's your startup logo?"
    
    jump checkpoint

screen startup_sector():
    modal True
    zorder 100

    default fields = return_random_ele(STARTUP_FIELDS, 6)

    for i in range(0, 6):
        textbutton _(fields[i]):
            xsize 540

            idle_background "#ffff00"
            hover_background "#00ff00"

            text_color "#000000"
            text_text_align 0.5

            action [SetVariable("startup_field", fields[i]), Hide("startup_sector")]

            xpos 80 + (i%3) * 600
            if i < 3:
                ypos 930
            else:
                ypos 1000

screen startup_logo(_transient=True):
    modal True
    zorder 100

    default fields = return_random_ele(STARTUP_ICONS, 3)

    hbox:
        xalign 0.5
        ypos 930
        spacing 300

        for i in range(0, 3):
            button:
                xysize(128, 128)

                idle_background Solid("#d3d3d3")
                hover_background Solid( Color("#d3d3d3").tint(0.5) )
                selected_background Solid( Color("#d3d3d3").shade(0.5) )

                add "images/icons/" + fields[i] zoom 0.20 xalign 0.5 yalign 0.5

                action [SetVariable("startup_icon", fields[i]), Hide("startup_logo")]

screen startup_review(bg):
    add bg
    add Solid("#00000050")

    use fl_window("startup_preview", startup_name, colour="#559fdd", width=900, height=550, cross=False):
        vbox:
            xsize 800
            xalign 0.5
            spacing 20

            add "images/icons/" + startup_icon zoom 0.3 xalign 0.5
            text "Another sprint completed [founder_name]" color "#000000" xalign 0.5

            grid 2 5:
                xpos 150
                spacing 10

                text "Energy Remaining Bonus      " color "#000000"
                text "[energy]" color "#000000"
                
                text "Morale Remaining Bonus" color "#000000"
                text "[morale]" color "#000000"
                
                text "Days as Founder Bonus" color "#000000"
                text str(month * 30) color "#000000"
                
                text "Founder XP Level Bonus" color "#000000"
                text "[founder_level]" color "#000000"
                
                text "{b}Sprint Score{/b}" color "#000000"
                text "{b}[current_sprint]{/b}" color "#000000"

        textbutton _("CONTINUE"):
            idle_background("#d3d3d3")
            hover_background Solid( Color("#d3d3d3").tint(0.5) )
            selected_background Solid( Color("#d3d3d3").shade(0.5) )

            action Return()

            xalign 0.5
            yalign 0.99

screen level_up(bg):
    add bg
    add Solid("#00000050")

    use fl_window("startup_preview", startup_name, colour="#559fdd", width=900, height=500, cross=False):
        vbox:
            xalign 0.5
            spacing 25

            add "images/icons/" + startup_icon zoom 0.3 xalign 0.5
            text "Founder Level: {color=#00ff00}[founder_level]{/color}" color "#000000" xalign 0.5
            text "Founder Status: {color=#00ff00}" + FOUNDER_INDEX[founder_level][0] + "{/color}" color "#000000" xalign 0.5
            text "Startup Valuation = $[money] (+$[current_sprint])" color "#000000" xalign 0.5

        textbutton _("CONTINUE"):
            idle_background("#d3d3d3")
            hover_background Solid( Color("#d3d3d3").tint(0.5) )
            selected_background Solid( Color("#d3d3d3").shade(0.5) )

            action Return()

            xalign 0.5
            yalign 0.99
