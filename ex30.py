ppl = 30
cars = 40
trucks = 15

if cars > ppl:
    print('We should take the cars.')
elif cars < ppl:
    print('We should not take the cars.')
else: print('We can\'t decide.')

if trucks > cars:
    print('That\'s too many trucks.')
elif trucks < cars:
    print('Maybe we could take the trucks.')
else: print('We still can\'t decide.')

if ppl > trucks:
    print('Alright, let\'s just take the trucks.')
else: print('Fine, let\'s stay home then.')
