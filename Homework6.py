#1
my_dict = {'Alexandr': 1993, 'Kris': 2000, 'Galina': 1973}
print(my_dict)
print(my_dict['Kris'])
print(my_dict.get('Andrey'))
my_dict.update({'Alex': 1995,
                'Max': 1997})
print(my_dict)
del my_dict['Max']
print(my_dict)

#2
my_set = {3,3,13.4,13.4,'Apple','Apple'}
print(my_set)
my_set.add('Kvas')
my_set.add(78)
my_set.discard('Apple')
print(my_set)

