style fl_button:
    idle_background Frame("gui/frame/idle.png", 1, 1)
    hover_background Frame("gui/frame/hover.png", 1, 1)
    selected_background Frame("gui/frame/idle.png", 1, 1)
    insensitive_background Frame("gui/frame/inactive.png", 1, 1)
    
    xsize 650

style fl_button_text:
    font "fonts/Dosis-Bold.ttf"
    size 45
    color "#ffffff"
    xalign 0.5
    yalign 0.5

style fl_text:
    font "fonts/Dosis-Light.ttf"
    bold True
    size 50
    color "#ffffff"
    
style feedback_text:
    font "fonts/Dosis-Bold.ttf"
    size 70
    color "#ffffff"

style hud_text:
    font "fonts/Dosis-Bold.ttf"
    color "#559fdd"
    size 45
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
