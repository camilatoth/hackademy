def count_name_letters(name):

	num_letters = {}

	for letter in name:
		if num_letters.has_key(name):
			num_letters[letter] += 1

		else:
			num_letters[letter] = 1

	return num_letters	

print count_name_letters("Tiago Motta Jorge")