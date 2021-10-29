# Author: IBN (ADMG) 10/27/2021

word1 = input("Give me any word: ")
word2 = input("Give me any word: ")
if word1 < word2:
    print(word1 + " comes before " + word2)
elif word2 < word1:
    print(word2 + " comes before " + word1)
else:
    print(word1 + " is equal to " + word2)
