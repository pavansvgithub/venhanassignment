import json
from typing import Dict, Any

def process_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Example processing: extracting specific fields
    processed_data = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("address", {}).get("city")  # Nested field extraction
    }
    
    return processed_data

