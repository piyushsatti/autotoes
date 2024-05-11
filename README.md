# Auto-Toes
This is the bot for Tales of Exandria server. It has been made as an experiment to augument the westmarching experience. This is a passion project, dont expect it to work but the ideas and patterns used should stand the test of time.

# Naming Convention
- `member/s` these are all members of a discord server
- `player/s` these are members that are players at tables
- `DM/s` these are special `player/s` that have additional capabilities such as DMing
- `authority/s` these are HIGHER AUTHORITY. Must be bowed to and respects :Prayge:
- `>` mention how high or `<` how low the priority is

# Features

## Tracking [>]
- Resource Points
- Downtime Availability
- Registering games: `DM/s` vs `Player/s`
- Rest: Long/Short
- Quests: Linking quests, and adventure summaries to the game
- Server Store
    - Alchemy
    - Supply Store

### Player [>>>]
- Active Player Token Thread -> `token link`
- All Player Token Threads -> `LIST(token link)`
- Linked Quests -> `MAP(token link -> quest link)`
- Linked Adventure Summaries -> `MAP(token link -> adventure summary link)`
- Used Shrine Services -> `MAP(token link -> quest link)`
- Automate number of games played - [msg link](https://discord.com/channels/1199048900452036699/1236960180793639002)


### DMs [>>]
- Quest Ran -> `quest link`
- Quest Hooks -> `link to any quest hook taken`
- Players
    - `members` played under this person's table - track when
    - 

## Automate DTQs [<<<]
- No one wants the feature it seems...? They will later.

## Automate Market [<<<]
- Market items can be put up for sale/auction; players can bid on them.

# Program Structure
This section details how the program has been laid out, it follows the MVC architecture. These exist in the `src/main`.
## Member Oriented Classes
These are models used in the project, these lie in the `src/main/model`.
### Player
Encapsulates the members associated with a player.
#### Attributes
- player discord id
- numbers of hours played
- number of games played
- number of characters created
- linked list of characters with head pointing to latest character
#### Members

### Character
#### Attributes
- linked list of dtqs

### DTQ
- type of DTQ
- character doing dtq

### DM extends Player
Extends the player class to add DM members into the class.
#### Attributes
#### Members

### Quest
Encapsulates the members associated with a quest. 
#### Attributes
Lists the data members associated with the quest class.
- Discord Message Link
- Link to DM
- Quest Type
- Quest Number
- Quest Duration
    - Expected
    - Actual
- List of Players
- Link to AdventureSummary
#### Methods
Lists the methods associated with the quest class.
- Getters and setters for members # implementing type checking and null returns
- contains methods # Generic implementation using checking object type

### AdventureSummary
Encapsulates the members associated with an adventure summary.
#### Attributes
- Discord Message Link
- Link to DM
- List of Players
- Link to Quest
- List of links to `self.type` # Allows linking of adventure summaries
#### Methods
Lists the methods associated with the quest class.
- Getters and setters for members # implementing type checking and null returns
- contains methods # Generic implementation using checking object type

## To-Do
- [ ] Talk to Irfan about tracking
- [ ] Create System Requirement Document (SRD)
    - [ ] Talk to Irfan about req
    - [ ] 
- [ ] Fix git issue
- [ ] 