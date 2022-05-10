def odd_even(num):
	if num % 2 == 0:
		return "even"
	else:
		return "odd"
		
num = int(raw_input("give no "))
print odd_even(num)
