image bg bedroom = Transform("images/bg/xp-1-bedroom.jpg", zoom=1.5)
image bg garage = Transform("images/bg/xp-2-garage.jpg", zoom=1.5)
image bg coworking = Transform("images/bg/xp-3-coworking.jpg", zoom=1.5)
image bg small office = Transform("images/bg/xp-4-small_office.jpg", zoom=1.5)
image bg modest office = Transform("images/bg/xp-5-sv_office_modest.jpg", zoom=1.5)
image bg upgrade office = Transform("images/bg/xp-6-sv_office_upgrade.jpg", zoom=1.5)
image bg major office = Transform("images/bg/xp-7-sv_office_major.jpg", zoom=1.5)
image bg googleplex = Transform("images/bg/xp-8-googleplex.jpg", zoom=1.5)
image bg boardroom = Transform("images/bg/xp-9-boardroom.jpg", zoom=1.5)
image bg spaceship = Transform("images/bg/xp-10-spaceship.jpg", zoom=1.5)

image side nell bot = Placeholder("girl")
image side nell normal = "images/contacts/nell.png"

image input_caret:
    Text("|")
    pause 0.5
    alpha 0.0
    pause 0.5
    alpha 1.0
    repeat
