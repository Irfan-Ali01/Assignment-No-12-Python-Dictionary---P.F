sentence=input('Enter Sentence: ')
word_counts={}
words = sentence.split()
for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
        result={'word':'word_counts'}
for word, count in result.items():
    print(word_counts)