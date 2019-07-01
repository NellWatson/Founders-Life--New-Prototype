label start:
    $ characters_roster = CharacterRooster()
    $ chapter_manager = ChapterManager()
    $ var_tracker = VarTracker()
    
    $ characters_roster.add_character("none", "None", "none", None)
    $ characters_roster.add_character("eileen", "Eileen", "e", "eileen")
    $ characters_roster.add_character("skylar", "Skylar", "s", "skylar")
    $ characters_roster.add_character("takashi", "Takashi", "t", "takashi")
    $ characters_roster.add_character("roger", "Roger", "r", "roger")
    $ chapter_manager.load_chapter("ch_01", "chapter_01")
    $ chapter_manager.load_chapter("ch_02", "chapter_02")
    $ chapter_manager.load_chapter("ch_03", "chapter_03")
    $ chapter_manager.load_chapter("ch_04", "chapter_04")
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
    $ event_code = _event.id

    if _event.character.sprite:
        pass#show expression _event.character.sprite at center
    
    if _event.has_multiple_description:
        while not _event.seeing_last_description:
            _event.get_speaker "[_event.description]"

    menu:
        _event.get_speaker "[_event.last_description]"

        "[_event.yes_caption]" if _event.is_yes:
            $ _event.yes

        "[_event.no_caption]" if _event.is_no:
            $ _event.no

    if _event.choice_have_description:
        while not _event.seeing_choice_last_description:
            _event.get_speaker "[_event.choice_description]" #_event.character.get_character_object

    jump checkpoint

label checkpoint:
    scene bg bedroom
    $ event_code = ""

    if productivity <= 0:
        $ renpy.unlink_save("custom")
        $ telemetry.end("No Productivity")
        $ persistent.leaderboard.append([ datetime.date.today(), founder_name, total_days, founder_score ])

        call screen startup_review(current_bg)
        call screen sprint_review(current_bg)

        play sound "sfx/fx012.wav"
        n normal "Game over.\nYour Startup Productivity level has dropped below zero.\nYou survived [total_days] days."
        
        if not persistent.submitted_form:
            n normal "Please let us know your feedback."
            call screen feedback_form_screen
        return

    elif energy <= 0:
        $ renpy.unlink_save("custom")
        $ telemetry.end("No Energy")
        $ persistent.leaderboard.append([ datetime.date.today(), founder_name, total_days, founder_score ])

        call screen startup_review(current_bg)
        call screen sprint_review(current_bg)

        play sound "sfx/fx012.wav"
        n normal "Game over.\nYour Energy level has dropped below zero.\nYou survived [total_days] days."
        
        if not persistent.submitted_form:
            n normal "Please let us know your feedback."
            call screen feedback_form_screen
        return

    elif morale <= 0:
        $ renpy.unlink_save("custom")
        $ telemetry.end("No Mindfulness")
        $ persistent.leaderboard.append([ datetime.date.today(), founder_name, total_days, founder_score ])

        call screen startup_review(current_bg)
        call screen sprint_review(current_bg)

        play sound "sfx/fx012.wav"
        n normal "Game over.\nYour Mindfulness level has dropped below zero.\nYou survived [total_days] days."
        
        if not persistent.submitted_form:
            n normal "Please let us know your feedback."
            call screen feedback_form_screen
        return

    elif money <= 0:
        $ renpy.unlink_save("custom")
        $ telemetry.end("No Cashflow")
        $ persistent.leaderboard.append([ datetime.date.today(), founder_name, total_days, founder_score ])

        call screen startup_review(current_bg)
        call screen sprint_review(current_bg)

        play sound "sfx/fx012.wav"
        n normal "Game over. You have run out of savings.\nYou survived [total_days] days."
        
        if not persistent.submitted_form:
            n normal "Please let us know your feedback."
            call screen feedback_form_screen
        return

    if turn_no and not (turn_no % 7):
        
        play week_sound "sfx/fx003.wav"
        n normal "Congratulations [founder_name].\nYou have survived [total_days] days as a founder."
        # current_sprint = energy * morale * turn_no * founder_level
        # money += current_sprint
        $ founder_score = (productivity + energy + morale + money + (total_days * founder_level)) * founder_level
        $ total_founder_score += founder_score
        $ level_up = False
        $ last_founder_level = founder_level
        $ week += 1
        $ week_event_bucket_type = set()
        $ check["money"] = ""

        $ telemetry.collect()
        $ telemetry.sync()
        $ money_manager.add_weekly_earning()

        call screen startup_review(current_bg)
        call screen sprint_review(current_bg)

        # If we have seen the achievement button once, mark it so that the flashing doesn't happen again
        if persistent.trophy_shelf.show_trophy_icon:
            $ persistent.trophy_shelf.unseen = False

        if turn_no == 28:
            $ current_chapter += 1
            call screen founder_map

            if not persistent.submitted_form:
                n normal "Please let us know your feedback."
                call screen feedback_form_screen

            $ renpy.unlink_save("custom")
            $ telemetry.end("done")
            $ persistent.leaderboard.append([ datetime.date.today(), founder_name, total_days, founder_score ])

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
        $ total_days = ((current_chapter-1) * CHAPTER_DAY_COUNT) + turn_no
        $ current_bg = "bg " + BACKGROUNDS[founder_level - 1]

        scene expression current_bg with dissolve

        if turn_no <= 27:
            jump week_event#expression find_event()
        else:
            jump chapter_finale

