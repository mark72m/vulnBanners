#########################################################################################
#    This program uses a list of vulnerable banners specified by the user to check      #
#          if they are vulnerable                                                       #
#########################################################################################

####################################################################
#                                                                  #
#                Simple FTP Vulnerability Checker                  #
#                                                                  #
####################################################################

import socket
import sys
# OS Module Allows program to independently interact with os environment,
# File System, user DB and permissions
import os 

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner

	except:
		return

def checkVulns(banner, filename):
	f = open(filename, 'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print ("[+] Server is Vlnerable: " + banner.strip('\n'))

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print ("[-]" + filename + " does not exist.")
			exit(0)

			if not os.access(filename, os.R_OK):
				print ("[-]" + filename + " access denied.")
				exit(0)
		else:
			print ("[*] Usage: " + str(sys.argv[0] + ' <Vulnerabilities file name> \n'))
			
			portList = [21, 22, 25, 80, 110, 443]
			for x in range(1, 255):
				ip = '192.168.56.' + str(x)
				print ("[+] Reading Vulnerabilities From: " + filename)
				for port in portList:
					banner = retBanner(ip, port)
					if banner:
						print ("[+] " + ip + ":" + banner)
						checkVulns(banner, filename)

if __name__ == '__main__':
	main()

