#Docker-compose project by Lilian Cizeron and Simon Provot
#1st Year of Cybersécurité du Logiciel at ENSIBS

#Translation of a and b :
#1 : stone
#2 : leaf
#3 : scissors

import socket
import sys

def affiche_resultat(resultat):
	if resultat == 2:
		print("You won !")
	elif resultat == 1:
		print("You loose...")
	elif resultat == 0:
		print("The other player did the same thing, try again !")
	elif resultat == -1:
		print("An error occur...")

def main():
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect the socket to the port where the server is listening
	server_address = ('localhost', 10000)
	print(sys.stderr, 'connecting to %s port %s' % server_address)
	sock.connect(server_address)
	try:
		# On demande le jeu du client
		jeu_client = input("Jeu : ")
		#print(sys.stderr, 'sending  : {}'.format(jeu_client))

		# On envoie le jeu au serveur
		sock.sendall(jeu_client.encode())

		# On attend la reponse du serveur
		msg = sock.recv(1024)
		affiche_resultat(int(msg.decode()))
				
	finally:
		print(sys.stderr, 'closing socket')
		sock.close()

if __name__ == '__main__':
	main()
