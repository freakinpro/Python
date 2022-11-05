# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def Mmmm():
    user_input = input("What is the tasty thing?")
    print("Mmm.... " + user_input + "!")
# Press the green button in the gutter to run the script.

def chalkBoard():
    user_input = input()
    number = int(input())

    print((user_input + " ") * number)

def temperature():
    c = int(input())

    f = (c * 9 / 5) + 32

    print(f"{c} degrees in Canada would be {f} degrees in Springfield. D'oh!")

def episodeProblem():
    user_input = input();
    length = len(user_input)
    s = user_input.find("_")
    season = user_input[0: s]
    slen = len(season)
    seasonNum = season[1: slen]
    e = user_input.find("_", s + 1)
    episode = user_input[s + 1: e]
    eplen = len(episode)
    episodeNum = episode[1: eplen]
    epName = user_input[e + 1: length]

    print(f"Season {seasonNum}, Episode {episodeNum}: {epName} (The Simpsons)")

episodeProblem()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
