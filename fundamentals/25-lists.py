# List can be considered a mutable array

basic_list = []
print(type(basic_list))
print(dir(basic_list))
# help(list)

basic_list.append(1)
basic_list.append(5)
print(basic_list)
basic_list.append('john')
print(basic_list)
print(len(basic_list))
basic_list.remove(5)
print(basic_list)
basic_list.append(2)

print(basic_list)
basic_list.reverse()
print(basic_list)
