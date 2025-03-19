def czytanie(str):

    if len(str) == 0:
        raise Exception("tekst musi być kurwa albo wypierdalasz")

    with open('test.txt', 'r') as f:  
        przed = f.read()
        print(f"Jego zawartość przed zmianą: {przed}")
    

    with open('test.txt', 'a') as f:
        f.write(str + "\n")
        
    with open('test.txt', 'a') as f:
        po = f.read()
        print(f"Jego zawartość po zmianie: {po}")
        

czytanie("nowy tekst")
