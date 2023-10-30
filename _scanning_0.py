from socket import *
import time

start_time = time.time() # Initial time of the code

if __name__ == "__main__":
    target = input("Enter host for scanning:")
    t_ip = gethostbyname()
    print("Starting scanninig on host:", t_ip)

    for i in range(50,500):
        s = socket(AF_INET,SOCK_STREAM)
        
        conn = s.connect_ex((t_ip,i))    
        if (conn == 0):       # Port open
            print('Port %d: OPEN' %(i,))
        s.close()

print("Time taken :",time.time() - start_time)
