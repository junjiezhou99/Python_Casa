def main():
    num1 = test()
    num2 = test()
    num3 = test()
    num = bigger(num1, num2, num3)
    print(num)

def test():
    a = int(input("introdueix el nombre: "))
    return a

def bigger(a, b, c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    return c

if __name__ == '__main__':
    main()