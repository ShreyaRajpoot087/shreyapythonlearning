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