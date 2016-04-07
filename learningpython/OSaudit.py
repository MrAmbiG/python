open("report.html","w")
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
    file('<th style="border:1px solid black">IP</th>')
    file('<th style="border:1px solid black">Platform</th>')
    file('<th style="border:1px solid black">Cpu Cores</th>')

    #data for the headers above
    import socket, platform, multiprocessing
    
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    System = platform.system()
    Release = platform.release()
    Version = platform.version()
    Ccores = multiprocessing.cpu_count()
    
    #fill the data under the headers created before in new rows and new cells
    #start of a new row
    file("<tr>")
    
    #adding data to the respective columns
    file("<td style='border:1px solid black'>")
    file("<p>%s</p>"%hostname) 
    file("</td>")
    
    file("<td style='border:1px solid black'>")
    file("<p>%s</p>"%IP)
    file("</td>")
    
    file("<td style='border:1px solid black'>")
    file("<p>%s %s (Build %s)</p>"%(System,Release,Version))
    file("</td>")
    
    file("<td style='border:1px solid black'>")
    file("<p>%s</p>"%Ccores)
    file("</td>")

    #end of row
    file("</tr>")
    
    #Ending & fixing the position of the table
    file("</td></tr></table>")
    file("</td></tr></table>")
    file("</td></tr></table>")
    file("<br>")
