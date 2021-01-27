#Modificar texto
def file_write():
    f= open("text.txt", "w")
    str = input("introdueix el text que vols modificar: ")
    f.write(str)
    f.close()

#Añadir texto
def file_add():
    f = open("text.txt", "a")
    str = input("introdueix el text que vols afegir: ")
    f.write(str)
    f.close()

#Opcion de menu
def file_menu():
    print("1. Crear un fitxer")
    print("2. Mostrar el contingut del fitxer")
    print("3. Modificar el contingut del fitxer")
    print("4. sortir")
    menu=int(input("Que vols fer?: "))
    if (menu==1):
        name=input("Introdueix el nom del fitxer nou: ")
        f = open(name, "a+")
        f.close()
    elif (menu==2):
        name=input("Introdueix el nom del fitxer que vols llegir: ")
        f = open(name, "r")
        print(f.read())
        f.close()
    elif (menu==3):
        name = input("Introdueix el nom del fitxer que vols modificar: ")
        text = input("Introdueix el text que vols introduir: ")
        f = open(name, "w")
        f.write(text)
        f.close()
    else:
        print("Adios!!!")