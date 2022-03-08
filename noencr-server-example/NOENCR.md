this is the readme file for the no-encryption-python-server

this project is only for educational purpose and is not created for actually 
usage. It shows the harm of unencrypted packages. 

setup: only edit both files and rewrite the host IP-address to your device address

usage: now create an arbitary file with a secret massage. Start the Wireshark 
sniffer sniffing on your ethernet. Then start both scripts 
and add the created file with the --f command to the client script. 
You should now be able to see the secret text of the file in a packate captured 
by Wirehark 
