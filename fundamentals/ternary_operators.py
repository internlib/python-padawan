raining = False
print('Today I have the clothes ' + ('dry', 'wet')
      [raining])  # 1 = Fase, 2 = True

print('Today I have the clothes ' + ('wet' if raining else 'dry'))
