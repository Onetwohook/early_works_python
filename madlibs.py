import time

print "Welcome to a wacky story."


name = raw_input("Gimmie a name: ")
noun1 = raw_input ("And a noun: ")
noun2 = raw_input ("Another noun: ")
adj1 = raw_input ("And an adjective: ")
adj2 = raw_input ("Another adjective: ")
ver1 = raw_input ("I need a verb ending in ing: ")
ver2 = raw_input ("One more ing verb: ")

print "Great, lets see what nonsense story we can make!"

time.sleep(1)

print "One day,", name, "was looking at their", noun1
print "It was", adj1, "and", name, "liked to go", ver1, "with it"
print noun1, "was", ver1, "when it bumped into a", adj2, noun2
print "That's when", noun1,"and", noun2, "went", ver2
