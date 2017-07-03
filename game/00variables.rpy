define STARTUP_FIELDS = ["Energy", "A.I.", "Robotics", "Biotech", "Healthcare", "Pharmaceuticals", "Education", "Human Augmentation", "VR and AR", "Transportation & Housing", "One Million Jobs", "Programming Tools", "Hollywood 2.0", "Diversity", "Enterprise Software", "Financial Services", "Computer Security", "Global Health", "Underserved Communities", "Food and Farming", "Mass Media", "Improving Democracy", "Future of Work", "News", "Water"]

# In the future, automate this process
define STARTUP_ICONS = ["biomass-512.png", "chip-512.png", "crab-512.png", "dice-512.png", "factory-512.png", "gas-512.png", "greentech-512.png", "in_love-512.png", "lighthouse-512.png", "matches-512.png", "pig-512.png", "plant_under_sun-512.png", "pretzel-512.png", "private-512.png", "queen-512.png", "retro_tv-512.png", "sparrow-512.png", "survival_bag-512.png", "thor_hammer-512.png"]

define FOUNDER_INDEX = {
    0: ("Validating Market", 0),
    1: ("Prototyping", 99000),
    2: ("Incorporating", 250000),
    3: ("Incubating", 500000),
    4: ("Accelerating", 1000000),
    5: ("Raising VC investment", 5000000),
    6: ("Capturing Product/Market Fit", 10000000),
    7: ("Scaling growth", 50000000),
    8: ("Preparing for IPO", 250000000),
    9: ("Making shareholders happy", 1000000000),
    10: ("The latest, greatest startup unicorn!", 100000000000),
}

default CURRENCY = "$"

default founder_name = ""
default startup_name = ""
default startup_field = ""
default startup_icon = ""

default founder_level = 1
default last_founder_level = 0

default energy = 100
default morale = 100
default money = 0
default current_sprint = 0

default turn_no = 0
default month = 1
default level_up = False

default event_name = ""

default energy_bar = SuperBar("#559fdd", "#00ff00", "#ff0000", "energy", width=500, height=50)
default morale_bar = SuperBar("#559fdd", "#00ff00", "#ff0000", "morale", width=500, height=50)
default review_bar = Bar(value=1, range=1, width=500, height=50)
