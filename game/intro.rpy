label event_intro:
    show screen block_keys("game_menu")

    n normal "Welcome to Founder Life."
    n "For a while now you have dreamed of being your own boss, getting more control over your life."
    n "You have a job at the moment, but want to break out and in your own venture."
    n "You resolve today to start your own little business and see where that adventure can take you."

    $ founder_name = renpy.input("Let's start off with the basics - what's your name?", length=30) or "Sam"
    $ startup_name = renpy.input("What's your startup name?") or "StartUP Inc"

    n "Awesome. Which self-portrait feels most right to you?"

    call screen choose_portrait
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
    n "... and Cashflow"

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
    "The idea occurred to you a year ago, and you dismissed it. It seemed ridiculous back then. Yet you haven't been able to kick it out of your head since."
    "In the shower. During your commute. At breakfast. Staring at the darkened ceiling of your room."
    "You're tired of working for someone else. You're tired of having no control over your time, your money, your trajectory. You're tired of being someone else's employee."
    "You want to start your own business."
    "Over the years, the ideas solidified. The work you'd need to do went from vague, shapeless blobs to crystalline task lists."
    "You where you want to go and how to get there, and you've finally decided to give it a shot."
    "You pick the first day of the new year to make this broad change. As the clock ticks down on New Year's Eve, you realize you're not completely sure what spurred you to do this."
    "Why do you want to do this?"

    menu:
        "I want to strike it rich!":
            $ money += 1000
            $ money_manager = MoneyManager(money)
        "I want to see just how far I can go.":
            $ productivity += 20
        "I want control over my time.":
            $ morale += 20
        "I want to achieve my dream.":
            $ energy += 20

    "5... 4... 3... 2... 1... HAPPY NEW YEAR!"
    "It's the start of what you hope will change the rest of your life."

    call screen character_intro

label skylar_intro:
    "This is Skylar, the love of your life. You knew as soon as you met them you wanted to be with them forever."
    "They've had a bit of a rough life, but despite that they have their life together and are pushing forward.
    "Their ambition, drive, and patience inspire you. You moved in together two months ago, and it's partially due to them you have the confidence to take this step."
    "That being said, you don't know how they will take this."

    call screen character_intro

label takashi_intro:
    "This is Takashi. You've been friends since you were in diapers, going to school together and wreaking havoc through town.
    "He's a bit of a joker. You were always the more serious one. He mellows you out and reminds you to enjoy the fun in life."
    "You're used to hanging out at least three times a week, and you won't be able to do that when you make this change.
    "His carefree nature has always been helpful, but you're worried you're not going to see eye-to-eye on this."

    call screen character_intro

label roger_intro:
    "This is Roger, your current boss. While not the worst boss you've had, you don't like working under him.
    "He'll throw temper tantrums, sulk, and push more work at people he doesn't like. You don't ever want to be a boss like that."
    "You're trying to hide your plans from him. You have a feeling if he finds out, things won't go well for you."

    call screen character_intro
