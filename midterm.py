#q1 write function to find distance between points and if the given points and distance make up a triangle.
from math import sqrt

def pyth(x1, y1, x2, y2):
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1)  ** 2)
    return distance

print(pyth(1,2,4,6))

#1b
def triangle(x1, y1, x2, y2):
    len_1, len_2 = abs(x2 - x1), abs(y2 - y1)
    #print(len_1, len_2)
    len_3 = pyth(x1, y1, x2, y2)

    if len_1 > (len_2 + len_3) or len_2 > (len_1 + len_3) or len_3 > (len_1 + len_2):
        print('Not a triangle')
    else: print('Can be a triangle')

triangle(1, 2, 4, 6)


#q2 write a function that iterates thru a str and adds 'ack' to the end of each ltr.
def acker(string):
    for ltr in string:
        print(ltr + 'ack')

acker('JKLMNOPQ')



#q3 write function that takes list of nums and return a new list with the cumulative sums of the preceding elements
def cumsum(lst):
    summer = 0
    sum_lst = list()

    for i in lst:
        summer += i
        sum_lst.append(summer)

    return sum_lst

print(cumsum((1,2,3,4)))


#q5 function takes 2 lists and returns T if have 1 common elements
def common_el(lst_1, lst_2):
    if len(lst_1) < len(lst_2):
        lst_1, lst_2 = lst_2, lst_1

    for el in lst_1:
        if el in lst_2:
            return True

    return False
lst_1 = [1, 2, 3]
lst_2 = [22, 45, 3, 87, 64]
print(f'Your lists {lst_1} and {lst_2} have at least one common element: {common_el(lst_1, lst_2)}')


#q7 chk if fermat theorem holds
def fermat(a, b, c, n):
    if n > 2 and (a ** n + b ** n == c ** n):
        print('Fermat was wrong!')
    else: print('that doesn\'t work')

num_a = int(input('Type your first number > '))
num_b = int(input('Type your second number > '))
num_c = int(input('Type your third number > '))
num_n = int(input('Type your "n" value > '))
fermat(num_a, num_b, num_c, num_n)



#bonus palendrome finder
def is_palendrome(string):
    str_lst = list()
    rev_lst = list()

    for i in string:
        if i != ' ':
            str_lst.append(i)
            rev_lst.insert(0, i)

    print(str_lst)
    print(rev_lst)
    return rev_lst == str_lst


print(is_palendrome('madam'))
print(is_palendrome('nurses run'))
print(is_palendrome('not a palen'))
