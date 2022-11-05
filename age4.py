names = ["Frodo", 
         "Samwise", 
         "Gandalf", 
         "Legolas",
         "Gimli", 
         "Aragorn", 
         "Boromir", 
         "Merry", 
         "Pippin"]

ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]

#function for getting character age and checking if its not negative
def get_age():
  age = int(input("Enter characters age: "))
  if age < 0:
      print("Invalid age.")
      return -1
  return age
    

#for getting the characters name
def get_character_name():
    return input("Enter the character's name: ")

#function for displaying the characters, lower or higher
def print_list(names_list, name, age, compared):
    if len(names_list) > 0:
        print(f"{name} is {age} years old, and they are {compared} than", end="")

        for name in names_list:           
            if name != names_list[-1]:
                print(f" {name}", end=",")
            else:
                print(f" {name}", end=".")



#for printing characters greater than user
def print_higher(user_name, user_age):
    names_list = []
    for i, age in enumerate(ages):
        if age > user_age:
            names_list.append(names[i])

    print_list(names_list, user_name, user_age, "younger")

#for printing characters smaller than user
def print_lower(user_name, user_age):
    names_list = []
    for i, age in enumerate(ages):
        if age < user_age:
            names_list.append(names[i])

    print_list(names_list, user_name, user_age, "older")

#main function
def main():
    char_name = get_character_name()
    entered_age = get_age()

    # check if there is no character that exists with that name or if the age is invalid
    if entered_age == -1:
        return 0
    # find the lower and higher characters
    print("\nName: " + char_name)
    print_lower(char_name, entered_age)
    print()
    print_higher(char_name, entered_age)


#main function call
main()