label productivity_minor_01:
    show player a at center
    menu:
        "(productivity_minor_01) Your designer thinks you should run some UX Research before we continue building out the product?"

        "$_YES":
            $ variable("productivity", -5)

        "$_NO":
            $ variable("productivity", 5)

    jump checkpoint

label productivity_minor_02:
    show player b at center
    menu:
        "(productivity_minor_02) Nobody has noticed that you've started up. Send out a press release to announce your new venture?"

        "$_YES":
            $ variable("productivity", 5)

        "$_NO":
            $ variable("productivity", -5)

    jump checkpoint

label productivity_minor_03:
    show player c at center
    menu:
        "(productivity_minor_03) Mike, the lead programmer, has got back with his MVP backlog estimates. Accept them."

        "$_YES":
            $ variable("productivity", 5)

        "$_NO":
            $ variable("productivity", -5)

    jump checkpoint

label productivity_minor_04:
    show player d at center
    menu:
        "(productivity_minor_04) The visual design still isn't quite right, it needs more iteration. Push back the MVP launch deadline?"

        "$_YES":
            $ variable("productivity", -5)

        "$_NO":
            $ variable("productivity", 5)

    jump checkpoint

label productivity_minor_05:
    show player e at center
    menu:
        "(productivity_minor_05) Figuring out the key positioning and messaging for your startup is distracting you from product development. Should you outsource this to a PR firm?"

        "$_YES":
            $ variable("productivity", -5)

        "$_NO":
            $ variable("productivity", 5)

    jump checkpoint

label productivity_major_01:
    show player a at center
    menu:
        "(productivity_major_01) Mike, the lead programmer, wants to add analytics to the MVP - without them, he says, we'll be releasing blind. Push back the MVP launch deadline?"

        "$_YES":
            $ variable("productivity", -10)

        "$_NO":
            $ variable("productivity", 10)

    jump checkpoint

label productivity_major_02:
    show player b at center
    menu:
        "(productivity_major_02) You have finally found your perfect Lead Designer but she wants 10%% equity to join. Should you agree to her terms?"

        "$_YES":
            $ variable("productivity", 10)

        "$_NO":
            $ variable("productivity", -10)

    jump checkpoint

label productivity_major_03:
    show player c at center
    menu:
        "(productivity_major_03) Domenique Martel emails to say that she really liked your recent blog post. She has a bunch of free time now that her startup has been acquired by Google. She'd like to mentor you for a 1%% stake but she's not willing to make an angel investment in the company right now. Accept the offer?"

        "$_YES":
            $ variable("productivity", 10)

        "$_NO":
            $ variable("productivity", -10)

    jump checkpoint

label productivity_major_04:
    show player d at center
    menu:
        "(productivity_major_04) We're shipping an MVP next week but the team feels the product is under-featured - it's bare bones and and lacking in 'sexy' bells and whistles. Do we stick to our launch plan?"

        "$_YES":
            $ variable("productivity", 10)

        "$_NO":
            $ variable("productivity", -10)

    jump checkpoint

label productivity_major_05:
    show player e at center
    menu:
        "(productivity_major_05) A VC wants to chat, shall we send them over an NDA to sign?"

        "$_YES":
            $ variable("productivity", -10)

        "$_NO":
            $ variable("productivity", 10)

    jump checkpoint
