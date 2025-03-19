from PIL import Image

# Ścieżka do obrazu
sciezka = "/home/bartosh/Downloads/junior.jpg"  # Użyj swojej lokalizacji


obraz = Image.open(sciezka)

szerokosc, wysokosc = obraz.size
print(f"Rozmiar: {szerokosc}x{wysokosc} px")
print(f"Format: {obraz.format}")  # np. JPEG, PNG
print(f"Tryb kolorów: {obraz.mode}")  # np. RGB, CMYK, L (czarno-biały)

mniejsza_sciezka = "mniejszy.jpg"
junior = obraz.save("mniejszy.jpg", quality=2)  # Jakość 2% (dla kompresji)

Image.open(mniejsza_sciezka).show()