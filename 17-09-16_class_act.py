num_txt = input('Input a number to see if it\'s divisible by four! >>>')

try:
    num = int(num_txt)
    if num % 4 == 0:
        print('Yes!')
    else: print('Ohhhhh.')
except:
    print('You didn\'t input an integer.  Try again.')


num2_txt = input('Input a number and I\'ll tell you if the number is between 6-12 and 121-151.')

try:
    num = int(num2_txt)
    if 6 <= num <=12:
        print(f'{num} is between 6-12.')
    elif 121 <= num <= 151:
        print(f'{num} is between 121-151.')
    else: print(f'{num} is outside both ranges.')
except:
    print('You didn\'t input an integer.  Try again.')

def greater(val_1, val_2):
    if val_1 > val_2:
        print_one()
        return val_1 / val_2
    elif val_1 == val_2:
        print_same()
        return val_1
    else:
        print_two()
        return val_1 * 10


def print_one():
    print('val_1 is greater!')

def print_two():
    print('val_2 is greater!')

def print_same():
    print('val_1 is the same as val_2')

greater(4, 5)
greater(5, 4)
greater(5, 5)

"""
install python
install atom
install git
set-up github
clone github repo
print function
strings
integers
floats
argv method
import module
variables
string formatting
str.format method
define functions
pararmetres
function call
arguments
function return values
booleans
conditionals 
"""
