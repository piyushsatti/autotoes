from main.models.Player import Player
from main.models.Quest import Quest

class DungeonMaster(Player):
    
    def __init__(self, p_discord_id) -> None:
        super().__init__(p_discord_id)
        self.quests_dmed = []

    def addQuest(self, p_quest: Quest) -> None:
        self.quests_dmed.append(p_quest)