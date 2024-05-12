from main.models.Character import Character
from main.exceptions.DTQexception import DTQexception

"""
### DTQ
- type of DTQ
- character doing dtq
"""
class DTQ:

    def __init__(self, p_characters: list) -> None:
        if not all(x for x in [isinstance(x, Character) for x in p_characters]):
            raise DTQexception
        self.target = p_characters