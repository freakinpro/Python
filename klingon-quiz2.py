CONSONANTS = ['b', 'ch', 'D', 'gh', 'H', 'j', 'l', ' m',
              'n', 'p', 'q', 'Q', 'r', 'S', 't', 'v', 'w', 'y', "'"]


def load_klingon():
    translated = []
    klingon = []
    try:
        #open file in read mode
        f = open("E:\klingon-english.txt", "r")
        #read file lines
        lines = f.readlines()
        #for each line split the klingon word and the english word and store them in two parallel lists.
        for line in lines:
            split = line.split("|")
            klingon.append(split[0].strip())
            translated.append(split[1].strip())
            #return the two lists.
        return (klingon, translated)
    except:
        print("Error loading the file klingon-english.txt")
        return (None, None)


def get_klingon_from_consonant(consonant, klingon_words):
    # returns the index of the found
    for i, word in enumerate(klingon_words):
        if consonant == word[0:len(consonant)]:
            return i
    return -1

#to check if consonent exisits in the CONSONENTS(LIST)
def does_consonant_exist(consonant):
    for cons in CONSONANTS:
        if cons == consonant:
            return True
    return False


def main():
    #get the two lists from the function
    klingon, english = load_klingon()
    if klingon == None or english == None:
        return -1
    consonant_found = False
    while not consonant_found:
        consonantInput = input("Choose a consonant: ")
        #check if correct consonent is found so change the consonent_found to True
        consonant_found = does_consonant_exist(consonantInput)
        #if consonent is incorrect so execute this statement
        if not consonant_found:
            print("Not Valid, Try again")
    
    
    found_index = get_klingon_from_consonant(consonantInput, klingon)
    print(f"Please translate {klingon[found_index]} into english")
    translated = input("")
    if translated == english[found_index]:
        print("Correct")
    else:
        print(
            f"Sorry you're wrong! The correct answer is {english[found_index]}")


main()