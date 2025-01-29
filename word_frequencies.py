from collections import Counter

with open('wordcount.txt', 'r') as file:
    words = file.read().split()

word_counts = Counter(words)

with open('word_frequencies.txt', 'w') as file:
    for word, count in word_counts.items():
        file.write(f"{word}: {count}\n")