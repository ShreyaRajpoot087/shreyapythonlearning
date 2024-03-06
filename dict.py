#  dict collection used to store key value pair#
dict1 = {'a': 1, 'b': 2, 'c':3}
print(dict1)

spanish_animals = {'dog': 'ggg'}
print(spanish_animals)

grades ={}
grades['john'] ='A-'
grades['smith'] ='B'
grades.update({'john':'C', 'smith':'V'})
print(len(grades))
del grades['smith']
print(grades)

list_a = [1, 2, 3]
list_b = list_a[-2:-1]
list_c = list_a[-1:-2]
print(list_b,list_c)

temp_list = [1, 2, 3]
for i in range(len(temp_list)):
    temp_list.insert(i, 0)
print(temp_list)

orig_list = [1, 2, 3]
new_list = orig_list
del new_list[1:2]
print(new_list,orig_list)

my_numbers = [[i for i in range(3)] for j in range(4)]
print(my_numbers)

values = [[3 - x for x in range(2)] for y in range(5)]
sum = 0.0
for row in values:
    for cell in row:
        sum += cell

print(sum)

ratings = [3.0, 4.5, 6.3, 4.5, 6.7]
print(ratings[-2:-4])

integers = [1, 4, -2]
print(integers[integers[-1]])

cities = ['Warsaw', 'Cracow', 'Gdansk', 'Szczebrzeszyn Dolny']
del cities[:]
print(cities)

list_a = [0, 1, 2, 3]
list_b = [3, 4, 5, 6]
for el in list_a:
  if el in list_b:
    print('*')

my_list = [0, 1, 2] * 3 + [0]
print(len(my_list))

vals = (1, 2, 3, 4)
vals = vals[1:-1]
vals = vals[1]
print(vals)

dictionary = {0: 'one', 1: 'two', 2: 'three'}
value = 0
for x in range(len(dictionary)):
  value = dictionary[x]
print(value)

dict = {'first': 2, 'second': 2}
dict['first'] = 1
print(dict)

nicks = {'Adam': 'Smasher', 'Kate': 'k4t3', 'John': 'xJohnx'}

if 'k4t3' in nicks.keys():
    print('a')

if 'k4t3' in nicks.values():
    print('b')