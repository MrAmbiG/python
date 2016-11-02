'''
.SYNOPSIS
    Increment IP Address
.DESCRIPTION
    This can be used to get a range of ip address. 
.NOTES
    File Name      : FunIncrementIp.py
    Author         : gajendra d ambi
    Prerequisite   : python 3.5 (tested on windows)
    Copyright      - none
.EXAMPLE1 : FunIncrementIp('1.1.1.1','10')
    This will increment your ipv4 addresses to 10 more
.EXAMPLE2 : FunIncrementIp('2001:db8:0:1:1:1:1:1','10')
    This will increment your ipv6 addresses to 10 more
.LINK
    Script posted over:
    github.com/gajuambi/python
'''
def FunIncrementIp(IPADDRESS,IPADDRESSES):
    #import the ipaddress module and also check whether it is an ipv6 or ipv4
    import ipaddress
    if ':' in IPADDRESS:
        IPADDRESSMOD = ipaddress.IPv6Address(IPADDRESS)
        print ('this is ipv6 address')
    else:
        IPADDRESSMOD = ipaddress.IPv4Address(IPADDRESS)
        print ('this is ipv4 address')
    IPADDRESSES = int(c)
    IPADDRESSES = IPADDRESSMOD+IPADDRESSES
    while IPADDRESSMOD < IPADDRESSES:
        IPADDRESSMOD += 1
        print(IPADDRESSMOD)
        