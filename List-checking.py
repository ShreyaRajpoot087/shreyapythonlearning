for char in 'Happy Message':
    print(char)
# if user message in the list print welcome else not invited

invite_guests = ['shreya', 'Chhoti','Diksha','Priyanka']
name = input('What is your name? ')
if name not in invite_guests:
    print('You are not an invited guest')

else:
    print(' Welcome')

#coping list
name_original ='Shreya Singh'
name_new = name_original
name_original= 'Shreya Rajpoot'
print(name_original, name_new)