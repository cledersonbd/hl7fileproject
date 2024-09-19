"""Definition of a simple HL7 file"""

class HL7File:
    
    def __init__(self) -> None:
        self.msh = None
        self.pid = None
        self.obr = None
        self.obx = None
        