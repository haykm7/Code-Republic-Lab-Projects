fl = open('text','r')
text = fl.read()
fl.close()

words_number = len(text.split(' '))
letter_number = 0
messy_sent = text.split('.')
sentence_number = 0
letter_frequency = {}
word_frequency = {}


for i in text.split(' '):
    letter_number += len(i)
    if i not in word_frequency:
        word_frequency[i] = 1
    else:
        word_frequency[i] += 1
    for j in i:
        if j not in letter_frequency:
            letter_frequency[j] = 1
        else:
            letter_frequency[j]+=1

for i in range(len(messy_sent)):
    sentence_number+=1
    if messy_sent[i+1] == '':
        break


print(letter_frequency)
