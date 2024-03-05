numbers = []
for i in range(1,101):
    numbers.append(i)
    print(numbers)

numbers = [i for i in range(1,101)]
print(numbers)

cells =[['A1','A2','A3'],['B1,B2,B3']]
for x in cells:
    for y in cells:
        print('Element',y)