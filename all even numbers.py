def list_even_numbers_between(start, end):
    if start < end:
        for i in range(start + 1, end):
            if i % 2 == 0:
                print(i, end=' ')
    else:
        for i in range(end + 1, start):
            if i % 2 == 0:
                print(i, end=' ')

def main():
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
    print("Even numbers between", start, "and", end, "are:")
    list_even_numbers_between(start, end)

if __name__ == "__main__":
    main()