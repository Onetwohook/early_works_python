name = raw_input("Hello adventurer, what is your name? ")

print "So,", name, "the legends are true."

print """
A roaring dragon appears on the horizon
Before you know it, it is upon you.
You draw your staff. 
what do you do?"""

print "Do you: "
print "1. Raise your mighty staff aloft"
print "2. Brandish your staff in two hands like a club"
print "3. Hide, like the little wizard bitch you are"

staff = raw_input(">>> ")

if staff == "1":
	print "Lightning cackles from your staff."
	print "Do you unleash it?"
	print "1. yes"
	print "2. no"
	
	unleash = raw_input(">>> ")
	
	if unleash == "1":
			print "You shoot a fat bolt and it fucks the dragon right up!"
	elif unleash == "2":
			print "The lightning overwhelms you and you become THOR GOD OF THUNDER"
			print "Do you ascend to the mighty realm of gods?"
			print "1. Fucking right I do."
			print "2. No, I've got some stuff on that I can't miss."
		    
			god = raw_input(">>> ")
			
			if god == '1':
				print "The world is your plaything. You are a diety"
			elif god == "2":
				print "Who says no to that? You deserve to be dragon et"
			else:
				print "Oh sorry, got it wrong. You're just a punk. The lightning explodes you"
	else:
		print "The dragon gobbles you up. Bitch"

elif staff == "2":
	print "A tough guy, eh? You ready to homer the fucker."
	print "Do you: "
	print "1. Try and smash its skull in as it swoops past?"
	print "2. Use the club as a pole vault, launching you on its back?"
	
	homer = raw_input(">>> ")
		
	if homer == "1":
			print "That's pretty sweet, but your staff snaps in half."
			print "Wanna try jumping on top of it anyway?"
			print "1. Sure, let's ride this fuck"
			print "2. No, that looks scary."
			
			jump = raw_input(">>> ")
			
			if jump == "1":
				print "Fucking sweet dude, but the dragon eats you."
			elif jump == "2":
				print "Your broken stick is shit against a dragon. You get et"
		
	elif homer == "2":
			print "That's pretty sweet, but the dragon eats you"
			
	else:
			print "The dragon eats you"

elif staff == "3":
	print "A coward isn't the worst thing to be"
	print "So what now, pussy? "
	print "1. Run"
	print "2. Cry"
	print "3. Piss yourself"
	
	piss = raw_input(">>> ")
		
	if piss == "1":
			print "You can't; outrun a dragon, fucker. You get et"
	elif piss == "2":
			print "Your tears make your flesh taste sweeter to the dragon as he ets you"
	elif piss == "3":
			print "Dragons don't eat piss. Well done, this is the only way to survive!"
			
else:
	print "The dragon eats you, you stupid fuck."
