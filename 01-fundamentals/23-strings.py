text = 'Today I woke up late, but tomorrow I will wake up early'
print('T' in text)
print('woke' in text)
print('1' in text)
print('1' not in text)
print(len(text))
print(text.lower())
print(text.upper())
print(text)  # Result keeps the same. There was no attribution

crop_text = text.split(' ')
print(crop_text)
