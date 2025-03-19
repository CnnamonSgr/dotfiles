from PIL import Image

# Ścieżka do obrazu
sciezka = "/home/user/Downloads/junior.jpg"  # Użyj swojej lokalizacji

# Otwórz obraz
obraz = Image.open(sciezka)

# Pokaż obraz
obraz.show()