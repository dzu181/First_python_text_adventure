from sys import exit
import time
import webbrowser

from displayer import Displayer

# Global constants
MENU_DELAY: float = 0.5

displayer = Displayer()

def start():
	first_intro()
	# to Chest zone
	got_chest_key = chest()
	# to Crow zone
	got_crow_key = crow()
	# to The Great Wall
	great_wall(got_chest_key, got_crow_key)


# The Chest zone
def chest():
	displayer.display_text("You see a shiny chest lying near a bush ahead.")
	displayer.display_text("Who knows what valuable stuff it would contain?")

	chest_key_obtained = False

	while not chest_key_obtained:
		show_chest_menu()

		chest_choice = input("> ")
	
		if chest_choice == "1":
			displayer.display_text("You look carefully at the lock area of the chest.", end=' ')
			displayer.display_text("It is rusted badly. \nAnd very FRAGILE.")
			
		elif chest_choice == "2":
			chest_key_obtained = open_chest()
		elif chest_choice == "3":
			displayer.display_text("Quit too soon?")
			dead("You died of giving up your purpose.")
	# Got the key
	return chest_key_obtained

def open_chest():
	displayer.display_text("Alright! Let's open this chest.")
	
	while True:
		show_open_chest_menu()

		open_choice = input("> ")
	
		if open_choice == "1":
			displayer.display_text("You kicked the chest hard!! BANG!!")
			displayer.display_text("The lock area is heavily damaged and the chest is wide open.")
			displayer.display_text("You found an amazing purple diamond. And a mysterious key.\n")
			return True

		elif open_choice == "2":
			displayer.display_text("Avada Kedavra!!")
			displayer.display_text("* The chest remains intact. And your smile disappeared.")
			
		elif open_choice == "3":
			displayer.display_text("Quit too soon?")
			dead("You died of giving up your purpose.")
		else:
			displayer.display_text("You look around. The peaceful atmosphere calms you down.")
	
# The Crow zone
def crow():
	displayer.display_text("After leaving the chest, you continue to the path ahead.")
	displayer.display_text("You see a strange short tree, with a white crow on the longest branch.")
	displayer.display_text("The crow is holding a shiny key in its mouth.")

	# Number of Failed attempts (max: 1)
	crow_false_attempt = 0

	while True:
		show_crow_menu()

		crow_choice = input("> ")
	
		if crow_choice == "1":
			displayer.display_text("You look at the crow. The crow looks back at you. In silence.")
			displayer.display_text("\nYou feel painful in your intestines, as if something wants to get out!")
			displayer.display_text("You shouldn't have stared at the crow from the beginning.\n")
			crow_false_attempt += 1
			count_mistake(crow_false_attempt)
		elif crow_choice == "2":
			displayer.display_text("The crow flies away, with the shiny key still in his mouth.")
			displayer.display_text("Damn it! The key must have been useful later!")
			displayer.display_text("Now you lost it forever!")
			return False
		elif crow_choice == "3":
			displayer.display_text("The crow rushes into your hand to grab the purple diamond.")
			displayer.display_text("He flies away to the sky, left the shiny key fall to the grass.")
			displayer.display_text("You pick up the key.\n\n")
			return True

# The Great Wall
def great_wall(chest_key, crow_key):
	displayer.display_text("You leave the tree to continue your journey.")
	displayer.display_text("You stand before a very high and sturdy wall.")
	displayer.display_text("The only way through the Great Wall is a locked door.")
	displayer.display_text("You look into your pockets:")
	time.sleep(MENU_DELAY)
	if chest_key:
		displayer.display_text("-> You have the key from the shiny chest.")
	if crow_key:
		displayer.display_text("-> You have the key from the white crow.")
	
	# A surprise later - hidden choice
	wall_attempt = 0
	max_wall_attempt = 3

	while True:
		show_great_wall_menu()
		great_wall_choice = input("> ")

		if great_wall_choice == "1":
			if chest_key:
				displayer.display_text("You tried the Chest key, but the door won't open.")
				displayer.display_text("Try something else.")
			else:
				displayer.display_text("You don't have the Chest Key to use. So sad.")
				displayer.display_text("Try something else.")
		elif great_wall_choice == "2":
			if crow_key:
				displayer.display_text("You tried the Crow key, and the door is opened.")
				good_ending()
			else:
				displayer.display_text("You don't have the Crow Key! Remember something at the tree?")
				displayer.display_text("Try something else.")
		elif great_wall_choice == "3":
			displayer.display_text("You cry like a baby, your guts hate you.")
			displayer.display_text("But no one can help you now. Better be back.")

		wall_attempt +=1

		# Player rage mode. Destroy things!	(wall_attempt == 3)	
		if wall_attempt >= max_wall_attempt:
			displayer.display_text("Damn it! Here goes nothing!")
			kick_door()

