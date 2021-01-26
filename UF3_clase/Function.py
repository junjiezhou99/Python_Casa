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