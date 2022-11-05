
def main():
  charName = input("Enter Character Name: ")
  charAge = int(input("Enter Character Age: "))


  frodo_age = 51
  gollum_age = 589
  
  #For character age smaller than frodo and gollum
  if (charAge < frodo_age and charAge < gollum_age):
    print(f"{charName} is {charAge} years old, and they are younger than Frodo and Gollum.")    
  #For character age greater than frodo but smaller than gollum
  elif (charAge > frodo_age and charAge < gollum_age):
    print(f"{charName} is {charAge} years old, and they are older than Frodo but younger than Gollum.")
  #for character age older than both frodo and gollum
  else:
    print(f"{charName} is {charAge} years old, and they are older than Gollum and Frodo.")
    
  
#call main function
main()