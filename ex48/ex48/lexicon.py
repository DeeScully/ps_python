def scan(inp):
    inp_list = inp.split()
    list_of_tups = list()

    word_ref = {'north':'direction', 'south':'direction', 'east':'direction', 'go':'verb', 'kill':'verb', 'eat':'verb', 'the':'stop', 'in':'stop', 'of':'stop', 'bear':'noun', 'princess':'noun'}

    for word in inp_list:
        #first_el = word_ref.get(word, 'error')
        try:
            word = int(word)
            first_el = 'number'
        except ValueError:
            first_el = word_ref.get(word, 'error')

        list_of_tups.append((first_el, word))

    return list_of_tups
