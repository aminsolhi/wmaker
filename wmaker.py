import hashlib  
import random  


def generate_hex_numbers(key, count):  
    hash_input = key.encode('utf-8')  
    hashed_value = hashlib.sha256(hash_input).hexdigest()  

    hex_numbers = set()  
    random.seed(hashed_value)  

    index_width = 7  
    hex_width = 25  
    start_range_width = 30  
    end_range_width = 30  

  
    print(f"{'BitRange':<{index_width}} {'Hex Value':<{hex_width}} {'Start Range':<{start_range_width}} {'End Range':<{end_range_width}}")  
    print("-" * (index_width + hex_width + start_range_width + end_range_width + 4))  

    for i in range(scount, count + 1):  
        random_number = random.randint(2 ** i, 2 ** (i + 1))  
        hex_number = hex(random_number).removeprefix('0x')  
        start_range = f'{2 ** i:x}'  
        end_range = f'{2 ** (i + 1):x}'  

     
        print(f"{i + 1:<{index_width}} {hex_number:<{hex_width}} {start_range:<{start_range_width}} {end_range:<{end_range_width}}")  

    return  


key = 'satoshi'  
scount = int(input ("Enter Start BitRange : "))-1
count = int(input ("Enter End BitRange : "))-1
key = input ("Enter Phrase pass : ")
hex_values = generate_hex_numbers(key, count)
