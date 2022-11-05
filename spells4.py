from random import randint
import time

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
    
    file = open(filename, 'r')
    spells = file.readlines()
    
    return spells

def get_random_spell(spells: list[str]):
    length = len(spells)
    spell = spells[randint(0, length-1)].strip()

    return spell.lower()

def get_user_input(spell: str) -> (str, float):
    """
    Gets input from the user
    Returns the input and the time it took the user to type the input
    """
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time


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

def get_target_time(spell: str) -> float:
    # Calculates length of the spell and multiplies it with 0.3 and then returns it
    TTT = len(spell) * 0.3
    return TTT

#I added an extra parameter to the function to match between the target time and the user time
def calculate_points(spell: str, user_input: str, user_time: float, target_time: float) -> int:
    """
    Calculates the points that the user gets.
    spell: The spell that the user is typing.
    user_input: The input that the user typed.
    user_time: The time that the user took to type the input.
    target_time: The time the user had to achieve
    """
    #checks if user_input matches the random spell
    if user_input == spell:
        #if user_time is less than or equal to the target time
        """ CONDITIONS MENTIONED IN THE LAB"""
        if user_time <= target_time:
            return 10
        elif user_time <= (target_time*1.5) and user_time > target_time:
            return 6
        elif user_time <= (target_time*2) and user_time >= (target_time*1.5):
            return 3
        elif user_time > (target_time*2):
            return 1
    else: # if the user input does not match the required spell
        return -5



def main():
    score = 0
    display_header()
    display_instructions()
    #variable if choice is true then go in while loop
    loop = True
    while loop == True:
        spells = read_spells('spells.txt')
        spell = get_random_spell(spells)
        #we use tuples like this. we pass index of the tuple we want to store
        user = get_user_input(spell)
        user_input = user[0]
        user_time = user[1]
        #Display if value is correct or incorrect
        display_feedback(spell, user_input)
        #for managing score
        score += calculate_points(spell, user_input, user_time, get_target_time(spell))
        
        loop = play_again()
        #if the users choice is No
        if loop == False:
            print(f"Your Score is {score}!")


main()
