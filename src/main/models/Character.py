from datetime import datetime, timezone

from main.exceptions.CharacterCreationException import CharacterCreationException

"""
### Character
#### Attributes
- name
- sheet json
- link to token
- created on
- linked list of dtqs
"""
class Character:

    def __init__(self, p_name: str, p_sheet: dict, p_link_to_token: str) -> None:
        # Checks if the correct types are given
        flag = [isinstance(p_name, str), isinstance(p_sheet, dict), isinstance(p_link_to_token, str)]
        if True in flag:
            raise CharacterCreationException("Error in Character Instantiation", flag)
        # Variable Instantiation
        self.name = p_name
        self.sheet = p_sheet
        self.link_to_token = p_link_to_token
        self.created_on = datetime.now(timezone.utc)
        self.dtq = []