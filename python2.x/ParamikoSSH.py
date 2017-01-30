'''
.SYNOPSIS
    SSH to ssh devices
.DESCRIPTION
    connect to devices/servers/clients , run an ssh command and get the output for the same
.NOTES
    File Name      : ParamikoSSH.ps1
    Author         : gajendra d ambi
    Date           : May 2016
    Prerequisite   : python 2.7
    Copyright      - None
.LINK
    Script posted over: github.com/mrambig
'''

target = '' #ip address of the target to which you want to connect to 
username = '' #username for the target
password = '' #password for the target
command  = '' #command to run and get the output for ex:- put hostname to know the hostname of the linux server, put show run to get the output for the show run command on cisco switches.

import paramiko #import paramiko module
ssh  = paramiko.SSHClient() #create an ssh client
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #auto accept ssh key
ssh.connect(target, port=22, username=username, password=password) #connect to the target
stdin, stdout, stderr = ssh.exec_command(command) #execute the command
output = stdout.readlines() #get the output
outstore = '\n'.join(output) #format the output to print each line in a new line
print outstore #print outstore