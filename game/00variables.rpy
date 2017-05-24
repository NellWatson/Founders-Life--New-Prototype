define STARTUP_FIELDS = ["Energy", "A.I.", "Robotics", "Biotech", "Healthcare", "Pharmaceuticals", "Education", "Human Augmentation", "VR and AR", "Transportation & Housing", "One Million Jobs", "Programming Tools", "Hollywood 2.0", "Diversity", "Enterprise Software", "Financial Services", "Computer Security", "Global Health", "Underserved Communities", "Food and Farming", "Mass Media", "Improving Democracy", "Future of Work", "News", "Water"]

# In the future, automate this process
define STARTUP_ICONS = ["biomass-512.png", "chip-512.png", "crab-512.png", "dice-512.png", "factory-512.png", "gas-512.png", "greentech-512.png", "in_love-512.png", "lighthouse-512.png", "matches-512.png", "pig-512.png", "plant_under_sun-512.png", "pretzel-512.png", "private-512.png", "queen-512.png", "retro_tv-512.png", "sparrow-512.png", "survival_bag-512.png", "thor_hammer-512.png"]

define FOUNDER_INDEX = {
    1: {
        "name": "Prototyping",
        "dev": 0,
        "pr": 0,
        "testing": 0
    },
    2: {
        "name": "Incorporating",
        "dev": 280,
        "pr": 0,
        "testing": 0
    },
    3: {
        "name": "Incubating",
        "dev": 680,
        "pr": 150,
        "testing": 300
    },
    4: "Accelerating",
    5: "Raising VC investment",
    6: "Capturing Product/Market Fit",
    7: "Scaling growth",
    8: "Preparing for IPO",
    9: "Making shareholders happy",
    10: "The latest, greatest startup unicorn!",
}

default CURRENCY = "$"

default founder_name = ""
default startup_name = ""
default startup_field = ""
default startup_icon = ""

default founder_level = 1

default energy = 100
default morale = 100
default money = 25000

default development = 0
default dev_employees = 3
default pr = 0
default pr_employees = 0
default testing = 0
default testing_employees = 0

default turn_no = 0
default month = 1

default event_name = ""
