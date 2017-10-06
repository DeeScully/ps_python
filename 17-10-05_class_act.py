# rectangle class with w, h attribs and area methods

class Rectangle:

    def __init__(self, sides):
        self.width = sides[0]
        self.height = sides[1]

    def area(self):
        return self.width * self.height

ex_1 = Rectangle((2, 4))

print(f'The width is {ex_1.width} and the height is {ex_1.height}.')
print(f'The area is: {ex_1.area()}.')


# class poly init with attribs side_nums and sides; meths input sides to get ea side, and to print ea side

# class triangle to inherit from poly; meths find area to cal area of triangle
