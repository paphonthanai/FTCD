import urllib2

filedata = urllib2.urlopen('http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg')
datatowrite = filedata.read()
 
with open('/Users/scott/Downloads/cat2.jpg', 'wb') as f:
    f.write(datatowrite)