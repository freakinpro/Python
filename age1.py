
def main():
    #input character name
    charName = input("Enter Character Name: ")
    #input character age
    charAge = int(input("Enter Character Age: "))
    
    #hard-coded
    frodo_age = 51

    if (charAge < frodo_age):
        #For character age greater than frodo
        print(f"{charName} is {charAge} years old, and they are younger than Frodo.")
    elif (charAge > frodo_age):
        #For character age smaller than frodo
        print(f"{charName} is {charAge} years old, and they are older than Frodo.")
    else:
        #For character age same as frodo
        print(f"{charName} is {charAge} years old, and they are are of the same age as Frodo.")


#call main function
main()