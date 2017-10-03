#create shapes class with attrib sides and methods perim and area
import math

class Shapes:

    def __init__(self, sides):
        self.side_lengths = sides
        self.side_nums = len(sides)

    def perim(self):
        perim = sum(self.side_lengths)
        return perim

    def area(self):
        if self.side_nums == 3:
            area = .5 * self.perim()
        elif self.side_nums == 4 and self.side_lengths[0] == self.side_lengths[1] and self.side_lengths[0] == self.side_lengths[2] and self.side_lengths[0] == self.side_lengths[3]:
            area = self.side_lengths[0] ** 2
        elif self.side_nums == 4 and ((self.side_lengths[0] == self.side_lengths[1] and self.side_lengths[2] == self.side_lengths[3]) or (self.side_lengths[0] == self.side_lengths[2] and self.side_lengths[1] == self.side_lengths[3])
        or (self.side_lengths[0] == self.side_lengths[3] and self.side_lengths[1] == self.side_lengths[2])):
            area = max(self.side_lengths) * min(self.side_lengths)
        else:
            area = (self.side_lengths[0] ** 2 * self.side_nums) / (4 * math.tan(math.radians(180 / self.side_nums)))

        return area

def pretty(shape):
    print(f'Shape with sides of {shape.side_lengths} has a perimetre of {shape.perim()} and an area of {shape.area()}.')

tri = Shapes([3,4,5])
pretty(tri)
square = Shapes([4, 4, 4 ,4])
pretty(square)
rect = Shapes([2, 2, 4, 4])
pretty(rect)
poly_6 = Shapes([6, 6, 6, 6, 6, 6])
pretty(poly_6)


# print out 15 most frequent words from file
import string
import os

# get file path from user, save cwd, and change cwd to path provided
path = input(r'Input the complete path and filename of the file you want to analyse: ')
orig_dir = os.getcwd()
dir_path, fname = os.path.split(path)
os.chdir(dir_path)

# try to open file, exit if unable to
try:
    fh = open(fname)
except:
    print(f'Unable to open file {fname}.  Check the name and try again.')
    exit()


# use dict to accumulate word freq, norm words by making lower and rem \n and punctuations
freq = {}
for line in fh:
    line_norm = line.lower().rstrip()
    line_clean = line_norm.translate(line.maketrans('', '', string.punctuation))
    words = line_clean.split()

    for word in words:
        freq[word] = freq.get(word, 0) + 1

# save dict_item, loop thru dict_item to reverse k, v to v, k pairs and save to new list
freq_tup = freq.items()
rev_freq_tup = []
for k, v in freq_tup:
    rev_freq_tup.append((v, k))

# sort v, k list to descending order
desc_rev_freq_tup = sorted(rev_freq_tup, reverse = True)


# print out 15 most frequent words
print(f'The fifteen most frequently used words in file {fname} are:')
for i in range(15):
    print(desc_rev_freq_tup[i][1], end = ' ')


# close file and change back to orig working dir
fh.close()
os.chdir(orig_dir)
