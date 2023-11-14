# Ask the user to input 5 unique words
word1 = input("Enter word 1: ")
word2 = input("Enter word 2: ")
word3 = input("Enter word 3: ")
word4 = input("Enter word 4: ")
word5 = input("Enter word 5: ")

# Construct a list of the 5 input values in the order that the user gave them
word_list = [word1, word2, word3, word4, word5]

# Display a list where each index corresponds to the length of the word given by the user at the corresponding index
length_list = [len(word1), len(word2), len(word3), len(word4), len(word5)]
print(length_list)