label start:
    $ characters_roster = CharacterRooster()
    $ chapter_manager = ChapterManager()
    
    $ characters_roster.add_character("eileen", "Eileen", "e", "eileen")
    $ chapter_manager.load_chapter("ch_01", "chapter_01")
    $ chapter_manager.set_chapter("ch_01")

    $ calculate_pool()
    $ telemetry.init()
    $ telemetry.setup()
    $ persistent.trophy_shelf.check_unlock(founder_level)

    play music "music/ost002.mp3" fadein 1.5
    scene bg bedroom
    # print renpy.display.core.scene_lists().get_all_displayables()

    jump event_intro
    #jump week_event

label week_event:
    $ _event = chapter_manager.get_event()

    show expression _event.character.sprite at center
    menu:
        _event.character.get_character_object "[_event.description]"

        "$_YES":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", 10)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", -10)

    jump checkpoint

label checkpoint:
    scene bg bedroom
    $ event_code = ""

    if productivity <= 0:
        $ renpy.unlink_save("custom")
        $ telemetry.end("No Productivity")
        $ persistent.leaderboard.append([ datetime.date.today(), founder_name, turn_no, founder_score ])

        play sound "sfx/fx012.wav"
        n normal "Game over.\nYour Startup Productivity level has dropped below zero.\nYou survived [turn_no] days."
        
        if not persistent.submitted_form:
            n normal "Please let us know your feedback."
            call screen feedback_form_screen
        return

    elif energy <= 0:
        $ renpy.unlink_save("custom")
        $ telemetry.end("No Energy")
        $ persistent.leaderboard.append([ datetime.date.today(), founder_name, turn_no, founder_score ])

        play sound "sfx/fx012.wav"
        n normal "Game over.\nYour Energy level has dropped below zero.\nYou survived [turn_no] days."
        
        if not persistent.submitted_form:
            n normal "Please let us know your feedback."
            call screen feedback_form_screen
        return

    elif morale <= 0:
        $ renpy.unlink_save("custom")
        $ telemetry.end("No Mindfulness")
        $ persistent.leaderboard.append([ datetime.date.today(), founder_name, turn_no, founder_score ])

        play sound "sfx/fx012.wav"
        n normal "Game over.\nYour Mindfulness level has dropped below zero.\nYou survived [turn_no] days."
        
        if not persistent.submitted_form:
            n normal "Please let us know your feedback."
            call screen feedback_form_screen
        return

    elif money <= 0:
        $ renpy.unlink_save("custom")
        $ telemetry.end("No Cashflow")
        $ persistent.leaderboard.append([ datetime.date.today(), founder_name, turn_no, founder_score ])

        play sound "sfx/fx012.wav"
        n normal "Game over. You have run out of savings.\nYou survived [turn_no] days."
        
        if not persistent.submitted_form:
            n normal "Please let us know your feedback."
            call screen feedback_form_screen
        return

    if turn_no and not (turn_no % 7):
        
        play week_sound "sfx/fx003.wav"
        n normal "Congratulations [founder_name].\nYou have survived [turn_no] days as a founder."
        # current_sprint = energy * morale * turn_no * founder_level
        # money += current_sprint
        $ founder_score = (productivity + energy + morale + money + (turn_no * founder_level)) * founder_level
        $ total_founder_score += founder_score
        $ level_up = False
        $ last_founder_level = founder_level
        $ week += 1
        $ week_event_bucket_type = set()
        $ check["money"] = ""

        $ telemetry.collect()
        $ telemetry.sync()

        call screen startup_review(current_bg)
        call screen sprint_review(current_bg)

        # If we have seen the achievement button once, mark it so that the flashing doesn't happen again
        if persistent.trophy_shelf.show_trophy_icon:
            $ persistent.trophy_shelf.unseen = False

        if turn_no == 28:
            $ current_episode += 1
            call screen founder_map

            if not persistent.submitted_form:
                n normal "Please let us know your feedback."
                call screen feedback_form_screen

            $ renpy.unlink_save("custom")
            $ telemetry.end("done")
            $ persistent.leaderboard.append([ datetime.date.today(), founder_name, turn_no, founder_score ])

            n normal "Thank you for playing Chapter 1 of Founder Life."
            return

        while total_founder_score > FOUNDER_INDEX[founder_level][1]:
            $ founder_level += 1
            $ level_up = True

            if founder_level > 10:
                $ founder_level = 10

        $ renpy.save("custom")
        play week_sound "sfx/fx004.wav"

        #call screen level_up(current_bg)
        if energy < 30 and morale < 30 and productivity < 30 and money < 1500:
            n normal "Wow, things are almost spinning out of control. You need to take a step back and start focusing on what's really important in your startup and your life. Try and eliminate all other distractions."

        elif energy < 30 and productivity < 30 and money < 1500:
            n normal "Wow, things are almost spinning out of control. You need to take a step back and start focusing on what's really important in your startup and your life. Try and eliminate all other distractions."

        elif productivity < 30 and morale < 30 and money < 1500:
            n normal "Wow, things are almost spinning out of control. You need to take a step back and start focusing on what's really important in your startup and your life. Try and eliminate all other distractions."

        elif energy < 30 and productivity < 30 and morale < 30:
            n normal "Wow, things are almost spinning out of control. You need to take a step back and start focusing on what's really important in your startup and your life. Try and eliminate all other distractions."

        elif energy < 30 and productivity < 30:
            n normal "Being a founder demands vision and momentum, you need to start being ruthless with your focus. But you also need to pro-actively manage your energy."

        elif energy < 30 and morale < 30:
            n normal "Being a founder is physically tough and mentally exhausting, you need to proactively manage your energy and be mindful of your mental well-being."

        elif energy < 30 and money < 1500:
            n normal "Being a founder is physically tough and financially draining, you need to proactively manage your energy and strike a balance between investing in your dreams and being frugal with your cash reserves."

        elif morale < 30 and productivity < 30:
            n normal "Being a founder demands vision and momentum, you need to start being ruthless with your focus. But you also need to pro-actively manage your mental wellbeing."

        elif morale < 30 and money < 1500:
            n normal "Being a founder is mentally exhausting and financially draining, you need to be mindful of your mental well-being and strike a balance between investing in your dreams and being frugal with your cash reserves."

        elif productivity < 30 and money < 1500:
            n normal "Being a founder demands vision and momentum, you need to start being ruthless with your focus. But even the most radical focus is worthless without enough cash reserves to fund yourself."

        elif productivity < 30:
            n normal "Being a founder demands vision and momentum, you need to start being ruthless with your focus."

        elif energy < 30:
            n normal "Being a founder is physically tough, you need to proactively manage your energy."

        elif morale < 30:
            n normal "Being a founder is mentally exhausting, you need to be mindful of your mental well-being."

        elif money < 1500:
            n normal "Being a founder is financially draining, you need to strike a balance between investing in your dreams and being frugal with your cash reserves."

        else:
            n normal "Congratulations, things are going great. But don't get complacent, founder life is a constant tension between taking care of your business and taking care of yourself."

    if energy > 0 and morale > 0:
        $ turn_no += 1
        $ current_bg = "bg " + BACKGROUNDS[founder_level - 1]

        scene expression current_bg with dissolve

        if turn_no <= 27:
            jump expression find_event()
        else:
            jump chapter_one_finale

label chapter_one_finale:
    $ event_code = "ch01e99"
    show dominique at center
    menu:
        d "Hi, [founder_name], I'm Dominique Martel. I just wanted to reach out to tell you how impressed I've been with the progress you've been making with [startup_name]. I love the idea and your execution.\nI've a lot of free time now I've left Google, and I'd like to spend some of it mentoring you.\nWhat do you say?"

        "$_YES":
            $ variable("productivity", 20)
            $ variable("energy", 20)
            $ variable("morale", 20)

        "$_NO":
            $ variable("productivity", -20)
            $ variable("energy", -20)
            $ variable("morale", -20)

    jump checkpoint
