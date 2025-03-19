f = open('test.txt', 'r')
print("Nazwa pliku: "+  f.name)

def czytanie():
    return("Jego zawartość: "+ f.read())

f.append("i wiktora")

czytanie()

f.close()