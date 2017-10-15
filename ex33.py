def count_func(number, inc):
	i = 1
	numbers = []
	for i in range(1, number + 1, inc):
		print "At the top i is %d" % i
		numbers.append(i)
		
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	print "the numbers: "

	for num in numbers:
		print num
	
number = input("How high do you want to count?")
inc = input("Increment by what number?")
count_func(number, inc)
