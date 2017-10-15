name = "Karl Siil"
age = 23 # As of 5/15/2015
height = 71.0 # inches
weight = 215.0 #lbs
eyes = 'Brown'
teeth = 'white'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %r cm tall." % (height*2.54) #inches to cm
print "He's %d years old" % age
print "He's %r Kg heavy." % (weight*2.2) #lbs to kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "if I add %d, %d, and %d I get %d." % ( age, 
height, weight, age + height + weight)

