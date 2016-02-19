def file_letters_count():
	lines = read_file_lines()
	num_letters = {}

	for line in lines:
		for letter in line:
			if num_letters.has_key(letter):
				num_letters[letter] += 1

			else:
				num_letters[letter] = 1

	return num_letters	


def read_file_lines():
	my_file = open('teachers_file.txt')
	file_lines = my_file.readlines()
	clean_lines = []
	for line in file_lines:
		clean_lines.append(line.strip())
	my_file.close()
	return clean_lines

print file_letters_count()