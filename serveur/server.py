#Docker-compose project by Lilian Cizeron and Simon Provot
#1st Year of Cybersécurité du Logiciel at ENSIBS

#Translation of a and b :
#1 : stone
#2 : leaf
#3 : scissors

#Libraries
import socket
import sys
from calcul import combat
from random import randint

def affiche_resultat(resultat):
	if resultat == 1:
		print("Server won !\n")
	elif resultat == 2:
		print("Server loose...\n")
	elif resultat == 0:
		print("The other player did the same thing, try again !\n")
	elif resultat == -1:
		print("An error occur...\n")

def main():

	#Dictionnary to translate
	possibility = {"1": "stone", "2": "leaf", "3": "scissors"}
	
	#Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#Bind the socket to the port
	server_address = ('192.168.2.1', 10000)
	print("\nStarting up on %s port %s" % server_address)
	sock.bind(server_address)

	#Wait for a connection
	print("Waiting for a connection")
	sock.listen(5)
	connection, client_address = sock.accept()
	
	try:
		#Connection done 
		print(client_address[0], "connected.")

		while True:
		
			#Receving client data
			jeu_client = connection.recv(16)

			if jeu_client:
			
				#The server play
				jeu = str(randint(1,3))
				print("\nServer has played :", possibility[jeu])

				#Check who won
				resultat = combat(int(jeu),int(jeu_client.decode()))

				#Print result
				affiche_resultat(resultat)
				
				#Sending result
				resultat = str(resultat)
				connection.send(resultat.encode())
			else:
				break
	except:
		#Clean up the connection
		connection.close()
	finally:
		#Clean up the connection
		connection.close()

if __name__ == '__main__':
	main()
