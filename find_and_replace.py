# Replace "old" with "new" in a file
with open('textfile.txt', 'r') as file:
    content = file.read().replace("old", "new")

with open('textfile.txt', 'w') as file:
    file.write(content)