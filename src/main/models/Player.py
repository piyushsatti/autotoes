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

        self.active_characters = []
        self.characters = []
        self.created_on = datetime.now(timezone.utc)
