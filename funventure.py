from sys import exit
import random

def found_safety():
	print "You slam the door shut. There is a loaded gun on the table ahead."
	print "Do you shoot the monsters through the door or yourself?"
	
	next = raw_input("> ")
	if next == "shoot self":
		print "You put the gun in your mouth and pull the trigger. Finally, it's over"
	elif next == "shoot door":
		print "You pump rounds into the door. It makes no difference. They're coming."
	else:
		print "You slip the gun into your belt, ready to shoot the next fuck that turns up."
		
def slime_room():
	print "The walls are oozing with slime."
	print "The slime starts to\ttake shape."
	print "It is turning into a humanoid shape."
	print "Are you going mad?"
	
	next = raw_input("Give me a number between 1 and 10, I'll tell you if you're mad. ")
	number = random.randint(0, 10)
	
	if next < number:
		print "You are quite, quite mad."
	elif next == number:
		print "You are INSANE"
	else:
		print "You're sane as they come."
		found_safety()

def room_finder():
	print "You're in a dark room."
	
	next = raw_input("Left door or right door?")
	
	if next == "left":
		print "You find another strange room"
		slime_room()
	elif next == "right":
		print "Poor choice"
		horror_room()
	else:
		print "you slip and die for being a smartass"
	
def horror_room():
	print "A mighty eye that takes up and entire wall blinks."
	print "It is enormous, unimaginable."
	print "It seems to be waiting."
	print "Do you kick the eye or run through the door to the right?"
	
	next = raw_input("> ")
	
	if next == "kick":
		print "It wasn't an eye at all! It was a huge mouth that swallows you."
	elif next == "door":
		found_safety()
	else:
		slime_room()

room_finder()
