# lib/cli.py
from models.players import Player
from blessed import Terminal

term = Terminal()

""" MAIN MENU CLI """
from helpers import (
    exit_program,
    view_all_players,
    view_players_in_next_session,  
)

from create_player import (
    create_new_player
)

def display_main_menu():
    while True:
        main_menu()
        choice = input("❯❯ ")
        if choice == "dm":
            print("It's a secret to everybody")
            password = input("❯❯ ")
            if password == "secret":
                run_dm_mode()
        elif choice == "0":
            exit_program()
        elif choice == "1":
            create_new_player()
        elif choice == "3":
            view_all_players()
        elif choice == "2":
            display_profile_menu()
        elif choice == "4":
            view_players_in_next_session()
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    print(term.goldenrod3_on_purple3(term.center("D&D Campaign Manager:")))
    print("0. Exit the program")
    print("1. Create new player")
    print("2. View your profile")
    print("3. View all players")
    print("4. View players attending next session")

""" PLAYER PROFILE CLI """
from helpers import (
    view_all_characters,
    get_active_char,
    delete_character,
    rsvp,
    delete_player,
    change_level,
    edit_active,
    cancel_game
)
from create_char import (
    create_new_char_menu
)

def display_profile_menu():
    current_player = None

    def profile_menu():
        print(term.rebeccapurple_on_dodgerblue(f"★ {current_player.name}'s Profile ★")) 
        print(term.red('----') + term.orange('----') + term.khaki1('----') + term.green('----') + term.blue('----') + term.purple('----'))
        print("0. Back to Main Menu")
        print("1. Create new character")
        print("2. View all characters")
        print("3. View your current character")
        print("4. RSVP for next session")
        print("5. Delete a character")
        print("6. Delete your profile")
        print(term.red('----') + term.orange('----') + term.khaki1('----') + term.green('----') + term.blue('----') + term.purple('----'))

    name = input('Name: ')
    name_list = [player.name.lower().strip() for player in Player.all()]
    if name.lower().strip() in name_list:
        index = name_list.index(name.lower().strip())
        password = input('Password: ')
        if password == [player for player in Player.all()][index].password:
            current_player = [player for player in Player.all()][index]
        else:
            print(term.red3_on_snow3("Incorrect Password!"))
    else:
        print(term.red3_on_snow3("No user found with that name!"))
        

    if current_player:
        while current_player:
            profile_menu()
            choice = input('❯❯ ')
            if choice == '0':
                break
            elif choice == '1':
                create_new_char_menu(current_player)
            elif choice == '2':
                print(term.red('----') + term.orange('----') + term.khaki1('----') + term.green('----') + term.blue('----') + term.purple('----'))
                print(term.blue4_on_green("Your Characters:"))
                view_all_characters(current_player)
            elif choice == '3':
                print(term.red('----') + term.orange('----') + term.khaki1('----') + term.green('----') + term.blue('----') + term.purple('----'))
                print(term.blue4_on_green("Your Current Character:"))
                get_active_char(current_player)
            elif choice == '4':
                rsvp(current_player)
            elif choice == '5':
                delete_character(current_player)
            elif choice == '6':
                deleted = delete_player(current_player)
                if deleted == True:
                    break
            else:
                print(term.red3_on_snow3("Invalid choice. Please try again."))

def run_dm_mode():
    def dm_menu():
        print(term.goldenrod3_on_blue3("★ Secret Dungeon Master Mode ★")) 
        print(term.red('----') + term.orange('----') + term.khaki1('----') + term.green('----') + term.blue('----') + term.purple('----'))
        print("0. Back to Main Menu")
        print("1. See all characters")
        print("2. Change a characters level")
        print("3. Remove players from next game")
        print("4. Cancel next game")
        print(term.red('----') + term.orange('----') + term.khaki1('----') + term.green('----') + term.blue('----') + term.purple('----'))

    while True:
        dm_menu()
        choice = input('❯❯ ')
        if choice == '0':
            break
        elif choice == '1':
            view_all_characters('dm')
        elif choice == '2':
            change_level()
        elif choice == '3':
            edit_active()
        elif choice == '4':
            cancel_game()
        else:
            print(term.red3_on_snow3('Invalid choice. Please try again.'))

if __name__ == "__main__":
    display_main_menu()

