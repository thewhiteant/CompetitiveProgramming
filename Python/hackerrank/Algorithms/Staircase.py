from pip._vendor.distlib.compat import raw_input
from pip._vendor.msgpack.fallback import xrange

n = int(raw_input())
s = '#'
for i in xrange( 1 , n+1):
    print (" "*(n-i) + s*i)