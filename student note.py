def categorize_number(num):
    if num >= 0 and num <= 49:
        return "bad"
    elif num >= 50 and num <= 69:
        return "not bad"
    elif num >= 70 and num <= 89:
        return "good"
    elif num >= 90 and num <= 100:
        return "super"

def main():
    num = int(input("Enter a number between 0 and 100: "))
    category = categorize_number(num)
    print(f"The number {num} is {category}.")

if __name__ == "__main__":
    main()