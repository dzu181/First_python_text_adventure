from sys import exit

def start():
	print("You don't remember anything. You are fallen.")
	print("You don't know anywhere to go, but the path ahead.")
	print("You begin to step forward into the forest...")
	# Game continue or quit
	global is_game_continue
	while is_game_continue:
		chest()
		is_game_continue = False

	print("Game over.")
	exit(0)


def chest():
	"""Chest on the way, containing a Key to open Treasure room's door"""

	# welcome message
	print("You see a shiny chest lying near a bush ahead.")
	print("Who knows what valuable stuff it would contain?")
	print("What do you do next?")
	print("1. Examine")
	print("2. Open chest")
	print("3. Leave the chest alone.")
	
	# Chest Key taken?
	key_obtained = False

	while is_game_continue and not key_obtained:
		chest_choice = input("> ")
	
		if chest_choice == "1":
			print("\n================================================")
			print("You look carefully at the lock area of the chest.", end=' ')
			print("It is rusted badly. \nAnd very FRAGILE.")
			print("================================================\n")
			
		elif chest_choice == "2":
			key_obtained = open_chest()
		else:
			print("Quit too soon?")
			dead("You died of giving up your purpose.")


def open_chest():
	print("Alright! Let's open this chest.")
	print("1. Kick the chest hard!")
	print("2. Cast a spell to open the chest.")
	print("3. Give up.")

	while True:
		open_choice = input("> ")
	
		if open_choice == "1":
			print("You kicked the chest hard!! BANG!!")
			print("The lock area is heavily damaged and the chest is wide open.")
			print("You found an amazing purple diamond. And a mysterious key.")
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
	
# Character dead -> End game
def dead(reason):
	print(reason, "Good game!")
	exit(0)

# Global CONTINUE status
is_game_continue = True
# Begin game
start()
