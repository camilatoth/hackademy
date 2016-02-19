def add_list(shopping_list, item):
	shopping_list.append(item)
	return shopping_list

def count_similar_item(shopping_list, item):
	count = shopping_list.count(item)

	if count >= 2:
		shopping_list.remove(item)

	return shopping_list
		
def sort_list(shopping_list):
	shopping_list.sort()
	return shopping_list

def len_list(shopping_list):
	return len(shopping_list)


my_list = raw_input("What's in your shopping list? ").split(',')
print my_list

item = raw_input("What would you like to add to your shopping list? ")
my_list = add_list(my_list, item)
print my_list

my_list = count_similar_item(my_list, item)
print my_list

my_list = sort_list(my_list)
print my_list
