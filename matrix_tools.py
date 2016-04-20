# (c) Brian Voyer 2016
# Module to provide functions for matrix
def tt_parse(inputstring, numexpected, ten_rep, eleven_rep):
	flag = 0
	po_int=list(inputstring)
	if(len(po_int) != numexpected):
		print("ERROR: INVALID ROW - NOT " + str(numexpected) + " TONES")
		raise NameError()
	for i in range(numexpected):
		if(po_int[i] == 't' or po_int[i] == 'T'):
			po_int[i] = ten_rep
		elif(po_int[i] == 'e' or po_int[i] == 'E'):
			po_int[i] = eleven_rep
		else:
			try:
				po_int[i] = int(po_int[i])
			except ValueError:
				print("ERROR: INVALID INPUT")
				raise NameError()
	return(po_int)



def hexachordsearch(hexachord, type_inp, matrix_inp):
	if( len(hexachord) != 6 ):
		raise ValueError()
	hc_type = str(type_inp)
	hex_int = []
	intint = []
	flag = 0
	pp_hexachord = '[' + ''.join( str(x) for x in hexachord ) + ']'
	for i in range(7)[1:]:
		for j in range(12):
			hex_int = matrix_inp[i][j:j+6]
			if( sorted(hex_int) == sorted(hexachord) ):
				if(flag == 0):
					flag = 1
					print(hc_type[0].capitalize() + hc_type[1:] + " of " + pp_hexachord + ":")
					print("P"+str(matrix_inp[i][0])+": "+"["+",".join( str(x) for x in matrix_inp[i][j:j+6])+"]")
				else:
					print("P"+str(matrix_inp[i][0])+": "+"["+",".join( str(x) for x in matrix_inp[i][j:j+6])+"]")
			hex_int = []
			intint = []
			for k in range(6):
				hex_int.append(matrix_inp[i:i+6][k][j])
				if(sorted(hex_int) == sorted(hexachord)):
					for k in range(6):
						intint.append(matrix_inp[i:i+6][k][j])
					if(flag == 0):
						flag = 1
						print(hc_type[0].capitalize() + hc_type[1:] + " of " + pp_hexachord + ":")
						print("I"+str(matrix_inp[0][j])+": "+"["+",".join( str(x) for x in hex_int)+"]")
					else:
						print("I"+str(matrix_inp[0][j])+": "+"["+",".join( str(x) for x in hex_int)+"]")
	if(flag == 0):
		print("No " + hc_type + " of " + pp_hexachord + " found.")

