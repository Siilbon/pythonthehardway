from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0, 0)
	print f.readline
	print len(f.readline)+1
	f.seek(len(str(f.readline))+1, 0)
	
def print_a_line(line_count, f):
	i = 0
	while i < line_count + 1:
		print i,">", f.readline(),
		i += 1
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"


print_a_line(2, current_file)


