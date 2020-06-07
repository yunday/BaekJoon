def main():
    n = int(input())
    if n == 1:
        print(1)
    else:
        print(int((3 + (12 * n - 15) ** 0.5)) // 6 + 1)


main()
