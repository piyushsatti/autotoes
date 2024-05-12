from datetime import datetime, timezone

from main.exceptions.CharacterCreationException import CharacterCreationException

"""
### Player
Encapsulates the members associated with a player.

#### Attributes
- player discord id
- linked list of characters with head pointing to latest character
#### Members
- number of games played
- numbers of hours played
"""
class Player:
    
    def __init__(self, p_discord_id) -> None:
        self.discord_id =  p_discord_id
        self.active_characters = []
        self.characters = []
        self.created_on = datetime.now(timezone.utc)
