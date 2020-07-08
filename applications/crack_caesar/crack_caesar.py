# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

ciphertext = open('ciphertext.txt', "r")
text = ciphertext.read()
ciphertext.close()
chars_to_ignore = ['\n', ' ', '!', '"', "'", '(', ')', ',', '-', '.', '1', ":", ';', '?', 'â', '”', '€' ]
count_cypher = {}
def letter_count(s):
    for c in s:
        if c in chars_to_ignore:
            continue
        if c in count_cypher:
            count_cypher[c] += 1
        else:
            count_cypher[c] = 1
    return count_cypher

def add_all_letters(count):
    total_letters = 0
    for i in count:
        amount = i[1]
        total_letters += amount
    return total_letters
    
def get_frequency(letters):
    total_letters = add_all_letters(letters)
    freq = {}
    count_letters = letters

    
# letters.sort()
letter_count(text)
letters = list(count_cypher.items())
letters.sort()

add_all_letters(letters)
print('sorted letters', letters)
print('add all letters total', get_frequency(letters))