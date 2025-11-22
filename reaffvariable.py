

def observer_references():
    x = 10
    print(f"x = {x}, id = {id(x)}")
    
    y = x  
    print(f"y = x → y = {y}, id = {id(y)} (même que x)")
    
    x = x + 5  
    print(f"x = x + 5 → x = {x}, id = {id(x)} (nouvel objet!)")
    print(f"y reste = {y}, id = {id(y)} (inchangé)")

observer_references()


def observer_listes():
    liste1 = [1, 2, 3]
    liste2 = liste1  
    print(f"\nliste1 = {liste1}, id = {id(liste1)}")
    print(f"liste2 = liste1 → id = {id(liste2)} (même objet)")
    
    liste1.append(9)  
    print(f"liste1.append(9) → liste1 = {liste1}")
    print(f"liste2 = {liste2} → liste2 aussi modifiée!")

observer_listes()