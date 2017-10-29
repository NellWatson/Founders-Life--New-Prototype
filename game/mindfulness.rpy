label morale_minor_01:
    menu:
        "You've found a precious ten minutes of quiet time but the latest release needs tested. Block out the time to meditate?"

        "$_YES":
            $ variable("morale", 5)

        "$_NO":
            $ variable("morale", -5)

    jump checkpoint

label morale_minor_02:
    menu:
        "You keep getting distracted by unimportant emails. Remove notifications from your phone?"

        "$_YES":
            $ variable("morale", 5)

        "$_NO":
            $ variable("morale", -5)

    jump checkpoint

label morale_minor_03:
    menu:
        "Some old school friends are in town and want to take you sailing this weekend. Accept their invitation?"

        "$_YES":
            $ variable("morale", 5)

        "$_NO":
            $ variable("morale", -5)

    jump checkpoint

label morale_minor_04:
    menu:
        "An aspiring founder wants to meet for coffee. Accept?"

        "$_YES":
            $ variable("morale", 5)

        "$_NO":
            $ variable("morale", -5)

    jump checkpoint

label morale_minor_05:
    menu:
        "You've stopped reflecting on your day. Reset the habit?"

        "$_YES":
            $ variable("morale", 5)

        "$_NO":
            $ variable("morale", -5)

    jump checkpoint

label morale_major_01:
    menu:
        "Danny is an incredible engineer but his arrogance and aloofness keeps upsetting the design team. Fire him?"

        "$_YES":
            $ variable("morale", 10)

        "$_NO":
            $ variable("morale", -10)

    jump checkpoint

label morale_major_02:
    menu:
        "Mandy has ordered in pizza for lunch. Leave your quinoa salad in the fridge and join the team for a slice?"

        "$_YES":
            $ variable("morale", 10)

        "$_NO":
            $ variable("morale", -10)

    jump checkpoint

label morale_major_03:
    menu:
        "With your current pace, there is no way that the MVP is going to ship to the schedule you promised interested VCs. Pressure the team to crunch over the weekend?"

        "$_YES":
            $ variable("morale", -10)

        "$_NO":
            $ variable("morale", 10)

    jump checkpoint

label morale_major_04:
    menu:
        "You have a hilarious idea for a little selfie app. Cancel brunch plans and crunch it as a weekend side-project?"

        "$_YES":
            $ variable("morale", -10)

        "$_NO":
            $ variable("morale", 10)

    jump checkpoint

label morale_major_05:
    menu:
        "These financials won't model themselves and you can't move forward without them. Finish them tonight, whatever it takes?"

        "$_YES":
            $ variable("morale", -10)

        "$_NO":
            $ variable("morale", 10)

    jump checkpoint