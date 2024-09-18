

class HL7Reader:
    
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
    
    def __init__(self, hl7_string):
        if not hl7_string:
            raise ValueError('Invalid HL7 String')
        
        self.parse(hl7_string)
    

    def parse(self, text_hl7: str):
        lines = text_hl7.splitlines()
        
        for line in lines:
            fields = line.split(self.DELIMITER)
            
            
            if fields[0] == 'MSH':
                subfields = fields[8].split('^')
                print(f'Type: {subfields[0]} - Event: {subfields[1]}') 
                
            print(f'Found {fields[0]} segment', 
                  f'meaning \'{self.segments[fields[0]]['description']}\'')

if __name__ == '__main__':
    
    reader = HL7Reader()