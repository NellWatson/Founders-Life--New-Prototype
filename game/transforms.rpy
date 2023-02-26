transform flash:
    alpha 1.0

    linear 0.5 alpha 0.5
    linear 0.5 alpha 1.0
    
    repeat

transform flash_fast:
    on idle:
        alpha 1.0

        linear 0.4 alpha 0.25
        linear 0.4 alpha 1.0
        
        repeat

transform zoom_out(factor):
    subpixel True
    zoom factor

transform set_size(x, y):
    size (x, y)

transform flash_zoom:
    alpha 1.0
    zoom 1.05
    
    xanchor 0.5
    yanchor  0.5
    xoffset 70
    yoffset 70

    block:
        parallel:
            linear 0.75 alpha 0.8
        parallel:
            linear 0.75 zoom 0.95
    block:
        parallel:
            linear 0.75 alpha 1.0
        parallel:
            linear 0.75 zoom 1.05

    repeat

transform slide_down_center:
    alpha 0.0
    xalign 0.5
    yalign -0.05

    on show:
        parallel:
            linear 0.7 alpha 1.0
        parallel:
            linear 0.7 yalign 0.05

    on hide:
        parallel:
            linear 0.7 alpha 0.0
        parallel:
            linear 0.7 yalign -0.05

transform im_center:
    xalign 0.5
    yalign 0.45
    alpha 0.0

    linear 0.75 alpha 1.0

transform button_hover:
    anchor (0.5, 0.5)
    on idle:
        alpha 1.0
        zoom 0.99

    on hover:
        parallel:
            linear 0.6 alpha 0.8
            linear 0.6 alpha 1.0
        parallel:
            linear 0.6 zoom 1.1
            linear 0.6 zoom 0.99

        repeat

transform credits_scroll(speed, wait_for):
    time wait_for
    subpixel True
    linear speed ypos -2430

transform hide_in(t):
    time t
    linear 0.5 alpha 0.0
