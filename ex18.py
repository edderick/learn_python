# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok, that *args is silly, we can just do
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument
def print_one(arg):
    print "arg: %r" % arg

# And this takes none
def print_none():
    print "I got nothing!"

print_two("Edward", "Seabrook")
print_two_again("Edward", "Seabrook")
print_one("FIRST!")
print_none()
