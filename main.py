def menu ():
  print("[1] Encrpty")
  print("[2] Decrpty")
  print("[0] Exit Program")

menu()
option = int(input("enter your option: ")) 

while option != 0:
  if option == 1:

   alphabets = 'abcdefghijklmnoqprstuvwxyz'

   string_input = input("Enter your message: ")
   key = int(input("Enter your key: "))

   n = len(string_input)

   string_output = ""

   for i in range (n):
     character = string_input[i]
     location = alphabets.find(character)
     new_location = (location + key) % 26
     print(character, location, new_location)
     string_output += alphabets[new_location]

    
     print(string_output)

   print ("Encrpty has been called. ")

  elif option == 2:
   #do option 2 stuff
   print("Decrpty has been called")
  else:
   print("Invaild option")
menu()
option = int(input("enter your option: ")) 

 
