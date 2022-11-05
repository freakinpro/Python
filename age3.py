
#main function
def main():
  #input character name
  charName = input("Enter Character Name: ")
  #input character age
  charAge = int(input("Enter Character Age: "))
  
  #hard-coded
  pippin_age = 29
  frodo_age = 51
  gollum_age = 589
  arwen_age = 2901

  #for age less than zero i.e. -1
  if (charAge < 0):
      print("Invalid Age")
  #for character age less than pippin, gollum, frodo, arwen
  elif (charAge < pippin_age and charAge < frodo_age and charAge < gollum_age and charAge < arwen_age):
      print(f"{charName} is {charAge} years old, and they are younger than Arwen, Gollum, Frodo, Pippin.")
  #for character age greater than pippin,frodo but less than gollum, arwen
  elif (charAge > pippin_age and charAge > frodo_age and charAge < gollum_age and charAge < arwen_age):
      print(f"{charName} is {charAge} years old, and they are older than Frodo, Pippin.")
      print(f"{charName} is {charAge} years old, and they are younger than Arwen, Gollum.")
  #for character age greater than pippin, but less than gollum, frodo, arwen
  elif (charAge > pippin_age and charAge < frodo_age and charAge < gollum_age and charAge < arwen_age):
      print(f"{charName} is {charAge} years old, and they are older than Pippin.")
      print(f"{charName} is {charAge} years old, and they are younger than Arwen, Frodo, Gollum.")
  #for character age greater than pippin, frodo and gollum but less than arwen
  elif (charAge > pippin_age and charAge > frodo_age and charAge > gollum_age and charAge < arwen_age):
      print(f"{charName} is {charAge} years old, and they are older than Pippin, Frodo, Gollum.")
      print(f"{charName} is {charAge} years old, and they are younger than Arwen.")
  #for character age greater than pippin, gollum, frodo, arwen
  elif (charAge > pippin_age and charAge > frodo_age and charAge > gollum_age and charAge > arwen_age):
      print(f"{charName} is {charAge} years old, and they are older than Arwen, Gollum, Frodo, Pippin.")
      

#main function call
main()