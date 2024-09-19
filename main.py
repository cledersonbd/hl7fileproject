from hl7lib import HL7Generator, HL7Reader
from faker import Faker
from time import sleep
import os

if __name__ == '__main__':
    
    file_dir = 'output/'
    qty = int(input('How many fake files? '))
    
    faker = Faker()
    gen = HL7Generator(faker)
    
    print('Generating {qty} files...')
    for i in range(qty):
        with open(f'{file_dir}file_{i}.txt', 'w') as fp:
            fp.write(gen.get_hl7_str())
            
    
    print(f'You have now {qty} example files in {file_dir}')
    sleep(3)
    
    
    print(f'Now reading HL7 files in {file_dir}')
    
    files = [os.path.join(file_dir, file) for file in os.listdir(file_dir) if os.path.isfile(os.path.join(file_dir, file))]
    for file in files:
        print(file)
        with open(file, 'r') as fp:
            print('abri o arquivo ')
            reader = HL7Reader(fp.readlines())
            if reader.is_valid():
                print(f'{file} is a valid')
    