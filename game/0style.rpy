style fl_button:
    idle_background Frame("gui/frame/idle.png", 1, 1)
    hover_background Frame("gui/frame/hover.png", 1, 1)
    selected_background Frame("gui/frame/idle.png", 1, 1)
    insensitive_background Frame("gui/frame/inactive.png", 1, 1)

    xsize 650

style fl_button_text:
    font "fonts/Dyslexie_Bold_159164.ttf"
    size 36
    color "#ffffff"
    xalign 0.5
    yalign 0.5

style fl_text:
    font "fonts/Dyslexie_Regular_159164.ttf"
    bold True
    size 36
    color "#ffffff"

style feedback_text:
    font "fonts/Dyslexie_Bold_159164.ttf"
    size 48
    color "#ffffff"

style hud_text:
    font "fonts/Dyslexie_Bold_159164.ttf"
    color "#559fdd"
    size 36
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
