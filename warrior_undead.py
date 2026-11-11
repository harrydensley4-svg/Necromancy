from undead import Undead

class WarriorUndead(Undead):
    """
    Represents a Warrior Undead type.
    This inherits from the Undead class.

    Attributes:
    -----------
    MIN_HEALTH (int = 60): The minimum health for a warrior undead.
    MAX_HEALTH (int = 130): The maximum health for a warrior undead.
    MIN_POWER (int = 10): The minimum power for a warrior undead.
    MAX_POWER (int = 150): The maximum power for a warrior undead.x

    Methods:
    --------
    command()
        Overrides the Undead command() method.
    combat_style()
        Returns the warrior undeads combat style.
    """
    MIN_HEALTH = 60
    MAX_HEALTH = 130
    MIN_POWER = 10
    MAX_POWER = 150

    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def command(self):
        """Returns the warrior undead command."""
        return super().command() + 'It prepares for battle. '

    def combat_style(self):
        """Returns the warrior undead combat style."""
        return 'Direct martial combat. '

    def __str__(self):
        """Returns a readable string description."""
        return 'Undead Warrior' + super().__str__()
