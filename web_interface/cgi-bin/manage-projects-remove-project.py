#!../src/Python-2.7.12/.localpython/bin/python2

import cgi, cgitb
cgitb.enable()

#form = cgi.FieldStorage()

arguments = cgi.FieldStorage()
folder = str(arguments['p'].value).strip()

os.rmdir(folder)




'''
<?php

$project = $_GET['p'];

$command = 'rm -rf --recursive ../user_projects/'. $project;

shell_exec($command);

?>
'''