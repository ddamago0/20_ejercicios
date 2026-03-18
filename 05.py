perro = 0
gato= 0
conejo = 0

print ("\nTipo de mascotas.")
print ("")
print ("1. Perro")
print ("2. Gato")
print ("3. Conejo")
print ("")

opcion = int (input("Ingrese tipo d mascota: " ))

if opcion == 1:
    print ("Alimento recomendado:  Hills Science Diet")

elif opcion == 2:
    print ("Alimento recomendado: pollo, pavo, pescado (salmón), huevo cocido, " \
    "y pequeñas cantidades de vegetales cocidos como zanahoria o calabacín")

else:
    print ("Alimento recomendado: festuca o avena")