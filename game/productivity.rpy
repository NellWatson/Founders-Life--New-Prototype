label productivity_minor_01:
    show player a at center
    menu:
        "(productivity_minor_01) Nobody has noticed that you've started up. Send out a press release to announce your new venture?"

        "$_YES":
            $ variable("productivity", -10)

        "$_NO":
            $ variable("energy", 10)

    jump checkpoint

label productivity_minor_02:
    show player b at center
    menu:
        "(productivity_minor_02) Your designer thinks you should run some UX Research before we continue building out the product?"

        "$_YES":
            $ variable("productivity", 10)

        "$_NO":
            $ variable("morale", -10)

    jump checkpoint

label productivity_minor_03:
    show player c at center
    menu:
        "(productivity_minor_03) Mike, the lead programmer, has got back with his MVP backlog estimates. Accept them or run some planning poker."

        "$_YES":
            $ variable("productivity", 10)

        "$_NO":
            $ variable("energy", -10)

    jump checkpoint

label productivity_minor_04:
    show player a at center
    menu:
        "(productivity_minor_04) The visual design still isn't quite right, it needs more iteration. Push back the MVP launch deadline?"

        "$_YES":
            $ variable("money", -500)

        "$_NO":
            $ variable("productivity", 10)

    jump checkpoint

label productivity_minor_05:
    show player b at center
    menu:
        "(productivity_minor_010) Figuring out the key positioning and messaging for your startup is distracting you from product development. Should you outsource this to a PR firm?"

        "$_YES":
            $ variable("energy", 10)

        "$_NO":
            $ variable("productivity", 10)

    jump checkpoint

label productivity_major_01:
    show player c at center
    menu:
        "(productivity_major_01) Mike, the lead programmer, wants to add analytics to the MVP - without them, he says, we'll be releasing blind. Push back the MVP launch deadline?"

        "$_YES":
            $ variable("morale", 20)

        "$_NO":
            $ variable("productivity", 20)

    jump checkpoint

label productivity_major_02:
    show player a at center
    menu:
        "(productivity_major_02) You have finally found your perfect Lead Designer but she wants 20%% equity to join. Should you agree to her terms?"

        "$_YES":
            $ variable("productivity", 20)

        "$_NO":
            $ variable("morale", -20)

    jump checkpoint

label productivity_major_03:
    show player b at center
    menu:
        "(productivity_major_03) You have noticed the team does not yet share your vision and focus. Start running KPIs?"

        "$_YES":
            $ variable("productivity", 20)

        "$_NO":
            $ variable("morale", -20)

    jump checkpoint

label productivity_major_04:
    show player c at center
    menu:
        "(productivity_major_04) We're shipping an MVP next week but the team feels the product is under-featured - it's bare bones and and lacking in 'sexy' bells and whistles. Do we stick to our launch plan?"

        "$_YES":
            $ variable("productivity", 20)

        "$_NO":
            $ variable("energy", -20)

    jump checkpoint

label productivity_major_05:
    show player a at center
    menu:
        "(productivity_major_010) A VC wants to chat, shall we send them over an NDA to sign?"

        "$_YES":
            $ variable("energy", -20)

        "$_NO":
            $ variable("productivity", 20)

    jump checkpoint
