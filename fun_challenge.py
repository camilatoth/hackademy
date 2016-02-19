def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'
do_twice(print_spam)		


def do_twice(f, value):
	f()
	f()

def print_twice():
	print 'i am a spam'
do_twice(print_twice, print_twice)
