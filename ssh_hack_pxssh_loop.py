#!/usr/bin/python
import getpass
from pexpect import pxssh


commands = ["su - ", "useradd meeto1","echo testing123|passwd meeto1 --stdin","useradd meeto2","echo testing123|passwd meeto2 --stdin"]
username = 'cisco'
password = 'testing'
# Starts the loop for devices


for i in open('server1.txt'):
	outputFileName = str(i)+'-logs.txt'
	device_prompt = "#"
	child = pxssh.pxssh()
	child.login(i, username.strip(),password.strip(), auto_prompt_reset=False)
# Starts the loop for commands and write to output
	with open(outputFileName, 'w') as f:
		for command in commands:
                	if "su" in command:  
	        	 	child.sendline(command)
		         	child.expect("Password:")
                         	child.sendline("testing\n")
                        
                	else:    
                         	child.sendline(command)
                         	child.expect(device_prompt)  
                	f.write(child.before)
        	child.expect("#")
        	f.write(child.before)
        	child.sendline("id meeto")
        	child.expect("#")
        	f.write(child.before)
        	child.sendline("exit")        
	child.logout()
