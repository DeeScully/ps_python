# create a class
class Song():
    # define constructor method with 1 param
    def __init__(self, lyrics):
        # create attribute
        self.lyrics = lyrics
    # define method
    def sing_me_a_song(self):
        # for loop that prints each line from constructor param
        for line in self.lyrics:
            print(line)

# create instance of class and pass argument
happy_bday = Song(['Happy birthday to you',
                   'I don\'t want to get sued',
                   'So I\'ll stop right there'])

# create instance of class and pass argument
bulls_on_parade = Song(['They rally around tha family',
                        'With pockets full of shells'])

# call class method
happy_bday.sing_me_a_song()

# call class method
bulls_on_parade.sing_me_a_song()
