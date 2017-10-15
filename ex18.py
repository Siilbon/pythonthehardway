#this one is like your scripts with argv
def print_sev(*karl):
	print "args: %r" % (karl,)
	
#ok, that *args is actually pointless we just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
#this one takes no arguments
def print_none():
	print"I got nothin'."
	

print_sev("Zed", "Shaw", "Woah, it worked!!!", "fuck", 5, 7); print_two_again("Karl", "Siil")

print_one("First!")
print_none()
