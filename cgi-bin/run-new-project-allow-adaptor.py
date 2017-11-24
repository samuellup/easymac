#!src/Python-2.7.12/.localpython/bin/python2

import cgi, cgitb, subprocess
cgitb.enable()

subprocess.call("./easymap.sh " + master_program_input, shell=True)
proc = subprocess.Popen("../src/Python-2.7.12/.localpython/bin/python2 allow-new-project.py", cwd=r'./config', shell=True, stdout=subprocess.PIPE)










# Fill html file
print "Content-type:text/html\r\n\r\n"