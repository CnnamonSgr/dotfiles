def czytanie():

    nowy = input('Dodaj tekst: ')

    if len(nowy) == 0:
        raise Exception("tekst musi być kurwa albo wypierdalasz")

    with open('test.txt', 'r') as f:  
        przed = f.read()
        print(f"Jego zawartość przed zmianą: {przed}")
    

    with open('test.txt', 'a') as f:
        f.write(nowy + "\n")
        
        
    with open('test.txt', 'r') as f:
        global po
        po = f.read()
        

czytanie()

print(f"Jego zawartość po zmianie: {po}")
