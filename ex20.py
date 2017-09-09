# import argv meth from sys module
from sys import argv

# assign argv vals to vars
script, input_file = argv

# function to read file handler then print contents
def print_all(f):
    print(f.read())

# function to return to beginning of file handler
def rewind(f):
    f.seek(0)

# function to print int and read a single line of file handler
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open file and assign to var (file handler)
with open(input_file) as current_file:

    # print str
    print("First let's print the whole file: \n")

    # print file handler
    print_all(current_file)

    # print str
    print("Now let's rewind, kind of like a tape.")

    # call rewind function with file handler argument
    rewind(current_file)

    # print str
    print("Let's print three lines:")

    # assign int to var
    current_line = 1
    # call function passing int and file handler
    print_a_line(current_line, current_file)

    # increment var
    current_line += 1
    # call function passing int and file handler
    print_a_line(current_line, current_file)

    # increment var
    current_line += 1
    # call function passing int and file handler
    print_a_line(current_line, current_file)
