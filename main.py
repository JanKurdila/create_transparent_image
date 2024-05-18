from PIL import Image

# Otvorenie obrázka
image_path = r'C:\Users\Ucitel\Desktop\transparency\t.jpg'  
image = Image.open(image_path)

# Konvertovanie obrázka na režim RGBA (ak už nie je v tomto režime)
image = image.convert("RGBA")

# Získanie dát obrázka (pixelov)
data = image.getdata()

# Definovanie prahovej hodnoty priehľadnosti (napr. všetko biele bude priehľadné)
threshold = 200

# Vytvorenie nových dát pre obrázok
new_data = []
for item in data:
    # Zisťovanie, či je pixel biely (alebo skoro biely)
    if item[0] > threshold and item[1] > threshold and item[2] > threshold:
        # Nastavenie priehľadnosti (0) pre biely pixel
        new_data.append((255, 255, 255, 0))
    else:
        # Ponechanie pôvodného pixelu
        new_data.append(item)

# Aktualizovanie dát obrázka
image.putdata(new_data)

# Uloženie nového obrázka
new_image_path = r'C:\Users\Ucitel\Desktop\transparency\tt.jpg'  # Pridaj predponu 'r'
image.save(new_image_path, 'PNG')

print(f"Priehľadný obrázok bol uložený ako {new_image_path}")
