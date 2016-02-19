def star(number):
	print number * " * "

def draw(number):
	i = 1
	while i <= number:
		star(number)
		i = i + 1

draw(4)
	

	
def draw_checkerboard_line(line_number):
	if line_number % 2 == 0:
		print " x o x o x o x o "
	else:
		print " o x o x o x o x "
	
def draw_checkerboard():
	for i in range(8):
		draw_checkerboard_line(i)
				
draw_checkerboard()
