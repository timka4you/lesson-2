def main():
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print("Successfully converted to integer:", number)
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()