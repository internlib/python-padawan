dc = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dc)


dc = {f'Number: {i}': i * 2 for i in range(10) if i % 2 == 0}
print(dc)
