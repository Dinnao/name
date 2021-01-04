def longest_word(word):
    count = 0
    for i in word:
        if len(i) > count:
            count = len(i)
            word = i
    print(word)
longest_word(input('Please, enter some string: ').split())
