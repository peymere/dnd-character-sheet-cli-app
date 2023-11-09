# D&D Character and Player Manager

Manage your Dungeons and Dragons characters and profiles with this CLI app.


# Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Features](#features)
- [Character Creation](#character-creation)
- [Character Management](#character-management)
- [RSVP for Game Sessions](#rsvp-for-game-sessions)
- [Player Profile Deletion](#player-profile-deletion)
- [DM Secret Menu](#dm-secret-menu)
- [Contributing](#contributing)
- [License](#license)


# Installation

   
### Clone the repository to your local machine:
    git clone https://github.com/peymere/dnd-character-sheet-cli-app

### Navigate to the app's directory
    cd dnd-campaign-manager

### Install dependencies and enter the pipenv shell
    pipenv install
    pipenv shell

### Run the program
    python lib/cli.py
   


# Usage

1. Manage the users and characters of a D&D campaign
2. Create player profiles where a user can create characters and RSVP to sessions


# Technology Stack
- Built with Python version 3.8.13
- Utilizes an ORM for database operations
- Uses SQLite 3 as the database engine


# Features


## Main Menu Features

- View a list of all players
- View a list of players that are attending the next session
- Create new player profiles
- Users can login to view their player profiles


## Player Profile Features

### Character Creation


Create new characters with the following attributes:

- **Name**
- **Race** (choose from a list of available races)
- **Class** (choose from a list of available classes)
- **Alignment** (choose from an alignment grid)
- **Level**

Generate character abilities by "rolling" 3 d6 dice and summing the results for each ability.

Save the character to your profile.


### Character Management


- View a list of all your characters.
- Delete characters you no longer need.


### RSVP for Game Sessions


- RSVP for upcoming game sessions.
- Choose which character you'll be bringing to the session.
- View your selected "active" character sheet.


### Player Profile Deletion


Delete your player profile as well as all characters you've made.


## DM Secret Menu


Input 'dm' to access the secret Dungeon Master menu (the password is secret 😉 ).

In the DM menu, you can:

- View all characters in the database (names, class, race, and level).
- Change a character's level.
- Edit player RSVP status for the next session.
- Cancel the next session, resetting all player characters to inactive.

# Collaborators

- Peyton Meredith
    - [github](https://github.com/peymere)
    - [LinkedIn](https://www.linkedin.com/in/peytonmeredith/)

- Joseph Szpigiel
    - [github](https://github.com/JosephSzpigiel)
    - [LinkedIn](https://www.linkedin.com/in/joseph-szpigiel/)

- Haylee Rees
    - [github](https://github.com/Sassy85)
    - [LinkedIn](https://www.linkedin.com/in/haylee-rees-8504s83blk/)

# Contributing


[Contributing Guidelines](./CONTRIBUTING.md)


# License


[MIT License](./LICENSE.md)

