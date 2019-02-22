label event_intro:
    show screen block_keys("game_menu")

    n normal "Welcome to Founder's Life."
    n "You've got an entirely new business to create from the bottom up."

    $ founder_name = renpy.input("Let's start off with the basics - what's your name?", length=30) or "Sam"
    $ startup_name = renpy.input("What's your startup name?") or "StartUP Inc"
    
    n "You've got a lot of work to do, and your savings won't keep you afloat forever."
    n "But remember to take care of yourself. You are your best investment, and you can't work if you run your body, mind, or spirit into the ground."
    n "Working on your own is about more than just business. If you can figure out what you want to do and why exactly you want to do it, you will be a lot happier."
    n "A good founder learns how to balance..."

    show intro productivity at im_center
    n "... Productivity"

    show intro energy at im_center
    n "... Energy"

    show intro morale at im_center
    n "... Mindfulness"

    show intro money at im_center
    n "... Cashflow"

    hide intro with dissolve
    call screen founder_map
    #call screen msg("Meeting Your Mentor", title="episode 1", show_button="Let's go!")

    hide screen block_keys

    # Set up a dummy screen
    $ current_sprint = 0
    $ last_founder_level = founder_level
    $ _game_menu_screen = "preferences"
    
    show screen hud

    #call screen level_up(current_bg)
    #with dissolve

    "You're finally fed up."
    "The idea occurred to you a year ago, and you dismissed it. It seemed ridiculous back then. But since, you haven't been able to kick it out of your head."
    "In the shower. During your commute. At breakfast. Staring at the darkened ceiling of your room."
    "You're tired of working for someone else. You're tired of having no control over your time, your money, your trajectory. You're tired of being someone else's employee."
    "You want to start your own business."
    "And over the years, the ideas solidified. The work you'd need to do went from vague, shapeless blobs to crystalline task lists."
    "You know what to do and how to get there, and you've finally decided to give it a shot."
    "You pick the first day of the new year to make this broad change. But as the clock ticks down on New Year's Eve, you realize you're not completely sure what spurred you on to do this."
    "Why do you want to do this?"

    menu:
        "I want to strike it rich!":
            $ money += 1000
            $ money_manager = MoneyManager(money)
        "I want to see just how far I can go.":
            $ productivity += 20
        "I want control over how I spend my time.":
            $ morale += 20
        "I want to achieve my dream.":
            $ energy += 20

    "5... 4... 3... 2... 1... HAPPY NEW YEAR!"
    "It's the start of what you hope will change the rest of your life."

    call screen character_intro

label skylar_intro:
    "This is Skylar, the love of my life. I knew as soon as I met him/her that I wanted to be with him/her forever."
    "She's had a bit of a rough life, but despite that he/she has her life together and is pushing forward. His/her ambition, drive, and patience inspire me. We moved in together two months ago, and it's partially due to him/her I have the confidence to take this step."
    "That being said, I don't know how he/she will take this."

    call screen character_intro

label takashi_intro:
    "This is Takashi. We've been friends since we were in diapers, going to school together and wreaking havoc through town. He's a bit of a joker. I was always the more serious one. But it's nice, because he mellows me out and reminds me to enjoy the fun in life."
    "We're used to hanging out at least three times a week, and I won't be able to do that anymore once I make this change. His carefree nature has always been helpful to me, but I'm worried we're not going to see eye-to-eye on this."

    call screen character_intro

label roger_intro:
    "This is Roger, the boss of my current job. While not the worst boss I've ever had, I don't like working under him. He'll throw temper tantrums and sulk, or passive-aggressively push more work at people he doesn't like. I don't ever want to be a boss like that."
    "I'm trying to hide my plans from him. I have a feeling that if he finds out, things won't go well for me."

    call screen character_intro
