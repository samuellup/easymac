#!../src/Python-2.7.12/.localpython/bin/python2

import cgi, cgitb
cgitb.enable()

#form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n" 
print "" 

arguments = cgi.FieldStorage()
for i in arguments.keys():
	if i == 'f':
		print arguments[i].value



'''
<?php

$file = $_GET['f'];

$command = 'rm ../user_data/'. $file;

shell_exec($command);

?>
'''