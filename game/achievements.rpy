init python:
    class Achievement():

        def __init__(self, title, description, image, colour, unlock_level, locked_image=None, locked_colour=None, add_to_shelf=None):
            self.title = title
            self.description = description
            self.image = image
            self.colour = colour
            self.unlock_level = unlock_level

            self.unlocked = False
            self.locked_image = locked_image
            self.locked_colour = locked_colour

            if add_to_shelf:
                shelf.add_achievement(self)

        @property
        def get_image(self):
            return self.image if self.unlocked else self.locked_image

    class Shelf():

        def __init__(self, name, locked_image, locked_colour, limit):
            self.name = name
            self.locked_image = locked_image
            self.locked_colour = locked_colour
            self.limit = limit

            self.show_trophy_icon = False
            self.unseen = True
            self.store = []

        def create_achievement(self, title, description, image, colour, unlock_level):
            ach = Achievement(title, description, image, colour, unlock_level, self.locked_image, self.locked_colour)

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

    def create_leaderboard_data():
        persistent.leaderboard = []
        persistent.trophy_shelf = Shelf("Achievements", "gui/achievements/locked.png", "#aaaaaa", 10)
        persistent.trophy_shelf.create_achievement(
            title="Founder vs. Entrepreneur",
            description="To be a Founder of a new business venture, school of thought, or social movement—is to perceive a possible future based on current trends, and to struggle to help make that vision of the future come true.\n\nFounding is hard. Being a Founder means smashing your will against the stony face of an uncaring universe, over and over again, until a dent appears: either in you, or in it.\n\nThere will come a time when you’ll be reticent to continue. There will be moments when you decide to either give it your all or give it all up. Moments that make or break you. Tragically, sometimes, it’s a matter of timing; if you had just kept on pounding even a couple months or days or minutes longer, the universe would have begun to give way to your will. Equally tragically, sometimes no matter what you try, the wall won’t give due to circumstances beyond your control. You break your skull—or you try something different.\n\nBut what keeps you standing, at the end of the day, is not the world around you. It is the world within you. It is the essence that defines you as a Founder. This is both your compass and your strength.\n\nThere is much extant literature that describes the process of finding a product/market fit or of navigating term sheets and the like. There appears to be far less documentation about the journey of the entrepreneur as an evolving human—what it truly takes to create something from nothing and have it be of value to others. What does it mean to harness your goals to your urges, to align your venture with your sense of purpose? What does it mean to ride the most intense of emotional rollercoasters while managing your own psychology, and all the time living and learning on-the-fly?\n\nEntrepreneurship requires finding, managing, and leveraging precious resources. By far, you are your most valuable asset, although you are also the most easily forgotten and neglected. You have unlimited power within you, if only you learn to tap it. It is your passion, your drive, and the adrenaline that keeps you burning through the midnight oil each night—that is your small touch of good madness. Realizing this— and then establishing systems and habits to make the most of your capabilities—is absolutely crucial. Only those who master their own character can truly rise to the zenith of their personal power. You must be brave enough to let go of who you are today in order to become even greater tomorrow.\n\nThe psychology of Founding takes the psychology of Entrepreneurship one step further. It is about building an engine of happiness that revolves around your life, benefitting you and the rest of the world. Building an engine of happiness means discovering your personal drive, aligning it with a venture, and amplifying that through the power of the free market and exponential curves. Maintaining an engine of happiness means ensuring your own personal wellbeing, motivation, and dedication along with your professional success…\n\nTherefore, not only must a Founder be an expert in the business—the Founder must also play the part of philosopher and psychologist to make it through the challenges with his or her personal and professional life intact. Business and Founder are not one and the same. Ideally, however, they grow and thrive in tandem.\n\nThe Founder way of life is an initiative. It’s an extreme sport with extreme potential. Within this book, I seek to outline the basics of becoming a Founder—what it is, what it takes, and where it can take you. Like any journey, these chapters are neither inclusive nor incontestable. They are my offering to you, an outstretched hand towards a bridge of logic and emotion that I traverse, while balancing my vulnerabilities and my triumphs. The adventure begins here, along with the dialogue.\n\nAs brothers and sisters in this strange and terrific journey, let us share our wisdom among us, for all of us are cut from the same cloth of ambition, altruism, and sacred madness.",
            image="gui/achievements/achievement.png",
            colour="#FFDC00",
            unlock_level=1
        )
        persistent.trophy_shelf.create_achievement(
            title="Creators, Farmers & Nestors",
            description="TBC",
            image="gui/achievements/achievement.png",
            colour="#FF851B",
            unlock_level=2
        )
        persistent.trophy_shelf.create_achievement(
            title="The Founder Virtue",
            description="TBC",
            image="gui/achievements/achievement.png",
            colour="#85144B",
            unlock_level=3
        )
        persistent.trophy_shelf.create_achievement(
        title="The Founder's Tightrope",
        description="TBC",
        image="gui/achievements/achievement.png",
        colour="#01FF70",
        unlock_level=4
        )
        persistent.trophy_shelf.create_achievement(
            title="Placeholder",
            description="TBC",
            image="gui/achievements/achievement.png",
            colour="#7FDBFF",
            unlock_level=5
        )
        persistent.trophy_shelf.create_achievement(
            title="Placeholder",
            description="TBC",
            image="gui/achievements/achievement.png",
            colour="#0074D9",
            unlock_level=6
        )
        persistent.trophy_shelf.create_achievement(
            title="Placeholder",
            description="TBC",
            image="gui/achievements/achievement.png",
            colour="#001F3F",
            unlock_level=7
        )
        persistent.trophy_shelf.create_achievement(
        title="Placeholder",
        description="TBC",
        image="gui/achievements/achievement.png",
        colour="#DDDDDD",
        unlock_level=8
        )
        persistent.trophy_shelf.create_achievement(
            title="Placeholder",
            description="TBC",
            image="gui/achievements/achievement.png",
            colour="#F012BE",
            unlock_level=9
        )
        persistent.trophy_shelf.create_achievement(
            title="Placeholder",
            description="TBC",
            image="gui/achievements/achievement.png",
            colour="#3D9970",
            unlock_level=10
        )

    if persistent.leaderboard is None:
        create_leaderboard_data()

