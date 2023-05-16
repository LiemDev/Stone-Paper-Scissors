import random
winner = ''
random_choise = random.randint(0, 2)
if random_choise == 0:
    computer_choise = 'Stein'
elif random_choise == 1:
    computer_choise = 'Papier'
elif random_choise == 2:
    computer_coise = 'Schere'
user_choise = input('Stein, Schere oder Papier?')
if computer_choise == user_choise:
    winner = 'Unentschieden'
elif computer_choise == 'Papier' and user_choise == 'Schere':
    winner = 'Spieler'
elif computer_choise == 'Stein' and user_choise == 'Papier':
    winner = 'Spieler'
elif computer_choise == 'Schere' and user_choise == 'Stien':
    winner = 'Spieler'
else:
    winner = 'Computer'
if winner == 'Tie':
    print('Unentschieden')
else:
    print('Spieler hat gewonnen!')


