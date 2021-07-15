# import sys
import socket
from filtered_logger import FilteredLogger
from file_like import FileLikeSocket
from file_like import FileLikeSyslog


sock1, sock2 = socket.socketpair()

fs = FileLikeSocket(sock1)
# fs = FileLikeSyslog(1)
logger = FilteredLogger('Error', fs)
logger.log('Warning: message number one')
logger.log('Error: message number two')

print('The socket received: %r' % sock2.recv(512))