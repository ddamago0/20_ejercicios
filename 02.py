edad = int (input("Ingrese su edad: "))

if edad < 13:
    print ("No puede ingresar!")

elif edad >= 13 and edad <= 17:
    print ("Ingrese a: Clase Juvenil")

elif edad >= 18 and edad <= 59:
    print ("INgrese a: Clase general")

else:
    print ("Ingrese a: Clase senior")
    