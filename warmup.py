import urllib2
import threading
import time
response = urllib2.urlopen('http://shop.sportlaedchen.de')
print response.headers
