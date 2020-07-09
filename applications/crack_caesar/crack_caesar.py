# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
normal_freq={'E': 11.53, 'T': 9.75, 'A': 8.46, 'O': 8.08, 'H': 7.71, 'N': 6.73, 'R': 6.29, 'I': 5.84, 'S': 5.56, 'D': 4.74, 'L': 3.92, 'W': 3.08, 'U': 2.59, 'G': 2.48, 'F': 2.42, 'B': 2.19, 'M': 2.18, 'Y': 2.02, 'C': 1.58, 'P': 1.08, 'K': 0.84, 'V': 0.59, 'Q': 0.17, 'J': 0.07, 'X': 0.07, 'Z': 0.03}
ciphertext = open('ciphertext.txt', "r")
text = ciphertext.read()
ciphertext.close()
chars_to_ignore = ['\n', ' ', '!', '"', "'", '(', ')', ',', '-', '.', '1', ":", ';', '?', 'â', '”', '€' ]
count_cypher = {}
# decode_table={}
# gt count of individual letters
def letter_count(s):
    for c in s:
        if c in chars_to_ignore:
            continue
        if c in count_cypher:
            count_cypher[c] += 1
        else:
            count_cypher[c] = 1
    return count_cypher

# get total number of letters
def add_all_letters(count):
    total_letters = 0
    for i in count:
        amount = i[1]
        total_letters += amount
    return total_letters
# calculate the frequency
def get_frequency(letters):
    freq = {}
    total = add_all_letters(letters)
    for i in letters:
        amount = i[1]
        freq[i[0]] = round(amount/total * 100, 2)
    return freq
# compare the 2 freq tables
decode_table = {}
def compare_freq(nor, cyp):
        for i in nor:
            for j in cyp:
                if i[1] == j[1]:
                    decode_table[i[0]] = j[0]
                    # decode_table[i] = cyp[j[0]]
        return decode_table

def add_ignore_to_decoded(arr):
    for i, v in enumerate(arr):
        decode_table[v] = v
    return decode_table

# letters.sort()
letter_count(text)
letters = list(count_cypher.items())
letters.sort()

# totals = add_all_letters(letters)
freq = get_frequency(letters)

# decoded = compare_freq(normal_freq, freq)
# print('decoded', decoded)
cypher_freq = list(freq.items())
cypher_freq.sort(key= lambda e: e[1], reverse=True)
normal = list(normal_freq.items())
# print('sorted letters', letters)
# print('add all letters total', add_all_letters(letters))
# print('freq', get_frequency(letters))
# print(cypher_freq)
# print(normal)
# print(normal_freq)
encoded = compare_freq(normal, cypher_freq)
add_ignore_to_decoded(chars_to_ignore)
decoded={'L': 'J'}
for k,v in encoded.items():
    decoded[v] = k

# decode the text
# print(decoded)
def decode(s):
    r=""
    # print(decoded)
    for c in s:
        r += decoded[c]
    return r

print(decode(text))