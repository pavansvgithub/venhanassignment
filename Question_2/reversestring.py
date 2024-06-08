def reverse_string(s):
    new = ""
    for i in s:
        new = i + new 
    return new

string = input() 
result = reverse_string(string)
print(result)