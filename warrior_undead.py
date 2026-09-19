from undead import Undead

class WarriorUndead(Undead):
    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def command(self):
        return super().command() + 'It prepares for battle. '

    def combat_style(self):
        return 'Direct martial combat. '

    def __str__(self):
        return 'Undead Warrior' + super().__str__()
