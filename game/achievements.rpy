init python early:

    class Shelf():

        def __init__(self, name, locked_image, locked_colour, limit):
            self.name = name
            self.locked_image = locked_image
            self.locked_colour = locked_colour
            self.limit = limit

            self.show_trophy_icon = False
            self.unseen = True
            self.store = []

        def create_achievement(self, title, description, image, colour, unlock_level, link=""):
            ach = Achievement(title, description, image, colour, unlock_level, self.locked_image, self.locked_colour, link=link)

            self.store.append(ach)

        def add_achievement(self, ach):
            ach.locked_image = self.locked_image
            ach.locked_colour = self.locked_colour

            self.store.append(ach)

        def check_unlock(self, current_level):
            for ach in self.store:
                if not ach.unlocked and current_level > ach.unlock_level:
                    ach.unlocked = True
                    self.show_trophy_icon = True

                    return ach.title

        def __eq__(self, other):
            return self.name == other
            
    class Achievement():

        def __init__(self, title, description, image, colour, unlock_level, locked_image=None, locked_colour=None, add_to_shelf=None, link=""):
            self.title = title
            self.description = description
            self.image = image
            self.colour = colour
            self.unlock_level = unlock_level

            self.unlocked = True
            self.locked_image = locked_image
            self.locked_colour = locked_colour

            self.link = link

            if add_to_shelf:
                shelf.add_achievement(self)

        @property
        def get_image(self):
            return self.image if self.unlocked else self.locked_image

init python:

    def create_leaderboard_data():
        persistent.leaderboard = []
        
        persistent.trophy_shelf = Shelf("Achievements", "gui/achievements/locked.png", "#66A8E0", 6)
        persistent.trophy_shelf.create_achievement(
            title="Ja-Naé Duane and Steve Fisher's Startup Equation",
            description="TBC",
            image="gui/achievements/the_startup_equation.jpg",
            colour="#3D9970",
            unlock_level=1,
            link="https://startupequation.com/"
        )
        persistent.trophy_shelf.create_achievement(
            title="Ja-Naé Duane and Steve Fisher's BASE Board Model for planning an enterprise",
            description="TBC",
            image="gui/achievements/base_board.jpg",
            colour="#3D9970",
            unlock_level=1,
            link="https://www.dropbox.com/s/0qdzkyqev23l50l/Base%20Board%20Model_Workbook.pdf"
        )
        persistent.trophy_shelf.create_achievement(
            title="Ja-Naé Duane and Steve Fisher's Startup Launch Kits",
            description="TBC",
            image="gui/achievements/achievement.png",
            colour="#3D9970",
            unlock_level=1,
            link="https://drive.google.com/drive/folders/0B9wuRcuwU59aaTVIUFdwSFlDOTQ"
        )
        persistent.trophy_shelf.create_achievement(
            title="Alex Hillman et al's Stacking the Bricks resources for entrepreneurs",
            description="TBC",
            image="gui/achievements/stacking_the_bricks.jpg",
            colour="#3D9970",
            unlock_level=1,
            link="https://stackingthebricks.com/articles"
        )
        persistent.trophy_shelf.create_achievement(
            title="Brendan Dunn's Double Your Freelancing resources",
            description="TBC",
            image="gui/achievements/double_your_freelancing.jpg",
            colour="#3D9970",
            unlock_level=1,
            link="https://doubleyourfreelancing.com/topics"
        )
        persistent.trophy_shelf.create_achievement(
            title="Nell Watson's Founder Life Book",
            description="TBC",
            image="gui/achievements/achievement.png",
            colour="#3D9970",
            unlock_level=1
        )

    if persistent.leaderboard is None:
        create_leaderboard_data()

