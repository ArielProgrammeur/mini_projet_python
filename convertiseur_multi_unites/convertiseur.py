SEPARATEUR = "=" * 48
ERROR_VALUE = "Veillez entrer un chiffre pas une lettre ni un caractere"

def ask_value(unity) :
    try :
       value = float(input(f"Entrez la valeur en degre {unity} : "))
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

def kilometres_to_milles (km) :
   result = km * 0.621371
   return round(result, 2)

def milles_to_kilometres (m) : 
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
         print("Vous retournez au menu principal")
         print(SEPARATEUR)
         break
      else :
         print("Votre choix est invalide vous ne pouvez entrer que 1, 2, 3 ou R ")

menu_temperature()