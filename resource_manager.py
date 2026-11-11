class ResourceManager:
    """
        Represents a way to manage resources, including colllecting, 
        spending and checking resource requirements. 

        Attributes
        --------
        MIN_RESOURCE (int = 0): The minimum amount of a resource you can have.
        necrotic_runes (int): The number of necrotic runes.
        spirit_runes (int): The number of spirit runes.
        bone_runes (int): The number of bone runes.
        flesh_runes (int): The number of flesh runes.
        ectoplasm (int): The amount of ectoplasm.

        Methods
        --------
        validate_runes(runes)
            Returns true if the runes are an integer and greater than or 
            equal to MIN_RESOURCE.
        get_necrotic_runes()
            Returns the number of necrotic runes.
        get_spirit_runes()
            Returns the number of spirit runes.
        get_bone_runes()
            Returns the number of bones runes.
        get_flesh_runes()
            Returns the number of flesh runes.
        get_ectoplasm()
            Returns the amount of ectoplasm.
        collect_resources()
            Acquire additional resources. 
        check_requirements()
            Returns true if the amount of resources exceed the resource cost.
        spend_resources()
            If check requiremenst is true, then the resources are 
            reduced by the respective cost.
    """
    MIN_RESOURCE = 0

    def __init__(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
        if self.validate_runes(necrotic_runes):
            self.__necrotic_runes = necrotic_runes
        else:
            self.__necrotic_runes = 0

        if self.validate_runes(spirit_runes):
            self.__spirit_runes = spirit_runes
        else:
            self.__spirit_runes = 0

        if self.validate_runes(bone_runes):
            self.__bone_runes = bone_runes
        else:
            self.__bone_runes = 0

        if self.validate_runes(flesh_runes):
            self.__flesh_runes = flesh_runes
        else:
            self.__flesh_runes = 0

        if self.validate_runes(ectoplasm):
            self.__ectoplasm = ectoplasm
        else:
            self.__ectoplasm = 0

    def validate_runes(self, runes):
        """Returns true if the runes are an integer and greater than or equal to 0."""
        return (isinstance(runes, int) and not isinstance(runes, bool) and runes >= self.MIN_RESOURCE)

    def get_necrotic_runes(self):
        """Returns the necrotic runes."""
        return self.__necrotic_runes

    def get_spirit_runes(self):
        """Returns the spirit runes."""
        return self.__spirit_runes

    def get_bone_runes(self):
        """Returns the bone runes."""
        return self.__bone_runes

    def get_flesh_runes(self):
        """Returns the flesh runes."""
        return self.__flesh_runes

    def get_ectoplasm(self):
        """Returns the ectoplasm."""
        return self.__ectoplasm

    necrotic_runes = property(get_necrotic_runes)
    spirit_runes = property(get_spirit_runes)
    bone_runes = property(get_bone_runes)
    flesh_runes = property(get_flesh_runes)
    ectoplasm = property(get_ectoplasm)

    def collect_resources(self, necrotic_runes=0, 
                          spirit_runes=0, bone_runes=0, flesh_runes=0, 
                          ectoplasm=0
    ):
        """
        Collect additional resources.

        Parameters:
        -----------
        necrotic_runes : int
            The number of collected necrotic runes.
        spirit_runes : int
            The number of collected spirit runes.  
        bone_runes : int
            The number of collected bone runes.
        flesh_runes : int
            The number of collected flesh runes.
        ectoplasm : int
            The number of collected ectoplasm.

        Returns
        -------
        bool
            Returns true and adds the collected resources to the existing resources.
        """
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
            return True
        else:
            return False

    def check_requirements(self, necrotic_runes=0, spirit_runes=0,
                           bone_runes=0, flesh_runes=0, ectoplasm=0):
        """Returns true if all the resources exceed the resource cost."""
        return (self.__necrotic_runes >= necrotic_runes
                and self.__spirit_runes >= spirit_runes
                and self.__bone_runes >= bone_runes
                and self.__flesh_runes >= flesh_runes
                and self.__ectoplasm >= ectoplasm)

    def spend_resources(self, necrotic_runes=0, spirit_runes=0,
                        bone_runes=0, flesh_runes=0, ectoplasm=0):
        """
        Checks the requirements based on the resource cost.
        Then, subtracts the resource cost from the existing resources.

        Parameters:
        -----------
        necrotic_runes : int
            The number of collected necrotic runes.
        spirit_runes : int
            The number of collected spirit runes.  
        bone_runes : int
            The number of collected bone runes.
        flesh_runes : int
            The number of collected flesh runes.
        ectoplasm : int
            The number of collected ectoplasm.

        Returns
        -------
        bool
            Returns true, and subtracts the resource requirements if the check_requirements() is passed.
            Otherwise it returns false.
        """
        if self.check_requirements(necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
            self.__necrotic_runes -= necrotic_runes
            self.__spirit_runes -= spirit_runes
            self.__bone_runes -= bone_runes
            self.__flesh_runes -= flesh_runes
            self.__ectoplasm -= ectoplasm
            return True
        else:
            return False

    def __str__(self):
        """Returns a readable string description of the object. """
        return (f"""Necrotic: {self.__necrotic_runes}, 
                Spirit: {self.__spirit_runes}, 
                Bone: {self.__bone_runes}, 
                Flesh: {self.__flesh_runes}, 
                Ectoplasm: {self.__ectoplasm}"""
        )
