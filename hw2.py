def avg(num_tuple):
    count = 0
    ttl = 0
    for num in num_tuple:
        count += 1
        ttl += num

    print(f"The mean of {count} numbers is {ttl / count}.")

tup_1 = (44, 64, 88, 53, 89)
tup_2 = (39, 45, 55, 90, 95, 96)
tup_3 = (54, -45, -10, 90)
tup_4 = (55, 65, 75, 95, 32)

avg(tup_1)
avg(tup_2)
avg(tup_3)
avg(tup_4)

def odd_even(num):
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else: print(f"{num} is an odd number.")

odd_even(4)
odd_even(9)
odd_even(19)
odd_even(20)
