init python:
    
    import store.telemetry as telemetry

    def label_callback(name, via):
        """
        Automatically called after every jump/call and saves the present label name in 'present_label' and old label name in 'old_label'.
        """
        store.present_label = name

    config.label_callback = label_callback

    renpy.music.register_channel("bar_sound", mixer="sfx", loop=True)
    renpy.music.register_channel("week_sound", mixer="sfx", loop=False)
    renpy.sound.set_volume(0.1, "week_sound")

    for slot in renpy.list_saved_games(fast=True):
        if slot != "custom" and not config.developer:
            renpy.unlink_save(slot)

    if not persistent.multiple_id:
        persistent.multiple_id = False

    if not persistent.submitted_form:
        persistent.submitted_form = False

    if not persistent.set_volumes:
        persistent.set_volumes = True
        _preferences.volumes['music'] = 0.25