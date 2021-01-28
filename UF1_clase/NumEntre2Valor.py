def main():
    num1 = int(input("introdueix primer valor"))
    while num1<0:
        print("Introdueix un valor correcte")
        num1 = int(input("introdueix primer valor"))
    num2 = int(input("introdueix segon valor"))
    while num2<0 or num2<num1:
        print("Introdueix un valor correcte")
        num2 = int(input("introdueix segon valor"))
    for i in range(num1, num2+1, 1):
        print(i)
    print("asdadsa")

if __name__ == '__main__':
    main()