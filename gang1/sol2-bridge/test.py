import sys 
import log_bridge as lb
import socket

sock1, sock2 = socket.socketpair()

# handler = lb.FileHandler(sys.stdout)
handler = lb.SocketHandler(sock1)


logger = lb.FilteredLogger('Error', handler)

logger.log('Ignored: this will not be logged')
logger.log('Error: this is important')

print('The socket received: %r' % sock2.recv(512))