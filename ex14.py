from sys import argv

script, user_name = argv
bleh = "TELL ME: "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(bleh)

print "Where do you live %s?" % user_name
home = raw_input(bleh)

print "What kind of computer do you have?"
computer = raw_input(bleh)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is...
Also you have a %r computer.  Nice...
""" % (likes, home, computer)
