#!/bin/bash

CONFIG_FILE=~/.config/hypr/hyprpaper.conf
WALLPAPER_DIR="/home/bartosh/TapetyJakies"

# Pobranie aktualnej tapety
CURRENT_WALLPAPER=$(grep "^wallpaper =" "$CONFIG_FILE" | awk -F ', ' '{print $2}')

# Wybór losowej tapety, ale innej niż obecna
NEW_WALLPAPER=""
while [[ -z "$NEW_WALLPAPER" || "$NEW_WALLPAPER" == "$CURRENT_WALLPAPER" ]]; do
    NEW_WALLPAPER=$(find "$WALLPAPER_DIR" -type f \( -iname "*.png" -o -iname "*.jpg" \) | shuf -n 1)
done

# Jeśli brak plików - zakończ skrypt
if [[ -z "$NEW_WALLPAPER" ]]; then
    echo "Brak tapet w katalogu!" >&2
    exit 1
fi

# Tworzenie nowego pliku konfiguracyjnego
echo "# Auto-generated hyprpaper.conf" > "$CONFIG_FILE"

# Dodanie preload dla każdej tapety
find "$WALLPAPER_DIR" -type f \( -iname "*.png" -o -iname "*.jpg" \) | while read -r file; do
    echo "preload = $file" >> "$CONFIG_FILE"
done

# Dodanie monitora
echo "monitor = eDP-1,1920x1080,0x0,1" >> "$CONFIG_FILE"

# Ustawienie nowej tapety
echo "wallpaper = eDP-1, $NEW_WALLPAPER" >> "$CONFIG_FILE"

# Restart Hyprpaper
pkill hyprpaper
hyprpaper &
