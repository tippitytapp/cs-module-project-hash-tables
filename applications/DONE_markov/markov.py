import random
import re

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
cache = {}
words2 = words.split()
for i in range(len(words2) -1):
    if words2[i] not in cache:
        cache[words2[i]] = [words2[i+1]]
    else:
        cache[words2[i]].append(words2[i+1])
# print(cache)

caps = r"((?:[A-Z][a-z']+)+)"
ends = r"(\w*\.|\w*\?|\w*\!)"
end_words = re.findall(ends, words)
cap_words = re.findall(caps, words)

starter = random.choice(cap_words)
# print(starter)
sentence = starter
# print(sentence)

# TODO: construct 5 random sentences
# Your code here

# count = 1
stop = False
while stop == False:
    rando = random.choice(cache[starter])

    if rando in end_words:
        sentence += f' {rando} \n\n'
        break
        # count += 1
    else:
        sentence += f' {rando}'
        starter = rando

print('')
print(sentence)





