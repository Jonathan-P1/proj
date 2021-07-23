from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('zzz', '555', '.', perm='elradfmwMT')
    
    handler = FTPHandler
    handler.authorizer = authorizer
    
    handler.banner = "pythonftpdlib based ftpd ready."
    
    address = ('192.168.0.10', 21)
    server = FTPServer(address, handler)
    
    server.max_cons = 10
    server.max_cons_per_ip = 1
    
    server.serve_forever()
    
if __name__ == '__main__':
    main()
    