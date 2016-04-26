# (c) Brian Voyer 2016
# matrix v2. 20 April 2016

from matrix_tools import *
import time
twelvetone = [0,1,2,3,4,5,6,7,8,9,10,11]
twelvetone_let = [0,1,2,3,4,5,6,7,8,9,'e','t']
build = range(12)[1:]
string_po = raw_input('Enter your row (no spaces, use t and e for 10 and 11): ')
try:
	matrix = matrix_builder(string_po)
except ValueError:
	print("ERROR")
	quit()
except NameError:
	print("ERROR")
	quit()

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

while(1):
	do_continue = raw_input('Search for common hexachords in another matrix? (y/n): ')
	try:
		do_continue_str = str(do_continue)
		if( do_continue_str == 'n' or do_continue_str == 'N'):
			break
		if( do_continue_str == 'y' or do_continue_str == 'Y'):
			new_tonerow = newhexachord_inp = raw_input('Enter your row (no spaces, use t and e for 10 and 11): ')
			new_matrix = matrix_builder(new_tonerow)
			print("Twelve Tone Matrix:")
			for i in range(12):
				print("[" + ",".join( str(x) for x in new_matrix[i]) + "]")
			originalmatrix_hexachord_list = hexachordlist(matrix)
			for i in originalmatrix_hexachord_list:
				hexachordsearch(i, "instances", new_matrix, printno = 0)
			break
		else:
			print("ERROR: INVALID INPUT")
			continue
	except ValueError:
		print("ERROR: INVALID INPUT")
		continue
