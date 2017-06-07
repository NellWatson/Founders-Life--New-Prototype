label start:

    scene bg lounge
    show screen hud

    jump set_startup

label checkpoint:
    $ event_name = ""

    if energy > 100:
        $ energy = 100

    if morale > 100:
        $ morale = 100
    
    if turn_no and not (turn_no % 4):
        $ current_sprint = energy * morale * turn_no * 7 * founder_level
        $ money += current_sprint

        call screen startup_review("bg lounge")

        if money > FOUNDER_INDEX[founder_level][1]:
            $ founder_level += 1
            if founder_level > 10:
                $ founder_level = 10
        $ month += 1

        call screen level_up("bg lounge")

    if energy > 0 and morale > 0:
        $ turn_no += 1
        
        jump expression find_event()

    elif energy < 0:
        call screen err_msg(message="You are out of Energy.", title="game over")
    elif morale < 0:
        call screen err_msg(message="You are out of Morale.", title="game over")

    if month > 1:
        "You survived [turn_no] weeks."
    else:
        "You survived [turn_no] weeks."

    return

label cloud:
    menu:
        "Your lead programmer wants us build and run our own servers. Do it?"

        "$_YES":
            $ variable("energy", -20)
            $ variable("morale", 20)

        "$_NO":
            $ variable("energy", 20)
            $ variable("morale", -20)

    "Until we have validated our startup, it would had been better to simply utilise cloud platforms and services."

    jump checkpoint

label day_one_pr:
    menu:
        "Send out a press release to announce your new venture?"

        "$_YES":
            $ variable("energy", -5)
            $ variable("morale", -10)

        "$_NO":
            $ variable("energy", 20)
            $ variable("morale", 20)

    "Don’t waste your time, energy and money on premature, unfocused publicity."

    jump checkpoint

label conference:
    menu:
        "There’s a conference coming up that looks interesting. Buy a ticket for $5,000?"

        "$_YES":
            $ variable("energy", -50)
            $ variable("morale", -10)

        "$_NO":
            $ variable("energy", 50)
            $ variable("morale", 50)

    "Don’t waste vital product development funds on conferences in the early stages of your startup."

    jump checkpoint

label key_messaging:
    menu:
        "Figuring out the key messaging for your startup is distracting you from product development. Should you hire a PR firm?"

        "$_YES":
            $ variable("energy", 20)
            $ variable("morale", -20)

        "$_NO":
            $ variable("energy", -30)
            $ variable("morale", 50)

    "\"Never outsource the key messaging of the company to a PR firm…You should figure int what the message if the company is going to be yourself.\" - Sam Altman"

    jump checkpoint

label premature_launch:
    menu:
        "We have a very basic working version. Should we roll out a public beta?"

        "$_YES":
            $ variable("energy", 0)
            $ variable("morale", -20)

        "$_NO":
            $ variable("morale", 20)

    "\"Launching too slowly has probably killed a hundred times more startups than too fast, but it is possible to launch too fast. The danger here is that you ruin your reputation. You launch something, the early adaptors try it out, and if it’s not good they don’t come back.\""

    jump checkpoint

label ux_research:
    menu:
        "Your designer thinks you should run some UX Research before we continue building out the product?"

        "$_YES":
            $ variable("energy", -20)
            $ variable("morale", 20)

        "$_NO":
            $ variable("energy", 30)
            $ variable("morale", -30)

    "UX Research is important. You are not your user."

    jump checkpoint

label delegation:
    menu:
        "Your workload is becoming distracting. Should you take a week out to train up your team to handle key tasks?"

        "$_YES":
            $ variable("energy", -20)
            $ variable("morale", 30)

        "$_NO":
            $ variable("energy", -40)
            $ variable("morale", -40)

    "\"Many founders try to delegate by having employees do all the grunt work, but then stuck try to make ask the decisions.\" - Sam Altman"

    jump checkpoint

label equity:
    menu:
        "You have finally found your perfect designer but she wants 10% equity to join. Should you agree to her terms?"

        "$_YES":
            $ variable("energy", 30)
            $ variable("morale", 30)

        "$_NO":
            $ variable("energy", -30)
            $ variable("morale", -30)

    "\"Equity is…a very important component of compensation. YC company data suggests the most successful companies give out a lot of equity.\" - Sam Altman"

    jump checkpoint

label beta:
    menu:
        "It is going to impossible to get to \"Feature Complete\" for the next scheduled Beta rollout. Should we push back the release date?"

        "$_YES":
            $ variable("morale", -10)

        "$_NO":
            $ variable("energy", -20)
            $ variable("morale", 30)

    "\"Fix Time and Budget, Flex Scope. “Scope down. It’s better to make half a product than a half-assed product.\" - Jason Fried"

    jump checkpoint

label nda:
    menu:
        "Your lawyer wants to draw up an NDA for potential VCs to sign?"

        "$_YES":
            $ variable("energy", -20)
            $ variable("morale", -50)

        "$_NO":
            $ variable("energy", 5)
            $ variable("morale", 40)

    "Typically, VCs won’t sign an NDA. Asking them diminishes their confidence in you."

    jump checkpoint

label micro_managing:
    menu:
        "Key team members want to own the tasks they have been delegated. Should you stop micro-managing key activities?"

        "$_YES":
            $ variable("energy", 40)
            $ variable("morale", 40)

        "$_NO":
            $ variable("energy", -40)
            $ variable("morale", -40)

    "\"Many founders try to delegate by having employees do all the grunt work, but then stuck try to make ask the decisions.\" - Sam Altman"

    jump checkpoint
