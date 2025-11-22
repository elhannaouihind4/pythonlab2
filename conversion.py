

print("\n Veuillez choisir le type de conversion :")
print("1. Celsius vers Fahrenheit et Kelvin")
print("2. Fahrenheit vers Celsius et Kelvin")
print("3. Kelvin vers Celsius et Fahrenheit")

choix = input("\nVotre choix (1-3) : ")

if choix == "1":

    celsius = float(input("\nEntrer la température en °C : "))
    fahrenheit = celsius * 9/5 + 32
    kelvin = celsius + 273.15
    print(f"\n{celsius}°C = {fahrenheit}°F = {kelvin}K")

elif choix == "2":
    
    fahrenheit = float(input("\nEntrer la température en °F : "))
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"\n{fahrenheit}°F = {celsius}°C = {kelvin}K")

elif choix == "3":
    
    kelvin = float(input("\nEntrer la température en K : "))
    celsius = kelvin - 273.15
    fahrenheit = celsius * 9/5 + 32
    print(f"\n{kelvin}K = {celsius}°C = {fahrenheit}°F")

else:
    print("\nChoix invalide ! Veuillez choisir 1, 2 ou 3.")