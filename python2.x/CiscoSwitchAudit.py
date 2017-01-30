'''
.SYNOPSIS
    Text Audit report for Cisco Switchhes
.DESCRIPTION
    This will generate an audit report Cisco Switches. Make sure you have the paramiko module installed and ready to be used in python.
    you can either do it via miniconda, pip or whichever you prefer.
.NOTES
    File Name      : CiscoSwitchAudit.ps1
    Author         : gajendra d ambi
    Date           : September 2016
    Prerequisite   : python 2.7.x, paramiko module
    Copyright      - None
.LINK
    Script posted over: https://github.com/MrAmbiG/python
'''

target   = '1.1.1.1'
username = 'admin'
password = '@dmin'

def N359ktext():
    commands = [ #Here we will list out all the commands that we have to run in a cisco switch
    "show feature                      ",
    "show banner motd                  ",
    "show run | inc route              ",
    "show int desc                     ",
    "show license usage                ",
    "show version                      ",
    "show inventory                    ",
    "show vpc brief                    ",
    "show hsrp brief                   ",
    "show environment                  ",
    "show port-channel summary         ",
    "show vlan                         ",
    "show module                       ",
    "show redundancy status            ",
    "show int counters errors          ",
    ]

    filename = target +'.commands.txt' #name of the file with commands and their output
    
    import inspect
    import os
    import sys
    
    def get_script_dir(follow_symlinks=True):
        if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
            path = os.path.abspath(sys.executable)
        else:
            path = inspect.getabsfile(get_script_dir)
        if follow_symlinks:
            path = os.path.realpath(path)
        return os.path.dirname(path)
    
    scriptpath = get_script_dir() #path where the script resides
    filepath = "%s\%s" % (scriptpath, filename) #full path to the filename including the file itself
    print filepath
    
    import paramiko #import paramiko module
    ssh  = paramiko.SSHClient() #create an ssh client
    
    open(filepath, 'w') #create file
    with open(filepath,"a") as myfile:
        for command in commands:
            print command
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #auto accept ssh key
            ssh.connect(target, port=22, username=username, password=password) #connect to the target
            stdin, stdout, stderr = ssh.exec_command(command) #execute the command
            output = stdout.readlines() #get the output
            outstore = '\n'.join(output) #format the output to print each line in a new line
            print outstore #print outstore
            file = myfile.write
            file('\n start of ' + command) #append the name of the command for which we have the ouput
            file('\n=====================================') 
            file('\n')
            file(outstore) #actual output of the command
            file('\n')
            file('\n end of ' + command)
            file('\n-------------------------------------') 
