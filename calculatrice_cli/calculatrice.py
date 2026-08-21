def additionner(a, b) :
    result = a + b
    return result

def soustraction(a, b) :
    result = a - b
    return result


def multiplication(a, b) : 
    result = a * b
    return result

def division(a, b) : 
    if b == 0 :
        return "Erreur : La Division par zero est impossible"
    result = a / b
    return result

def demander_nombre(operation) :
    try : 
        a = float(input(f"Entrez le premier nombre de la {operation} : "))
        b = float(input(f"Entrez le deuxieme nombre de la {operation} : "))
        return a, b
    except ValueError :
        print(VALUE_ERROR)
        return None, None


SEPARATEUR = "=" * 40
VALUE_ERROR = "Erreur de valeur veillez entrer des nombres pas des lettres"


def calculatrice() :
    while True :
        print (SEPARATEUR)
        print ("BIEN VENU SUR VOTRE CALCULATRICE PYTHON")
        print (SEPARATEUR)
        print ("1. Addition")
        print ("2. Soustraction")
        print ("3. Multiplication")
        print ("4. Division")
        print ("Q. Quitter")

        choice = input("Choisisez l'operation que ous souhaitez effectuer en entrant le caractere qui y est associe EXP: 1,2,3,4 ou Q pour quitter : ")

        if choice == "1" :
            print("Vous avez choisis l'addition !!!")
            a,b =demander_nombre("Addition")
            if a is not None :
                print(f"Le resultat de l'addition de {a} + {b} est : ",additionner(a, b))
        elif choice == "2" :
            print("Vous avez choisis la soustraction !!!")
            a, b =demander_nombre("Soustraction")
            if a is not None :
                print(f"Le resultat de la soustraction de {a} - {b} est : ",soustraction(a, b))
        elif choice == "3" :
            print("Vous avez choisi la multiplication !!!")
            a, b = demander_nombre("Multiplication")
            if a is not None :
                print(f"Le resultat de la multiplicationtion de {a} * {b} est : ",multiplication(a, b))
        elif choice == "4" :
            print("Vous avez choisis la division !!!")
            a, b = demander_nombre("Division")
            if a is not None :
                print(f"Le resultat de la division de {a} / {b} est : ",division(a, b))
        elif choice.upper() == "Q" :
            print(SEPARATEUR)
            print("Vous avez choisis quitter le Programme!")
            print(SEPARATEUR)
            break
        else : 
            print("Choix invalide veuillez entrer 1, 2, 3, 4 ou Q ")

calculatrice()