from scgen.modules.BaseModule import BaseModule
from scgen.helpers.JointGeneration import generateJointly

class PurchasePrice(BaseModule):
    name = "purchasePrice"

    def __init__(self, forElements, distributions, elementList, moduleList, distributionsProvider, **additionalSettings):
        super().__init__(forElements, distributions, elementList, moduleList, distributionsProvider)