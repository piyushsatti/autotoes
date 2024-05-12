from datetime import datetime, timezone

from main.exceptions.CharacterCreationException import CharacterCreationException

"""
### Player
Encapsulates the members associated with a player.

#### Attributes
- player discord id
- numbers of hours played
- number of games played
- number of characters created
- linked list of characters with head pointing to latest character
#### Members
- createCharacter
"""
class Player:
    
    def __init__(self, p_discord_id, p_playtime, p_game_count, p_character_count) -> None:
        self.discord_id =  p_discord_id
        self.playtime = p_playtime
        self.game_count = p_game_count
        self.character_count = p_character_count
        self.characters = []
        self.created_on = datetime.now(timezone.utc)

    def createCharacter(self, p_name: str, p_sheet: dict, p_link_to_token: str) -> bool:
        try:
            self.characters.append(self.Character(p_name, p_sheet, p_link_to_token))
            return True
        except CharacterCreationException as e:
            # should return a message that says that creation failed due to xyz reason
            if e.type[0]:
                print(e.message + "Incorrect parameter for name")
            if e.type[1]:
                print(e.message + "Incorrect parameter for sheet")
            if e.type[2]:
                print(e.message + "Incorrect parameter for link_to_token")
            return False
