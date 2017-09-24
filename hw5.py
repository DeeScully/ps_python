#ex 34
# animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']
#
# The animal at 1 is a python3.6.
# The third (3rd) animal is a peacock.
# The first (1st) animal is a bear.
# The animal at 3 is a kangaroo.
# The fifth (5th) animal is a whale.
# The animal at 2 is a peacock.
# The sixth (6th) animal is a platypus.
# The animal at 4 is a kangaroo.
#
# The first (1st) animal is at 0 and is a bear.
# The second (2nd) animal is at 1 and is a python3.6.
# The third (3rd) animal is at 2 and is a peacock.
# The fourth (4th) animal is at 3 and is a kangaroo.
# The fifth (5th) animal is at 4 and is a whale.
# The sixth (6th) animal is at 5 and is a platypus.
#
# The animal at 0 and at -6 is the 1st animal and is a bear.
# The animal at 1 and at -5 is the 2nd animal and is a python3.6.
# The animal at 2 and at -4 is the 3rd animal and is a peacock.
# The animal at 3 and at -3 is the 4th animal and is a kangaroo.
# The animal at 4 and at -2 is the 5th animal and is a whale.
# The animal at 5 and at -1 is the 6th animal and is a platypus.

import math
import datetime
from time import sleep

# how many seconds in 42 mins 42 secs
def secs(m, s):
    """(int, int) -> int
    returns the number of seconds given (minutes, seconds)
    """
    return m * 60 + s

#print(secs(42, 42))


# how many miles in 10 klicks
def miles(klicks):
    """ num -> num
    returns the number of miles given kilometres
    """
    return klicks * 1.61

#print(miles(10))

# how much is 83f converted to c
def fahr_to_cel(fahr):
    """int -> float
    returns the number of centigrade given fahrenheit
    """
    return (fahr - 32) / (9 / 5)

#print(fahr_to_cel(83))


# sqrt of [81, 19, 16, 121]
def squareroot(num):
    """num -> num
    returns squareroot of num
    """
    return math.sqrt(num)

num_list = [81, 19, 16, 121]
#for num in num_list:
#    print(squareroot(num))


# area of circ r = 9
def circ_area():
    """num -> num
    returns area of circle given the radius
    """
    rad_str = input('type in the number you want the area of > ')
    rad = float(rad_str)
    return (rad ** 2) * math.pi

#print(circ_area())


# bool if 'x' is in str
def x_in():
    """
    ask for num and return if 'x' is in it
    """
    word = input('What is your word you want to check for \'x\'? > ')
    return 'x' in word.lower()

#print(x_in())


# bool if str contains vowel
def vowel_in():
    vows = ('a', 'e', 'i', 'o', 'u')
    user_str = input('Type in your string here and I\'ll let you know if there are any vowels. > ')

    for char in user_str:
        normalized = char.lower()
        if normalized in vows:
            return True
    return False

#print(vowel_in())



# What is the volume of a sphere with radius 5? The volume of a sphere with radius r is  (4/3)πr3
def sphere_vol(rad):
    """num -> num
    return volume of sphere given the radius
    """
    return (4 / 3) * math.pi * rad ** 3

#print(sphere_vol(5))


# Write a boolean function that returns true if a given input is divisible by 3 or return false otherwise
def div_by_three():
    """
    get input val and returns true if val is divisible by 3
    """
    num_str = input('What number do you want to check is divisible by 3? > ')

    try:
        num = int(num_str)
    except:
        print('Only input a number.')
        div_by_three

    return num % 3 == 0

#print(div_by_three())


# Import data/time library and print out today's data and current time
def current_datetime():
    """
    prints date in YYYY-MM-DD format
    prints time in HH:MM format
    """
    now = str(datetime.datetime.now())
    #print(now)
    print(f'Date is {now[0:11]}')
    print(f'Time is {now[12:16]}')

#current_datetime()


# using the data time library, print out the current year
def current_yr():
    """
    print current year
    """
    now = datetime.datetime.now()
    print(f'Year is {now.year}')

#current_yr()

# write a function that counts how  many times the letter a is repeated in a given word (get the work from the user as an input)
def a_count():
    """
    Returns count for the number of 'a' in given word.
    """
    word = input("Type in your word you want the 'a' count for > ")
    count = 0

    for ltr in word:
        if ltr.lower() == 'a':
            count += 1

    return count

#print(a_count())


# write code that counts the number of letters in a word provided by the user
def ltr_count():
    word = input('What word do you want the letter count for? > ')
    return len(word)

#print(ltr_count())

# triangle test. If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle.

def triangle_chk(s1, s2, s3):
    """(int, int, int) -> str
    Print No if any one side is greater than sum of other two; otherwise print Yes
    """
    if (s1 > s2 + s3) or (s2 > s1 + s3) or (s3 > s1 + s2):
        print('No')
    else:
        print('Yes')

def three_inputs():
    """
    Get and unpack 3 inputs - assign to vars and pass vars to triangle_chk call
    """
    length_1, length_2, length_3 = input('Type in the lengths of the three sides of your hypothetical triange - separate the numbers with a space. > ').split(' ')

    try:
        s1, s2, s3 = int(length_1), int(length_2), int(length_3)
        assert s1 > 0 and s2 > 0 and s3 > 0
    except:
        print('Please only input positive integers.  Please try again. \n')
        three_inputs()

    triangle_chk(s1, s2, s3)

#three_inputs()


# Countdown function
def countdown(time):
    ''' num -> None
    counts down from given time unit. timer set to 300 miliseconds per unit.
    '''
    counter = time

    for i in range(time):
        print(f'Time go BOOM in t-{counter}')
        counter -= 1
        sleep(.3)
    print('BOOOOOOOOOOooooooooommmm!!!')

#countdown(20)


#function that tell if the given input is even or odd
def odd_even():
    '''
    gets int from user and prints whether int is odd or even
    '''
    num_str = input('Type in the integer that you want to determine is odd or even: ')

    try:
        num = int(num_str)
    except:
        print('Please only input integers.  Try again. \n')
        odd_even()

    if num == 0:
        result = 'zero'
    elif num % 2 == 0:
        result = 'even'
    else: result = 'odd'

    print(f'Your number: {num} is {result}.')

#odd_even()


#length of str given as input
def length():
    '''str -> int
    gets str from user and returns the length
    '''
    string = input('Type in the string that you want to determine the length of: ')
    count = 0

    for ltr in string:
        count += 1

    return count

#print(length())



#loop that prints one letter at time of a str given as input
def letter_printer():
    '''
    for each letter of given str, print each letter in newline
    '''
    string = input('Type in the string that you want to print each letter of: ')

    for ltr in string:
        print(ltr)
        sleep(.3)

letter_printer()

#print(secs(42, 42))
#print(miles(10))
#print(fahr_to_cel(83))
#for num in num_list:
#    print(squareroot(num))
#print(circ_area())
#print(x_in())
#print(vowel_in())
#print(sphere_vol(5))
#print(div_by_three())
#current_datetime()
#current_yr()
#print(a_count())
#print(ltr_count())
#three_inputs()
#countdown(20)
#odd_even()
#print(length())
