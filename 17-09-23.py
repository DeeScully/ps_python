import math
import datetime

# how many seconds in 42 mins 42 secs
def secs(m, s):
    """(int, int) -> int
    returns the number of seconds given (minutes, seconds)
    """
    return m * 60 + s

print(secs(42, 42))


# how many miles in 10 klicks
def miles(klicks):
    """ num -> num
    returns the number of miles given kilometres
    """
    return klicks * 1.61

print(miles(10))

# how much is 83f converted to c
def fahr_to_cel(fahr):
    """int -> float
    returns the number of centigrade given fahrenheit
    """
    return (fahr - 32) / (9 / 5)

print(fahr_to_cel(83))


# sqrt of [81, 19, 16, 121]
def squareroot(num):
    """num -> num
    returns squareroot of num
    """
    return math.sqrt(num)

num_list = [81, 19, 16, 121]
for num in num_list:
    print(squareroot(num))


# area of circ r = 9
def circ_area():
    """num -> num
    returns area of circle given the radius
    """
    rad_str = input('type in the number you want the area of > ')
    rad = float(rad_str)
    return rad ** 2 * math.pi

print(circ_area())


# bool if 'x' is in str
def is_in():
    """
    ask for num and return if 'x' is in it
    """
    word = input('What is your word you want to check for \'x\'? > ')
    return 'x' in word.lower()

print(is_in())


# bool if str contains vowel
def vowel_in(str):
    vows = ('a', 'e', 'i', 'o', 'u')
    for ltr in str:
        normalized = ltr.lower()
        if ltr in vows:
            return True
    return False

print(vowel_in('lin'))
print(vowel_in('ln'))


# What is the volume of a sphere with radius 5? The volume of a sphere with radius r is  (4/3)πr3
def sphere_vol(rad):
    """num -> num
    return volume of sphere given the radius
    """
    return (4 / 3) * math.pi * rad ** 3

print(sphere_vol(5))


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

print(div_by_three())


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

current_datetime()


# using the data time library, print out the current year
def current_yr():
    """
    print current year
    """
    now = datetime.datetime.now()
    print(f'Year is {now.year}')

current_yr()

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

print(a_count())


# write code that counts the number of letters in a word provided by the user
def ltr_count():
    word = input('What word do you want the letter count for? > ')
    return len(word)

print(ltr_count())


def triangle_chk(s1, s2, s3):
    """(int, int, int) -> str
    Print No if any one side is greater than sum of other two; otherwise print Yes
    """
    if (s1 <= s2 + s3) and (s2 <= s1 + s3) and (s3 <= s1 + s2):
        print('Yes')
    else:
        print('No')

def three_inputs():
    """
    assign 3 inputs to vars and pass it to triangle_chk call
    """
    length1 = float(input('What is the 1st length : '))
    length2 = float(input('What is the 2nd length : '))
    length3 = float(input('What is the 3rd length : '))

    triangle_chk(length1, length2, length3)

three_inputs()
