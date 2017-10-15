from sys import argv
prompt = "> "

script, filename = argv

txt = open(filename)

print "Here's you file %r" % filename
print txt.read()
txt.close()

print "ype the filename again,"
file_again = raw_input(prompt)

txt_again = open(file_again)

print txt_again.read()
txt_again.close()