screen achievement_screen(shelf):
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

        text "X" font "DejaVuSans.ttf" size 60 color "#ffffff" yalign 0.5 xalign 0.52

        action Hide("achievement_screen")

        xalign 0.99
        yalign 0.01

    if page == 1:
        use say("Nell", "Welcome to Founderpedia, where I'll be sharing some of my best startup lessons and worst entrepreneurial expreciences.", "side nell normal")

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
                    xysize (160, 160)

                    idle_background Solid(ach.colour)
                    hover_background Solid( Color(ach.colour).tint(0.5) )
                    selected_background Solid( Color(ach.colour).shade(0.5) )
                    insensitive_background Solid(ach.locked_colour)

                    add ach.get_image xalign 0.5 yalign 0.5

                    sensitive ach.unlocked == True

                    action SetScreenVariable("desc", ach.description), SetScreenVariable("page", 2)

    elif page == 2:
        button:
            xysize (90, 90)

            idle_background Solid("#559fdd")
            hover_background Solid(Color("#559fdd").tint(0.5))
            selected_background Solid(Color("#559fdd").shade(0.5))

            text "←" font "DejaVuSans.ttf" size 60 color "#ffffff" yalign 0.5 xalign 0.52

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

            text desc xpos 10 xmaximum 1710

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

    add Solid("#ffffff")
    text "LOCAL LEADERBOARD" color "#000000" bold True size 80 xalign 0.5 yalign 0.06
    button:
        xysize (90, 90)

        idle_background Solid("#559fdd")
        hover_background Solid(Color("#559fdd").tint(0.5))
        selected_background Solid(Color("#559fdd").shade(0.5))

        text "X" font "DejaVuSans.ttf" size 60 color "#ffffff" yalign 0.5 xalign 0.52

        action Hide("achievement_screen")

        xalign 0.99
        yalign 0.01

    if persistent.leaderboard:
        vpgrid:
            cols 4
            draggable True
            mousewheel True
            xsize 1200
            ysize 850

            xalign 0.50
            ypos 200

            fixed:
                xysize (300, 50)
                text "Date" color "#559fdd" bold True
            text "Founder Name" color "#559fdd" bold True
            text "Days Survived" color "#559fdd" bold True
            text "Founder Score" color "#559fdd" bold True

            for index, i in enumerate(persistent.leaderboard):
                for j in i:
                    fixed:
                        if index % 2 == 0:
                            add Solid("#d3d3d3")
                        text str(j) color "#000000" yalign 0.5
    else:
        text "Empty :(" color "#000000" xalign 0.5 yalign 0.5

    button:
        xysize (200, 1080)
        xalign 0.0

        idle_background Solid("#559fdd", xysize=(200, 1080))
        hover_background Solid("#88bbe7", xysize=(200, 1080))

        text "<" color "#ffffff" size 100 bold True xalign 0.5 yalign 0.5

        action Hide("leaderboard_screen")

    button:
        xysize (200, 1080)
        xalign 1.0

        idle_background Solid("#559fdd", xysize=(200, 1080))
        hover_background Solid("#88bbe7", xysize=(200, 1080))

        add "gui/achievements/achievement_white.png" xalign 0.5 yalign 0.5

        action Show("achievement_screen", shelf=persistent.trophy_shelf)
