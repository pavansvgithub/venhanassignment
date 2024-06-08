from typing import List 

def write_file(filepath: str,lines: List[str]) ->None:
    with open(filepath,'w') as file:
        for line in lines:
            file.write(line + "\n") 

lines = ["Hello World","This is a testfile","It has mutliple lines"]
write_file("listofstringsfile.txt",lines)
