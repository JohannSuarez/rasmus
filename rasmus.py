import os
import sys
import argparse
import pysftp

parser = argparse.ArgumentParser()
parser.add_argument("operation")
user_input = parser.parse_args()


#First make a check if the config.txt exists in the first place. If not, exit and close.


#-------------------------Grabbing lines of config.txt-------------------#

conf = open("configs.txt")

name_str = conf.readline()
host_str = conf.readline()
private_key_str = conf.readline()
pass_str = conf.readline()

conf.close()

#-------------------------Parsing information from config.txt------------#

if "=" in name_str:
    name = name_str[name_str.find("=")+1:].split()[0]
else:
    sys.exit("Could not get name data. Closing...")

if "=" in host_str:
    host = host_str[host_str.find("=")+1:].split()[0]
else:
    sys.exit("Could not get host data. Closing...")

if "=" in private_key_str:
    p_key = private_key_str[private_key_str.find("=")+1:].split()[0]
else:
    sys.exit("Could not get private key. Closing...")

if "=" in pass_str:
    pwd = pass_str[pass_str.find("=")+1:].split()[0]
else:
    sys.exit("Could not get pass. Closing...")

#-------------------------------------------------------------------------#


#------------------------Reciting parsed information for clarity----------#

print("")								  # Empty space.
print("Name is: " + name)
print("Host is: " + host)
print("Private key is: " + p_key)					  

#------------------------Performing specified operation-------------------#



if(user_input.operation == "get"):
	print("Input is get. Retrieving files.")
	with pysftp.Connection(host, username=name, private_key=p_key, private_key_pass=pwd) as sftp:
		sftp.get_r('to_local', 'received', preserve_mtime=True)        

			
elif (user_input.operation == "put"):
	print("Input is put. Sending files.")
	with pysftp.Connection(host, username=name, private_key=p_key, private_key_pass=pwd) as sftp:	#Sends both files AND folders. Function complete.
		sftp.put_r('send', 'received', preserve_mtime=True)
else:
	sys.exit("Input not recognized. Argument is either get or put.")



