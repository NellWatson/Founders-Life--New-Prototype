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
            if effect:
                return At(Text(str(value), color="#000000"), effect), None
            else:
                return Text(str(value), color="#000000"), None

    def dynamic_show(st, at, req_st, d):
        if req_st > st:
            return Text(""), .1
        else:
            return d, None

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

    use fl_window("startup_preview", "SPRINT REVIEW", colour="#559fdd", width=900, height=600, cross=False):
        vbox:
            xsize 800
            xalign 0.5
            spacing 20

            add "images/icons/" + startup_icon zoom 0.3 xalign 0.5
            text "Another sprint completed [founder_name]" color "#000000" xalign 0.5

            grid 2 6:
                xpos 150
                spacing 10

                text "Energy Remaining Bonus      " color "#000000"
                text DynamicDisplayable(dynamic_show_text, 1, energy) color "#000000"
                
                text "Morale Remaining Bonus" color "#000000"
                text DynamicDisplayable(dynamic_show_text, 2, morale) color "#000000"
                
                text "Days as Founder Bonus" color "#000000"
                text DynamicDisplayable(dynamic_show_text, 3, month*30) color "#000000"
                
                text "Founder XP Level Bonus" color "#000000"
                text DynamicDisplayable(dynamic_show_text, 4, founder_level) color "#000000"
                
                text "{b}Valued Added{/b}" color "#000000"
                text DynamicDisplayable(dynamic_show_text, 5, "{b}$[current_sprint]{/b}") color "#000000"

                text "{b}Startup Valuation{/b}" color "#000000"
                text DynamicDisplayable(dynamic_show_text, 6, "{color=#00ff00}{b}$[money]{/b}{/color}", flash) color "#000000"

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

    default next_xp = FOUNDER_INDEX[founder_level+1][1] if founder_level < 11 else 100000000000

    use fl_window("startup_preview", founder_name, colour="#559fdd", width=900, height=550, cross=False):
        vbox:
            xalign 0.5
            spacing 10

            text "[startup_name]" color "#000000" xalign 0.5
            add "images/icons/" + startup_icon zoom 0.3 xalign 0.5
            if level_up:
                text DynamicDisplayable(dynamic_show_text, 1, "Startup Valuation: {color=#00ff00}$[money] (+$[current_sprint]{/color})", flash, default="") xalign 0.5
                text DynamicDisplayable(dynamic_show_text, 2, "Founder Level: {color=#00ff00}[founder_level]{/color}", flash, default="") xalign 0.5
            else:
                text DynamicDisplayable(dynamic_show_text, 1, "Startup Valuation: $[money] ({color=#00ff00}+$[current_sprint]{/color})", default="") xalign 0.5
                text DynamicDisplayable(dynamic_show_text, 2, "Founder Level: [founder_level]", default="") xalign 0.5
            text " " size 7
            add DynamicDisplayable(dynamic_show, 3, Bar(value=AnimatedValue(value=money, range=next_xp, delay=2, old_value=0), ysize=10)) xalign 0.5
            text DynamicDisplayable(dynamic_show_text, 5, "[money] / " + str(next_xp), default="") xalign 0.5
            text DynamicDisplayable(dynamic_show_text, 6, "Founder Status: {color=#00ff00}" + FOUNDER_INDEX[founder_level][0] + "{/color}", default="") xalign 0.5

        textbutton _("CONTINUE"):
            idle_background("#d3d3d3")
            hover_background Solid( Color("#d3d3d3").tint(0.5) )
            selected_background Solid( Color("#d3d3d3").shade(0.5) )

            action Return()

            xalign 0.5
            yalign 0.99
