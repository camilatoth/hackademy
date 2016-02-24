def compare_favs(me_favs, you_favs):
	
	if me_favs == you_favs:
		print "We like the same food!"

	else:
		print "We don't like the same food!"


Camila_favs = ["sushi", "burguer", "pizza"]
Tiago_favs = ["sushi", "burguer", "pizza"]

compare_favs(Camila_favs, Tiago_favs)

Camila_favs = ["salad", "burritos", "steak"]
Tiago_favs = ["sushi", "burguer", "pizza"]

compare_favs(Camila_favs, Tiago_favs)

