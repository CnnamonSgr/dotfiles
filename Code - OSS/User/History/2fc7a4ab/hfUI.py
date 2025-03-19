from PIL import Image

# Ścieżka do obrazu
sciezka = "/home/bartosh/Downloads/junior.jpg"  # Użyj swojej lokalizacji


obraz = Image.open(sciezka)

szerokosc, wysokosc = obraz.size
print(f"Rozmiar: {szerokosc}x{wysokosc} px")
print(f"Format: {obraz.format}")  # np. JPEG, PNG
print(f"Tryb kolorów: {obraz.mode}")  # np. RGB, CMYK, L (czarno-biały)


# Stopień pikselizacji (im mniejsza wartość, tym większa pikselizacja)
rozmiar_bloku = 20

# Zmniejszamy obraz (zmniejszenie = większa pikselizacja)
mniejszy = obraz.resize(
    (obraz.width // rozmiar_bloku, obraz.height // rozmiar_bloku), Image.NEAREST
)

# Powiększamy z powrotem do oryginalnych wymiarów
mniejszy_piksel = mniejszy.resize(obraz.size, Image.NEAREST)

mniejsza_sciezka = "mniejszy.jpg"
junior = mniejszy_piksel.save("mniejszy.jpg", quality=5)  # Jakość 5% (dla kompresji)

Image.open(mniejsza_sciezka).show()