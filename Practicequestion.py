for a in range(1, 6):
    for b in range(1, 10):
         if (a == b):
           print(a)
#List#
empty_list =[]
top_cities =['New York', 'San']
#top_cities.append('San Francisco')
for city_index in range (len(top_cities)):
 print('The city is ',city_index)

spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

low = 0
normal = 0
high = 0

for month in spendings:
    if month < 1000.0:
        low += 1
    elif month <= 2500.0:
        normal += 1
    else:
        high += 1

print('Numbers of months with low spendings: ' + str(low) + ', normal spendings: ' + str(
    normal) + ', high spendings: ' + str(high) + '.')



