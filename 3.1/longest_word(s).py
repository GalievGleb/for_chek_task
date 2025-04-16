def longest_word(s):
    words=s.split()
    long = ("")
    for word in words:
        if len(word)>len(long):
            long = word
    print(long)
s=input('Введите строку:')
longest_word(s)

