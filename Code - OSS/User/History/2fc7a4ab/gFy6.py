from PIL import Image, ImageDraw, ImageFont

# Ścieżka do obrazu
sciezka = "/home/bartosh/Downloads/junior.jpg"  # Ustaw swoją lokalizację

# Otwieramy obraz
obraz = Image.open(sciezka)

# Pobieramy rozmiar obrazu
szerokosc, wysokosc = obraz.size

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
mniejszy_piksel.save(mniejsza_sciezka, quality=5)

# 🔹 **Dodajemy tekst na obraz**
obraz_finalny = Image.open(mniejsza_sciezka)
rysownik = ImageDraw.Draw(obraz_finalny)

# Czcionka (możesz podać własną ścieżkę do TTF)
try:
    czcionka = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 200)  # Linux
except:
    czcionka = ImageFont.load_default()  # Domyślna czcionka

# Tekst do dodania
tekst = "Rio De Janeiro"
kolor_tekstu = "white"

# 🔹 **Wyśrodkowanie tekstu - POPRAWKA**
bbox = rysownik.textbbox((0, 0), tekst, font=czcionka)  # Pobieranie wymiarów tekstu
szerokosc_tekstu = bbox[20] - bbox[0]
wysokosc_tekstu = bbox[30] - bbox[10]

# Obliczamy pozycję na środku dolnej części obrazu
pozycja = ((szerokosc - szerokosc_tekstu) // 2, wysokosc - wysokosc_tekstu - 1000)

# Dodajemy tekst
rysownik.text(pozycja, tekst, font=czcionka, fill=kolor_tekstu)

# 🔹 **Zapisujemy obraz z tekstem**
obraz_finalny.save("mniejszy_z_tekstem.jpg")

# 🔹 **Otwieramy gotowy obraz**
Image.open("mniejszy_z_tekstem.jpg").show()
