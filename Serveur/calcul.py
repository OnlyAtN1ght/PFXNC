#Docker-compose project by Lilian Cizeron and Simon Provot
#1st Year of Cybersécurité du Logiciel at ENSIBS

#Translation of a and b :
#1 : stone
#2 : leaf
#3 : scissors

def combat(a,b):
	if a == b:
		return 0
	elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1): #Client win
		return 2
	elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2): #Server win
		return 1
	else:
		return -1