screen achievement_screen(shelf):
    tag menu

    on "replace":
        action Play("music", "music/ost004.mp3")
    modal True

    default page = 1
    default desc = ""

    add Solid("#ffffff")

    text "FOUNDERPEDIA" color "#000000" size 80 bold True xalign 0.5 yalign 0.06
    button:
        xysize (90, 90)

        idle_background Solid("#559fdd")
        hover_background Solid(Color("#559fdd").tint(0.5))
        selected_background Solid(Color("#559fdd").shade(0.5))

        text "X" font "fonts/Dyslexie_Regular_159164.ttf" size 60 color "#ffffff" yalign 0.5 xalign 0.52

        action Return()

        xalign 0.99
        yalign 0.01

    if page == 1:
        use say("Nell", "Welcome to Founderpedia, where you'll find some of the best startup lessons and resources.", "side nell normal")

        $ row = 2
        $ column = shelf.limit / 2

        vpgrid:
            rows row
            cols column

            xspacing 16
            yspacing 16

            xalign 0.5
            yalign 0.26

            for ach in shelf.store:
                button:
                    xysize (376, 189)

                    idle_background Solid(ach.colour)
                    hover_background Solid( Color(ach.colour).tint(0.5) )
                    selected_background Solid( Color(ach.colour).shade(0.5) )
                    insensitive_background Solid(ach.locked_colour)

                    add ach.get_image xalign 0.5 yalign 0.5

                    sensitive ach.unlocked == True

                    action If(ach.link, true=OpenURL(ach.link), false=[SetScreenVariable("desc", ach.description), SetScreenVariable("page", 2)])

    elif page == 2:
        button:
            xysize (90, 90)

            idle_background Solid("#559fdd")
            hover_background Solid(Color("#559fdd").tint(0.5))
            selected_background Solid(Color("#559fdd").shade(0.5))

            text "←" font "fonts/Dyslexie_Regular_159164.ttf" size 60 color "#ffffff" yalign 0.5 xalign 0.52

            action [SetScreenVariable("page", 1), SetScreenVariable("desc", "")]

            xalign 0.01
            yalign 0.01

        viewport id "founderpedia":
            area (80, 200, 1750, 800)
            child_size (1750, 2100)

            add Solid("#559fdd")

            draggable True
            mousewheel True
            scrollbars "vertical"

            text desc justify True xpos 100 ypos 50 xmaximum 1600

screen achievement_notify(title):
    zorder 100

    timer 4.0 action Hide("achievement_notify")
    frame:
        xsize 700
        ysize 100

        background Solid("#ffffff")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 8

            text "ACHIEVEMENT UNLOCKED" color "#000000" xalign 0.5
            text title color "#000000" xalign 0.5

        at slide_down_center

screen leaderboard_screen():
    tag menu

    add Solid("#ffffff")
    text "LOCAL LEADERBOARD" color "#000000" bold True size 80 xalign 0.5 yalign 0.06
    button:
        xysize (90, 90)

        idle_background Solid("#559fdd")
        hover_background Solid(Color("#559fdd").tint(0.5))
        selected_background Solid(Color("#559fdd").shade(0.5))

        text "X" font "fonts/Dyslexie_Regular_159164.ttf" size 60 color "#ffffff" yalign 0.5 xalign 0.52

        action Hide("achievement_screen")

        xalign 0.99
        yalign 0.01

    if persistent.game_data:
        vpgrid:
            cols 6
            draggable True
            mousewheel True
            xsize 1500
            ysize 850

            xalign 0.50
            ypos 200

            fixed:
                xysize (250, 50)
                text "Room" color "#559fdd" bold True
            text "Date" color "#559fdd" bold True
            text "Founder Name" color "#559fdd" bold True
            text "Days" color "#559fdd" bold True
            text "Score" color "#559fdd" bold True
            text "Delete" color "#559fdd" bold True

            for index, i in enumerate(persistent.game_data):
                for j in persistent.game_data[i]:
                    fixed:
                        if index % 2 == 0:
                            add Solid("#d3d3d3")
                        if j == "":
                            text "Default" color "#000000" yalign 0.5
                        else:
                            text str(j) color "#000000" yalign 0.5
                button:
                    xsize 250
                    ysize 50
                    if index % 2 == 0:
                        idle_background Solid("#d3d3d3")
                    else:
                        idle_background Solid("#ffffff")
                    hover_background Solid("#ff0000")
                    text _("X") color "#000000" xalign 0.5 yalign 0.5
                    action Show("delete_data_confirm", room_id=persistent.game_data[i][0], game_id=i)
    else:
        text "Empty :(" color "#000000" xalign 0.5 yalign 0.5

    button:
        xysize (200, 1080)
        xalign 0.0

        idle_background Solid("#559fdd", xysize=(200, 1080))
        hover_background Solid("#88bbe7", xysize=(200, 1080))

        text "<" color "#ffffff" size 100 bold True xalign 0.5 yalign 0.5

        action Return()

    button:
        xysize (200, 1080)
        xalign 1.0

        idle_background Solid("#559fdd", xysize=(200, 1080))
        hover_background Solid("#88bbe7", xysize=(200, 1080))

        add "gui/achievements/achievement_white.png" xalign 0.5 yalign 0.5

        action ShowMenu("achievement_screen", shelf=persistent.trophy_shelf)
