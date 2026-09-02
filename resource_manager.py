class ResourceManager:
    MIN_RESOURCE = 0

    def __init__(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
        if isinstance(necrotic_runes, int) and not isinstance(necrotic_runes, bool) and necrotic_runes >= self.MIN_RESOURCE:
            self.__necrotic_runes = necrotic_runes
        else:
            self.__necrotic_runes = 0

        if isinstance(spirit_runes, int) and not isinstance(spirit_runes, bool) and spirit_runes >= self.MIN_RESOURCE:
            self.__spirit_runes = spirit_runes
        else:
            self.__spirit_runes = 0

        if isinstance(bone_runes, int) and not isinstance(bone_runes, bool) and bone_runes >= self.MIN_RESOURCE:
            self.__bone_runes = bone_runes
        else:
            self.__bone_runes = 0

        if isinstance(flesh_runes, int) and not isinstance(flesh_runes, bool) and flesh_runes >= self.MIN_RESOURCE:
            self.__flesh_runes = flesh_runes
        else:
            self.__flesh_runes = 0

        if isinstance(ectoplasm, int) and not isinstance(ectoplasm, bool) and ectoplasm >= self.MIN_RESOURCE:
            self.__ectoplasm = ectoplasm
        else:
            self.__ectoplasm = 0

    def get_necrotic_runes(self):
        return self.__necrotic_runes

    def get_spirit_runes(self):
        return self.__spirit_runes

    def get_bone_runes(self):
        return self.__bone_runes

    def get_flesh_runes(self):
        return self.__flesh_runes

    def get_ectoplasm(self):
        return self.__ectoplasm

    necrotic_runes = property(get_necrotic_runes)
    spirit_runes = property(get_spirit_runes)
    bone_runes = property(get_bone_runes)
    flesh_runes = property(get_flesh_runes)
    ectoplasm = property(get_ectoplasm)

    def collect_resources(self, necrotic_runes=0, spirit_runes=0, bone_runes=0, flesh_runes=0, ectoplasm=0):
        if (isinstance(necrotic_runes, int) 
            and isinstance(spirit_runes, int) 
            and isinstance(bone_runes, int) 
            and isinstance(flesh_runes, int)
            and isinstance(ectoplasm, int)):
            self.__necrotic_runes += necrotic_runes
            self.__spirit_runes += spirit_runes
            self.__bone_runes += bone_runes
            self.__flesh_runes += flesh_runes
            self.__ectoplasm += ectoplasm
        else:
            print('Not an integer')

    def check_requirements(self, necrotic_runes=0, spirit_runes=0,
                       bone_runes=0, flesh_runes=0, ectoplasm=0):

        return (self.__necrotic_runes >= necrotic_runes 
                and self.__spirit_runes >= spirit_runes 
                and self.__bone_runes >= bone_runes 
                and self.__flesh_runes >= flesh_runes 
                and self.__ectoplasm >= ectoplasm)

    def spend_resources(self, necrotic_runes=0, spirit_runes=0,
                       bone_runes=0, flesh_runes=0, ectoplasm=0):
        if self.check_requirements(necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
            self.__necrotic_runes -= necrotic_runes
            self.__spirit_runes -= spirit_runes
            self.__bone_runes -= bone_runes
            self.__flesh_runes -= flesh_runes
            self.__ectoplasm -= ectoplasm
        else:
            print('Not enough resources')

    def __str__(self):
        return f'Necrotic: {self.__necrotic_runes}, Spirit: {self.__spirit_runes}, Bone: {self.__bone_runes}, Flesh: {self.__flesh_runes}, Ectoplasm: {self.__ectoplasm}'