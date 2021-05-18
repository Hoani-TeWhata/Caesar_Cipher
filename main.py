#This is my menu function menu to get the menu function 
def menu ():
  print("[1] Encrypt")
  print("[2] Decrypt")
  print("[0] Exit Program")
#This makes it so the user will have to choose what they want before it the code is started 
def my_introduction(fname):
  print("Ceasar Cipher Game")
  print("Welcome ", fname, "\n")

#My introduction to my game
string_input = input("Enter your name: ")
my_introduction(string_input)
menu()

option = int(input("enter your option: ")) 
#This is my option function, this is were the users chooses what they want to do 
while option != 0:
  #This while option makes the code loop until the '0' is choosen when the option function is active 
 
  if option == 1:
#This option function means if the option is eqaul to '1' then it run the code that has been inputed into it.
   alphabets = 'abcdefghijklmnoqprstuvwxyz'
#This is just showing what alpahbet is the code of moving the characters
   string_input = input("Enter your message: ")
   key = int(input("Enter your key: "))
#This function is asking for the word and the movement they want the letters to move
   n = len(string_input)
#this is taking the string input which is the message that you want Encrypt or Decrypt
   string_output = ""
#After moveing the letters this is where it will print 
   for i in range (n):
     character = string_input[i]
     location = alphabets.find(character)
     new_location = (location + key) % 26
     print(character, location, new_location)
     string_output += alphabets[new_location]

     print(string_output)
#This code is taking every Character individualy and moving them to the number of times the key the user inputed. It also shows the loaction of the character and the outcome e.g (A=1 Key=2 1+2 A=3 and the A turns into a C) it goes through this process for all of them 
   print ("Encrypt has been called. ")
  #Then after showing the outcome of Encrypted message is tells you that you choose Ecryption
  elif option == 2:
    #Since we have 0-2 option if the user choose 2 then it will use the code that has been inputed under this option
   alphabets = 'abcdefghijklmnoqprstuvwxyz'
#This is just showing what alpahbet is the code of moving the characters
   string_input = input("Enter your message:  ")
   key = int(input("Enter your key: "))
#This function is asking for the word and the movement they want the letters to move
   n = len(string_input)
#this is taking the string input which is the message that you want Encrypt or Decrypt
   string_output = ""
#After moveing the letters this is where it will print
   for i in range (n):
     character = string_input[i]
     location = alphabets.find(character)
     new_location = (location - key) % 26
     print(character, location, new_location)
     string_output += alphabets[new_location]
     
     print(string_output)
#This code is taking every Character individualy and moving them to the number of times the key the user inputed. It also shows the loaction of the character and the outcome e.g (A=1 Key=2 1-2 A=3 and the A turns into a Y) it goes through this process for all of them
   print("Decrypt has been called")
  #Then after showing the outcome of Encrypted message is tells you that you choose Decryption
  else:
   print("Invalid option") 
#If they didnt choose 0-2 then it will print an error message telling them this is an Invalid Option
  menu()
  option = int(input("Enter your option: ")) 
  #Having this printed again at the bottom makes sure it loops again will not until the option '0' is choosen to end the program 

print("End of Program")
 #This just prints a message that when the sure chooses '0' to give them a farewell 


