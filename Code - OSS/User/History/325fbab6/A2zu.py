f = open('test.txt', 'elo', encoding = 'utf-8', buffering = 1)
print("Nazwa pliku: "+  f.name + "\ntryb otwarcia: ", f.mode +"\nBuforowanie: " + str(f.line_buffering))