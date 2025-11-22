

texte = input("Entrez un mot ou une phrase : ")

longueur = len(texte)
majuscules = texte.upper()
minuscules = texte.lower()
inverse = texte[::-1]


print(f"\n ANALYSE DU TEXTE : '{texte}'")
print(f"Longueur : {longueur} caractères")
print(f"En majuscules : {majuscules}")
print(f"En minuscules : {minuscules}")
print(f"Inversé : {inverse}")


inverse = texte[::-1]

if texte == inverse:
    print(f"'{texte}' est un palindrome !")
    print(f"Car '{texte}' se lit comme '{inverse}' à l'envers")
else:
    print(f"'{texte}' n'est pas un palindrome")
    print(f"Car à l'envers ça donne '{inverse}'")