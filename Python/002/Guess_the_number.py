import random
import readline

rand_num = random.randrange(0, 1000000)
num = -1
while num != rand_num:
    num = -1
    while num == -1:
        #usr_input = readline.()
        try:
            num = int(input('Please input number:'))
        except:
            num = -1
    if num > rand_num:
        print('Too high!')
    elif num < rand_num:
        print('Too low!')

print('Well done!. That is the correct number')