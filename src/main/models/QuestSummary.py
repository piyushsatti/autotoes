

from main.models.DungeonMaster import DungeonMaster
from main.models.Character import Character
from main.models.Quest import Quest

"""
### QuestSummary
Encapsulates the members associated with an quest summary.

#### Attributes
- Discord Message Link
- Link to DM
- List of Players
- Link to Quest
- List of links to `self.type` # Allows linking of quest summaries

#### Methods
Lists the methods associated with the quest class.
- Getters and setters for members # implementing type checking and null returns
- contains methods # Generic implementation using checking object type
"""
class QuestSummary:

    def __init__(
            self, 
            p_discord_msg_link: str, 
            p_dungeon_master: DungeonMaster, 
            p_characters: list,
            p_quest: Quest
        ) -> None:
        self.discord_msg_link = p_discord_msg_link
        self.dungeon_master = p_dungeon_master
        self.characters = p_characters
        self.quest = p_quest
        self.linked_summaries = []
    
    def linkSummary(self, p_summary):
        self.linked_summaries.append(p_summary)