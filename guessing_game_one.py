import random
print('My number is between 1 to 9.')

my_num = int(random.randrange(1, 9))

user_guess = 0
n = 0

while user_guess != my_num and user_guess != 'exit':
    user_guess = input('What`s my number?')

    if user_guess == 'exit':
        print('Game over!')
        break

    user_guess = int(user_guess)

    if user_guess < my_num:
        print('Too low')
        n += 1
        print(f'That`s your {n} try!')
    elif user_guess > my_num:
        print('Too high')
        n += 1
        print(f'That`s your {n} try!')
    else:
        print('That`s write!')
        n += 1
        print(f'That`s your {n} try!')





