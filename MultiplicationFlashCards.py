import random
from datetime import datetime


greeting_messages = ['Hi!']
right_answer_messages = ['Freaking awesome!  You got it right, I knew you could do it!!!']
wrong_answer_messages = ['Oops! Either you got the wrong answer, or Daddy didn\'t code this right! Let\'s try another one...']

level1_base = [0, 1, 2, 5, 10]
level2_base = [0, 1, 2, 4, 5, 10, 11]
level3_base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
common_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print('\n\n')
name = input('Hello, thanks for wanting to play Daddy\'s super amazing multiplication game!!!\n\nPlease type your name:\t')
# name = 'maddie'

if str.lower(name) == 'maddie':
	pass
else:
	print("\nEither you're trying to trick me, OR you spelled you're name wrong!  I'm going to call you Maddie McStinkerButt for now!",
		"anyway! :-)")
	name = 'Maddie McStinkerButt'


keep_playing = 'y'

while keep_playing == str.lower('y'):
	right = []
	wrong = []
	total = []

	f = open('Maddie multiplaction results.txt', 'a+')
	level = input('What level would you like to play? (Please type 1, 2, or 3 and then press enter:\t')
	# level = 1
	if int(level) == 1:
		print('OK, ' + str.title(name) + ', let\'s get started on Level ' + str(level) + '.\n')
		print('10 problems coming your way, let\'s get started!!!')
		# try:
		start = datetime.now()
		starttime = start.strftime('%Y-%m-%d, %H:%M:%S')
		f.write(starttime + '\n')
		for i in range(10):
			num1 = level1_base[random.randint(0,(len(level1_base)-1))]
			num2 = common_numbers[random.randint(0,(len(common_numbers)-1))]
			answer = num1*num2
			problem = 'What is ' + str(num1) + ' x ' + str(num2) + ' ?\t'
			print(problem)
			x = input('\n')
			if int(x) == int(answer):
				print(str(right_answer_messages) + '\n')
				right.append(i)
				f.write('Problem ' + str(i) +': ' + problem + '\tCorrect answer is ' + str(answer) + '.  Your answer was '+ str(x) + '.  CORRECT\n')
			else:
				print(str(wrong_answer_messages) + '\n')
				wrong.append(i)
				f.write('Problem ' + str(i) +': ' + problem + '\tCorrect answer is ' + str(answer) + '.  Your answer was '+ str(x) + '.  WRONG\n')

			total.append(i)
		end = datetime.now()
		duration = end - start
		time_message = 'Total time to answer 10 problems: ' + str(duration) + ' seconds.\n'
		accuracy = 'You answered ' + str(len(right)) + ' out of 10 questions correctly.\n'
		linebreak = '\n ################################################ \n\n'

		print(time_message)
		print(accuracy)
		print(linebreak)
		f.write(time_message)
		f.write(accuracy)
		f.write(linebreak)

		
		keep_playing = input('Do you want to play again? (Type y or n and then press enter)')
	elif int(level) == 2:
		print('OK, ' + str.title(name) + ', let\'s get started on Level ' + str(level) + '.\n')
		print('10 problems coming your way, let\'s get started!!!')
		# try:
		start = datetime.now()
		starttime = start.strftime('%Y-%m-%d, %H:%M:%S')
		f.write(starttime + '\n')
		for i in range(10):
			num1 = level2_base[random.randint(0,(len(level2_base)-1))]
			num2 = common_numbers[random.randint(0,(len(common_numbers)-1))]
			answer = num1*num2
			problem = 'What is ' + str(num1) + ' x ' + str(num2) + ' ?\t'
			print(problem)
			x = input('\n')
			if int(x) == int(answer):
				print(str(right_answer_messages) + '\n')
				right.append(i)
				f.write('Problem ' + str(i) +': ' + problem + '\tCorrect answer is ' + str(answer) + '.  Your answer was '+ str(x) + '.  CORRECT\n')
			else:
				print(str(wrong_answer_messages) + '\n')
				wrong.append(i)
				f.write('Problem ' + str(i) +': ' + problem + '\tCorrect answer is ' + str(answer) + '.  Your answer was '+ str(x) + '.  WRONG\n')

			total.append(i)
		end = datetime.now()
		duration = end - start
		time_message = 'Total time to answer 10 problems: ' + str(duration) + ' seconds.\n'
		accuracy = 'You answered ' + str(len(right)) + ' out of 10 questions correctly.\n'
		linebreak = '\n ################################################ \n\n'

		print(time_message)
		print(accuracy)
		print(linebreak)
		f.write(time_message)
		f.write(accuracy)
		f.write(linebreak)

		
		keep_playing = input('Do you want to play again? (Type y or n and then press enter)')
		# except Exception as e:
		# 	print(e)
		# 	f.write("An error occurred: " + str(e))
		# 	print("Uh oh, an error occurred.  Go ask Daddy for help!!! :-( ")

		f.close()

	elif int(level) == 3:
		print('OK, ' + str.title(name) + ', let\'s get started on Level ' + str(level) + '.\n')
		print('10 problems coming your way, let\'s get started!!!')
		# try:
		start = datetime.now()
		starttime = start.strftime('%Y-%m-%d, %H:%M:%S')
		f.write(starttime + '\n')
		for i in range(10):
			num1 = level3_base[random.randint(0,(len(level3_base)-1))]
			num2 = common_numbers[random.randint(0,(len(common_numbers)-1))]
			answer = num1*num2
			problem = 'What is ' + str(num1) + ' x ' + str(num2) + ' ?\t'
			print(problem)
			x = input('\n')
			if int(x) == int(answer):
				print(str(right_answer_messages) + '\n')
				right.append(i)
				f.write('Problem ' + str(i) +': ' + problem + '\tCorrect answer is ' + str(answer) + '.  Your answer was '+ str(x) + '.  CORRECT\n')
			else:
				print(str(wrong_answer_messages) + '\n')
				wrong.append(i)
				f.write('Problem ' + str(i) +': ' + problem + '\tCorrect answer is ' + str(answer) + '.  Your answer was '+ str(x) + '.  WRONG\n')

			total.append(i)
		end = datetime.now()
		duration = end - start
		time_message = 'Total time to answer 10 problems: ' + str(duration) + ' seconds.\n'
		accuracy = 'You answered ' + str(len(right)) + ' out of 10 questions correctly.\n'
		linebreak = '\n ################################################ \n\n'

		print(time_message)
		print(accuracy)
		print(linebreak)
		f.write(time_message)
		f.write(accuracy)
		f.write(linebreak)

		
		keep_playing = input('Do you want to play again? (Type y or n and then press enter)')
		

	else:
		print("\n\nI'm sorry, I know I'm just a computer, but I don't think you typed a 1, 2, or 3.")
		print("\nPlease try again")
	
print('Thanks for playing!!!  Goodbye!')
