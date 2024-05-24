my_dict = {'Дмитрий' : 1975, 'Татьяна' : 1982, 'Арсений' : 2013, 'Никита' : 2006}
print(my_dict)
print(my_dict['Татьяна'])
print(my_dict.get('Тимофей'))
print(my_dict.get('Татьяна'), my_dict.get('Кирил'))
my_dict.update({'Тимофей' : 2009, 'Кирил' : 2015})
del my_dict['Дмитрий']
print(my_dict)

my_set = {1,2,3,4,2,3, 'Video', True, (5,6,7), (6,7), 'Video'}
print(my_set)
my_set.update({8,9})
print(my_set)
my_set.discard(1)
print(my_set)

