listx = ['ana', 'lia', 'joh', 'maria']
print(listx[1:3])  # 3 Does not enter
print(listx[0:3])
print(listx[0:55])  # all
print(len(listx))

print(listx[:])
print(listx[::2])
del listx[2]
print(listx)  # Excludes joh
