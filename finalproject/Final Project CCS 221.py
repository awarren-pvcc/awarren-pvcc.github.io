print("This is a text-based adventure. Type 'end' at any time to quit the game.")
#Library of locations and actions for each location
places = {
    "start" : {
    "description" : "Your entire journey to retrieve the ancient diamond of power has lead you to this point. As you enter the temple, the entrance shuts and seals you in. Before you lie three doors.",
    "actions" : ["enter left door", "enter center door", "enter right door"],
    "Enter left door" : "startdoorleft",
    "Enter center door" : "startdoorcenter",
    "Enter right door" : "startdoorright"
    },
    "backstart" : {
    "description" : "You go back to the first room",
    "actions" : ["enter left door", "enter center door", "enter right door"],
    "Enter left door" : "startdoorleft",
    "Enter center door" : "startdoorcenter",
    "Enter right door" : "startdoorright"
    },
    "startdoorleft" : {
    "description" : "You enter the door on the left. You're met with a pedestal with a golden statuette atop it.",
    "actions" : ["go back", "take the statue"],
    "go back" : "backstart",
    "take the statue" : "deathstatue"
    },
    "deathstatue" : {
    "description" : "You pick up the statue, but it was a trap. As soon as you put it in your backpack, a large stone falls from the cieling and crushes you. Try again?",
    "actions" : ["try again"],
    "try again" : "startdoorleft"
    },
    "startdoorright" : {
    "description" : "You enter the door on the right. There is a trapdoor on the cieling and a trapdoor on the floor.",
    "actions" : ["open floor trapdoor", "open cieling trapdoor", "go back"],
    "go back" : "backstart",
    "open floor trapdoor" : "deathfloortrap",
    "open cieling trapdoor" : "cielingtrap"
    },
    "deathfloortrap" : {
    "description" : "You open the trapdoor on the floor and the ground around it crumbles a bit, causing you to fall in. You fall directly into the jaws of a hungry dragon and are eaten. Try again?",
    "actions" : ["try again"],
    "try again" : "startdoorright"
    },
    "cielingtrap" : {
    "description" : "You open the trapdoor on the cieling and climb up into the space above. You are met with a giant venomous spider who does not look happy to see you.",
    "actions" : ["fight the spider", "go back"],
    "go back" : "backstartdoorright",
    "fight the spider" : "deathspider"
    },
    "deathspider" : {
    "description" : "You draw your sword to fight the spider, but it lunges at you first and injects you with its venom. Try again?",
    "actions" : ["try again"],
    "try again" : "cielingtrap"
    },
    "backstartdoorright" : {
    "description" : "You back down out of the cieling door and shut it behind you.",
    "actions" : ["open floor trapdoor", "open cieling trapdoor", "go back"],
    "go back" : "backstart",
    "open floor trapdoor" : "deathfloortrap",
    "open cieling trapdoor" : "cielingtrap"
    },
    "startdoorcenter" : {
    "description" : "You enter the door in the center. In this room, there are two more doors which lead down sets of stairs. The left door seems to reflect a feint golden shimmer, while the right seems to glow with a light blue hue.",
    "actions" : ["go back", "enter left door", "enter right door"],
    "go back" : "backstart",
    "enter left door" : "golddoor",
    "enter right door" : "bluedoor"
    },
    "golddoor" : {
    "description" : "You descend the stairs behind the left door. At the bottom lies a huge stache of gold! But on top of it rests a sleeping dragon. You can just barely see a large gate behind the dragon.",
    "actions" : ["go back", "steal some gold", "sneak to the gate", "kill the dragon"],
    "go back" : "backupstairs",
    "steal some gold" : "deathstealgold",
    "sneak to the gate" : "gate",
    "kill the dragon" : "deathdragon"
    },
    "backupstairs" : {
    "description" : "You go back up the stairs to the previous room.",
    "actions" : ["go back", "enter left door", "enter right door"],
    "go back" : "backstart",
    "enter left door" : "golddoor",
    "enter right door" : "bluedoor"
    },
    "deathstealgold" : {
    "description" : "You carefully sneak up to the gold and begin to scoop some into your backpack. Unfortunately, the jingling noise of the gold awoke the dragon, who then incinerated you with its breath. Try again?",
    "actions" : ["try again"],
    "try again" : "golddoor"
    },
    "deathdragon" : {
    "description" : "You climb atop the mound of gold, being careful not to wake the beast. As you go to plunge your sword into its heart, you lose your footing and cause an avalanche of gold to cascade down. You are crushed underneath its weight. Try again?",
    "actions" : ["try again"],
    "try again" : "golddoor"
    },
    "bluedoor" : {
    "description" : "You descend the stairs behind the right door. At the bottom is what seems to be a tear in space. You are compelled to reach out and touch it.",
    "actions" : ["go back", "touch the anomaly"],
    "go back" : "backupstairs",
    "touch the anomaly" : "deathrift",
    },
    "deathrift" : {
    "description" : "You rach out to touch the tear and are immeditaly teleported high into the sky above the temple. You fall to the ground and are killed upon impact. Try again?",
    "actions" : ["try again"],
    "try again" : "bluedoor"
    },
    "gate" : {
    "description" : "You successfully sneak past the dragon to the gate on the other side of the room. Within the room lies the diamond of power atop a pedestal in the center. As you enter, the door seals behind you.",
    "actions" : ["take the diamond", "it's a fake"],
    "take the diamond" : "takediamond",
    "it's a fake" : "deathfake",
    },
    "deathfake" : {
    "description" : "You are convinced the diamond is a fake. However, you are sealed in to this room and cannot find any evidence of another diamond. While searching for clues, you slip in a puddle and hit your head on a rock on the floor, killing you. Try again?",
    "actions" : ["try again"],
    "try again" : "gate"
    },
    "takediamond" : {
    "description" : "You reach to the diamond and take it off its pedestal. An exit from the temple opens before you and you safely leave with the artifact. Congradulations!",
    "actions" : ["end"],
    }
    
    

}

# Preprocess places dictionary to normalize keys to lowercase
places = {key.lower(): {**value, **{k.lower(): v for k, v in value.items()}} for key, value in places.items()}

# Starting location
current_location = "start"

def describe(location):
    # Displays the description and possible actions of the current location
    print("\n" + places[location]["description"])
    print("Available actions:", ", ".join(places[location]["actions"]))

def handle_command(command, location):
    # Handles player commands
    if command in places[location]:
        return places[location][command]
    else:
        print("You can't do that here.")
    return location  # Return the same location if action not possible

# Main game loop
while True:
    describe(current_location)
    player_command = input("\nWhat do you want to do? ").lower()

    # Exit condition
    if player_command in ["end"]:
        print("Thanks for playing!")
        break

    # Handle player's command and update location
    current_location = handle_command(player_command, current_location)

