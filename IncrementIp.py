'''
.SYNOPSIS
    Increment IP Address
.DESCRIPTION
    This can be used to get a range of ip address. 
.NOTES
    File Name      : IncrementIp1.py
    Author         : gajendra d ambi
    Prerequisite   : python 3.5 (tested on windows)
    Copyright      - none
.LINK
    Script posted over:
    github.com/gajuambi/python
'''
#get the initial ip address from the user
a = input("Initial Ip Address: ")
#import the ipaddress module and also check whether it is an ipv6 or ipv4
import ipaddress
if ':' in a:
    b = ipaddress.IPv6Address(a)
    print ('this is ipv6 address')
else:
    b = ipaddress.IPv4Address(a)
    print ('this is ipv4')
#get the user input on how many ip address to be generated
c = input("Number of Ip Addresses to be generated: ")
c = int(c)
d = b+c
while b < d:
    b += 1
    print(b)