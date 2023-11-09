import random
from models.characters import Character

character_info = {
    'name': '',
    'class': '',
    'race': '',
    'alignment': '',
    'abilities': '',
    'level': '',
    'player_id': ''
}

states = ['name', 'class', 'race', 'alignment', 'abilities', 'level']


def create_random_char_menu(current_player):
    print('-----------------------')
    print("Generating your character...")
    print('-----------------------')
    character_info['player_id'] = current_player.id
    creating = True
    while creating:
        current_state = 'name'

        while current_state:
            if current_state == 'name':

                get_name()
                current_state = 'class'
            elif current_state == 'class':

                get_class()
                current_state = 'race'
            elif current_state == 'race':

                get_race()
                current_state = 'alignment'
            elif current_state == 'alignment':

                get_alignment()
                current_state = 'abilities'
            elif current_state == 'abilities':

                get_abilities()
                current_state = 'level'
            elif current_state == 'level':

                get_level()
                current_state = None
        print(f'☺ {character_info["name"]}\'s Character Sheet ☺')
        print('-----------------------')
        print(f'→ Class: {character_info["class"]}')
        print(f'→ Race: {character_info["race"]}')
        print(f'→ Level: {character_info["level"]}')
        print(f'→ Alignment: {character_info["alignment"]}')
        print('→ Ability Stats:')
        for ability, score in character_info["abilities"].items():
            print(f'    • {ability}: {score}')
        print('-----------------------')
        while True:
            print("Confirm your new character (Y/N)?")
            choice = input("❯❯ ")
            if choice == "Y":
                Character.create_char(
                    character_info["name"],
                    character_info["class"],
                    character_info["race"],
                    character_info["abilities"]["Strength"],
                    character_info["abilities"]["Dexterity"],
                    character_info["abilities"]["Constitution"],
                    character_info["abilities"]["Intelligence"],
                    character_info["abilities"]["Wisdom"],
                    character_info["abilities"]["Charisma"],
                    character_info["alignment"],
                    character_info["player_id"],
                    character_info['level']
                )
                print("✔ ✔ SUCCESS ✔ ✔")
                print("Your new character has been saved!")
                print("Returning to your profile...")
                return True
            elif choice == "N":
                print("✖ ✖ CANCELLED ✖ ✖")
                print("Returning to your Profile...")
                creating = False
                break
            else:
                print("Type Y or N to confirm or restart your new character")


def get_name():
    character_info["name"] = random.choice([
        "Alaric",
        "Elara",
        "Gareth",
        "Rhysand",
        "Theron",
        "Lyra",
        "Tobias",
        "Seraphina",
        "Nesta",
        "Aria",
        "Reynard",
        "Livia",
        "Lucien",
        "Elysia",
        "Azriel",
        "Evangeline",
        "Darian",
        "Elowen",
        "Kellan",
        "Casimir",
        "Eleanora",
        "Seraphim",
        "Alaric",
        "Isolde",
        "Feyre",
        "Selene",
        "Thaddeus",
        "Celestia",
        "Octavius"
    ])
    # print(f'★ Character\'s name: {character_info["name"]} ★')


def get_class():
    character_info["class"] = random.choice([
        "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
        "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"
    ])
    # print(f'★ You chose: {character_info["class"]} ★')


def get_race():
    character_info["race"] = random.choice([
        "Dragonborn", "Dwarf", "Elf", "Gnome",
        "Goblin", "Halfling", "Human", "Orc", "Tiefling"
    ])
    # print(f'★ You chose: {character_info["race"]} ★')


def get_alignment():
    alignments = [
        ["Lawful Good", "Lawful Neutral", "Lawful Evil"],
        ["Neutral Good", "True Neutral", "Neutral Evil"],
        ["Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
    ]
    character_info['alignment'] = random.choice(
        [alignment for row in alignments for alignment in row]
    )
    # print(f'★ You chose: {character_info["alignment"]} ★')


"""returns a list of 3 random numbers between 1-6. adds the 3 numbers and assigns it to a variable 'ability score'
"""


def roll_3d6():
    # print('-----------------------')
    # print("Rolling 3 d6...")
    dice_rolls = [random.randint(1, 6) for _ in range(3)]
    # print(f"Dice results: {dice_rolls}")
    ability_score = sum(dice_rolls)
    return ability_score


"""returns the list of abilities, user can select an ability and invoke roll_3d6. adds ability: score pair to dictionary and removes ability from list of abilities. loops until ability list is empty 
"""


def get_abilities():
    abilities = ['Strength', 'Dexterity', 'Constitution',
                'Intelligence', 'Wisdom', 'Charisma']
    ability_scores = {}
    for _ in range(len(abilities)):
        selected_ability = abilities.pop(0)
        ability_scores[selected_ability] = roll_3d6()
        # print(
        #     f'★ {selected_ability} Score: {ability_scores[selected_ability]} ★'
        # )
        # print('-----------------------')

    character_info["abilities"] = ability_scores


def get_level():
    character_info["level"] = random.randint(1, 10)
    # print(f'★ Level: {character_info["level"]} ★')
