
from art import text2art
from termcolor import colored
zero = u'\u200B'
one = u'\u200C'
beginning = u'\u200E'
end = u'\u200F'
divider = u'\u2060'

def encode():
	global beginning, end, zero, one
	secret = input('Enter the secret text: ')
	
	stringlit = [str(format(ord(u), '08b')) for u in secret]
	public = input('Enter the public text: ')
	# print(stringlit)
	public += beginning
	for digits in str(stringlit):
		if digits == '0':
			public += zero
		elif digits == '1':
			public += one
	
	public += end
	print('Encrtpted text(you may need to copy this): {}'.format(public))


def decode():
	global beginning, end, zero, one
	text = input('Enter the text You want to check: ')
	starting = text.index(beginning) + 1
	ending = text.index(end)
	char = ''
	
	# Hello‎‌‌​​​​‌‌​​​​​‌‌​​​‌‌‏
	# print(text[starting:starting+8])
	print('Decrypted text: ', end='')
	for t in range(len(range(starting, ending+1))//8):
		for u in text[starting:starting+8]:
			if u == zero:
				char += '0'
			elif u == one:
				char += '1'
		#print(char)
		
		print(chr(int(char, 2)), end='')
		
		char = ''
		starting += 8
	print()

print(colored(text2art('Stenography', 'smallcaps2'), 'green'))
choice = input("""1. Encode
2. Decode
Enter your choice: """).strip()

if choice == '1':
	encode()
elif choice == '2':
	decode()
	

