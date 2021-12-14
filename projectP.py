
def info_personne(nom, age, taille):
   print(f"la personne s'appelle {nom}, son age est {age} ans ", f"elle mesure {taille} cm ")


def demander_nom():
   nom=input("Quel est votre nom ")
   return nom

def demander_age():
 age_int = 0
 while age_int == 0:
    age_str = input("Quel est votre age ? ")
    try:
        age_int = int(age_str)
    except:
        print("Erreur: vous devez rentrer un nombre pour l'age")
 return age_int

def demander_taille():
  taille_int = 0
  while taille_int == 0:
    taille_str = input("Quel est votre taille ? ")
    try:
        taille_int = int(taille_str)
    except:
        print("Erreur: vous devez rentrer un nombre pour la taille")
  return taille_int

nb_persone= 3
for i in range (0,nb_persone):
    nom="personne" + str(i+1)
    age=demander_age()
    taille=demander_taille()
    info_personne(nom, age, taille)