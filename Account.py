
from getpass import getpass

account = input("Type Login to Log in and Signup to Signup\n")

def login_cred():
    username = input("what is your username?\n")
    password = getpass("what is your password?\n")
    print("\n" "Username:", username, "\n" "password:", password)


def Signup_cred():
    firstname = str(input("What is your First name?\n"))
    lastname = str(input("What is your Last name?\n"))
    age = int(input("How old are you?\n"))
    occupation = str(input("What is you occupation?(Student(STU) or Worker(WOR))\n"))
    location = str(input("Where do you stay currently?\n"))
    print(
        "\nfirstname:",
        firstname,
        "\n" "lastname:",
        lastname,
        "\n" "age:",
        age,
        "\n" "occupation:",
        occupation,
        "\n" "location:",
        location,
    )


def initials():
    initials = input("Are you sure of the filled spaces?(y,n)\n")
    n = "n"
    y = "y"
    if initials == y:
        print("success")
    elif initials == n:
        print("restart")
    else:
        exit("wrong option chosen")


if account == "login":
    login_cred()
    initials()

elif account == "signup":
    Signup_cred()
    initials()
else:
    exit("wrong answer required")
