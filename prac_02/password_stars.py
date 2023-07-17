MINIMUM_CHARACTER = 0


def main():
    """The function that we can call"""
    password = get_password()
    show_password(password)


def show_password(password):
    """The function that will show the asterisks."""
    print("Your new password is:", "*" * len(password))


def get_password():
    """The function that will ask the user for the input and error checking."""
    password = input("Enter your password: ")
    while len(password) <= MINIMUM_CHARACTER:
        print("The password doesn't meet a minimum length set by a variable. Please try again.")
        password = input("Enter your password: ")
    return password


main()
