#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
string_letters = "".join(letters)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
string_numbers = "".join(numbers)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
string_symbols = "".join(symbols)

print("Welcome to the PyPassword Generator!\nBased on your wants, we will create an unbreakable password.\nFirst, we need your input in numbers as to what type of symbols you want to have and in what quantity, and then we will randomly select these characters\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
long = nr_letters + nr_symbols + nr_numbers
print(f"Your password will be {long} characters long")


let = "".join(random.choice(string_letters) for i in range(nr_letters))
sym = "".join(random.choice(string_symbols) for i in range(nr_symbols))
num = "".join(random.choice(string_numbers) for i in range(nr_numbers))
ordered = let + sym + num


shuffled = "".join(random.sample(ordered, len(ordered)))
print(f"Here's your fabulous randomized password, anon:\n{shuffled}")
        