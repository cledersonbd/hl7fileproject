from hl7lib.HL7File import HL7File

class HL7Reader(HL7File):
    
    DELIMITER = '|'
    
    segments = {
        "MSH": {
            "description": "Message Header",
            'fields': {
                9:'Event',
                }
            },
        "PID": {"description": "Patient Identification"},
        "NK1": {"description": "Next of Kin"},
        "PV1": {"description": "Patient Visit"},
        "ORC": {"description": "Common Order"},
        "OBR": {"description": "Observation Request"},
        "OBX": {"description": "Observation/Result"},
        "AL1": {"description": "Allergy Information"},
        "DG1": {"description": "Diagnosis Information"},
        "PR1": {"description": "Procedures"},
        "RXA": {"description": "Pharmacy/Treatment Administration"},
        "RXO": {"description": "Pharmacy/Treatment Order"},
        "RXR": {"description": "Pharmacy/Treatment Route"},
        "IN1": {"description": "Insurance Information"},
        "GT1": {"description": "Guarantor Information"},
        "FT1": {"description": "Financial Transaction"},
        "ACC": {"description": "Accident Information"},
        "ROL": {"description": "Role Segment"},
        "EVN": {"description": "Event Type"},
        "PD1": {"description": "Patient Additional Demographics"},
        "PV2": {"description": "Patient Visit - Additional Information"},
        "CTI": {"description": "Clinical Trial Identification"},
        "PRB": {"description": "Problem Details"},
        # "Z-segments": {"description": "Custom Segments"},
    }
    
    def __init__(self, content):
        super().__init__()
        
        if not content:
            raise ValueError('Invalid HL7')
        self.parse(content)
    
    
    def is_valid(self):
        # considering a valid HL7 file if it has these 4 sections
        return self.msh and self.pid and self.obr and self.obx
    
    def parse(self, content: str | list):
        
        if isinstance(content, str):
            self.lines = content.splitlines()
        else:
            self.lines = content
        
        for line in self.lines:
            fields = line.split(self.DELIMITER)
            
            match fields[0]:
                case 'MSH':
                    self.msh = line
                case 'PID':
                    self.pid = line
                case 'OBR':
                    self.obr = line
                case 'OBX':
                    self.obx = line
                case _:
                    pass
        
        
        return self.is_valid()
    
if __name__ == '__main__':
    pass
