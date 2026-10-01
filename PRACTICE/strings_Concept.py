#program that takes a sentence from the user and Convert the sentence into lowercase,Split it into words,Count how many words are present,Create a list containing the words whose length is greater than 4,Print the words in reverse order.
sentence=input("Enter a Sentence:")
print(sentence.lower())
words=sentence.split()
print("Words",words)
print(f"The Total no of Words In the Sentence:",len(words))
long_words=[word for word in words if len(word) > 4]
print("Words longer than 4 characters:", long_words)
print("Reverse Order:",long_words[::-1])