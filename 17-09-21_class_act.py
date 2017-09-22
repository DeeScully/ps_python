grade_inp = input('Type in an integer from 0-100 >')

try:
    grade  = int(grade_inp)
    if grade > 100:
        print(grade)
        raise ValueError('Please only input an int between 0-100')
except:
    raise TypeError('Please only input an int between 0-100')

def grade_converter(num):
    if num < 55:
        return 'F'
    elif num <= 70:
        return 'D'
    elif num <= 80:
        return 'C'
    elif num <= 90:
        return 'B'
    else: return 'A'


#print(f'You get an {grade_converter(grade)}')

# multiples of 3 from 3 - 90
for i in range(3, 90 + 1, 3):
    print(i)


# list with multiples of 2 from 2 - 48

lst = [num for num in range(12, 48 + 1) if num % 2 == 0]
print(lst)
