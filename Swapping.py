first = input("Enter first number: ")
second = input("Enter second number: ")
print('Before Swapping: ', first, second)
temp = first
first = second
second = temp
print('After Swapping: ', first, second)

# By python method
first = input("Enter first number: ")
second = input("Enter second number: ")
print('Before Swapping: ', first, second)
first ,second =second , first
print('After Swapping: ', first, second)
# swapping by list
top_cities =['Yew york ', 'San Francisco ', 'UK','Colombia']
#print(top_cities)
top_cities[0],top_cities[1] = top_cities[1],top_cities[0]
#print(top_cities)
top_cities.sort(reverse=True)
print(top_cities)
