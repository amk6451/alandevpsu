def pig_latin(text):
    for words in text.split():
        if words[0] in "aeiou":
                return words + 'yay'
        else:
            counter = 0
            counter2 = 0
            while counter2 == 0:
                if words[counter] not in "aeiouy":
                    counter += 1
                else:
                    counter2 = 1
            return words[counter:] + words[:counter] + 'ay'


text = input("Please enter text:")
print(' '.join(pig_latin(words) for words in text.split()))
