

label cloud:
    menu:
        "Your lead programmer wants us build and run our own servers. Do it?"

        "$_YES":
            $ variable("energy", -20)
            $ variable("morale", 20)
            $ variable("money", 2000)

        "$_NO":
            $ variable("energy", 20)
            $ variable("morale", -20)
            $ variable("money", -100)

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
            $ variable("money", -5000)

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
            $ variable("money", -1000)

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
            $ variable("money", -3000)

        "$_NO":
            $ variable("morale", 20)

    "\"Launching too slowly has probably killed a hundred times more startups than too fast, but it is possible to launch too fast. The danger here is that you ruin your reputation. You launch something, the early adaptors try it out, and if it’s not good they don’t come back.\""
