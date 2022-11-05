import string

def decrypt_caesar(text: str, shift: int):
    alphabets = string.ascii_lowercase
    upperCaseAlphabets = string.ascii_uppercase
    
    converted = ""
    
    for letter in text:
        #checks if letter is upper case or lower case
        if letter.isupper():
            #checks if letter is found then gets the position of the letter and then subtracts 3 from it
            if letter in upperCaseAlphabets:
                position = upperCaseAlphabets.find(letter)
                new_position = (position - shift) % 26 #gets the modulo of the subtracted number which is the new position of the letter
                new_character = upperCaseAlphabets[new_position]            
                converted += new_character
        #for lower case letters
        elif letter.islower():    
            if letter in alphabets:
                position = alphabets.find(letter)
                new_position = (position - shift) % 26
                new_character = alphabets[new_position]
                converted += new_character
        else:
            converted += letter  #if any space or any other letter that doesnt match the alphabets is printed as it is
            
    print(f"Caesar cipher: {converted}")

def decrypt_atbash(text: str):
    alphabets = string.ascii_lowercase
    upperCaseAlphabets = string.ascii_uppercase
    
    converted = ""
    
    for letter in text:
        #checks if letter is upper case or lower case
        if letter.isupper():
            #checks if letter is found then gets the position of the letter and then subtracts 3 from it
            if letter in upperCaseAlphabets:
                position = upperCaseAlphabets.find(letter)
                new_position = (25 - position) #gets the modulo of the subtracted number which is the new position of the letter
                new_character = upperCaseAlphabets[new_position]            
                converted += new_character
        #for lower case letters
        elif letter.islower():    
            if letter in alphabets:
                position = alphabets.find(letter)
                new_position = (25 - position) 
                new_character = alphabets[new_position]
                converted += new_character
        else:
            converted += letter  #if any space or any other letter that doesnt match the alphabets is printed as it is    
            
    print(f"Atbash cipher: {converted}")
              
    
def decrypt_a1z26(text: str):
    alphabets = string.ascii_uppercase
    
    
    converted = ""
    # split the lines that have a white space
    lines = text.split()
    
    # looping through the lines
    for line in lines:
        # spliting the lines with a "-"
        data = line.split("-")
        # looping again
        for num in data:
            # checking if number is a digit or not
            if num.isdigit():
                # converting string to integer
                index = int(num)
                #making a new character from the index in the input. -1 is used because the index starts from 0
                new_char = alphabets[index-1]
                # adding the letter to the converted variable
                converted += new_char
            else:
                converted += num
        # adding space after each line or word
        converted += " "
            
    print(f"A1Z26 cipher: {converted}")
#main function
def main():
    user_input = input("Enter a text to decipher: ")
    print("\nLet's try all the methods we have:\n")
    # call all the 3 functions with the 
    decrypt_caesar(user_input, 3)
    decrypt_atbash(user_input)
    decrypt_a1z26(user_input)
    

#main function call
main()