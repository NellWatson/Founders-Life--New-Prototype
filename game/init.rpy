init python:
    
    import store.telemetry as telemetry

    class MoneyManager():
        def __init__(self, starting_fund):
            self.starting_fund = starting_fund
            self._last_calc_total = starting_fund
            self.store = {}

        def add_weekly_earning(self, amount=0, month=None):
            if not month:
                month = store.month
            if amount == 0:
                amount = store.money
            
            if month not in self.store:
                self.store[month] = []
                
            self.store[month].append(amount-self._last_calc_total)
            _last_calc_total = amount

        def get_monthly_earning(self, month=None):
            if not month:
                month = store.month
            return str(sum(self.store.get(month, [0])))

    def label_callback(name, via):
        """
        Automatically called after every jump/call and saves the present label name in 'present_label' and old label name in 'old_label'.
        """
        store.present_label = name
    config.label_callback = label_callback

    def next_chapter():
        store.current_chapter += 1
        chapter_manager.set_chapter("ch_0" + str(store.current_chapter))
        store.turn_no = 0
        store.month += 1

    for slot in renpy.list_saved_games(fast=True):
        if config.developer:
            break
            
        if slot != "custom":
            renpy.unlink_save(slot)

    renpy.music.register_channel("bar_sound", mixer="sfx", loop=True)
    renpy.music.register_channel("week_sound", mixer="sfx", loop=False)
    renpy.sound.set_volume(0.1, "week_sound")

    if not persistent.multiple_id:
        persistent.multiple_id = False

    if not persistent.submitted_form:
        persistent.submitted_form = False

    if not persistent.set_volumes:
        persistent.set_volumes = True
        _preferences.volumes['music'] = 0.25
