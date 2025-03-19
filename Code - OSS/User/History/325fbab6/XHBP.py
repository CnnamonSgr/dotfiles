def czytanie(*args):
    with open('test.txt', 'r') as f:  
        return "Jego zawartość: " + f.read()  

print(czytanie())
