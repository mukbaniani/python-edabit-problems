import socket

def get_domain(ip_address):
	name = socket.gethostbyaddr(ip_address)[0]
	return name
	