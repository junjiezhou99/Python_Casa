print("*****************************************")
print("********* Gestió d'alumnes **************")
print("*****************************************")

number = int(input("Indica el nombre d'alumnes que vols introduir: "))
for i in range(number):
    student_ID = int(input("Introdueix l'identificador: "))
    first_name = input("Introdueix el nom de l'estudiant: ")
    last_name = input("Introdueix el cognom de l'estudiant: ")
    subject = input("Introdueix l'assignatura: ")
    grade = int(input("Introdueix la nota: "))

    student = {
        "student_ID": student_ID,
        "first_name": first_name,
        "last_name": last_name,
        "subject": subject,
        "grade": grade
    }
    print(student)