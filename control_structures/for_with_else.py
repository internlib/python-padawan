WORDS = ('football', 'religion', 'politics')

texts = ['John likes football', 'but hates politics']


for text in texts:
    found = False
    for word in text.lower().split():
        if word in WORDS:
            print('has forbidden word:', word)
            found = True
            break

    else:
        print('authorized:', text)
