chars_to_ignore = ['"', ":", ';', ',', '.', '-', '+', '=', '/', "\\", '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']





def word_count(s):
    # Your code here
    counts = {}
    words = s.split()
    for i, v in enumerate(words):
        for chr in chars_to_ignore:
            v = v.replace(chr, '')
            words[i] = v.lower()
    for v in words:
        if v == "":
            return {}
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    return counts 
    
    

x = {'', 1}




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))