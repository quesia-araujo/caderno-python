import random
def play():
    user = input(" What is your choise? 'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    
    # r > s, s > p, p> r
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p> r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
'''
    Se nenhuma das condições dentro do if for satisfeita, a função simplesmente não retornará nada, ou implicitamente retornará None. Em termos de avaliação booleana, None é considerado falso.
'''

### Outras formas de escrever a function is_win ###

def is_win2(player, opponent):
    # return True if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False

def is_win3(player, opponent):
    # return True if player wins
    # r > s, s > p, p > r
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')


print(play())
