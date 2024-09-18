import datetime
import random
from faker import Faker

class HL7Generator:
    
    def __init__(self, fake=None):
        self.msh = None
        self.pid = None
        self.obr = None
        self.obx = None 
        self.fake = fake
        
    def get_hl7_str(self):
        self.gen_msh()
        self.gen_pid()
        self.gen_obr()
        self.gen_obx()
        
        message = f"{self.msh}\n{self.pid}\n{self.obr}\n{self.obx}\n"
        
        return message
        
    def gen_msh(self):
        # MSH Segment (Message Header)
        
        self.msh = f"MSH|^~\\&|{self.fake.company()}|{self.fake.company()}|{self.fake.company()}|{self.fake.company()}|" \
            f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}||ORU^R01|{random.randint(100000, 999999)}|P|2.3"
            
        return self.msh
            
    def gen_pid(self):
        # PID Segment (Patient Identification)
        self.pid = f"PID|1||{random.randint(10000000, 99999999)}^^^{self.fake.company()}^MR||" \
            f"{self.fake.last_name()}^{self.fake.first_name()}||" \
            f"{self.fake.date_of_birth().strftime('%Y%m%d')}|{random.choice(['M', 'F'])}||" \
            f"{self.fake.address().replace('\n', ' ')}|{self.fake.phone_number()}|||{self.fake.ssn()}"
        return self.pid
    
    def gen_obr(self):
        
        # OBR Segment (Observation Request)
        self.obr = f"OBR|1||{random.randint(10000, 99999)}^LAB|0001^COMPLETE BLOOD COUNT^L|" \
            f"{datetime.datetime.now().strftime('%Y%m%d%H%M')}||||||||||{self.fake.company()}^LAB"
            
        return self.obr
    
    def gen_obx(self):
        
        # OBX Segment (Observation Result)
        wbc = round(random.uniform(4.0, 10.0), 1)
        self.obx = f"OBX|1|NM|0002^WBC^L|{wbc}|10^9/L|4.0-10.0|N|||F"
    
        return self.obx

if __name__ == '__main__':
    
    gen = HL7Generator(Faker())
    print(gen.get_hl7_str())