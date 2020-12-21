WORDS = {'football', 'religion', 'politics'}

texts = ['Maria likes football', 'but hates politics']

for text in texts:
    intersection = WORDS.intersection(set(text.lower().split()))
    if intersection:
        print('has forbidden word:', intersection)
    else:
        print('authorized')
