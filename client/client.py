#Docker-compose project by Lilian Cizeron and Simon Provot
#1st Year of Cybersécurité du Logiciel at ENSIBS

#Translation of a and b :
#1 : stone
#2 : leaf
#3 : scissors

import socket
import sys
from time import sleep

def jeu():
	print("You have three choices for this game :")
	print("1 : stone")
	print("2 : leaf")
	print("3 : scissors")
	choice = input("You choice ? ")
	return str(choice)

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
	print("Welcome in our game of stone - leaf - scissors !")
	sleep(5) #Waiting to wakeup server
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect the socket to the port where the server is listening
	#server_address = ('192.168.2.1', 10000)
	server_address = ('localhost', 10000)
	print("Connecting to %s port %s" % server_address)
	sock.connect(server_address)
	try:
		# On demande le jeu du client
		jeu_client = jeu()
		#print(sys.stderr, 'sending  : {}'.format(jeu_client))

		# On envoie le jeu au serveur
		sock.sendall(jeu_client.encode())

		# On attend la reponse du serveur
		#msg = sock.recv(1024)
		#print(msg.decode())
		msg = sock.recv(1024)
		affiche_resultat(int(msg.decode()))
				
	finally:
		print(sys.stderr, 'closing socket')
		sock.close()

if __name__ == '__main__':
	main()
