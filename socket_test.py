#ValueError: Extra data: line 1 column 172 - line 1 column 226 (char 172 - 226)
# two dict dumps have been merged into one string

import socket as s; a=s.socket(s.AF_INET,s.SOCK_STREAM); 
import sys
import pdb

req = '{"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}'
#creat TCP,   address, timeout, source_address
#a=s.create_connection(("localhost", 9090),10, ("",0)) 
try:
  a=s.create_connection(("localhost", 9092))
except: 
  (ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
  (errno, err_msg) = ErrorValue
  print "failed: %s, errno=%d" % (err_msg, errno)

a.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
a.send(req)
#a.setblocking(False)  settimeout is better
a.settimeout(3)

b=None
try:
 b = a.recv(4096)
except:
 (ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
 (errno, err_msg) = ErrorValue
 print "failed: %s, errno=%d" % (err_msg, errno)
