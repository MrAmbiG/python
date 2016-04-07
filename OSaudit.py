'''
.SYNOPSIS
    Windows Audit
.DESCRIPTION
    This will give you basic windows configuration and statistics 
.NOTES
    File Name      : WinOsAudit.py
    Author         : gajendra d ambi
    Prerequisite   : python 3.5 (tested on windows)
    Date           : March 2016
    Last Update    : April 2016
    Copyright      - none
.LINK
    Script posted over:
    github.com/gajuambi/python
'''
open("report.html","w+")
with open("report.html","a") as myfile:
    file = myfile.write
    #The Main Script
    file('<!DOCTYPE html>')
    file('<html>')
    file('<head>')
    file('<title>Windows Audit</title>')
    file('<style>')
    file('p{')
    file('font-size: 74%;')
    file('font-family: Calibri, Times, serif;')
    file('color: #196aa5;')
    file('text-align: left;')
    file('padding-left: 3px;')
    file('padding-right: 3px;')
    file('}')
    file('th{')
    file('font-size: 77%;')
    file('font-family: Arial, Helvetica, sans-serif;')
    file('color: #196aa5;')
    file('text-align: left;')
    file('padding-left: 3px;')
    file('}')
    file('</style>')
    file('</head>')
    file('<body bgcolor="#f8f8f8">')
    
    file('<table style="border:2px solid black" width=100% bgcolor="#005a9c" cellspacing="0" cellpadding="0"><tr><td><font face="Calibri, Times, serif" size="2" color="#ffffff"><a id=section_1></a><h2><i><center>Windows Audit</center></i></h2></td></tr></table>')
    #main indenting/enclosing table
    file('<table style="border:1px solid black" width="100%" bgcolor="white" cellspacing="0" cellpadding="0"<tr><td>')
    #a #ffffff separator between the main&data table 
    file('<table style="border:1px solid #ffffff" width="100%" bgcolor="white" cellspacing="0" cellpadding="0"<tr><td>')
    #data table
    file('<table style="border:1px solid black" width="100%" bgcolor="white" cellspacing="0" cellpadding="0">')
    #colors from http://www.color-hex.com/
    file('<th style="border:1px solid black">Hostname</th>')
    file('<th style="border:1px solid black">Domain</th>')
    file('<th style="border:1px solid black">IP</th>')
    file('<th style="border:1px solid black">Platform</th>')
    file('<th style="border:1px solid black">Total CPU</th>')
    file('<th style="border:1px solid black">Memory(GB)</th>')

    ##data for the headers##
    import socket, platform, multiprocessing, os, sys
    
    hostname = socket.gethostname()
    #domain name
    a = socket.getfqdn()
    b = a.split('.')
    del b[0]
    domain = ".".join(b)

    IP = socket.gethostbyname(hostname)
    System = platform.system()
    Release = platform.release()
    Version = platform.version()
    Ccores = multiprocessing.cpu_count()
    #calcuate memory
    from ctypes import Structure, c_int32, c_uint64, sizeof, byref, windll
    class MemoryStatusEx(Structure):
        _fields_ = [
            ('length', c_int32),
            ('memoryLoad', c_int32),
            ('totalPhys', c_uint64),
            ('availPhys', c_uint64),
            ('totalPageFile', c_uint64),
            ('availPageFile', c_uint64),
            ('totalVirtual', c_uint64),
            ('availVirtual', c_uint64),
            ('availExtendedVirtual', c_uint64)]
        def __init__(self):
            self.length = sizeof(self)
    m = MemoryStatusEx()
    assert windll.kernel32.GlobalMemoryStatusEx(byref(m))
    TotalMemory = (round(m.totalPhys / (1024.)**3))

    #architecture
    def machine():
        """Return type of machine."""
        if os.name == 'nt' and sys.version_info[:2] < (2,7):
            return os.environ.get("PROCESSOR_ARCHITEW6432", 
                   os.environ.get('PROCESSOR_ARCHITECTURE', ''))
        else:
            return platform.machine()
    
    def os_bits(machine=machine()):
        """Return bitness of operating system, or None if unknown."""
        machine2bits = {'AMD64': 64, 'x86_64': 64, 'i386': 32, 'x86': 32}
        return machine2bits.get(machine, None)
    z = os_bits()
    y = "bit"
    architecture = "{0} {1}".format (z, y)


    
    #fill the data under the headers created before in new rows and new cells
    #start of a new row
    file("<tr>")
    
    #adding data to the respective columns
    file("<td style='border:1px solid black'>")
    file("<p>%s</p>"%hostname) 
    file("</td>")

    file("<td style='border:1px solid black'>")
    file("<p>%s</p>"%domain) 
    file("</td>")
    
    file("<td style='border:1px solid black'>")
    file("<p>%s</p>"%IP)
    file("</td>")
    
    file("<td style='border:1px solid black'>")
    file("<p>%s %s (Build %s) %s </p>"%(System,Release,Version,architecture))
    file("</td>")
    
    file("<td style='border:1px solid black'>")
    file("<p>%s</p>"%Ccores)
    file("</td>")
    
    file("<td style='border:1px solid black'>")
    file("<p>%s</p>"%TotalMemory)
    file("</td>")

    #end of row
    file("</tr>")
    
    #Ending & fixing the position of the table
    file("</td></tr></table>")
    file("</td></tr></table>")
    file("</td></tr></table>")
    file("<br>")
