#!../src/Python-2.7.12/.localpython/bin/python2

import cgi, cgitb
cgitb.enable()

#form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n" 
arguments = cgi.FieldStorage()
nbrOfLines = 1000
file = str(arguments['f'].value).strip()
c=0


# Header
print(
	"""
	<p>File: """ + file.split('user_data/')[1] + """</p>
	<p>(showing first """ +str(nbrOfLines)+ """ lines)</p>
	<p><pre>***********************************************************</pre></p>
	"""
	)

# File
with open(file) as file:
	print('<pre>')
	for line in file:
		print line.strip()
		c+=1
		if c == nbrOfLines: break
	print('</pre>')






'''
<?php

$file = $_GET['f'];

$nbrOfLines = 1000;

$command = 'head -'. $nbrOfLines .' ../user_data/'. $file;

$preview = shell_exec($command);

echo '
	<p>File: '. $file .'.</p>
	<p>(showing first '. $nbrOfLines .' lines)</p>
	<p><pre>***********************************************************</pre></p>
	<pre>'. htmlentities($preview) .'</pre>
';

?>
'''