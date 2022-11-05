from random import randint

def display_header():
    print("############################################################")
    print("Harry Potter Typing Trainer")
    print("############################################################")
    
def display_instructions():
    file = open("instructions.txt","r")
    instructions = file.readlines()
    
    for line in instructions:
        print(line.strip())

def read_spells(filename: str):
    file = open(filename, 'r')
    spells = file.readlines()
        
    return spells

def get_random_spell(spells: list[str]):
    length = len(spells)
    spell = spells[randint(0, length-1)].strip()

    return spell.lower()

def get_user_input(spell: str):
    
    print(f"Type the following spell: {spell}")
    user_input = input("")
    
    return user_input.lower()

def display_feedback(spell: str, user_input: str):
     
    if user_input == spell:
        print("Correct!")
        #added a return statement for every correct spell returns true so score can be added
        return True
    else:
        print(f"Incorrect!\nThe spell was {spell}")


#asks the user if he/she wants to play again then returns true or false according to the choice      
def play_again():
    print("Do you want to play again? Y/N")
    user_input = input("")
    if user_input.lower() == "y":
        return True
    else:
        return False

def main():
    score = 0
    display_header()
    display_instructions() 
    #variable if choice is true then go in while loop
    loop = True

    while loop == True:
        spells = read_spells('spells.txt')
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)
        feedback = display_feedback(spell, user_input)
        #for managing score
        if feedback == True:
            score += 10
        else:
            score -= 5
        loop = play_again()
        #if the users choice is No
        if loop == False:
            print(f"Your Score is {score}!")


main()