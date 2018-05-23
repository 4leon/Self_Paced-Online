#!/usr/bin/env python3

# Activity 1:  Dictionaries and Sets
# Dictionaries 1
print('\nDictionaries 1')
dict_1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'chocolate'}
print(dict_1)
del dict_1['cake']
print(dict_1)
dict_1['fruit'] = 'mango'
print(dict_1)
print(list(dict_1.keys()))
print(list(dict_1.values()))
print('cake' in dict_1)
print('mango' in dict_1.values())

# Dictionaries 2
print('\nDictionaries 2')
dict_1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'chocolate'}
lst_keys = list(dict_1.keys())
lst_values = list(dict_1.values())
lst_t_values = [word.count('t') for word in lst_values]
dict_2 = dict(zip(lst_keys, lst_t_values))
print(dict_2)

# Sets 1
print('\nSets 1')
s2 = {i for i in range(0, 21) if i % 2 == 0}
s3 = {i for i in range(0, 21) if i % 3 == 0}
s4 = {i for i in range(0, 21) if i % 4 == 0}
print(f"s2 = {s2}\ns3 = {s3}\ns4 = {s4}")
print(s3 <= s2)
print(s4 <= s2)

# Sets 2
print('\nSets 2')
set_1 = set('Python')
set_1.add('i')
print(set_1)
set_2 = frozenset('marathon')
print(set_2)
print(set_1 | set_2)
print(set_1 & set_2)
