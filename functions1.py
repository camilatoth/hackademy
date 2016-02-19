name = raw_input("What's your name?")
color = raw_input("What's your favourite color?")
hobby = raw_input("What's your favourite hobby?")
movie = raw_input("What's your favourite movie?")

def print_survey_results(name, color, hobby, movie): 

	print " %s 's favorite color is %s." % (name, color)

	print " %s 's favorite hobby is %s." % (name, hobby)

	print " %s 's favorite movie is %s." % (name, movie)

print_survey_results(name, color, hobby, movie)


#Write a function called print_survey_results that takes in four arguments: name, color, hobby, movie. 
#The print_survey_results function should print:
#[name]’s favorite color is [color].
#[name]’s favorite hobby is [hobby].
#[name]’s favorite movie is [movie].
#Call print_survey_results with the name, color, hobby, and movie variables as arguments.
#Run your survey.py file. What happens?
#Add parameters to print_survey_results for the two questions you made up. 
#Call print_survey_results with arguments for those new parameters.
#Run your survey.py file to make sure it works.








