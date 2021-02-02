import csv

def main():
    print("*****************************************")
    print("********* Gestió d'alumnes **************")
    print("*****************************************")

    print("----Menu inicial----")
    print("1. Introdueir alumnes")
    print("2. Mostrar alumnes")
    print("3. Analitzar registres")
    menu = int(input("Introdueix l'opcio: ")) #selecció de les opcions del menu
    if (menu==1):
        add_menu()
    elif (menu==2):
        show_menu()
    elif (menu==3):
        analyze_menu()


def add_menu():
    number = int(input("Indica el nombre d'alumnes que vols introduir: "))
    err=0
    for i in range(number):
        #introduccion y validacion de los datos
        while (err==0):
            try:
                student_ID = int(input("Introdueix l'identificador: "))
                err=1
            except:
                print("Introdueix l'identificador correctament")
        first_name = input("Introdueix el nom de l'estudiant: ")
        last_name = input("Introdueix el cognom de l'estudiant: ")
        subject = input("Introdueix l'assignatura: ")
        while (err==1):
            try:
                grade = int(input("Introdueix la nota: "))
                err=0
            except:
                print("Introdueix la nota correctament")

        #introduccion al csv
        with open('algo.csv', 'a', newline="") as csvfile:
            head = ['student_ID', 'first_name', 'last_name', 'subject', 'grade']
            writeCSV = csv.DictWriter(csvfile, fieldnames=head)
            writeCSV.writeheader()
            writeCSV.writerow({'student_ID': student_ID, 'first_name': first_name, 'last_name': last_name, 'subject': subject, 'grade': grade})

def show_menu():
    with open('algo.csv') as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            try:
                print(f'\t Identificador:{row[0]}, Nom:{row[1]}, Cognom:{row[2]}, Assignatura:{row[3]}, Nota:{row[4]}.')
            except:
                print("error")

def analyze_menu():
    print("1. Mostrar el total de registres")
    print("2. Els 2 primers registres")
    print("3. Els 2 ultims registres")
    register=int(input("Quants registres vol consultar: "))
    if (register==1):
        with open('algo.csv') as csvfile:
            readCSV = csv.reader(csvfile)
            print(csvfile.readline())

if __name__ == '__main__':
    main()