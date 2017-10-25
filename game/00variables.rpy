define STARTUP_FIELDS = ["Energy", "A.I.", "Robotics", "Biotech", "Healthcare", "Pharmaceuticals", "Education", "Human Augmentation", "VR and AR", "Transportation & Housing", "One Million Jobs", "Programming Tools", "Hollywood 2.0", "Diversity", "Enterprise Software", "Financial Services", "Computer Security", "Global Health", "Underserved Communities", "Food and Farming", "Mass Media", "Improving Democracy", "Future of Work", "News", "Water"]

# In the future, automate this process
define STARTUP_ICONS = ["biomass-512.png", "chip-512.png", "crab-512.png", "dice-512.png", "factory-512.png", "gas-512.png", "greentech-512.png", "in_love-512.png", "lighthouse-512.png", "matches-512.png", "pig-512.png", "plant_under_sun-512.png", "pretzel-512.png", "private-512.png", "queen-512.png", "retro_tv-512.png", "sparrow-512.png", "survival_bag-512.png", "thor_hammer-512.png"]

define FOUNDER_INDEX = {
    1: ("Starting Up", 0),
    2: ("Tiny Traction", 49999),
    3: ("Incubating", 149999),
    4: ("Problem/Solution Fit", 249999),
    5: ("Raising Seed", 499999),
    6: ("Accelerating", 999999),
    7: ("Product/Market Fit", 1999999),
    8: ("Raising Series A", 4999999),
    9: ("Preparing for IPO", 9999999),
    10: ("Unleashing a Unicorn", 10000000)
}
define BACKGROUNDS = ["bedroom", "garage", "coworking", "small office", "modest office", "upgrade office", "major office", "googleplex", "boardroom", "spaceship"]

default CURRENCY = "$"

default founder_name = ""
default startup_name = ""
default startup_field = ""
default startup_icon = ""

default founder_level = 1
default last_founder_level = 0

default productivity = 100
default energy = 100
default morale = 100
default money = 5000
default current_sprint = 0
default current_bg = "bg bedroom"

default turn_no = 0
default week = 0
default level_up = False

default event_name = ""
default last_event_bucket = None
default events_pool = {}

default productivity_bar = SuperBar("#559fdd", "#00ff00", "#ff0000", "productivity", xysize=(700, 36))
default energy_bar = SuperBar("#559fdd", "#00ff00", "#ff0000", "energy", xysize=(700, 36))
default morale_bar = SuperBar("#559fdd", "#00ff00", "#ff0000", "morale", xysize=(700, 36))
default review_bar = Bar(value=1, range=1, width=500, height=50)
