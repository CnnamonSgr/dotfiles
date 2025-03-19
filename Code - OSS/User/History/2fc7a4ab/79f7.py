from PIL import Image, ImageDraw, ImageFont

# Ścieżka do obrazu
sciezka = "/home/bartosh/Downloads/junior.jpg"  # Ustaw swoją lokalizację

# Otwieramy obraz
obraz = Image.open(sciezka)

# Pobieramy rozmiar obrazu
szerokosc, wysokosc = obraz.size
print(f"Rozmiar: {szerokosc}x{wysokosc} px")
print(f"Format: {obraz.format}")  # np. JPEG, PNG
print(f"Tryb kolorów: {obraz.mode}")  # np. RGB, CMYK, L (czarno-biały)

# 🔹 **Pikselizacja**
rozmiar_bloku = 20  # Im mniejsza wartość, tym większa pikselizacja

# Zmniejszamy obraz
mniejszy = obraz.resize(
    (szerokosc // rozmiar_bloku, wysokosc // rozmiar_bloku), Image.NEAREST
)

# Powiększamy go z powrotem do oryginalnego rozmiaru
mniejszy_piksel = mniejszy.resize((szerokosc, wysokosc), Image.NEAREST)

# 🔹 **Zapisujemy obraz z niską jakością**
mniejsza_sciezka = "mniejszy.jpg"
mniejszy_piksel.save(mniejsza_sciezka, quality=5)  # Jakość 5% (dla kompresji)

# 🔹 **Dodajemy tekst na obraz**
obraz_finalny = Image.open(mniejsza_sciezka)
rysownik = ImageDraw.Draw(obraz_finalny)

# Czcionka (możesz podać własną ścieżkę do TTF)
try:
    czcionka = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)  # Linux
except:
    czcionka = ImageFont.load_default()  # Domyślna czcionka

# Tekst do dodania
tekst = "Rio De Janeiro"
kolor_tekstu = "white"

# 🔹 **Wyśrodkowanie tekstu**
szerokosc_tekstu, wysokosc_tekstu = rysownik.textsize(tekst, font=czcionka)
pozycja = ((szerokosc - szerokosc_tekstu) // 2, wysokosc - wysokosc_tekstu - 20)  # Na dole obrazu

# Dodajemy tekst
rysownik.text(pozycja, tekst, font=czcionka, fill=kolor_tekstu)

# 🔹 **Zapisujemy obraz z tekstem**
obraz_finalny.save("mniejszy_z_tekstem.jpg")

# 🔹 **Otwieramy gotowy obraz**
Image.open("mniejszy_z_tekstem.jpg").show()
