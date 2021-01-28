def main():
    #Missatge de benvinguda
    print("****************************************")
    print("*****Aplicació d'anàlisi estadístic*****")
    print("****************************************")

    #Introducció de dades
    #Nombre de histoia clinica (int)
    number=int(input("Introdueix l'história clínica: "))
    while (number<0):
        number = int(input("El nombre no pot ser negatiu: "))

    #Edat del pacient (int)
    age=int(input("Introdueix l'edad de debut del pacient (en mesos): "))
    while (age<0):
        age = int(input("L'edad no pot ser negatiu: "))

    #Diagnosis (str)
    diagnosis=str(input("Introdueix el seu diagnòstic (DX): "))

    #Nivell de NT (bool)
    validation=int(input("Té els nivells de NT aterats?: "))
    while (validation>1 or validation<0):
        validation = int(input("Valor ha de ser 1 (si) o 0 (no): "))
    disturbance = bool(validation)

    #Convulsions (bool)
    validation=int(input("Té convulsions generalitzades?: "))
    while (validation>1 or validation<0):
        validation = int(input("Valor ha de ser 1 (si) o 0 (no): "))
    convulsions=bool(validation)

    #Mostre de les dades
    print("|HC    |Edat          |DX                  |Alteració NT   |Conv. Generals  |")
    print(number, end="   ")
    if (age>12):
        year=int(age/12)
        month=age%12
        print(year, "any ", month, "mesos", end="  ")
    else:
        print(age, "mesos", end="        ")
    print(diagnosis, end="  ")
    if (disturbance==True):
        print("Si", end="            ")
    else:
        print("No", end="            ")
    if (convulsions==True):
        print("Si")
    else:
        print("No")


if __name__ == '__main__':
    main()