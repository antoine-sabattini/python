
l, L, i, j = 0, 0, None, None


l = int (input ())
L = int (input ())

for i in range (1, l + 1):
	for j in range (1, L + 1):
		if i == 1 or i == l or j == 1 or j == L:
			print (end="|  ")
		else:
			print(end="   ")

	print (end="\n\n")
