from resource_manager import ResourceManager
from undead import Undead

class SummoningRitual:
    """
    represents a summoning ritual

    Attributes
    -------
    name : str
    undead_name : str
    health : int
    power : int
    ectoplasm : int
    necrotic : int
    spirit : int
    bone : int
    flesh : int
    """
    def __init__(self, name, undead_name, health, power, ectoplasm, necrotic=0, spirit=0, bone=0, flesh=0):
        self.__name = name
        self.__undead_name = undead_name
        self.__health = health
        self.__power = power

        
        self.__ectoplasm = ectoplasm
        self.__necrotic = necrotic
        self.__spirit = spirit
        self.__bone = bone
        self.__flesh = flesh

    def get_name(self):
        return self.__name

    def get_undead_name(self):
        return self.__undead_name

    def get_health(self):
        return self.__health

    def get_power(self):
        return self.__power

    def get_ectoplasm(self):
        return self.__ectoplasm

    def get_necrotic(self):
        return self.__necrotic

    def get_spirit(self):
        return self.__spirit

    def get_bone(self):
        return self.__bone

    def get_flesh(self):
        return self.__flesh

    name = property(get_name)
    undead_name = property(get_undead_name)
    health = property(get_health)
    power = property(get_power)
    ectoplasm = property(get_ectoplasm)
    necrotic = property(get_necrotic)
    spirit = property(get_spirit)
    bone = property(get_bone)
    flesh = property(get_flesh)

    def check_ritual(self, resources):
        if isinstance(resources, ResourceManager):
            return (
            resources.get_necrotic_runes() >= self.__necrotic
            and resources.get_spirit_runes() >= self.__spirit
            and resources.get_bone_runes() >= self.__bone
            and resources.get_flesh_runes() >= self.__flesh
            and resources.get_ectoplasm() >= self.__ectoplasm
        )

    def consume_resources(self, resources):
        pass

    def create_undead(self, undead_ID):
        return Undead(undead_ID, self.__undead_name, self.__health, self.__power)

    def __str__(self):
        """Returns a readable string description of the object. """
        return f'{self.undead_name}, {self.health}, {self.power}'