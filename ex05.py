name = 'Edward JF Seabrook'
age = 21 # not a lie
height = 70 # inches
weight = 200 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Blond'

print "Let's talk about %s." % name
print "He is %d inches tall." % height
print "He is %d pounds heavy." % weight
print "Damn girl - dat's heavy."
print "He has %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s" % (teeth)

# This line is tricky, try to get it perf
print "If I add %d, %d, and %d I get %d" % (
    age, height, weight, age + height + weight)
