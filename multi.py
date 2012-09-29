from multiprocessing import Pool
import urllib2
line= [line.strip() for line in open('url.txt')]
#urlFile.close()
def f(x):
    res = urllib2.urlopen(x)
    print x
    return res.headers()

if __name__ == '__main__':
    pool = Pool(processes=8)              # start 4 worker processes
    print pool.map(f, line)          # prints "[0, 1, 4,..., 81]"
