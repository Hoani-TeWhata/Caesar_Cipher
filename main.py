
 
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

def main():
  choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): ")
  if choice == 1 
   Encryption()
  elif choice == 2 
   Decryption()
  else:
    print("Wrong Choice")



                                                                                                                                                                                                                                                                                                                                                                                               