import string

def decrypt_caesar(text: str, shift: int):
    alphabets = string.ascii_lowercase
    upperCaseAlphabets = string.ascii_uppercase
    
    converted = ""
    index = None
    
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
            
    print(converted)
    
                
#main function
def main():
    user_input = input("Enter a caesar cipher to decrypt: ")
    # call the decrypt ceasar function and pass the user_input and 3 in the parameters
    decrypt_caesar(user_input, 3)
    

#main function call
main()