password = input("Do you know secret password? ")
if password != '--secret':
    print(' correct password')
else:
    print(' no correct password')

# 2nd program using multiple condition#
user_age =int(input('what is your age? '))
user_country=input('What is your country? ')
if user_age<25 and user_country=='Germeny':
    print('you can apply to Germany student exchange program')
else:
    print('sorry , you are not allowed to apply to Germany')

#user country with or conditions#
user_country= input('what is your country? ')

if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('you can apply for a scanvidian country student exchange program')
else:
    print('sorry , you are not allowed to apply')

#User country with conditions#
user_country = input('where do you came from? ')
if not user_country == 'Sweden':
    print('sorry , you are not from Sweden')
else:
    print('you are from Sweden')


#User age and User Country#
user_age = int(input('what is your age? '))
user_country = input('What is your country? ')

if not user_country == 'Germeny' and user_age<25 or user_country == 'Germeny' and user_age<23:
    print('you qualify')
else:
    print('sorry , you do\'nt qualify!')






