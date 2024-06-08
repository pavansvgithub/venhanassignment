import csv
from typing import List, Dict

def read_csv(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            return row  

rows = read_csv('example.csv')
print(rows)


