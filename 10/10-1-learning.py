from pathlib import Path

path = Path('text_files/learning.txt')
contents = path.read_text()
print(contents)

lines = contents.splitlines()
count = 1
for line in lines:
    print(f"Ligne {count} : {line}")
    count += 1
