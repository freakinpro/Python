from random import randint

def display_header():
    print("############################################################")
    print("Harry Potter Typing Trainer")
    print("############################################################")
    
def display_instructions():
    """ Open file in read mode and read the lines and print using for loop"""

    file = open("instructions.txt","r")
    instructions = file.readlines()
    
    # Please note that strip() method is used because
    # it removes the white spaces and the \n tags and
    # returns the string

    # If we dont use strip(), extra white spaces will be printed between the lines
    for line in instructions:
        print(line.strip())

def read_spells(filename: str):
    #open file in read mode and read the lines from it and return the list
    file = open(filename, 'r')
    spells = file.readlines()
        
    return spells

def get_random_spell(spells: list[str]):
    # This calculates the length of the spells list and
    # then applies randint() function
    # here I gave randint a range of 0 to length - 1 because
    # the list index starts with zero upto length - 1
    # strip() method is used to remove the white spaces between the word
    # if strip() is not used then it will not match the user input because of
    # the empty spaces present around the words
    length = len(spells)
    spell = spells[randint(0, length-1)].strip()

    return spell.lower()

def get_user_input(spell: str):
    
    print(f"Type the following spell: {spell}")
    user_input = input("")
    #user Input is taken and returns the input in lowercase using the lower() method
    return user_input.lower()

def display_feedback(spell: str, user_input: str):
     #checks if the user_input matches the string and if it does
     # prints correct and incorrect respectively
    if user_input == spell:
        print("Correct!")
    else:
        print(f"Incorrect!\nThe spell was {spell}")
        

def main():
    # function calls in main function =>

    spells = read_spells('spells.txt')
    spell = get_random_spell(spells)
    display_header()
    display_instructions()
    user_input = get_user_input(spell)
    display_feedback(spell, user_input)
    
main()