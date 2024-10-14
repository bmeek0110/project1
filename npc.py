class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

    def talk(self):
        print(f"{self.name}: {self.dialogue}")

    def give_quest(self):
        # Logic for giving quests
        print(f"{self.name} has a quest for you!")
