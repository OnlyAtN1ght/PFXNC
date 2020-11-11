#Docker-compose project by Lilian Cizeron and Simon Provot
#1st Year of Cybersécurité du Logiciel at ENSIBS

#Translation of a and b :
#1 : stone
#2 : leaf
#3 : scissors

#Libraries
import socket
import sys
from time import sleep
from random import randint

def affiche_resultat(resultat):
	if resultat == 2:
		print("Client won !\n")
	elif resultat == 1:
		print("Client loose...\n")
	elif resultat == 0:
		print("The other player did the same thing, try again !\n")
	elif resultat == -1:
		print("An error occur...\n")

def main():

	#Dictionnary to translate
	possibility = {"1": "stone", "2": "leaf", "3": "scissors"}
	
	print("Welcome in our game of stone - leaf - scissors !")
	
	#Waiting to wakeup server
	sleep(2)
	
	#Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#Connect the socket to the port where the server is listening
	server_address = ('192.168.2.1', 10000)
	print("Connecting to %s port %s" % server_address)
	sock.connect(server_address)
	
	try:
		#Ask for client play
		jeu_client = str(randint(1, 3))
		print("\nClient has played :", possibility[jeu_client])

		#Sending data to server
		sock.sendall(jeu_client.encode())

		#Waiting to server's answer and display result
		msg = sock.recv(1024)
		affiche_resultat(int(msg.decode()))
	
	except Exception as e:
		print(e)
				
	finally:
		#Close the connection
		sock.close()

if __name__ == '__main__':
	main()
