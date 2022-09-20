import random


def fruits_game(fruits):
	
	correct_answer = fruits[random.randint(0,len(fruits)-1)]

	for i in range(3):
		print("Possible choises:\n")
		for fruit in fruits:
			print("- "+fruit+"\n")
		print("-"*10)
		answer = input("Your answer: ")
		
		if answer.lower() == correct_answer.lower():
			print("\n\n[+]Congratulations[+]")
			exit()
		else:
			if i == 2:
				pass
			else:
				print("[-]Try again[-]")
	print("\n\n\nYou Lost...the correct answer was {}".format(correct_answer))

def kitchen_game(kitchen_objects, correct=False):

	correct_answer = kitchen_objects[random.randint(0,len(kitchen_objects)-1)]

	for i in range(3):
		print("Possible choises:\n")
		for oobject in kitchen_objects:
			print("- "+oobject+"\n")
		print("-"*10)
		answer = input("Your answer: ")

		if answer.lower() == correct_answer.lower():
			print("\n\n[+]Congratulations[+]")
			exit()
		else:
			if i == 2:
				continue
			else:
				print("\n[-]Try again[-]\n")
	print("\n\n\nYou Lost...the correct answer was {}".format(correct_answer))

def animals_game(animals, correct=False):

	correct_answer = animals[random.randint(0,len(animals)-1)]
	
	for i in range(3):
		print("Possible choises:\n")
		for animal in animals:
			print("- "+animal+"\n")
		print("-"*10)
		answer = input("Your answer: ")

		if answer.lower() == correct_answer.lower():
			print("\n\n[+]Congratulations[+]")
			exit()
		else:
			if i == 2:
				continue
			else:
				print("[-]Try again[-]")
	print("\n\n\nYou Lost...the correct answer was {}".format(correct_answer))



def main():
	animals = ["tigre", "penguin", "lion", "shark", "parrot", "dog", "zebra"]
	kitchen_objects = ["knife", "fork", "pan", "stove", "plate", "cup", "spoon", "fridge"]
	fruits = ["banana", "orange", "strawberry", "lemon", "apple", "grape", "mango", "peach"]


	animal_g = "Guess the animal: "
	kitchen_object_g = "Guess the kitchen: "
	fruit_g = "Guess the animal: "


	choise = input("Which game do you wanna play ? \n\n[1]Animals\n[2]Kitchen Objects\n[3]Fruits\n\n==> ")

	if choise == "1":
		animals_game(animals) 
	elif choise == "2":
		kitchen_game(kitchen_objects) 
	elif choise == "3":
		fruits_game(fruits)
	else:
		print("Invalid choice")



if __name__ == "__main__":
	TRYS = 3
	main()