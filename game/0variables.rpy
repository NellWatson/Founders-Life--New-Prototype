default dev_option__event_play = []

default founder_name = ""
default startup_name = ""
default founder_portrait = Null()

default founder_level = 1
default last_founder_level = 0

default founder_score = 0
default total_founder_score = 0

default productivity = 75
default energy = 75
default morale = 75
default money = 5000
default current_sprint = 0
default current_bg = "bg bedroom"

default money_manager = MoneyManager(money)

default turn_no = 0
default current_chapter = 1
default total_days = 0
default week = 0
default month = 0
default event_code = ""
default event_name = ""
default level_up = False
default persistent.give_hints = False
default choice_hover_on = False

default feedback = {}
default feedback_given = False

default productivity_bar = SuperBar("#559fdd", "#00ff00", "#ff0000", "productivity", xysize=(700, 36))
default energy_bar = SuperBar("#559fdd", "#00ff00", "#ff0000", "energy", xysize=(700, 36))
default morale_bar = SuperBar("#559fdd", "#00ff00", "#ff0000", "morale", xysize=(700, 36))
default review_bar = Bar(value=1, range=1, width=500, height=50)

default no_of_times_died = 0
default is_telemetry_allowed = False

default gid = ""

define _game_menu_screen = "preferences"
define skip_splashscreen = False
define choice_effects = {}
