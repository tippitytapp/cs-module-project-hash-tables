def no_dups(s):
    # Your code here
    count = 0
    words = {}
    # print(words)
    # print(s.split())
    for word in s.split():
        if word in words:
            continue
        else:
            count +=1
            words[word] = count
    return ' '.join(words.keys())



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))