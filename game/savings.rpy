label money_minor_01:
    show player a at center
    menu:
        "(savings_minor_01) An old friend gets in touch. His company need some technical writing done and he thought you'd be perfect. It pays $500, take the day off do the job?"

        "$_YES":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", 10)
            $ variable("money", 500)

        "$_NO":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", -10)

    jump checkpoint

label money_minor_02:
    show player b at center
    menu:
        "(savings_minor_02) A lawyer advises that you incorporate your startup. It might feel 'too soon' but is an unincorporated idea a risk worth taking?"

        "$_YES":
            $ variable("money", -500)

        "$_NO":
            $ variable("productivity", 10)

    jump checkpoint

label money_minor_03:
    show player c at center
    menu:
        "(savings_minor_03) The MVP needs a Terms of Service. Enlist the help of a lawyer?"

        "$_YES":
            $ variable("money", -500)

        "$_NO":
            $ variable("productivity", -10)
            $ variable("morale", -10)

    jump checkpoint

label money_minor_04:
    show player a at center
    menu:
        "(savings_minor_04) A tech publication wants to pay to syndicate your blog posts. The catch? You'll have to write a new one every week. Accept?"

        "$_YES":
            $ variable("productivity", -10)
            $ variable("energy", -10)
            $ variable("morale", -10)
            $ variable("money", 1000)

        "$_NO":
            $ variable("productivity", 10)
            $ variable("energy", 10)
            $ variable("morale", 10)

    jump checkpoint

label money_minor_05:
    show player b at center
    menu:
        "(savings_minor_05) There's a great office downtown but the agent is demanding a long-term lease. Sign?"

        "$_YES":
            $ variable("money", -2000)

        "$_NO":
            $ variable("morale", 10)

    jump checkpoint

label money_major_01:
    show player c at center
    menu:
        "(savings_major_01) Draw up NDA"

        "$_YES":
            $ variable("money", -2000)

        "$_NO":
            $ variable("productivity", 20)

    jump checkpoint

label money_major_02:
    show player a at center
    menu:
        "(savings_major_02) Amazon want you to use AWS instead of building your own server infrastructure. Accept?"

        "$_YES":
            $ variable("productivity", 20)
            $ variable("energy", 20)

        "$_NO":
            $ variable("money", -500)

    jump checkpoint

label money_major_03:
    show player b at center
    menu:
        "(savings_major_03) Squarespace want to sponsor your podcast but it's conditional on a weekly cadence for your startup's show. Accept?"

        "$_YES":
            $ variable("productivity", -20)
            $ variable("energy", -20)
            $ variable("morale", 20)
            $ variable("money", 500)

        "$_NO":
            $ variable("productivity", 20)
            $ variable("energy", 20)
            $ variable("morale", 20)

    jump checkpoint

label money_major_04:
    show player c at center
    menu:
        "(savings_major_04) TechCrunch offer you a 50%% discount on conference tickets. Attend?"

        "$_YES":
            $ variable("productivity", -20)
            $ variable("energy", -20)
            $ variable("morale", 20)
            $ variable("money", -100)

        "$_NO":
            $ variable("productivity", 20)
            $ variable("energy", 20)
            $ variable("morale", 20)

    jump checkpoint

label money_major_05:
    show player a at center
    menu:
        "(savings_major_05) Your accountant emails to advise that you get rid of free Uber and Lunch perks. It would reduce your burn rate by $500pm. Take the advice? "

        "$_YES":
            $ variable("morale", -20)
            $ variable("money", 500)

        "$_NO":
            $ variable("morale", 20)
            $ variable("money", -500)

    jump checkpoint
