import socket
import sys



def main():
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect the socket to the port where the server is listening
	server_address = ('localhost', 10000)
	print(sys.stderr, 'connecting to %s port %s' % server_address)
	sock.connect(server_address)
	try:
		# On demande le jeu du client
		jeu_client = demande_jeu()
		print(sys.stderr, 'sending  : {}'.format(message))

		# On envoie le jeu au serveur
		sock.sendall(message.encode())

		# On attend la reponse du serveur
		data = sock.recv(16)
		while True:
			data = sock.recv(16)
			# On a recu la reponse du serveur
			if data:
				print(sys.stderr, 'received {}'.format(data))
				affiche_resultat_client()
				



			

	finally:
		print(sys.stderr, 'closing socket')
		sock.close()

if __name__ == '__main__':
	main()