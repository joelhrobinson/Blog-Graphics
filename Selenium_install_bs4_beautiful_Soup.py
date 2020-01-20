# fails
# fails
# fails
import urllib
import tarfile
import os
url = 'http://pypi.python.org/packages/source/b/beautifulsoup4/beautifulsoup4-4.1.3.tar.gz'
file_name = url.split('/')[-1]
u = urllib.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print ("Downloading: %s Bytes: %s" % (file_name, file_size) )
file_size_dl = 0
block_sz = 4096
while True:
	buffer = u.read(block_sz)
	if not buffer:
		break
	file_size_dl += len(buffer)
	f.write(buffer)
	status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	status = status + chr(8)*(len(status)+1)
	print (status)
print ('\n')
f.close()
tar = tarfile.open(file_name,'r')
for items in tar:
	tar.extract(items,'bs4')
os.chdir('bs4')
os.chdir('beautifulsoup4-4.1.3')
os.system('python setup.py install')
print ('\nBeautifulSoup should now be installed. If not, check if the python executable is in your PATH.')