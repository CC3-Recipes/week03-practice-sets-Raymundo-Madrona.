with open('source.txt', 'w') as file:
    file.write("Hello, World!\n")


with open('source.txt', 'a') as file:
    file.write("This is appended text.\n")

with open('source.txt', 'r') as src, open('destination.txt', 'w') as dest:
    dest.write(src.read())
