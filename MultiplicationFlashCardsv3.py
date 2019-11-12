import random
from datetime import datetime


greeting_messages = ['Hi!']
right_answer_messages = ['Freaking awesome!  You got it right, I knew you could do it!!!', 
						'Awesome-sauce!', 'You rock!!!',
						'You are a multiplication GENIUS!!!',
						'How did you get so smart?!?!']

wrong_answer_messages = ['Oops! Either you got the wrong answer, or Daddy didn\'t code this right! Let\'s try another one...',
						'Almost! Maybe try one of your math strategies next time you\'re having trouble?',
						'Oops! I know you can figure that one out, maybe you typed the wrong number by accident?',
						'Uh Oh! You missed that one, but I KNOW you can get the next one right!!']

level1_base = [0, 1, 2, 5, 10]
level2_base = [0, 1, 2, 4, 5, 10, 11]
level3_base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
common_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def do_level(level, values, common, name):
	f = open('Maddie multiplaction results.txt', 'a+')
	print('OK, ' + str.title(name) + ', let\'s do Level ' + str(level) + '.\n\n')
	print('10 problems coming your way, let\'s get started!!!\n\n')
	start = datetime.now()
	starttime = start.strftime('%Y-%m-%d, %H:%M:%S')
	f.write(f'Level {level} start time: {starttime}\n')
	
	for i in range(10):
		num1 = random.choice(values)
		num2 = random.choice(common)
		answer = num1 * num2
		problem = 'What is ' + str(num1) + ' x ' + str(num2) + ' ?\t '
		while True:
			x = input(problem)
			try:
				int(x)
				break
			except ValueError:
				print("\nThat's not a number silly!!! Try typing your answer again!!! :-)")

		if int(x) == int(answer):
			print(str(random.choice(right_answer_messages)) + '\n')
			right.append(i)
			f.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  CORRECT\n')
		elif int(x) != int(answer):
			print('\nOops, you missed it that time.  Let\'s try it one more time!')
			x = input(problem)
			if int(x) == int(answer):
				print(str(random.choice(right_answer_messages)) + '\n')
				right.append(i)
				f.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  CORRECT (2nd try)\n')
			else:
				print(str(random.choice(wrong_answer_messages)) + '\n')
				wrong.append(i)
				f.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  WRONG\n')

		total.append(i)
	end = datetime.now()
	duration = end - start
	time_message = '\nTotal time to answer 10 problems: ' + str(duration) + ' seconds.\n'
	accuracy = 'You answered ' + str(len(right)) + ' out of 10 questions correctly.\n'
	linebreak = '\n ################################################ \n\n'

	print(time_message)
	print(accuracy)
	print(linebreak)
	f.write(time_message)
	f.write(accuracy)
	f.write(linebreak)

print('\n\n')
name = input('Hello, thanks for wanting to play Daddy\'s super amazing multiplication game!!!\n\nPlease type your name:\t')
if str.lower(name) == 'maddie':
	pass
else:
	print("\nEither you're trying to trick me, OR you spelled you're name wrong!  I'm going to call you Maddie McStinkerButt for now!",
		"anyway! :-)\n\n")
	name = 'Maddie McStinkerButt'

keep_playing = 'y'
while keep_playing == str.lower('y'):
	right = []
	wrong = []
	total = []
	level = int(input('What level would you like to play? (Please type 1, 2, or 3 and then press enter:\t'))
	
	if level == 1:
		do_level(level, level1_base, common_numbers, name)
	elif level == 2:
		do_level(level, level2_base, common_numbers, name)
	elif level == 3:
		do_level(level, level3_base, common_numbers, name)
	else:
		print('Oops!  I don\'t think you entered a number when selecting a level!')
	keep_playing = input('Do you want to play again? (Type y or n and then press enter)\n')

print('Thanks for playing!!!  Goodbye!')
