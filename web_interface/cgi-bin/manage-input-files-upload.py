#!/usr/bin/python

### !../src/Python-2.7.12/.localpython/bin/python2

import cgi, os, shutil
import cgitb; cgitb.enable()
import gzip

'''
try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    #pass
    with open('out.txt', 'w') as out:
		out.write('module missing')
'''

form = cgi.FieldStorage()



# Generator to buffer file chunks
def fbuffer(f, chunk_size=10000):
	while True:
		chunk = f.read(chunk_size)
		if not chunk:
			break
		yield chunk


# A nested FieldStorage instance holds the file
fileitem = form['file']
fileName = form['name'].value
currentChunk = form['chunk'].value
currentChunkOneBased = str(int(currentChunk) + 1)
totalChunks = str(form['chunks'].value)

testOut = open('out.txt', 'a')


# Test if the file was uploaded
if fileitem.filename:
	# strip leading path from file name to avoid directory traversal attacks
	fn = os.path.basename(fileitem.filename)
	f = open('tmp_upload_files/' + fn, 'ab', 10000)

	# Read the file in chunks
	for chunk in fbuffer(fileitem.file):
		f.write(chunk)
	f.close()
	message = 'The file "' + fn + '" was uploaded successfully'
else:
	message = 'No file was uploaded'


testOut.write(currentChunk + ', ' + currentChunkOneBased + ', ' + totalChunks + ', ')

if currentChunk == str(int(totalChunks) - 1):
	testOut.write('yes\n')

	if fileName[-3:] == '.gz':
		testOut.write('file is .gz\n')
		inF = gzip.open('tmp_upload_files/blob', 'rb')
		outF = open('tmp_upload_files/' + fileName[:-3], 'wb')
		outF.write(inF.read())
		inF.close()
		outF.close()

		os.remove('tmp_upload_files/blob')
		shutil.move('tmp_upload_files/' + fileName[:-3], '../user_data/' + fileName[:-3])

	else:
		shutil.move('tmp_upload_files/blob', '../user_data/' + fileName)

else:
	testOut.write('no\n')


testOut.close()



print 'Content-Type: text/html'
print ''
print '{"jsonrpc" : "2.0", "result" : null, "id" : "id"}'


