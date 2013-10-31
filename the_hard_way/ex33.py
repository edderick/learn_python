def add_num(i, l):
	print "At the top i is %d" % i
	l.append(i)

	i += 1
	print "Numbers now: ", l
	print "At the bottom i is %d" % i
	
	return i

i = 0 
numbers = []

for i in range(1, 6):
	i = add_num(i, numbers)

print "The numbers: "

for num in numbers:
	print num
