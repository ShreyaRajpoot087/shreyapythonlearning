def greet():
    print("Hello Shreya")
greet()
greet()
#get the average
def get_average(input_numbers):
    sum=0.0
    for number in input_numbers:
        sum= sum+number
        average= sum/len(input_numbers)
        print(average)
get_average([1.0,2.0,3.0,4.0,5.0,6.0])

def print_letter_count(text ,letter):
    counter=0
    for char in text:
        if char==letter:
            counter+=1
            print('Number of times letter',letter,'is',counter)
print_letter_count('shreya','e')

