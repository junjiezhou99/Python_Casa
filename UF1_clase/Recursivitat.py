def main():
    n = int(input("introdueix el nombre (suma de tots els nombres): "))
    print(sum(n))
    num1 = int(input("introdueix el nombre (factor d'un nombre): "))
    num2 = int(input("introdueix el nombre (factor d'un nombre): "))
    print(fact(num1, num2))
    num3 = int(input("introdueix el nombre (potencia d'un nombre): "))
    print(pot(num3))

def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)

def fact(num1, num2):
    if num2==0:
        return 1
    else:
        return num1 * fact(num1, num2-1)

def pot(num3):
    if num3==1:
        return 1
    else:
        return num3 * pot(num3-1)

if __name__ == '__main__':
    main()