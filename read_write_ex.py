read_name = input('What is the name of file we are reading? ')
with open(read_name) as read_file:
    read_file_text = read_file.read()

write_name = input('What would you like to name the file you are saving to? ')

with open(write_name, 'w') as write_file:
    write_file.write(read_file_text)
