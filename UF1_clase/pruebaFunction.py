def main():
    print("======================Menú=======================")
    prueba()
    selection = introNom()
    num1 = nombres()
    num2 = nombres()
    operation(selection, num1, num2)

def prueba():
    print("1. Multiplicar")
    print("2. Dividir")
    print("Que desea hacer?")

def introNom():
    a = int(input("Introdueix l'opció: "))
    while (a>2 or a<1):
        a = int(input("Introduzca valor correcto: "))
    return a

def nombres():
    a = int(input("introdueix num: "))
    return a

def operation(a, b, c):
    if (a==1):
        print("Multiplicacio: " + str(b*c))
    else:
        print("Divisio: " + str(b/c))

if __name__ == '__main__':
    main()