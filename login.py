import ast

MENU_OPTIONS = """
Enter:
'a' - to add an account
'l' - to login to your account
'q' - to quit
"""

users = []

def add_account():
    """
    A function that creates a new user object.
    """

    users = open_txtfile()

    username = input("\nEnter a username: ")
    #Checks if the username exits already
    for user in users:
        if user.get("username") == username:
            print("\nSorry that name is already in use.")
            return
    password = input("\nEnter a password: ")

    #Creates the user object
    user = {"username": username, "password": password}

    if user_confirmation(username, password):
        users.append(user)
        print(f"\nOkay, you have made an account under the name '{username}'")
        with open("account.txt", "w") as s:
            for user in users:
                s.write(f"{user}\n")

def user_confirmation(username, password):
    """
    A function that confirm whether a user wants there username and password.
    """

    print(f"\nWould you like to create you account with the username '{username}' and password '{password}'\n")

    confirmation = input("Enter 'y' to confirm or anything else to cancel: ")
    if confirmation.lower() == "y":
        return True
    else:
        return False

def open_txtfile():
    """
    A function that opens accounts.txt and converts it to a list of dictionaries.
    """

    all_accounts = open("account.txt").read().split("\n")
    for i in range(0, len(all_accounts) - 1):
        #Converts dictionary string to dictionary 
        acc = ast.literal_eval(all_accounts[i])
        users.append(acc)

    return users

def login():
    """
    A function that allows a user to login to their account.
    """

    users = open_txtfile()
    account = {}

    username = input("\nPlease enter you username: ")
    for user in users:
        if user.get("username") == username:
            account = user
            break
    
    if account != user:
        print("\nSorry that account is not in our database")
        return

    password = input("\nPlease enter your password: ")
    if account.get("password") == password:
        print(f"\nWelcome back, {username}")
    else:
        print("\nSorry the username and password don't match")

def menu():
    while True:
        user_options = input(MENU_OPTIONS)

        if user_options.lower() == 'a':
            add_account()
        elif user_options.lower() == 'l':
            login()
        elif user_options.lower() == 'q':
            break
        else:
            print("\nPlease enter a valid option")

if __name__ == '__main__':
    menu()