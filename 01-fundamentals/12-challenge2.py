trabalho_terca = True
trabalho_quinta = True


tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_30 = trabalho_terca != trabalho_quinta  # xor
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudavel={}"
      .format(tv_50, tv_30, sorvete, mais_saudavel))

print("Name = {0}, Age = {1}" .format('John', 24))
