hours = input('Number of hours worked per week:')
hours = int(hours)

below_equal35hrs = 51.45
above35hrs = 88.9

if hours > 35:
    payment = (35 * below_equal35hrs) + ((hours-35) * above35hrs)
else:
    payment = hours * below_equal35hrs
print(f'The weekly payment of (Tzu-Yi) Elysa Wu is:{payment}')

#input the number in console (e.g. hours=40)

# Exercise 2
numbers = [-2, 3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15, 10]
largest_num = numbers[0]
print('Before', largest_num)
for number in numbers:
    if number > largest_num:
        largest_num = number
print(number, largest_num)
print(f'The largest value is {largest_num}')

# Exercise 3
for i in range(1, 4):
    for j in range(1, 4):
        if i <= j:
            print(i, j)