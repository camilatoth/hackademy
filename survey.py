name = raw_input("What's your name?")
color = raw_input("What's your favourite color?")
hobby = raw_input("What's your favourite hobby?")
movie = raw_input("What's your favourite movie?")

def print_survey_results(name, color, hobby, movie): 

	print " %s 's favorite color is %s." % (name, color)

	print " %s 's favorite hobby is %s." % (name, hobby)

	print " %s 's favorite movie is %s." % (name, movie)

print_survey_results(name, color, hobby, movie)










