#######################################################################################################################
#                                                                                      sAtUrDaY lOoPiE fUn WiTh da BoyZ
#                                                                                                                   ELS
#                                                                                                                   TRS
#                                                                                                                  2020
# begin including libraries
from colorama import Fore, Back, Style   # COLOR STUFF
from os import system, name              # SYSTEM STUFF (console output)
from time import sleep                   # SLEEP STUFF

# list of foreground colors
foregroundColors = [Fore.RED,
					Fore.GREEN,
					Fore.YELLOW,
					Fore.BLUE,
					Fore.MAGENTA,
					Fore.CYAN]

# list of background colors
backgroundColors = [Back.CYAN,
					Back.MAGENTA,
					Back.BLUE,
					Back.YELLOW,
					Back.GREEN,
					Back.RED]

# define our nifty console clearing function
def clear():

	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for everything else
	else: 
		_ = system('clear') 

# this constructs an infinate loop
theVoid = 0
while theVoid == 0:

	# CLEAR SCREEN
	clear()

	# STEP I
	for bruhs in range(0,18):
		print("       ONE HOP THIS TIME       ")

		for dinks in range(0,6):
			# make the pretty borders and output the loop count
			print(Fore.WHITE + " =>=>=>=>=>=>= " + str(dinks) + " =<=<=<=<=<=<=")

			# do the rainbow effect for every loop
			for LOOPY in foregroundColors:
				print(LOOPY + backgroundColors[dinks] + '<<< to ThE lEfT to ThE rIgHt >>>' + Style.RESET_ALL)

	# sleep for 3 seconds after printing output
	sleep(3)

	# now call function we defined above
	clear()

	# STEP II
	for bruhs in range(0,18):
		print("     TAKE IT BACK NOW YALL     ")

		for dinks in range(0,6,2):
			# make the pretty borders and output the loop count
			print(Fore.WHITE + " =>=>=>=>=>=>= " + str(dinks) + " =<=<=<=<=<=<=")

			# do the rainbow effect for every loop
			for LOOPY in foregroundColors: 
				print(LOOPY + backgroundColors[dinks] + '<<< to ThE lEfT to ThE rIgHt >>>' + Style.RESET_ALL)

	# sleep for 3 seconds
	sleep(3)

# colorama library examples
#
#print(Fore.RED + 'some red text') 
#print(Back.GREEN + 'and with a green background') 
#print(Style.DIM + 'and in dim text') 
#print(Style.RESET_ALL)
#print('back to normal now')
#
# possible inputs
#
#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL
#
#
#
#######################################################################################################################