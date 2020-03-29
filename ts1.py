import sys
import threading
import time
import random
import socket as mysoc

# server task
def server():
  
    # Getting port in which rs listens to requests
    ts1ListenPort = int(sys.argv[1])

    # Fetching and storing DNS table data in list of lists
    with open("PROJ2-DNSTS1.txt") as file_in:
      dns_table = []
      for line in file_in:
          dns_table.append(line.strip().split(" "))
    print(dns_table)        
          
    
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created on port "+ str(ts1ListenPort))
    except mysoc.error as err:
        print(format("socket open error ",err))

    #print("DNS table: ",dns_table)


    server_binding=('',ts1ListenPort)
    ss.bind(server_binding)
    ss.listen(2)

    # Getting hostname of current machine
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    print ("[S]: Got a connection request from a client at", addr)
    
    c =[]

    while True:
      stream = ''
      # Initially setting new_msg flag to true
      new_msg = True
      while True:
      # Recieving header info of data sent from clieent
        data = csockid.recv(20).decode('utf-8')
        
        
        if new_msg:
            #print("new msg len:",data[:10])
            ###print("msglen preview:",len(data[:10]))
            try:
              # Obtaining headersize from stream
              msglen = int(data[:10])
            except ValueError:
              break
            new_msg = False

        #print(f"full message length: {msglen}")
        
        stream += data

        ###print(len(stream))


        if len(stream)-10 == msglen:
            #print("full msg recvd:")
           
            #print(stream[10:])
            recieved_hostname=stream[10:]
            #print(recieved_hostname)
            e = dns_LookUp(recieved_hostname,dns_table)
            # Sending back either A record or NS record back to client
            
            if (e is not None):
                csockid.send(e.encode('utf-8'))


            # Resetting buffer
            new_msg = True
            stream = ""

      break



   # Close the server socket
    ss.close()
    exit()


# Does a DNS lookup in table for given hostname
def dns_LookUp(hostname,dns_table):
  for entries in dns_table:
    #print(entries[0])
    if (hostname.lower() == entries[0].lower()) and (entries[1] != "-"):
      
      #print("{} {} A".format(entries[0],entries[1]))
      #print("Found in TS!")
      return "{} {} A".format(entries[0],entries[1])

  #print("Not found in TS!")
    
    
  #return "{} - Error:HOST NOT FOUND".format(hostname)

  
  # Entry not found -- must direct to TS server

  # Find entry with NS record

  '''
  for entries in dns_table:
    if (entries[1] == "-"):
      #print("Not Found in TS!")
      return "{} - Error:HOST NOT FOUND".format(entries[0])
'''

server()