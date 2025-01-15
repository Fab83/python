from pathlib import Path

path = Path('text_files/learning.txt')
contents = path.read_text()

count = 1
for line in contents.splitlines():
    print(f"Ligne {count} : {line.replace('Python', 'Java')}")
    count += 1
