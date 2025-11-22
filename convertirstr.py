#age_str = input("Quel âge as-tu ? ")
#print("Tu as saisi :", age_str, "→", type(age_str))

#age = int(age_str)
#print("Après conversion :", age, "→", type(age))

try:
    age = int(input("Quel âge as-tu ? "))
    print(f"Dans 5 ans tu auras {age + 5} ans.")
except ValueError:
    print("Saisie invalide, merci d'entrer un entier.")