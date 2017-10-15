def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d slices of cheese!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print"Or, we can use variables from our script:"

amount_of_cheese = 25
amount_of_crackers = 35

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can also do some math:"
cheese_and_crackers(10+20, 5+6)


print "And we can combine the two:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

amount_of_cheese = int(raw_input("Or I can just ask you, how much cheese?"))
amount_of_crackers = int(raw_input("Or I can just ask you, how many crackers?"))
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
