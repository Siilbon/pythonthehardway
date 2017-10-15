from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit ctrl C (^C)"
print "Press enter to continue"

raw_input('> ?')

print "Opening the file..."
target = open(filename, "a+")

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"
target.write("%s\n%s\n%s" % (line1, line2, line3))
target.close()
print "The file is closed"