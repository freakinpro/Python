from random import randint

def read_spells(filename: str):
    file = open(filename, 'r')
    spells = file.readlines()
        
    return spells

def get_random_spell(spells: list[str]):
    length = len(spells)
    # This calculates the length of the spells list and
    # then applies randint() function
    # here I gave randint a range of 0 to length - 1 because
    # the list index starts with zero upto length - 1
    # strip() method is used to remove the white spaces between the word
    spell = spells[randint(0, length-1)].strip()
    return spell.lower()


def main():
    # main function is calling other functions

    # this will only work if the file is placed in the same directory as this file
    spells = read_spells('spells.txt')
    print('Harry Potter Keyboard Trainer')
    # gets a random spell from the number and then prints it
    spell = get_random_spell(spells)
    print(spell)

    
main()