from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "copying from %s to %s" % (from_file, to_file);

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
