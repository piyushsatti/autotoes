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
- contains methods # Generic implementation using checking object type
- endQuest # Updates the actual end time of the quest
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

    def contains(self, **kwargs) -> list:
        """Provide kargs to query a contains method, returns a nested list of bools

        There are four kwargs that can be used for the query. These are:
        - discord_msg_link: type discord message hyperlink
        - dm_discord_id: type discord id
        - characters: type list of discord ids
        - quest_summary: type discord message hyperlink
        Returns a list of the same size as the query, containing bools.
        Returns a list of list of bools in case of query on player discord ids
        """
        p_discord_msg_link: str = kwargs["discord_msg_link"]
        p_dm_discord_id: int = kwargs["dm_discord_id"]
        p_characters: Character = kwargs["characters"]
        p_quest_summary: QuestSummary = kwargs["quest_summary"]

        ret = []

        if p_discord_msg_link is not None:
            ret.append(True if p_discord_msg_link == self.discord_msg_link else False)
        if p_dm_discord_id is not None:
            ret.append(True if p_dm_discord_id == self.dm_discord_id else False)
        if p_characters is not None:
            ret.append(
                [
                    x in self.player_discord_ids for x in p_characters
                ]
            )
        if p_quest_summary is not None:
            ret.append(True if p_quest_summary == self.quest_summary else False)
        
        return ret