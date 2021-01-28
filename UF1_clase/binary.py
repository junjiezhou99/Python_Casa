def main():
    decimal = int(input("introdueix el decimal"))
    count=1
    binary=0

    while decimal!=0:
        if decimal%2==0:
            count*=10
            decimal/=2
        else:
            binary+=count
            count *= 10
            decimal-=1
            decimal/=2
    print(binary)

if __name__ == '__main__':
    main()