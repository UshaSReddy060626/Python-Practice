"""
Convert the sentence to lowercase.
Split it into words.
Find how many words are present.
Find the longest word.
Create a list containing only words whose length is greater than 4.
Print the words in reverse order."""
sentence=input("Enter a Sentence:")
lwr=sentence.lower()
print(lwr)
words=sentence.split()
print(words)
lengths=[len(word) for word in words]
max_len=max(lengths)
longest=[word for word in words if len(word)==max_len]
print(f"The Longest Word in the Sentence is:{longest}")
wordlen=[word for word in words if len(word)>4]
print(wordlen)
print(len(words))
print(words[::-1])
