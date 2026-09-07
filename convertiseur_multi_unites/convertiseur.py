SEPARATEUR = "=" * 40

def celsius_to_fahrenheit(c) :
   result = c * 1.8 + 32
   return round (result, 2)

def fahrenheit_to_celsuis(f) :
   result = (f - 32) * 5/9
   return round (result, 2)

def celsuis_to_kelvin (c) :
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