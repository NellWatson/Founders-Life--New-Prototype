label start:
    $ calculate_pool()
    scene bg bedroom
    # print renpy.display.core.scene_lists().get_all_displayables()
    
    jump event_intro

screen game_screen():
    modal True
    default b = ReviewB()
    
    add DynamicDisplayable(dynamic_review, b)

label checkpoint:
    $ event_name = ""

    if productivity <= 0:
        "Game over.\nYour Startup Productivity level has dropped below zero.\nYou survived [turn_no] days."
        return

    elif energy <= 0:
        "Game over.\nYour Energy level has dropped below zero.\nYou survived [turn_no] days."
        return

    elif morale <= 0:
        "Game over.\nYour Mindfulness level has dropped below zero.\nYou survived [turn_no] days."
        return

    elif money <= 0:
        "Game over. You have run out of savings."
        return

    if turn_no and not (turn_no % 7):

        hide player
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

        call screen startup_review(current_bg)
        call screen sprint_review(current_bg)

        if turn_no == 28:
            n normal "Thank you for playing Chapter 1 of Founders Life."
            return

        while total_founder_score > FOUNDER_INDEX[founder_level][1]:
            $ founder_level += 1
            $ level_up = True

            if founder_level > 10:
                $ founder_level = 10

        #call screen level_up(current_bg)
        if energy < 30 and morale < 30 and productivity < 30 and money < 1000:
            n normal "Wow, things are almost spinning out of control. You need to take a step back and start focusing on what's really important in your startup and your life. Try and eliminate all other distractions."

        elif energy < 30 and productivity < 30 and money < 1000:
            n normal "Wow, things are almost spinning out of control. You need to take a step back and start focusing on what's really important in your startup and your life. Try and eliminate all other distractions."

        elif productivity < 30 and morale < 30 and money < 1000:
            n normal "Wow, things are almost spinning out of control. You need to take a step back and start focusing on what's really important in your startup and your life. Try and eliminate all other distractions."

        elif energy < 30 and productivity < 30 and morale < 1000:
            n normal "Wow, things are almost spinning out of control. You need to take a step back and start focusing on what's really important in your startup and your life. Try and eliminate all other distractions."

        elif energy < 30 and productivity < 30:
            n normal "Being a founder demands vision and momentum, you need to start being ruthless with your focus. But you also need to pro-actively manage your energy."

        elif energy < 30 and morale < 30:
            n normal "Being a founder is physically tough and mentally exhausting, you need to proactively manage your energy and be mindful of your mental well-being."

        elif energy < 30 and money < 1000:
            n normal "Being a founder demands vision and momentum, you need to start being ruthless with your focus. But you also need to pro-actively manage your energy."

        elif morale < 30 and productivity < 30:
            n normal "Being a founder demands vision and momentum, you need to start being ruthless with your focus. But you also need to pro-actively manage your mental wellbeing."

        elif morale < 30 and money < 1000:
            n normal "Being a founder is mentally exhausting and financially draining, you need to be mindful of your mental well-being and strike a balance between investing in your dreams and being frugal with your cash reserves."

        elif productivity < 30 and money < 1000:
            n normal "Being a founder demands vision and momentum, you need to start being ruthless with your focus. But even the most radical focus is worthless without enough cash reserves to fund yourself."

        elif productivity < 30:
            n normal "Being a founder demands vision and momentum, you need to start being ruthless with your focus."

        elif energy < 30:
            n normal "Being a founder is physically tough, you need to proactively manage your energy."

        elif morale < 30:
            n normal "Being a founder is mentally exhausting, you need to be mindful of your mental well-being."

        elif money < 1000:
            n normal "Being a founder is financially draining, you need to strike a balance between investing in your dreams and being frugal with your cash reserves."

        else:
            n normal "Congratulations, things are going great. But don't get complacent, founder life is a constant tension between taking care of your business and taking care of yourself."

    if energy > 0 and morale > 0:
        $ turn_no += 1
        $ current_bg = "bg " + BACKGROUNDS[founder_level - 1]

        scene expression current_bg with dissolve
        jump expression find_event()
