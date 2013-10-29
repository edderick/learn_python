from sys import argv

script, filename = argv

print "We're going to ease %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line = []

for i in range(1, 4):
    line.append(raw_input("line %d: " % i))

print "I'm going to write these to the file."

for l in line: 
    target.write("%s\n" % l)

print "And finally, we close it."
target.close()
