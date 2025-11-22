

try:
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    
    print("\nOpérations  :")
    print("+ : Addition")
    print("- : Soustraction")
    print("* : Multiplication")
    print("/ : Division")
    
    operation = input("Veulliez choisir une opération (+, -, *, /) : ")
    
    if operation == "+":
        somme = nombre1 + nombre2
        print(f"\n{nombre1} + {nombre2} = {somme}")
    
    elif operation == "-":
        difference = nombre1 - nombre2
        print(f"\n{nombre1} - {nombre2} = {difference}")
    
    elif operation == "*":
        resultat = nombre1 * nombre2
        print(f"\n{nombre1} * {nombre2} = {resultat}")
    
    elif operation == "/":
        try:
            resultat = nombre1 / nombre2
            print(f"\n{nombre1} / {nombre2} = {resultat}")
        except ZeroDivisionError:
            print("\nErreur : Division par zéro impossible !")
    
    else:
        print("\nErreur : Opérateur invalide !")
        print("Veuillez choisir autre +, -, *, /")

except ValueError:
    print("\nErreur : Veuillez entrer des nombres valides !")