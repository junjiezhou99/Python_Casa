def main():
    num = int(input("Introdueix un nombre"))
    suma=0
    while suma<num:
        print("")
        suma+=1
        count=0
        while count<suma:
            print(suma, end="")
            count+=1
if __name__ == '__main__':
    main()