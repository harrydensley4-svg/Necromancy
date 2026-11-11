from undead import Undead
from resource_manager import ResourceManager
from skeleton_warrior import SkeletonWarrior
from vengeful_ghost import VengefulGhost
from putrid_zombie import PutridZombie
from phantom_guardian import PhantomGuardian
from death_knight import DeathKnight

class SummoningRitual:
    """
    Represents a summoning ritual.
    This is responsible for the creation of undead.

    Attributes
    -------
    undead_name (str): The name of the undead to be created.
    summon_class (Undead): The class of the undead creature.
    health (int): The health of the undead creature.
    power (int): The starting power of the undead creature.
    ectoplasm (int): The ectoplasm cost.
    necrotic (int): The necrotic rune cost to summon the undead.
    spirit (int): The spirit rune cost to summon the creature.
    bone (int): The bone rune cost to summon the creature.
    flesh (int): The flesh rune cost to summon the creature.

    Methods:
    --------
    get_undead_name()
        Returns the name of the undead being created.
    get_summon_class()
        Returns the summon class of the undead.
    get_health()
        Returns the starting health of the undead.
    get_power()
        Returns the starting power of the undead.
    get_ectoplasm()
        Returns the ectoplasm cost of creating the undead.
    get_necrotic()
        Returns the necrotic rune cost of creating the undead.
    get_spirit()
        Returns the spirit rune cost of creating the undead.
    get_bone()
        Returns the bone rune cost of creating the undead.
    get_flesh()
        Returns the flesh rune cost of creating the undead.
    check_ritual(resources)
        Checks that the resource manager has enough resources to undertake the summoning ritual.
    consume_resources()
        If it passes the resource check, the resources are consumed.
    create_undead()
        Returns the created undead.
    """
    def __init__(self, undead_name, ritual_id, summon_class, health, power, ectoplasm, necrotic=0, spirit=0, bone=0, flesh=0):
        self.__undead_name = undead_name
        if issubclass(summon_class, Undead):
            self.__summon_class = summon_class
        else:
            self.__summon_class = Undead
        self.__health = health
        self.__power = power

        self.__ritual_ID = ritual_id
        self.__ectoplasm = ectoplasm
        self.__necrotic = necrotic
        self.__spirit = spirit
        self.__bone = bone
        self.__flesh = flesh

    def get_undead_name(self):
        """Returns the name of the undead."""
        return self.__undead_name

    def get_summon_class(self):
        """Returns the undead summon class."""
        return self.__summon_class

    def get_health(self):
        """Returns the starting health of the undead."""
        return self.__health

    def get_power(self):
        """Returns the starting power of the undead."""
        return self.__power

    def get_ectoplasm(self):
        """Returns the ectoplasm cost."""
        return self.__ectoplasm

    def get_necrotic(self):
        """Returns the necrotic cost."""
        return self.__necrotic

    def get_spirit(self):
        """Returns the spirit cost."""
        return self.__spirit

    def get_bone(self):
        """Returns the bone cost."""
        return self.__bone

    def get_flesh(self):
        """Returns the flesh cost."""
        return self.__flesh

    def get_ritual_ID(self):
        return self.__ritual_ID

    ritual_ID = property(get_ritual_ID)

    undead_name = property(get_undead_name)
    health = property(get_health)
    power = property(get_power)
    ectoplasm = property(get_ectoplasm)
    necrotic = property(get_necrotic)
    spirit = property(get_spirit)
    bone = property(get_bone)
    flesh = property(get_flesh)
    summon_class = property(get_summon_class)

    def check_ritual(self, resources):
        """
        Checks that there are enough resources to carry out the summoning ritual

        Parameters
        ----------
        resources: ResourceManager
            The resources that will be used for the summoning ritual

        Returns
        -------
        bool
            If all the resources exceed the cost, then it returns true.
            Otherwise, it returns false.
        """
        if isinstance(resources, ResourceManager):
            return (
            resources.get_necrotic_runes() >= self.__necrotic
            and resources.get_spirit_runes() >= self.__spirit
            and resources.get_bone_runes() >= self.__bone
            and resources.get_flesh_runes() >= self.__flesh
            and resources.get_ectoplasm() >= self.__ectoplasm
        )

    def consume_resources(self, resources):
        """
        If it passes the resource check, 
        then the resources are consumed.

        Parameters:
        -----------
        resoureces: ResourceManaager
            The resources that will be used for the summoning ritual.

        Returns:
        --------
        bool
            If the check is passed, the resources are consumed and true is returned.
            Otherwise, false is returned.
        """
        if self.check_ritual(resources):
            resources.spend_resources(
                self.__necrotic,
                self.__spirit,
                self.__bone,
                self.__flesh,
                self.__ectoplasm
            )
            return True
        return False

    def create_undead(self, undead_ID):
        """
        Create the undead based on the values and some undead_ID.

        Parameters:
        -----------
        undead_ID : int
            The unique identifier for the undead being created.

        Returns:
        --------
        Undead
            It returns an undead class based on the summon class.
        """
        return self.__summon_class(undead_ID, self.__undead_name, self.__health, self.__power)

    def __str__(self):
        """Returns a readable string description of the object. """
        return f'{self.undead_name}, {self.health}, {self.power}'