label start:

    scene bg lounge
    show screen hud

    jump set_startup

label checkpoint:
    $ event_name = ""
    $ weekly_deductions()
    $ startup_development(10)
    $ startup_pr(10)
    
    $ can_upgrade_startup()
    if turn_no and not (turn_no % 4):
        $ month += 1

        call screen startup_review("bg lounge")

        if founder_level > 10:
            $ founder_level = 10

        call screen startup_preview("bg lounge")

    if energy > 0 and morale > 0 and money > 0:
        $ turn_no += 1
        "And here comes another turning point in Mr. X's life."
        
        jump expression find_event()

    elif energy < 0:
        $ print energy
        call screen err_msg(message="You are out of Energy.", title="game over")
    elif morale < 0:
        $ print morale
        call screen err_msg(message="You are out of Morale.", title="game over")
    elif money < 0:
        $ print money
        call screen err_msg(message="You are out of Cash.", title="game over")

    if month > 1:
        "You survived [month] months."
    else:
        "You survived [month] month."

    return

label pr_vs_development:
    menu:
        "One of your friend who is helping you out in your startup think you should focus on PR more than development to create hype. So do you follow his advice?"

        "$_YES":
            $ move_employees("development", "pr")
            $ variable("morale", 10)

            "Your small team bounced with joy when they saw their first like and follow. Though opening a new front has slowed down the app development."

        "$_NO":
            $ variable("morale", -10)

            "Your friend seemed a bit down by your rejection but at this stage, it's important that you focus on developing the app."

    jump checkpoint

label hire_more:
    menu:
        "Progress is going slower then you expected. But a small team can only do so much. Should you hire a new employee?"

        "$_YES":
            $ variable("morale", 10)
            $ variable("energy", -25)
            $ variable("money", -100)
            $ dev_employees += 1

            "Your budget only allowed you to hire a freshly graduated kid. He seems enthusiastic and a new face brought the morale up a bit."

        "$_NO":
            $ variable("morale", -10)
            $ variable("energy", -5)

            "You looked at your finance and decided against hiring. You need all the money you can right now, and there is no way you could have hired a decent developer at the price you would have offered."

    jump checkpoint

label late_night_sprint:
    menu:
        "You and your team have been working since morning. It's almost midnight and you are just about done. The last meal you all had was lunch. Treat your employees to dinner?"

        "$_YES":
            $ variable("morale", 25)
            $ variable("money", -600)

            "You ordered pizza and soft drinks for everyone. It wasn't much, but your team appreciated your thoughtfulness."

        "$_NO":
            $ variable("morale", -10)
            $ variable("energy", -25)

            "You decided against it. Money is tight and it's not like you are not paying them salaries."

    jump checkpoint

label holiday:
    menu:
        "You evaluated the development progress and realised that you might not make the deadline. There are a couple of holidays coming. If you cancel them, you might be able to finish it by the deadline. What do you do?"

        "$_YES":
            $ variable("morale", -15)
            $ variable("energy", -10)
            $ startup_development(20)

            "You gave a very moving speech and all of your employees agreed to come on holidays. They aren't super happy about it though."

        "$_NO":
            $ variable("energy", -25)

            "You remembered your own working days and decided against it. You always hated when your boss pulled that card and you are not going to put your employees through the same."

    jump checkpoint

label bad_ui:
    "You were browsing through 'StartUp Unite' and got jealous and a bit depressed looking at other people beautiful looking app. Your app looked like as if it was imagined by a guy high on the world's most potent drugs."

    menu:
        "Since you don't have a UI guy on team, you need to outsource it. Do you?"

        "$_YES":
            $ variable("morale", 15)
            $ variable("energy", 10)
            $ variable("money", -5000)

            "Everyone in your team was happy looking at the fabulous UI. It will definitely give you some bragging points while hyping your app."
            "But your wallet took a bit hit. You need to budget more now or you will go under."

        "$_NO":
            $ variable("morale", -5)

            "You decided against it because honestly, you don't have the money. You googled \"apps which were ugly in their start\" to give yourself some mental peace."

    jump checkpoint

label testing:
    menu:
        "Your app is at a stage where internal testing just doesn't cut it. Do you find more people to test your app?"

        "$_YES":
            $ variable("morale", -15)
            $ variable("energy", -10)
            $ variable("money", -100)
            $ startup_development(-25)

            "Your testing was a success... and depressing. Everything seemed broken in the hands of people who weren't from your team. That was hard to watch."
            "And you had to buy some of those kids ice creams and stuff for their 'help'."
            "Well atleast now your app will be much more robust when you finally let it loose in the wild."

        "$_NO":
            $ move_employees("development", "testing")

            "You decided against external testing. You don't want people to find out about your idea and you can test it out yourself."
            "It might be slow but it will protect your 'unique' idea and you don't have to bother figuring out what was a 'user error' and what was a genuine error."

    jump checkpoint

label nda:
    menu:
        "One of your lawyer friend told you about NDAs and it seemed interesting and particularly useful. Do you get one?"

        "$_YES":
            $ variable("morale", -25)
            $ variable("money", -2000)

            "The lawyer drafted one quickly but after doing some research, you find that investors usually frown upon NDAs, especially when you ask them to sign it."

        "$_NO":
            $ variable("energy", -25)

            "You researched about them some more and found that investors usually frown upon NDAs, especially when you ask them to sign it."
            "Since you want to be in the good graces of any future investors, you decided against getting a NDA."

    jump checkpoint
