from undead import Undead

class CursedUndead(Undead):
    """
    Represents a Cursed Unded object.
    It inherits from the Undead class.

    Methods:
    --------
    command()
        Returns the overidden command.
    combat_style()
        Returns the Cursed Undead combat style.
    """
    def __init__(self, undead_ID, name, health, power):
        super().__init__(undead_ID, name, health, power)

    def command(self):
        """Returns the updated command."""
        return super().command() + 'It casts a curse. '

    def combat_style(self):
        """Returns the cursed undead combat style."""
        return 'Supernatural combat. '

    def __str__(self):
        """Returns a readable string description."""
        return 'Cursed Undead' + super().__str__()