import random


def compare_numbers(user_number, random_number):
    if user_number > random_number:
        return "smaller"
    elif user_number < random_number:
        return "bigger"
    else:
        return "Congratulations! You guessed the number."


def main():
    random_number = random.randint(1, 10)
    user_number = int(input("Enter your number (between 1 and 10): "))

    result = compare_numbers(user_number, random_number)
    print("Your number is", result, "than the random number.")


if __name__ == "__main__":
    main()