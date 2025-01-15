from pathlib import Path

name = input("Votre nom ? ")
path = Path("text_files/guests.txt")
path.write_text(name)
