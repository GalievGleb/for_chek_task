def is_palindrome(s):
    words = s.split(" ")

    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)



is_palindrome("In the middle of a vast desert, an extraordinary adventure awaits")