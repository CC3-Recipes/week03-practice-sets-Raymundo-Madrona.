with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2, open('merged.txt', 'w') as merged:
    merged.write(file1.read() + "\n" + file2.read())