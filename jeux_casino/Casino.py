""" nous allons ecrire un jeu de casino dans ce programme notament le fameux jeu de la roulette .
Comment il vas ce presenter : nous allons tout d'abord demande a l'utilisateur de saisir un montant qu'il souhaite utiliser pour le jeu en suite nous lui demanderons a chaque fois le montant qu'il souhaite miser et nous lui demanderons donc de choisir un nombnre entre 0 et 50 qui sera genere aleatoirement
grace a la fonction randint du module random
-Une partie est gagner si le chiffre choisi par l'utilisateur correspont a celui generer et dans ce cas son gain sera la mise * 3
 -Une partie est recompensee si : le numero choisi par et le numero genere sont tous 2 paires ou impaires dans ce cas son gain est de 50% de la mise dans ce cas si le gain est un nombre float on va utiliser le module ceil pour l'arrondir en exce
 -Si ce n'es pas le cas le joueur perd tous"""

# on importe d'abord nos 2 fonctions dans leurs modules respectif:
# le module random pour genere aleatoirement des valeurs dans ce module pon utilisera la fonctio randint pour generer un nombre aleatoirement 
# la fonction ceil du module math qui vas ce charger de convertir par exce la valeur en argent qu'on aura obtenu


from random import  randint
from math import ceil

tokens = int(input(" How many token will you use to start the game :  "))
continue_gamme = True # On declare un booleen qui est vrai tant que l'utilisateur doit continuer la partie
print(f" You are sitting at a table with {tokens} tokens . ")
while continue_gamme:
    player_number = -1
    while player_number < 0:
        player_number = int(input(" Enter you bet number (between 0 and 49) : "))
        try :
            if player_number < 0 or player_number > 49 :
                raise ValueError
        except ValueError:
            print(" You did not enter a valid number.")
            player_number = -1

    bet = -1
    while bet <= 0 or bet > tokens :
        bet = int(input(" Enter the number of tokens you want bet : "))
        try :
            if bet <= 0 or bet > tokens :
                raise ValueError
        except ValueError:
            print(f" The amount you entered is not valid. You have {tokens} tokens. ")
    winning_number = randint(0, 49)
    print(f" The wheel is spinning....... and stops on the number {winning_number} .")
    if player_number == winning_number:
        print(f" Congratulations ! you won the game ! Your gain is {bet * 3} Tokens.")
        tokens += bet * 3
    elif winning_number % 2 == 0 and player_number % 2 == 0 or winning_number % 3 == 0 and player_number % 3 == 0 :
        partial_win = ceil(mise * 0.5)
        print(f" You guessed the correct category! You win {partial_win * 0.5} tokens")
        tokens += partial_win
    else :
        print(" Sorry,  you lost your bet. Try again!")
        tokens -= bet

    if token <= 0 :
        print(" Game over! You have no token left.")
        continu_game = False
    else:
        print(f" You now have {tokens} tokens.")
        match input(" Do you want to leave the casino (y/n)?").lower():
            case "y" :
                print(" You leave the game with your winnings")
                continu_game = False
