import random

file = open('four_letters.txt', 'r')
list_of_words = []
for line in file:
    words = line.split(' ')
    j = len(words)
    i = 0
    while i < j:
        list_of_words.append(words[i].rstrip('\n'))
        i = i+1


class StringDatabase:
    @classmethod
    def get_word(cls):
        index = random.randint(0, len(list_of_words)-1)
        return list_of_words[index]