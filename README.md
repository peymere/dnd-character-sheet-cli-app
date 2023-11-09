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

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/peymere/dnd-character-sheet-cli-app

    cd dnd-character-manager

# Usage

1. Manage the users and characters of a D&D campaign
2. Create player profiles where a user can create characters and RSVP to sessions

# Technology Stack
- Built with Python
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


---

## Updating README.md

`README.md` is a Markdown file that should describe your project. You will
replace the contents of this `README.md` file with a description of **your**
actual project.

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this assignments's resources for a basic guide to Markdown.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
