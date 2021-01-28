def main():
    print("Comienza el juego, introducirás un número inicial, a partir del número inicial entre tu y pc iréis restando entre 1-3, el último que reste pierde el juego")
    print("introduce un numero inicial")
    num = int(input())
    while num < 2:
        print("El numero inicial tiene que ser mayor de 1")
        num = int(input())
    print("has introducido: ", num)
    while num != 1:
        if num % 4 == 1:
            print("Comienza tu")
        elif num % 4 == 2:
            print("Le quito 1")
            num -= 1
            print("ahora el numero es ", num)
        elif num % 4 == 3:
            print("le quito 2")
            num -= 2
            print("ahora el numero es ", num)
        elif num % 4 ==0:
            print("Le quito 3")
            num-=3
            print("ahora el numero es ", num)
        if num!=1:
            value = int(input())
            while value<1 or value>3:
                print("num tiene que ser entre 1-3")
                value = int(input())
            num -= value
            print("has restado", value)
    value = int(input())
    while value < 1 or value > 3:
        print("num tiene que ser entre 1-3...")
        value = int(input())
    while value>num:
        print("num demasiado grande")
        value = int(input())
    num -= value
    print("has restado", value)
    print("has perdido")
if __name__ == '__main__':
    main()