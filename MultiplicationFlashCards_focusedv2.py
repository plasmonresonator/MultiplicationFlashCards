import random, winsound, os, pygame, time
from datetime import datetime
from collections import deque
from pathlib import Path
from os import path
import requests


path = Path(os.getcwd())
print(os.getcwd())
sound_path = 'c:\\windows\\media\\'
correct_image_path = 'pictures/correct/'
wrong_image_path = 'pictures/wrong/'
correct_image_list = os.listdir(path / correct_image_path)
wrong_image_list = os.listdir(path / wrong_image_path)
# correct_image_path = 'c:\\users\\krist\\desktop\\cat pictures\\correct\\'
# wrong_image_path = 'c:\\users\\krist\\desktop\\cat pictures\\wrong\\'
# correct_image_list = os.listdir(correct_image_path)
# wrong_image_list = os.listdir(wrong_image_path) 

greeting_messages = ['Hi!']
right_answer_messages = ['Freaking awesome!  You got it right, I knew you could do it!!!', 
						'Awesome-sauce!', 'You rock!!!',
						'You are a multiplication GENIUS!!!',
						'How did you get so smart?!?!',
						'Nice job! Keep it up!!!',
						'Nailed it!!  Here, check out this cat!\n\n\t /\\_/\\\n\t( o.o )\n\t > ^ <\n\n',
						"Perfect!  Look at this cute little lion:\n\n(\"`-''-/\").___..--''\"`-._\n `6_ 6  )   `-.  (     ).`-.__.`)\n (_Y_.)'  ._   )  `._ `. ``-..-' \n   _..`--'_..-_/  /--'_.'\n  ((((.-''  ((((.'  (((.-' ",
						]

wrong_answer_messages = ['Oops! Either you got the wrong answer, or Daddy didn\'t code this right! Let\'s try another one...',
						'Almost! Maybe try one of your math strategies next time you\'re having trouble?',
						'Oops! I know you can figure that one out, maybe you typed the wrong number by accident?',
						'Uh Oh! You missed that one, but I KNOW you can get the next one right!!',
						'Bummer, you missed that one, now you have to look at dog poop again!!! :-p ',
						]

focused_base = [10, 11]
# level1_base = [0, 1, 2, 5, 10]
level1_base = [2, 5, 10, 6, 7, 8, 9]
level2_base = [0, 1, 2, 4, 5, 10, 11]
level3_base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
common_numbers_master = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def play_correct_sound():
	os.chdir(sound_path)
	winsound.PlaySound('Windows Exclamation.wav', winsound.SND_FILENAME)
	os.chdir(path)
	

def play_wrong_sound():
	os.chdir(sound_path)
	winsound.PlaySound('ir_begin.wav', winsound.SND_FILENAME)
	os.chdir(path)
	

def display_image(image_type, question_number):
	def do_it(image_type):
		if image_type == 'correct':
			picture = pygame.image.load(correct_image_path + str(random.choice(correct_image_list)))
			sleep_time = 2.5
		else:
			picture = pygame.image.load(wrong_image_path + str(random.choice(wrong_image_list)))
			sleep_time = 1.75
		pygame.display.set_mode(picture.get_size())
		main_surface = pygame.display.get_surface()
		main_surface.blit(picture,(0,0))
		pygame.display.update()
		time.sleep(sleep_time)
		pygame.quit()
	
	if image_type == 'wrong':
		do_it(image_type)
	elif image_type == 'correct':
		if question_number % 3 == 0:
			do_it('correct')
		else:
			pass
	

def do_level(level, values, common, name, i):

	try:
		random.shuffle(common)
		start1 = datetime.now()
		starttime1 = start1.strftime('%Y-%m-%d-%H-%M-%S')
		if not os.path.exists('mathresultfiles'):
			os.mkdir('mathresultfiles')
		indiv_path = path / 'mathresultfiles' #'C:\\Users\\krist\\Desktop\\mathresultfiles\\'
		indiv_filename = os.path.join(indiv_path, starttime1 + '.txt')
		with open(indiv_filename, 'a+') as ff:
			with open('Maddie multiplaction results.txt', 'a+') as f:
				print('OK, ' + str.title(name) + ', let\'s do it!!!\n\n')
				start = datetime.now()
				starttime = start.strftime('%Y-%m-%d, %H:%M:%S')
				f.write(f'Level {level} start time: {starttime}\n')
				ff.write(f'Level {level} start time: {starttime}\n')
				
				while len(common) > 0:
					i += 1
					num1 = int(random.choice(values))
					num2 = int(common.popleft())
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
						display_image('correct', i)
						f.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  CORRECT\n')
						ff.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  CORRECT\n')
					elif int(x) != int(answer):
						print('\nOops, you missed it that time.  Let\'s try it one more time!')
						x = input(problem)
						if int(x) == int(answer):
							print(str(random.choice(right_answer_messages)) + '\n')
							f.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  CORRECT (2nd try)\n')
							ff.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  CORRECT (2nd try)\n')
						else:
							print(str(random.choice(wrong_answer_messages)) + '\n')
							print(f'The correct answer was {num1} x {num2} = {answer}')
							display_image('wrong', i)
							common.append(num2)
							f.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  WRONG\n')
							ff.write(f'Problem {i}: {problem} \tCorrect answer is {answer}.  Your answer was {x}.  WRONG\n')

					total.append(i)
				end = datetime.now()
				duration = end - start
				time_message = '\nTotal time to answer 13 problems: ' + str(duration) + ' seconds.\n'
				# accuracy = 'You answered ' + str(len(right)) + ' out of 10 questions correctly.\n'
				linebreak = '\n ################################################ \n\n'

				print(time_message)
				# print(accuracy)
				print(linebreak)
				f.write(time_message)
				# f.write(accuracy)
				f.write(linebreak)
				ff.write(time_message)
				# ff.write(accuracy)
				ff.write(linebreak)
	except Exception as e:
		print(f'An error occurred with the message: \n\t{e}\nPlease let Daddy know!')

		


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
	first = []
	second = []
	wrong = []
	total = []
	while True:
		focus = input('What number would you like to practice on for this round?\t')
		# try:
		# 	int(focus)
		# 	break
		# except ValueError:
		# 	print("\nThat's not a number silly!!! Try typing the number you want to focus on again!!! :-)")
	# common_numbers = deque(common_numbers_master)
	i = 0
	do_level('focused practice', focus, common_numbers, name, i)
	keep_playing = input('Do you want to play again? (Type y or n and then press enter)\n')

print('Thanks for playing!!!  Goodbye!')
