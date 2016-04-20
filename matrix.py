# (c) Brian Voyer 2016
# matrix v2. 20 April 2016

from matrix_tools import *
twelvetone = [0,1,2,3,4,5,6,7,8,9,10,11]
twelvetone_let = [0,1,2,3,4,5,6,7,8,9,'e','t']
build = range(12)[1:]

while(1):
	string_po = raw_input('Enter your row (no spaces, use t and e for 10 and 11): ')
	try:
		po = tt_parse(string_po, 12, 10, 11)
		if(sorted(po) != twelvetone):
			print("ERROR: INVALID ROW - REPEATED PITCH")
			continue
	except NameError:
		continue
	break
			
#generate matrix
sub_po = po[:]
matrix = [sub_po,[],[],[],[],[],[],[],[],[],[],[]]

for i in build:
	inter = []
	flag_a = 0
	for j in range(12):
		inter.append((sub_po[j] + i) % 12)
		if(((sub_po[j] + i ) % 12) == sub_po[0]):
			flag_a = j
			matrix[flag_a] = inter
		
for i in range(12):
	for j in range(12):
		if(matrix[i][j] == 10):
			matrix[i][j] = 't'
		if(matrix[i][j] == 11):
			matrix[i][j] = 'e'

print("Twelve Tone Matrix:")
for i in range(12):
	print("[" + ",".join( str(x) for x in matrix[i]) + "]")

#search for self-complementing hexachords
#of H1 of P0
hexachordsearch(matrix[0][:6], "complementing hexachords", matrix) 		# search for combinatorial hexachords of H1 of P0
hexachordsearch(matrix[0][6:], "combinatorial hexachords", matrix) 		# search for self-complementing hexachords of H1 of P0
while(1):
	do_continue = raw_input('Search for other hexachords? (y/n): ')
	try:
		do_continue_str = str(do_continue)
		if( do_continue_str == 'n' or do_continue_str == 'N'):
			break
		if( do_continue_str == 'y' or do_continue_str == 'Y'):
			newhexachord_inp = raw_input('Enter the hexachord to search for (no spaces, use t and e for 10 and 11): ')
			newhexachord = tt_parse(newhexachord_inp, 6, 't', 'e')
			hexachordsearch(newhexachord, "instances", matrix)
			continue
		else:
			print("ERROR: INVALID INPUT")
			continue
	except ValueError:
		print("ERROR: INVALID INPUT")
		continue
