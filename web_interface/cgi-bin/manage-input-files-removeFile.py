#!../src/Python-2.7.12/.localpython/bin/python2

import cgi, cgitb, os
cgitb.enable()

#form = cgi.FieldStorage()

arguments = cgi.FieldStorage()
file = str(arguments['f'].value).strip()
os.remove(file)

'''
<?php

$file = $_GET['f'];

$command = 'rm ../user_data/'. $file;

shell_exec($command);

?>
'''