import random

# set arrays for winning numbers
lottery_nums = []
bonus_num = []

# Draw six random numbers between 1 and 65
for i in range (0,6):
    num = random.randint(1,66)

    while num in lottery_nums:
        num = random.randint(1,66)

# Add numbers to the array
    lottery_nums.append(num)
# Sort numbers from least to greatest within the array
lottery_nums.sort()

#  Draw the random bonus number
rand_num = random.randint(1,66)
bonus_num.append(rand_num)

# Output Results
print('Today\'s winning numbers are:')
print(f'{lottery_nums}  Bonus:  {bonus_num}')



