# # Your code here
from word_count import word_count

robin = open('robin.txt', 'r').read()

count_of_words = word_count(robin)

# print(count_of_words)

for i in count_of_words:
    count_of_words[i] = "#"*count_of_words[i]

count_of_words = sorted(count_of_words.items(), key= lambda e: (e[1], e[0]), reverse= True)

for i in count_of_words:
    if len(i[0]) < 7:
        print(i[0], "\t\t\t", i[1])
    elif len(i[0]) >= 14:
        print(i[0], "\t", i[1])
    else: 
        print(i[0], "\t\t", i[1])
