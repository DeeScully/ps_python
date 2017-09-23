from math import sqrt, floor

def is_prime (x):
    ''' (int) -> boolean

    Returns true if a given int value is a prime number.

    >>> is_prime (17)
    True
    >>> is_prime (25)
    False
    >>> is_prime (14057)
    True
    '''
    if x <= 1:
        return False

    if x == 2:
        return True

    if x > 2 and x % 2 == 0:
        return False

    for i in range(3, floor(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False

    return True


# for i in range(1, 101):
#     print(f'{i} is a prime >', is_prime(i))



def odd_even_counter(val_1, val_2, val_3, val_4, val_5):
    num_list = [val_1, val_2, val_3, val_4, val_5]
    odd = 0
    even = 0

    for num in num_list:
        if num == 0:
            continue
        elif num % 2 == 0:
            even += 1
        else: odd += 1

    return odd, even

# print('odd|even numbers counts are', odd_even_counter(7, 19, 85, 22, 0))



# convert bytes
a = 'Kilobytes to Bytes', 1000
b = 'Megabytes to Bytes', 1000000
c = 'Terabytes to Bytes', 1000000000000
d = 'Terabytes to Megabytes', 1000000

print(f'''We'll help you convert bytes!
      a.  {a[0]}
      b.  {b[0]}
      c.  {c[0]}
      d.  {d[0]}
      '''
      )

selection = input('Make your selection > ')
selection = selection.lower()

if selection not in('a', 'b', 'c', 'd'):
    raise ValueError("Only input 'a', 'b', 'c' or 'd'.")
if selection == 'a':
    choice, convert_rate = a
elif selection == 'b':
    choice, convert_rate = b
elif selection == 'c':
    choice, convert_rate = c
else: choice, convert_rate = d

print(f'Excellent, you chose to convert {choice}')

num_to_convert = input('How many would you like to convert? > ')
num = float(num_to_convert)

print(f'Converting {num} {choice} > {(num * convert_rate)}')
