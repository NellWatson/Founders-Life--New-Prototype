label event_intro:
    show screen block_keys("game_menu")

    n normal "Welcome to Founder's Life."
    n "You've got an entirely new business to create from the bottom up."

    $ founder_name = renpy.input("Let's start off with the basics - what's your name?", length=30) or "Sam"
    $ startup_name = renpy.input("What's your startup name?") or "StartUP Inc"
    
    n "You've got a lot of work to do, and your savings won't keep you afloat forever."
    n "But remember to take care of yourself. You are your best investment, and you can't work if you run your body, mind, or spirit into the ground."
    n "Working on your own is about more than just business. If you can figure out what you want to do and why exactly you want to do it, you will be a lot happier."

    call screen founder_map
    #call screen msg("Meeting Your Mentor", title="episode 1", show_button="Let's go!")

    hide screen block_keys

    # Set up a dummy screen
    $ current_sprint = 0
    $ last_founder_level = founder_level
    
    show screen hud

    #call screen level_up(current_bg)
    #with dissolve

    jump checkpoint
