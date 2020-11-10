#Docker-compose project by Lilian Cizeron and Simon Provot
#1st Year of Cybersécurité du Logiciel at ENSIBS

#Translation of a and b :
#1 : stone
#2 : leaf
#3 : scissors


import socket
import sys
from calcul import combat

def affiche_resultat(resultat):
	if resultat == 1:
		print("You won !")
	elif resultat == 2:
		print("You loose...")
	elif resultat == 0:
		print("The other player did the same thing, try again !")
	elif resultat == -1:
		print("An error occur...")

def main():
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the port
	server_address = ('192.168.2.1', 10000)
	print(sys.stderr, 'starting up on %s port %s' % server_address)
	sock.bind(server_address)

	sock.listen(1)

	while True:
		# Wait for a connection
		print(sys.stderr, 'waiting for a connection')
		connection, client_address = sock.accept()
		try:
			# La connection est faites 
			print(sys.stderr, 'connection from', client_address)

			while True:
				# On recoit des données
				jeu_client = connection.recv(16)

				#print(sys.stderr, 'received data : {}'.format(jeu_client.decode()))

				if jeu_client:
					# Dans le cas où on recoit une valeur de jeu du client

					# On demande au joueur serveur son jeu
					jeu = input("Jeu : ")

					# On verifie qui gagne
					resultat = combat(int(jeu),int(jeu_client.decode()))

					# Affiche le resultat
					affiche_resultat(resultat)

					resultat = str(resultat)

					#print(sys.stderr, 'sending data back to the client : {}'.format(resultat.encode()))
					#clientSocket.sendto(message.encode(),("localhost", serverPort))
					connection.send(resultat.encode())
				else:
					#print(sys.stderr, 'no more data from', client_address)
					break
		except:
			connection.close()
		finally:
			# Clean up the connection
			connection.close()

if __name__ == '__main__':
	main()
