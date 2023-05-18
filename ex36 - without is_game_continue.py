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
	great_wall(got_chest_key, got_crow_key)

	# Good ending?
	print("Game over.")
	exit(0)

# The Chest zone
def chest():

	print("You see a shiny chest lying near a bush ahead.")
	print("Who knows what valuable stuff it would contain?")

	# Chest Key taken?
	chest_key_obtained = False

	while not chest_key_obtained:
		## Remind player of choices
		show_chest_menu()

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
		## Remind player of choices
		show_open_chest_menu()

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

	# Number of Failed attempts (max: 3)
	crow_false_attempt = 0

	while True:
		# Remind player of choices
		show_crow_menu()

		crow_choice = input("> ")
	
		if crow_choice == "1":
			print("\n================================================")
			print("You look at the crow. The crow looks back at you. In silence.")
			print("================================================\n\n")
			print("\nYou feel painful in your intestines, as if something wants to get out!")
			print("You shouldn't have stared at the crow from the beginning.\n")
			crow_false_attempt += 1
			count_mistake(crow_false_attempt)
		elif crow_choice == "2":
			print("The crow flies away, with the shiny key still in his mouth.")
			print("Damn it! The key must have been useful later!")
			print("Now you lost it forever!")
			return False
		elif crow_choice == "3":
			print("The crow rushes into your hand to grab the purple diamond.")
			print("He flies away to the sky, left the shiny key fall to the grass.")
			print("You pick up the key.\n\n")
			return True

# The Great Wall
def great_wall(chest_key, crow_key):
	print("You stand before a very high and sturdy wall.")
	print("The only way through the Great Wall is a locked door.")
	print("You look into your pockets.")
	## TODO list
	# Write a key_selection procedure: what key you have, try out the key.
	# Write a 100 HP wall, which you can kick until it opens.
	# Plus some surprises if too many same actions are repeated (Hidden action).
	if chest_key:
		print("You have the key from the shiny chest.")
	if crow_key:
		print("You have the key from the white crow.")
	
	# A surprise later - hidden choice
	wall_attempt = 0

	while True:
		# Remind player of choices
		show_great_wall_menu()
		great_wall_choice = input("> ")

		if great_wall_choice == "1":
			if chest_key:
				print("You tried the Chest key, but the door won't open.")
				print("Try something else.")
			else:
				print("You don't have the Chest Key to use. So sad.")
				print("Try something else.")
		elif great_wall_choice == "2:"
			if crow_key:
				print("You tried the Crow key, and the door is opened.")
				print("A new journey awaits you ahead.")
				print("TO BE CONTINUED...")
				exit(0)
			else:
				print("You don't have the Crow Key! Remember something at the tree?")
				print("Try something else.")
		elif great_wall_choice == "3":
			print("You cry like a baby, your guts hate you.")
			print("But no one can help you now. Better be back.")


		# Player rage mode. Destroy things!	(wall_attempt == 3)		
		wall_attempt +=1
		if wall_attempt == 3:
			print("Damn it! Here goes nothing!")
			kick_door()

def kick_door():
	
	## TODO list:
	# Make this a 100 HP door to kick until open, and win the game.
	pass



# A more painful dead.
def count_mistake(number):	
	if number >= 2:
		dead("Your intestines blow up, and a giant centipede runs out from it.")


# Character dead -> End game
def dead(reason):
	print(reason, "Good game!")
	exit(0)

def show_crow_menu():
	print("What do you do next?")
	print("1. Look at the crow")
	print("2. Scare the crow off.")
	print("3. Show the crow your purple diamond.")

def show_open_chest_menu():
	print("So how will you open it?")		
	print("1. Kick the chest hard!")
	print("2. Cast a spell to open the chest.")
	print("3. Give up.")

def show_chest_menu():
	print("What do you do next?")
	print("1. Examine")
	print("2. Open chest")
	print("3. Leave the chest alone.")

def show_great_wall_menu():
	print("How do you think about this wall??")
	print("1. Use Chest Key.")
	print("2. Use Crow Key.")
	print("3. Shout to the sky!")

# Begin game
start()
