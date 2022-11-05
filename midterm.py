def printName(name):
    return name

def printLastName(firstname, lastname):
    print(f"{firstname} {lastname}")


def main():
    name = input("Enter your name: ")
    lastname = input("Enter your last name: ")

    printLastName(printName(name), lastname)

main()