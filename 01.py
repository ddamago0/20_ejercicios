vainilla = 0
chocolate = 0
fresa = 0

for i in range(5):
    print("\nMenú de sabores:")
    print("1. Vainilla")
    print("2. Chocolate")
    print("3. Fresa")
    
    opcion = int(input("Elige tu sabor de helado :) (1-3): "))

    if opcion == 1:
        vainilla += 1
    elif opcion == 2:
        chocolate += 1
    else:  # asumimos que solo puede ser 3
        fresa += 1

print("\nResultados:")
print("Vainilla:", vainilla)
print("Chocolate:", chocolate)
print("Fresa:", fresa)