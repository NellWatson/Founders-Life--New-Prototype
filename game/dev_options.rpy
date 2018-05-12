init python:
    from collections import OrderedDict
    import json
    import datetime

    SORT_DATA = {
        "achievements": "Achivements",
        "choice": "Choices",
        "mainmenu": "Main menu elements",
        "bg": "Background",
        "contacts": "Sprites for In game Characters",
        "intro": "KPI Icon images show during during Intro"
    }

    def image_details():
        image_data = OrderedDict({})
        for file in renpy.list_files():
            if (".png" in file or ".jpg" in file or ".webp" in file) and "icons" not in file:
                pass
            else:
                continue

            x, y = renpy.image_size(file)
            key = file.split("/")[1]
            desc = SORT_DATA.get(key, "Default GUI element")
            if "window_icon" in file:
                desc = "Game icon"

            image_data[file] = {
                "Extenstion": file.split(".")[1],
                "Width": x,
                "Height": y,
                "Information": desc
            }

        return image_data

    def write_data(image_data):
        with open((renpy.game.basepath + "/image_data.json"), "a") as data:
            data.write("{}\n".format(json.dumps(image_data)))

screen image_data_screen():
    zorder 10
    modal True

    default data = image_details()
    default showing_image = Null()

    add Solid("#000000") alpha 0.5
    add showing_image xalign 1.0 yalign 0.5

    vpgrid:
        area (0, 0, 1920, 1080)
        child_size (1920, 34440)

        draggable True
        mousewheel True

        cols 2

        vbox:
            spacing 20

            for path, details in data.iteritems():
                button:
                    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
                    xsize 940
                    ysize 248

                    vbox:
                        spacing 5

                        text "Path: [path]"
                        for line, value in details.iteritems():
                            text "[line]: [value]"

                    action SetScreenVariable("showing_image", path)

    textbutton _("Save"):
        text_color "#ffffff"
        action Function(write_data, image_data=data)

        xalign 1.0
        yalign 0.0
