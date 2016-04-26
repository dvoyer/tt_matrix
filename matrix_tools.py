# (c) Brian Voyer 2016
# Module to provide functions for matrix
def tt_parse(inputstring, numexpected, ten_rep, eleven_rep):
	_flag = 0
	_po_int=list(inputstring)
	if(len(_po_int) != numexpected):
		print("ERROR: INVALID ROW - NOT " + str(numexpected) + " TONES")
		raise NameError()
	for i in range(numexpected):
		if(_po_int[i] == 't' or _po_int[i] == 'T'):
			_po_int[i] = ten_rep
		elif(_po_int[i] == 'e' or _po_int[i] == 'E'):
			_po_int[i] = eleven_rep
		else:
			try:
				_po_int[i] = int(_po_int[i])
			except ValueError:
				print("ERROR: INVALID INPUT")
				raise NameError()
	return(_po_int)



def hexachordsearch(hexachord, type_inp, matrix_inp, printno = 1):
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
	if(flag == 0 and printno == 1):
		print("No " + hc_type + " of " + pp_hexachord + " found.")

def matrix_builder(tonerow):
	_twelvetone = [0,1,2,3,4,5,6,7,8,9,10,11]
	_build = range(12)[1:]
	try:
		_po = tt_parse(tonerow, 12, 10, 11)
	except NameError:
		print("TTPARSE ERROR")
		return(0)
	if(sorted(_po) != _twelvetone):
		print("ERROR: INVALID ROW - REPEATED PITCH")
		raise NameError()
	_sub_po = _po[:]
	_matrix = [_sub_po,[],[],[],[],[],[],[],[],[],[],[]]
	for i in _build:
		_inter = []
		_flag_a = 0
		for j in range(12):
			_inter.append((_sub_po[j] + i) % 12)
			if(((_sub_po[j] + i ) % 12) == _sub_po[0]):
				_flag_a = j
				_matrix[_flag_a] = _inter
	for i in range(12):
		for j in range(12):
			if(_matrix[i][j] == 10):
				_matrix[i][j] = 't'
			if(_matrix[i][j] == 11):
				_matrix[i][j] = 'e'
	return(_matrix)

def hexachordlist(matrix_inp):
	hex_int = []
	hexachord_list = []
	for i in range(7)[:]:
		for j in range(12):
			hex_int = matrix_inp[i][j:j+6]
			if( len(hex_int) == 6 ):
				hexachord_list.append(hex_int)
			hex_int = []
			for k in range(6):
				hex_int.append(matrix_inp[i:i+6][k][j])
			if( len(hex_int) == 6 ):
				hexachord_list.append(hex_int)
	return(hexachord_list)

def to_pitches(tonerow, fundamental):
	pitches = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
	basis_pitch_ = pitches.index(fundamental)
	internal = []
	for i in tonerow:
		__int_ = pitches[(basis_pitch_ + int(tt_parse(i,1,10,11)[0]))%12]
		internal.append(__int_)
	return(internal)
