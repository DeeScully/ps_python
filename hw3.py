import sys

script, name = sys.argv

color = input('What color describes your mood right now? > ')
food = input(f'What would you like to eat since you\'re feeling {color}? >')
drink = input(f'What beverage would go nice with your {food}? >')
spot = input(f'Where would you go for your favorite {food} and {drink}? >')

print(f'Well {name}, I\'m not feeling {color}, but I\'d love to grab some {food} & {drink} with you!')
