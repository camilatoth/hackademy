def read_file(file_name):
	my_file = open(file_name)
	file_content = my_file.readlines()
	clean_content = []

	for line in file_content:
		clean_line = line.strip()

		if clean_line != "":
			clean_content.append(line.strip())

	my_file.close()

	return clean_content


def compare_favs(me_file, you_file):
	me_favs = read_file(me_file)
	you_favs = read_file(you_file)

	if me_favs == you_favs:
		print "We like the same food!"
	else:
		print "We don't like the same food!"

compare_favs('Camila_favfood.txt', 'Tiago_favfood.txt')
