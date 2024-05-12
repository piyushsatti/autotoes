from datetime import datetime, timezone

from main.models.QuestSummary import QuestSummary
from main.models.Character import Character


"""
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
- Link to QuestSummary

#### Methods
Lists the methods associated with the quest class.
- endQuest # Updates the actual end time of the quest
- setQuestSummary # Sets the quest summary object
"""
class Quest:

    def __init__(
            self, 
            p_discord_msg_link: str, 
            p_dm_discord_id: int, 
            p_quest_type: str, 
            p_quest_number: int,
            p_expected_quest_duration: int,
            p_characters: list
        ) -> None:
        self.discord_msg_link = p_discord_msg_link
        self.dm_discord_id = p_dm_discord_id
        self.quest_type = p_quest_type
        self.quest_number = p_quest_number
        self.expected_quest_duration = p_expected_quest_duration
        self.characters = p_characters
        self.quest_summary = None
        # Private vars for calculating quest actual time
        self.__quest_start_time = datetime.now(timezone.utc)
        self.__quest_end_time = None

    def endQuest(self) -> None:
        # Updating the quest actual time
        self.__quest_end_time = datetime.now(timezone.utc)
        self.actual_quest_duration = self.__quest_end_time - self.__quest_start_time
    
    def setQuestSummary(self, p_quest_summary: QuestSummary) -> None:
        self.quest_summary = p_quest_summary