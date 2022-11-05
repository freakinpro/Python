CONSONANTS = ['b', 'ch', 'D', 'gh', 'H', 'j', 'l', ' m',
              'n', 'p', 'q', 'Q', 'r', 'S', 't', 'v', 'w', 'y', "'"]


def load_klingon():
    translated = []
    klingon = []
    try:
        f = open("klingon-english.txt", "r")
        lines = f.readlines()
        for line in lines:
            split = line.split("|")
            klingon.append(split[0].strip())
            translated.append(split[1].strip())
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


def does_consonant_exist(consonant):
    for cons in CONSONANTS:
        if cons == consonant:
            return True
    return False


def get_hint(english):
    starred = english[0]
    starred += ""(len(english)-2)
    starred += english[-1]
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
    n_attempts = 2
    curr_attempt = 1
    translated_correctly = False
    translated = input("")
    while not translated_correctly and curr_attempt <= n_attempts:

        if translated == english[found_index]:
            translated_correctly = True
            print("Correct")
        else:
            print(
                f"Sorry you're wrong! Hint {get_hint(english[found_index])}")
            translated_correctly = False
        translated = input("")

        curr_attempt += 1

    if translated != english[found_index]:
        print(
            f"Sorry you're Wrong! The Correct answer is {english[found_index]}")
    else:
        print("Correct")


main()