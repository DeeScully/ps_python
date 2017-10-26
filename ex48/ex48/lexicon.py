def scan(inp):
    inp_list = inp.split()
    list_of_tups = list()

    for word in inp_list:
        if word in {'north', 'south', 'east'}:
            first_el = 'direction'
        elif word in {'go', 'kill', 'eat'}:
            first_el = 'verb'
        elif word in {'the', 'in', 'of'}:
            first_el = 'stop'
        elif word in {'bear', 'princess'}:
            first_el = 'noun'
        elif word.isdigit():
            try:
                word = int(word)
                first_el = 'number'
            except ValueError:
                return None
        else:
            first_el = 'error'

        list_of_tups.append((first_el, word))

    return list_of_tups
