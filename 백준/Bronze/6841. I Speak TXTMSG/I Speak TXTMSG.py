dict = {
    'CU': 'see you',
    ':-)': 'I’m happy',
    ':-(': 'I’m unhappy',
    ';-)': 'wink',
    ':-P': 'stick out my tongue',
    '(~.~)': 'sleepy',
    'TA': 'totally awesome',
    'CCC': 'Canadian Computing Competition',
    'CUZ': 'because',
    'TY': 'thank-you',
    'YW': 'you’re welcome',
    'TTYL': 'talk to you later'
}

while True:
    try:
        msg = input()
        try:
            print(dict[msg])
        except KeyError:
            print(msg)
    except EOFError:
        break