SEPARATEUR = "=" * 48
ERROR_VALUE = "Veillez entrer un chiffre pas une lettre ni un caractere"

def ask_value(unity) :
    try :
       value = float(input(f"Entrez la valeur en {unity} : "))
       return value
    except ValueError :
       print(ERROR_VALUE)
       return None

def celsius_to_fahrenheit(c) :
   result = c * 1.8 + 32
   return round (result, 2)
def fahrenheit_to_celsius(f) :
   result = (f - 32) * 5/9
   return round (result, 2)

def celsius_to_kelvin (c) :
   result = c + 273.15
   return round (result, 2)

def kilometres_to_miles (km) :
   result = km * 0.621371
   return round(result, 2)

def miles_to_kilometres (m) : 
   result = m * 1.60934
   return round(result, 2)

def metres_to_pieds(m) :
   result = m * 3.28084
   return round(result, 2)

def kilogrammes_to_livres(kg) :
   result = kg *2.20462
   return round(result, 2)

def livres_to_kilogrammes(lbs) :
   result = lbs * 0.453592
   return round(result, 2)

def grammes_to_onces(g) :
   result = g * 0.035274
   return round(result, 2)

def menu_temperature() :
   while True :
      print(SEPARATEUR)
      print("VOUS ETES SUR LE SOUS MENU CONVERSION DE TEMPERATURE !!!")
      print(SEPARATEUR)
      print("1. degre Celsius(°C) vers degre Fahrenheit (°F)")
      print("2. degre Fahrenheit (°F) vers degre Celsius(°C)")
      print("3. degre Celsius(°C) vers degre Kelvin (°K)")
      print("R. Retour au menu principal")

      choice = input("Entrez le carractere qui correspond a la conversion que vous souhaitez effectuer : ")

      if choice == "1" :
         print("Vous avez choisi la conversion du degre Celsius en degre Fahrenheit !!!")
         valeur = ask_value("Celsius")
         if valeur is not None :
            print(f"La conversion de {valeur}°C en °F est : ",celsius_to_fahrenheit(valeur))
      elif choice == "2" :
         print("Vous avez choisi la conversion du degre Fahrenheit en degre Celsius !!!")
         valeur = ask_value("Fahrenheit")
         if valeur is not None :
            print(f"La conversion de {valeur}°F en °C est de : ",fahrenheit_to_celsius(valeur))
      elif choice == "3" :
         print("Vous avez choisi la conversion du degre Celsius en degre Kelvin")
         valeur = ask_value("Celsius")
         if valeur is not None :
            print(f"La conversion de {valeur} °C en °K est : ",celsius_to_kelvin(valeur))
      elif choice.upper()== "R" :
         print(SEPARATEUR)
         print("VOUS AVEZ CHOISIS DE RETOURNEZ AU MENU PRINCIPAL")
         print(SEPARATEUR)
         break
      else :
         print("Votre choix est invalide vous ne pouvez entrer que 1, 2, 3 ou R ")

def menu_distance() :
   while True :
      print(SEPARATEUR)
      print("VOUS ETES SUR LE SOUS MENU CONVERSION DE CONVERSION DE DISTANCE")
      print(SEPARATEUR)
      print("1. Kilometres (Km) en Miles (M)")
      print("2. Miles (M) en Kilometres (Km)")
      print("3. Metres (M) en Pieds (P)")
      print("R. Retour au menu principal")

      choice = input("Entrez le carractere qui correspond a la conversion que vous souhaitez effectuer : ")

      if choice == "1" :
         print("Vous avez choisis la conversion du Kilometre (Km) en Miles (M)")
         valeur = ask_value("Kilometre")
         if valeur is not None :
            print(f"La conversion de {valeur} Kilometre (Km) en Miles (M) est de : ",kilometres_to_miles(valeur))
      elif choice == "2" :
         print ("Vous avez choisis la conversion du Miles (M) en Kilometres (Km)")
         valeur = ask_value("Kilometres")
         if valeur is not None :
            print(f"La conversion de {valeur} Miles (M) en Kilometres (Km) est de : ",miles_to_kilometres(valeur))
      elif choice == "3" :
         print("Vous avez choisis la conversion du Metres (M) en Pieds (Foot-Ft)")
         valeur = ask_value("Metres")
         if valeur is not None :
            print(f"La conversion de {valeur} Metres (M) en Pied (Foot-Ft) est de : ",metres_to_pieds(valeur))
      elif choice.upper() == "R" :
          print(SEPARATEUR)
          print("VOUS AVEZ CHOISIS DE RETOURNEZ AU MENU PRINCIPAL")
          print(SEPARATEUR)
          break
      else :
         print("Votre choix est invalide vous ne pouvez entrer que 1, 2, 3 ou R ")


def menu_poids ():
   while True :
      print(SEPARATEUR)
      print("VOUS ETES SUR LE SOUS MENU DE CONVERSION DE POIDS")
      print(SEPARATEUR)
      print("1. Kilogrammes (Kg) en Livres (Lbs-Pound)")
      print("2. Livres (Lb) en Kilogrammes (Kg)")
      print("3. Grammes (G) en Onces (Oz)")
      print("R. Retour au menu principal")

      choice = input("Entrez le carractere qui correspond a la conversion que vous souhaitez effectuer : ")

      if choice == "1" :
         print("Vous avez choisis la conversion du Kilogrammes (Kg) en Livres (Lbs) !!!")
         valeur = ask_value("Kilogrammes")
         if valeur is not None :
            print(f"La conversion de {valeur} Kilogrammes (Kg) en Livres (Lbs) est de : ",kilogrammes_to_livres(valeur))
      elif choice == "2" :
         print("Vous avez choisis la conversion du Livre (Lbs) en Kilogramme (kg) ")
         valeur = ask_value("Livres")
         if valeur is not None : 
            print(f"La conversion de {valeur} Livres (Lbs) en Kilogrammes (Kg) est de : ",livres_to_kilogrammes(valeur))
      elif choice == "3" :
         print("Vous avez choisis la conversion du Grammes (G) en Onces (Oz)")
         valeur = ask_value("Grammes")
         if valeur is not None : 
            print(f"La conversion de {valeur} Grammes (G) en Onces (Oz) est de : ",grammes_to_onces(valeur))
      elif choice.upper() == "R" :
        print(SEPARATEUR)
        print("VOUS AVEZ CHOISIS DE RETOURNEZ AU MENU PRINCIPAL")
        print(SEPARATEUR)
        break
      else :
         print("Votre choix est invalide vous ne pouvez entrer que 1, 2, 3 ou R ")

def convertiseur ():
   while True :
      print(SEPARATEUR)
      print("BIENVENU SUR LE MENU PRINCIPAL DES CONVERSIONS !!!")
      print(SEPARATEUR)
      print("-1- Temperatures")
      print("-2- Distances")
      print("-3- Poids")
      print("-Q- Quitter")

      choice = input("Entrez le caractere de la conversion que vous souhaitez effectuer : ")

      if choice == "1" :
         menu_temperature()
      elif choice == "2" :
         menu_distance()
      elif choice == "3" :
         menu_poids()
      elif choice.upper() == "Q" :
         break
      else :
         print("Votre choix est invalide vous ne pouvez entrer que 1, 2, 3 ou Q ")

convertiseur()