# vulnBanners

Simple FTP Vulnerability scanner will read in a provided text file and use it to make
decisions if our banner is vulnerable

It might prove valuable to check to see if
that file exists and the current user has read permissions to that file. If either
condition fails, it would be useful to display an appropriate error message to use a for-loop
to iterate through multiple elements. 

Consider, for example: if we wanted to
iterate through the entire /24 subnet of IP addresses for 192.168.95.1 through
192.168.95.254, using a for-loop with the range from 1 to 255 allows us to
print out the entire subnet.

The script will test all 254 IP addresses on the 192.168.95.0/24 subnet with the ports offering telnet, SSH, smtp, http,
imap, and https services.

To use this program first install python on your pc be it linux or windows operating system based on the environment of your choice.

#############windows##############

download python from the official python website install and add a path to the installation folder on your pc's enveronmental variables.

#############Linux################
As for linux, python comes pre_installed on the operating system so there is no need of downloading the installation packages.

##############Running the Program##############
Open the terminal and type....
> python checkVuln.py
