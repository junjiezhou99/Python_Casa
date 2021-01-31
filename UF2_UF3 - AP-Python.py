import csv

def main():
    print("*****************************************")
    print("********* Gestió d'alumnes **************")
    print("*****************************************")

    print("----Menu inicial----")
    print("1. Introdueir alumnes")
    print("2. Mostrar alumnes")
    print("3. Analitzar registres")
    menu = int(input("Introdueix l'opcio: "))
    if (menu==1):
        add_menu()
    elif (menu==2):
        show_menu()


def add_menu():
    number = int(input("Indica el nombre d'alumnes que vols introduir: "))
    for i in range(number):
        student_ID = int(input("Introdueix l'identificador: "))
        first_name = input("Introdueix el nom de l'estudiant: ")
        last_name = input("Introdueix el cognom de l'estudiant: ")
        subject = input("Introdueix l'assignatura: ")
        grade = int(input("Introdueix la nota: "))
        '''student = {
            "student_ID": student_ID,
            "first_name": first_name,
            "last_name": last_name,
            "subject": subject,
            "grade": grade
        }'''
        with open('algo.csv', 'a') as csvfile:
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

if __name__ == '__main__':
    main()