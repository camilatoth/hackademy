def prime_number(number):

	for i in range(2,number):
		if number % i == 0:
			return False

	return True


my_number = int(raw_input("Choose a number: "))

if prime_number(my_number):
	print "This is a prime number!"

else:
	print "This is not a prime number."
