class SummoningRitual:
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