def kick_door():
	## TODO list:
	# Make this a 100 HP door to kick until open, and win the game.
	displayer.display_text("You got super angry!! You tried anything but the door won't open!")
	displayer.display_text("You decide to stomp your feet towards the door until it cracks.")

	wall_hp = 100
	while wall_hp > 0:
		show_kick_door_menu(wall_hp)
		kicking = input("> ")
		if kicking == "1":
			displayer.display_text("Brahmmm!! The door vibrates strongly from your kick.")
			displayer.display_text("You have no idea you have this strength in you. The rage.")
			wall_hp -= 1
		elif kicking == "2":
			displayer.display_text("You enter another dimension, where nothing moves and awares.")
			webbrowser.open('https://bit.ly/41Wp0v8')
			displayer.display_text("Then, you are pushed back to your reality, in front of the Great Wall.")
			displayer.display_text("What the...?!")
			# Return to while loop in great_wall(), reset wall's HP
			return
		elif kicking == "3":
			displayer.display_text("It is never too late to correct our mistakes.")
			dead("Die! And reset the cycle.")
		else:
			displayer.display_text("Fuck! What do you want me to do??!?")

	displayer.display_text("The door is brokenly open. You see a big new road ahead of you.")
	good_ending()


def first_intro():
	displayer.display_text("You don't remember anything. You are fallen.")
	displayer.display_text("You don't know anywhere to go but the path ahead.")
	displayer.display_text("You begin to step forward into the forest...")

def dead(reason):
	displayer.display_text(reason, "Good game!")
	exit(0)

# A more painful dead.
def count_mistake(number):	
	if number >= 2:
		dead("Your intestines blow up, and a giant centipede runs out from it.")

def show_crow_menu():
	time.sleep(MENU_DELAY)
	displayer.display_text("What do you do next?")
	displayer.display_text("1. Look at the crow")
	displayer.display_text("2. Scare the crow off.")
	displayer.display_text("3. Show the crow your purple diamond.")

def show_open_chest_menu():
	time.sleep(MENU_DELAY)
	displayer.display_text("So how will you open it?")		
	displayer.display_text("1. Kick the chest hard!")
	displayer.display_text("2. Cast a spell to open the chest.")
	displayer.display_text("3. Give up.")

def show_chest_menu():
	time.sleep(MENU_DELAY)
	displayer.display_text("What do you do next?")
	displayer.display_text("1. Examine")
	displayer.display_text("2. Open chest")
	displayer.display_text("3. Leave the chest alone.")

def show_great_wall_menu():
	time.sleep(MENU_DELAY)
	displayer.display_text("How do you think about this wall??")
	displayer.display_text("1. Use Chest Key.")
	displayer.display_text("2. Use Crow Key.")
	displayer.display_text("3. Shout to the sky!")

def show_kick_door_menu(hp):
	time.sleep(MENU_DELAY)	
	displayer.display_text("The wall's HP is:", hp, "\n")
	displayer.display_text("Wanna kick the damn door?")
	displayer.display_text("1. Hell yeah!")
	displayer.display_text("2. ☌⟟⎐⟒ ⎍⌿")
	displayer.display_text("3. Give up.")	

def good_ending():
	time.sleep(MENU_DELAY)
	displayer.display_text("A new journey awaits you ahead.")
	displayer.display_text("TO BE CONTINUED...")
	exit(0)

# Begin game
start()
