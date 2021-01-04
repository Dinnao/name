def fake_string(string, change_from, change_to, times):
    n_string = string.replace(change_from, change_to, times)
    print(n_string)
fake_string(input('Enter string: '), input('Wich word change? '),
            input('To what?'), int(input('How many words?')))
