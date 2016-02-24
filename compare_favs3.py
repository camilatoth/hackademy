def compare_favs(my_list, your_list):
	
	for item in my_list:
		if item in your_list:
			print "We both like %s!" % (item)

Camila_favs = ["sushi", "burguer", "pizza"]
Tiago_favs = ["steak", "salad", "burguer"]

compare_favs(Camila_favs, Tiago_favs)



