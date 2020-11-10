import socket
import sys
from calcul import combat



def main():
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the port
	server_address = ('localhost', 10000)
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

	            print(sys.stderr, 'received data : {data}'.format(data))

	            if jeu_client:
	            	# Dans le cas où on recoit une valeur de jeu du client

	            	# On demande au joueur serveur son jeu
	            	jeu = demande_jeu()

	            	# On verifie qui gagne 
	            	resultat = combat(jeu,jeu_client)

	            	# Serveur gagne
	            	affiche_resultat_serveur()



	                print(sys.stderr, 'sending data back to the client')
	                #clientSocket.sendto(message.encode(),("localhost", serverPort))
	                connection.sendall(resultat)
	            else:
	                print(sys.stderr, 'no more data from', client_address)
	                break
	            
	    finally:
	        # Clean up the connection
	        connection.close()