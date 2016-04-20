# (c) Brian Voyer 2016

string_po = raw_input('Enter your row (no spaces, use t and e for 10 and 11): ')
twelvetone = [0,1,2,3,4,5,6,7,8,9,10,11]
twelvetone_let = [0,1,2,3,4,5,6,7,8,9,'e','t']

#generate matrix
po=list(string_po)
if(len(po) != 12):
	print("ERROR: INVALID ROW - NOT 12 TONES")
	quit()

for i in range(12):
	if(po[i] == 't' or po[i] == 'T'):
		po[i] = 10
	if(po[i] == 'e' or po[i] == 'E'):
		po[i] = 11
	else:
		try:
			po[i] = int(po[i])
		except ValueError:
			print("ERROR: INVALID INPUT")
			quit()

if(sorted(po) != twelvetone):
	print("ERROR: INVALID ROW - REPEATED PITCH")
	quit()

matrix = [po,[],[],[],[],[],[],[],[],[],[],[]]
build = range(12)[1:]

for i in build:
	int = []
	flag = 0
	for j in range(12):
		int.append((po[j] + i) % 12)
		if(((po[j] + i ) % 12) == po[0]):
			flag = j
	matrix[flag] = int

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
int = matrix[0][:6]
hex_int = []
intint = []
#print(int)
flag = 0
for i in range(7)[1:]:
	for j in range(12):
		hex_int = matrix[i][j:j+6]
		if(sorted(list(int) + hex_int) == twelvetone_let):
			if(flag == 0):
				flag = 1
				print("Self-complementing hexachords:")
				print("P"+str(matrix[i][0])+": "+"["+",".join( str(x) for x in matrix[i][j:j+6])+"]")
			else:
				print("P"+str(matrix[i][0])+": "+"["+",".join( str(x) for x in matrix[i][j:j+6])+"]")
		hex_int = []
		intint = []
		for k in range(6):
			hex_int.append(matrix[i:i+6][k][j])
		if(sorted(list(int) + hex_int) == twelvetone_let):
			for k in range(6):
				intint.append(matrix[i:i+6][k][j])
			if(flag == 0):
				flag = 1
				print("Self-complementing hexachords:")
				print("I"+str(matrix[0][j])+": "+"["+",".join( str(x) for x in hex_int)+"]")
			else:
				print("I"+str(matrix[0][j])+": "+"["+",".join( str(x) for x in hex_int)+"]")
if(flag == 0):
	print("No self-complementing hexachords found.")

flag = 0
for i in range(7)[1:]:
	for j in range(12):
		hex_int = matrix[i][j:j+6]
		if(sorted(list(hex_int)) == sorted(list(int))):
			if(flag == 0):
				flag = 1
				print("Combinatorial hexachords:")
				print("P"+str(matrix[i][0])+": "+"["+",".join( str(x) for x in matrix[i][j:j+6])+"]")
			else:
				print("P"+str(matrix[i][0])+": "+"["+",".join( str(x) for x in matrix[i][j:j+6])+"]")
		hex_int = []
		intint = []
		for k in range(6):
			hex_int.append(matrix[i:i+6][k][j])
		if(sorted(hex_int) == sorted(list(int))):
			for k in range(6):
				intint.append(matrix[i:i+6][k][j])
			if(flag == 0):
				flag = 1
				print("Combinatorial hexachords:")
				print("I"+str(matrix[0][j])+": "+"["+",".join( str(x) for x in hex_int)+"]")
			else:
				print("I"+str(matrix[0][j])+": "+"["+",".join( str(x) for x in hex_int)+"]")

if(flag == 0):
	print("No combinatorial hexachords found.")
