import socket
import sys 

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #ip = socket.gethostbyaddr("www.github.com")
    #ip = socket.gethostbyname("")## Place some web address to Know the ip address
    #print(ip)
    print("Socket Succesfully created")

except socket.error as err:
    print(f"Socket creation failes{err}")

port = 80
try:
    host_ip = socket.gethostbyname("")

except socket.gaierror:
    print('error resolving  the host')
    sys.exit()

s.connect((host_ip,port))
print(f"Socket has succesfully connectef to wensite on port == {host_ip}")
