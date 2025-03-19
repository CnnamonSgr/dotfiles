def czytanie(str):

    if len(str) == 0:
        raise Exception("tekst musi być kurwa albo wypierdalasz")

    with open('test.txt', 'r') as f:  
        return "Jego zawartość przed zmianą: " + f.read()  

    with open('test.txt', 'a') as f:
        nowy = (f"Jego zawartość po zmianie: {f.write(str)}")
        

    return nowy

czytanie("kurwa")
