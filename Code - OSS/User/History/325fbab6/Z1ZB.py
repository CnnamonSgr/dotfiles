f = open('test.txt', 'r')
print("Nazwa pliku: "+  f.name)
print("Jego zawartość: "+ f.read())
f.close()