label chapter_finale:
    $ next_chapter()
    if current_chapter == 2:
        jump chapter_one_finale
    elif current_chapter == 3:
        jump chapter_two_finale
    elif current_chapter == 4:
        jump chapter_three_finale
    elif current_chapter == 5:
        jump chapter_four_finale

label chapter_one_finale:
    $ event_code = "chapter_01_99"
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

    hide dominique

    call screen founder_map
    $ event_code = "chapter_02_00"

    "It's the second full month of pursuing your dreams, and you've had a terrible realization: you aren't making nearly enough money to be able to quit your job."
    "But what can you do? While you're still working your full-time job, there's only so much time you can put into this venture."
    "At least you have a safety net. If you'd quit your job and jumped into this first thing, you'd be feeling the burn."

    menu:
        "It's disappointing, but you have to work harder to make this viable. You decide to focus on making more money this month.":
            pass

    jump checkpoint

label chapter_two_finale:
    call screen founder_map

    $ event_code = "chapter_03_00"
    
    "You've finally proven to Skylar that you are, in fact, capable of achieving your dreams, but the measures you had to take to do it leave you dissatisfied."
    "You didn't start out on this journey just to wind up working on other people's dreams, after all. You wanted to be your own boss, not gain sixty. But how are you supposed to bide the time between now and when your work is finished?"
    "As you're mulling this and checking your inbox, you notice another e-mail from Dominique."

    "Dear [founder_name],"
    "I'm writing again because divine intervention has enabled me to be in your area at the end of the month, on the 28th. If you are available, I would like to meet."
    "Pitch me your venture. Tell me your plans. Let me know the progress you have made. Then, we can see whether I can be of use to you.\nBest,\nDominique Martel"

    "Before you can give yourself too much time to stop, you reply and accept. But you can't help asking: why are you doing this? The answer comes almost immediately."
    "Because part of the reason I chose to chase my success was to help others when they chased their own."

    menu:
        "The 28th? That gives you a whole month to prepare your pitch.":
            pass

    jump checkpoint

label chapter_three_finale:
    if characters_roster.get_character_object(character).affection < 15:
        $ renpy.unlink_save("custom")
        $ telemetry.end("Game Over at Chapter 03")
        $ persistent.leaderboard.append([ datetime.date.today(), founder_name, total_days, founder_score ])

        call screen startup_review(current_bg)
        call screen sprint_review(current_bg)

        play sound "sfx/fx012.wav"
        n normal "Game over.\nYou survived [total_days] days."
        
        if not persistent.submitted_form:
            n normal "Please let us know your feedback."
            call screen feedback_form_screen
        return

    $ characters_roster.get_character_object(character).affection = 0
    "[founder_name],\nI'm very excited to move forward with you on this. A few things to note:"
    "There is an event coming up in two months. I think it would be prudent to release your product to correspond with that event, as that should help gain it a lot of publicity. I know that's likely a much faster timeline than you were hoping for, but trust me on this."
    "On the first of the next month, we will release the product to beta-testers, who will give us valuable feedback. Thus, this month should be spend ensuring the product working as well as we can get it."
    "I'm having my team look over your project and will send back our notes. It will be a lot to handle, but fixing what they find will go a long way to making a lasting impression on the beta-testers."
    "Take some rest now while you can. You'll need it.\nDominique"

    menu:
        "That sounds... ominous.":
            $ variable("energy", 20)
            $ variable("morale", 20)
            
            "You take some time off, trying to have the most relaxing day possible."
            "You're deeply grateful you did."

    jump checkpoint

label chapter_four_finale:
    $ event_code = "chapter_04_99"
    show dominique at center

    "On the last day, just in the nick of time, you have everything finalized and ready for the beta."
    "You've been working so furiously hard you haven't even had time to process the fact that tomorrow, real live people will be seeing what you've poured your heart and soul into over the past few months. In fact, you're now too exhausted to even be worried."
    "Later that night, when you're explaining this to Dominique, he smiles."

    d "That was exactly the point. Trust me, you'll thank me later."
    "You crawl into bed. Tomorrow, things change for good."

    n normal "Game over.\nThank you for playing."
    
    if not persistent.submitted_form:
        n normal "Please let us know your feedback."
        call screen feedback_form_screen

    return
