cafe = 4000
te = 3500
jugo = 5000

print("\nMenú de bebidas:")
print("")
print("1. Café")
print("2. Té")
print("3. Jugo")
print("")

opcion = int (input("Ingrese su bebida deseada: (1-3): "))

if opcion == 1:
    print ("Execelente decicion :) ")
    opcion = cafe

elif opcion == 2:
    print ("Execelente decicion :) ")
    opcion = te

elif opcion == 3:
    print ("Execelente decicion :) ")
    opcion = jugo

else:
    print ("Bebida no disponible.")

print("") 
cantidad = int (input("Ingrese la cantidad que desea comprar: "))

total = opcion * cantidad

print ("Total a pagar: ",total)


    







