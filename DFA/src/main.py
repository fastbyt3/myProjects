from dfaObject import FA
from fileParser import parseFile

def main():
	FILE = input('Enter file name: ')
	while True:
		with open(FILE, 'r') as f:
			nStates, initState, finalState, transitions = parseFile(f)
	
		dfa = FA(nStates, initState, finalState, transitions)
		dfa.print()

		word = input('\nGive any word as input: ')
		if word == 'q':
			exit(1)
		
		for letter in word:
			state = dfa.step(letter)
		print('--------------------------------------------------------')
		try:
			if state[0] == finalState:
				print(f"word: {word} in language")
			else:
				print(f"word: {word} not in language")
		except:
			print('Possible dead state or word is NOT valid')
		print('--------------------------------------------------------')
		print('\nTo exit type q in the prompt')

if __name__ == '__main__':
	main()