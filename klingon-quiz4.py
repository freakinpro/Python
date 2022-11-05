from random import randint
CONSONANTS = ['b', 'ch', 'D', 'gh', 'H', 'j', 'l', ' m',
              'n', 'p', 'q', 'Q', 'r', 'S', 't', 'v', 'w', 'y', "'"]

#loading file from directory and separating the klingon and english words in 2 lists.
def load_klingon():
    translated = []
    klingon = []
    try:
        f = open("E:\klingon-english.txt", "r")
        lines = f.readlines()
        for line in lines:
            split = line.split("|")
            klingon.append(split[0].strip())
            translated.append(split[1].strip())
        return (klingon, translated)
    except:
        print("Error loading the file klingon-english.txt")
        return (None, None)

#for cbecking if  the answer is correct
def get_klingon_from_consonant(consonant, klingon_words):
    # returns the index of the found
    for i, word in enumerate(klingon_words):
        if consonant == word[0:len(consonant)]:
            return i
    return -1

#function for confirming if input is present in CONSONENTS
def does_consonant_exist(consonant):
    for cons in CONSONANTS:
        if cons == consonant:
            return True
    return False

#function for getting a hint when the answer is false.
def get_hint(english, is_random=False):
    starred = english[0]
    starred += "*"*(len(english)-2)
    starred += english[-1]
    #if is_random is true
    #makes a list and gets random value from randint function and replaces the letter at that index
    if is_random:
        starred_list = list(starred)
        
        rand_index = randint(1, len(starred)-2)
        starred_list[rand_index] = english[rand_index]
        starred = "".join(starred_list)
    #return the hint
    return starred


def main():
    klingon, english = load_klingon()
    if klingon == None or english == None:
        return -1
    consonant_found = False
    while not consonant_found:
        consonantInput = input("Choose a consonant ")
        consonant_found = does_consonant_exist(consonantInput)

        if not consonant_found:
            print("Not Valid, Try again")

    found_index = get_klingon_from_consonant(consonantInput, klingon)
    print(f"Please translate {klingon[found_index]} into english")
    #no of attempts left
    n_attempts = 2
    #current attempt
    curr_attempt = 1
    translated_correctly = False
    translated = input("")
    #while translated_correctly = false and current attempts are less than or equal to number of attempts left.
    while not translated_correctly and curr_attempt <= n_attempts:
        
        #if input is correct so print correct and terminate the loop
        if translated == english[found_index]:
            translated_correctly = True
            print("Correct")
        else:
            #if input is not correct so increment the curr_attempt and keep running the loop
            hint = get_hint(english[found_index], is_random = curr_attempt == 2)
            print(
                f"Sorry you're wrong! Hint {hint}")
            translated_correctly = False
            translated = input("")

        curr_attempt += 1

    
    if translated != english[found_index]:
        print(f"Sorry you're Wrong! The Correct answer is {english[found_index]}")



main()