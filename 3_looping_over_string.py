# Example Practice:
# Ask the user for a word.
# Use a for loop to print each letter on a new line.
# Challenge:
# Count how many vowels are in the word.



word = input("Give a random word: ")
for letter in word:
    print(letter)

vowels = "aeiouAEIOU"
count = 0

for letter in word:
    if letter in vowels:
        count += 1
        print("Amount of Vowels", count)