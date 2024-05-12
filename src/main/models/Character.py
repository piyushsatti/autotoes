from datetime import datetime, timezone

from main.exceptions.CharacterCreationException import CharacterCreationException
from main.models.Player import Player

"""
### Character
#### Attributes
- name
- sheet json
- link to token
- number of games played
- numbers of hours played
- created on
- linked list of dtqs
"""
class Character:

    def __init__(self, p_player: Player, p_name: str, p_sheet: dict, p_link_to_token: str, p_is_active: bool = True) -> None:
        # Checks if the correct types are given
        flag = [not isinstance(p_player, Player), not isinstance(p_name, str), not isinstance(p_sheet, dict), not isinstance(p_link_to_token, str)]
        if True in flag:
            raise CharacterCreationException("Error in Character Instantiation", flag)
        # Variable Instantiation
        self.player: Player = p_player
        self.name = p_name
        self.sheet = p_sheet
        self.link_to_token = p_link_to_token
        self.is_active = p_is_active
        self.created_on = datetime.now(timezone.utc)
        self.dtq = []
        self.player.characters.append(self)

    def setIsActive(self, p_is_active: bool) -> None:
        
        self.is_active = p_is_active

        if p_is_active and (self not in self.player.active_characters):
            self.player.active_characters.append(self)
        else:
            while self in self.player.active_characters:
                self.player.active_characters.remove(self)