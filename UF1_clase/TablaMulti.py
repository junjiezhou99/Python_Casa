def main():
    num = int(input("introdueix un nombre"))
    for i in range(1, 10, 1):
        print(num,"*", i, "=", num * i)
if __name__ == '__main__':
    main()