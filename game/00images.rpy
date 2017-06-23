image bg lounge = "images/bg/lounge.jpg"
image nell bot = Placeholder("girl")
image nell normal = Transform("images/contacts/nell.png", crop=(0, 0, 210, 255))

image input_caret:
    Text("|")
    pause 0.5
    alpha 0.0
    pause 0.5
    alpha 1.0
    repeat
