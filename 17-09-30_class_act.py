# string frequency counter
# def str_counter():
#     string = input ('Input the string that you want to get the letter frequency counter of: ')
#     # if len(fname) < 1: fname = 'xxx.txt'
#     #
#     # with open(fname) as fh:
#     # #open file and closes it automatically. syntax 'with open("file", "mode") as variable:'
#
#     count_dict = {}
#
#     for char in string:
#         count_dict[char] = count_dict.get(char, 0) + 1
#
#     return count_dict
#
# print(str_counter())
#
#
# read txt file and count number of lines
# def line_counter():
#
#     fname = input ('Input file name: ')
#
#     with open(fname) as fh:
#         counter = 0
#
#         for line in fh:
#             counter += 1
#
#         return counter
#
# print(f'There were {line_counter()} lines in the file you selected.')


# read txt file and count the number of words
def word_counter():

    fname = input ('Input file name: ')

    with open(fname) as fh:
        counter = 0

        for line in fh:
            text = line.split()

            for word in text:
                counter += 1

        return counter

print(f'There were {word_counter()} words in the file you selected.')
