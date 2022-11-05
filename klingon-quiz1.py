def main():
    #for opening the file in read mode
    file = open("D:\klingon-english.txt","r")

    #temporary variable
    specificLine = "";

    #for finding line 3 in file and storing it in temporary variable initialized above
    for i, line in enumerate(file):
        if i == 2:  
            specificLine = line.strip()

            #for separating the klingon word from the english word and storing it in a variable.
    x = specificLine.find("|");
    klingonText = specificLine[0:x]

    user_input = input("Enter the word computer in klingon language: ")
    #conditional statement for checking if the user has entered the correct word or not
    if user_input == klingonText:
        print("Correct!")
    else:
        print(f"Sorry, you're wrong! \nThe correct answer is {klingonText}.")
        
#main function call:
main()



