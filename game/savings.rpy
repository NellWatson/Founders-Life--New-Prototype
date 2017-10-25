label money_minor_01:
    menu:
        "An old friend gets in touch. His company need some technical writing done and he thought you'd be perfect. It pays $500, take the day off do the job?"

        "$_YES":
            $ variable("money", 500)

        "$_NO":
            $ variable("money", -1)

    jump checkpoint

label money_minor_02:
    menu:
        "A lawyer advises that you incorporate your startup. It might feel 'too soon' but is an unincorporated idea a risk worth taking?"

        "$_YES":
            $ variable("money", -500)

        "$_NO":
            $ variable("money", 1)

    jump checkpoint

label money_minor_03:
    menu:
        "The MVP needs a Terms of Service. Enlist the help of a lawyer?"

        "$_YES":
            $ variable("money", -500)

        "$_NO":
            $ variable("money", 1)

    jump checkpoint

label money_minor_04:
    menu:
        "A tech publication wants to pay to syndicate your blog posts. The catch? You'll have to write a new one every week. Accept?"

        "$_YES":
            $ variable("money", 100)

        "$_NO":
            $ variable("money", -1)

    jump checkpoint

label money_minor_05:
    menu:
        "There's a great office downtown but the agent is demanding a long-term lease. Sign?"

        "$_YES":
            $ variable("money", -100)

        "$_NO":
            $ variable("money", 100)

    jump checkpoint

label money_major_01:
    menu:
        "Draw up NDA"

        "$_YES":
            $ variable("money", 500)

        "$_NO":
            $ variable("money", -500)

    jump checkpoint

label money_major_02:
    menu:
        "Amazon want you to use AWS instead of building your own server infrastructure. Accept?"

        "$_YES":
            $ variable("money", 1)

        "$_NO":
            $ variable("money", -500)

    jump checkpoint

label money_major_03:
    menu:
        "Squarespace want to sponsor your podcast but it's conditional on a weekly cadence for your startup's show. Accept?"

        "$_YES":
            $ variable("money", 500)

        "$_NO":
            $ variable("money", -1)

    jump checkpoint

label money_major_04:
    menu:
        "TechCrunch offer you a 50%% discount on conference tickets. Attend?"

        "$_YES":
            $ variable("money", -100)

        "$_NO":
            $ variable("money", 100)

    jump checkpoint

label money_major_05:
    menu:
        "Your accountant emails to advise that you get rid of free Uber and Lunch perks. It would reduce your burn rate by $500pm. Take the advice? "

        "$_YES":
            $ variable("money", 500)

        "$_NO":
            $ variable("money", -500)

    jump checkpoint
