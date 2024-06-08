from typing import List 

def read_file(file_path: str) -> List[str]:
    with open(file_path,'r') as file:
        lines = file.readlines() 
        for line in lines:
            return line.strip() 
    
lines = read_file("listofstringsfile.txt")
print(lines)