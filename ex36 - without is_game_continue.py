from sys import exit


def start():
	print("You don't remember anything. You are fallen.")
	print("You don't know anywhere to go but the path ahead.")
	print("You begin to step forward into the forest...")
	# to Chest zone
	got_chest_key = chest()
	# to Crow zone
	got_crow_key = crow()
	# to The Great Wall
	great_wall()

	# Good ending?
	print("Game over.")
	exit(0)

# The Chest zone
def chest():
	"""Chest on the way, containing a Key to open Treasure room's door"""

	print("You see a shiny chest lying near a bush ahead.")
	print("Who knows what valuable stuff it would contain?")

	# Chest Key taken?
	chest_key_obtained = False

	while not chest_key_obtained:
		# Repeated menu
		print("What do you do next?")
		print("1. Examine")
		print("2. Open chest")
		print("3. Leave the chest alone.")

		chest_choice = input("> ")
	
		if chest_choice == "1":
			print("\n================================================")
			print("You look carefully at the lock area of the chest.", end=' ')
			print("It is rusted badly. \nAnd very FRAGILE.")
			print("================================================\n")
			
		elif chest_choice == "2":
			chest_key_obtained = open_chest()
		else:
			print("Quit too soon?")
			dead("You died of giving up your purpose.")
	# Got the key
	return chest_key_obtained


def open_chest():
	print("Alright! Let's open this chest.")
	
	while True:
		# Repeated menu
		print("So how will you open it?")		
		print("1. Kick the chest hard!")
		print("2. Cast a spell to open the chest.")
		print("3. Give up.")

		open_choice = input("> ")
	
		if open_choice == "1":
			print("\n================================================")
			print("You kicked the chest hard!! BANG!!")
			print("The lock area is heavily damaged and the chest is wide open.")
			print("You found an amazing purple diamond. And a mysterious key.\n")
			print("================================================\n\n")
			return True

		elif open_choice == "2":
			print("\n================================================")
			print("Avada Kedavra!!")
			print("* The chest remains intact. And your smile disappeared.")
			print("================================================\n\n")
			
		elif open_choice == "3":
			print("Quit too soon?")
			dead("You died of giving up your purpose.")
		else:
			print("\n================================================")
			print("You look around. The peaceful atmosphere calms you down.")
			print("================================================\n\n")
	
# The Crow zone
def crow():
	print("After leaving the chest, you continue to the path ahead.")
	print("You see a strange short tree, with a white crow on the longest branch.")
	print("The crow is holding a shiny key in its mouth.")

	# So lan pham sai lam cho phep (max: 3)
	crow_false_attempt = 0

	while True:
		# Repeated menu
		print("What do you do next?")
		print("1. Look at the crow")
		print("2. Scare the crow off.")
		print("3. Show the crow your purple diamond.")

		crow_choice = input("> ")
	
		if crow_choice == "1":
			print("\n================================================")
			print("You look at the crow. The crow looks back at you. In silence.")
			print("================================================\n\n")
			print("\nYou feel painful in your intestines, as if something wants to get out!")
			print("You shouldn't have stared at the crow from the beginning.")
			crow_false_attempt += 1
			mistake_count(crow_false_attempt)
		elif crow_choice == "2":
			print("The crow flies away, with the shiny key still in his mouth.")
			print("Damn it! The key must have been useful later!")
			print("Now you lost it forever!")
			crow_false_attempt += 2
			mistake_count(crow_false_attempt)
			return False
		elif crow_choice == "3":
			print("The crow rushes into your hand to grab the purple diamond.")
			print("He flies away to the sky, left the shiny key fall to the grass.")
			print("You pick up the key.\n\n")
			return True

# The Great Wall
def great_wall():
	print("You stand before a very high and sturdy wall.")
	print("The only way through the Great Wall is a locked door.")
	## An com xong viet tiep, nhung khong biet khi nao an com xong.
	

# A more painful dead.
def mistake_count(number):	
	if number >= 3:
		dead("Your intestines blow up, and a giant centipede runs out from it.")


# Character dead -> End game
def dead(reason):
	print(reason, "Good game!")
	exit(0)


# Begin game
start()
