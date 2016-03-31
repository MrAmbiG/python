'''
.SYNOPSIS
    Increment IP Address
.DESCRIPTION
    This can be used to get a range of ip address. 
.NOTES
    File Name      : IncrementIp.py
    Author         : gajendra d ambi
    Prerequisite   : python 3.5 (tested on windows)
    Copyright      - none
.LINK
    Script posted over:
    github.com/gajuambi/python
'''
#get the initial ip address from the user
IPADDRESS = input("Initial Ip Address: ")
#import the ipaddress module and also check whether it is an ipv6 or ipv4
import ipaddress
if ':' in IPADDRESS:
    IPADDRESSMOD = ipaddress.IPv6Address(IPADDRESS)
    print ('this is ipv6 address')
else:
    IPADDRESSMOD = ipaddress.IPv4Address(IPADDRESS)
    print ('this is ipv4')
#get the user input on how many ip address to be generated
IPADDRESSES = input("Number of Ip Addresses to be generated: ")
IPADDRESSES = int(c)
IPADDRESSES = IPADDRESSMOD+IPADDRESSES
while IPADDRESSMOD < IPADDRESSES:
    IPADDRESSMOD += 1
    print(IPADDRESSMOD)
