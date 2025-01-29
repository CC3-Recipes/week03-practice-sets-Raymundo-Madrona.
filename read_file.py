# Read and print file contents line by line
with open('hello.py', 'r') as file:
    for line in file:
        print(line.strip())

# Count total lines in the file
with open('hello.py', 'r') as file:
    lines = file.readlines()
    print("Total lines:", len(lines))

# Count total words in the file
with open('hello.py', 'r') as file:
    words = file.read().split()
    print("Total words:", len(words))

# Count total characters in the file
with open('hello.py', 'r') as file:
    content = file.read()
    print("Total characters:", len(content))