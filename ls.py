# Recieve hostname query 
# Start timeout interval of about 7 seconds
# Send query to TS1
#   If entry found, respond back 
# Send query to TS2
#   If entry found, respond back
# If timeout achieved, send error string to client
# Otherwise send record back to client


import sys
import threading
import time
import random
import socket as mysoc

def queryTS1(s1,hostname):
  hostname = str(hostname)
  full = ("{:<10}".format(len(hostname))+hostname)

  #print(full)
  # Sending the word to TS1 server
  print("[LS]: LS sending hostname to TS1 through Socket:: " + str(hostname))
  # Sending hostname to LS server
  s1.send(full.encode("utf-8"))
  # Setting timeout interval
  s1.settimeout(7)
  timeoutflag = 0
  stream = ''
      # Initially setting new_msg flag to true
  new_msg = True
  while True:
    try:
      # Recieving header info of data sent from client
      data = s1.recv(20).decode('utf-8')
    except mysoc.timeout:
      # Could not find entry, thus timeout
      # Setting timeout flag to 1
      timeoutflag = 1
      print("timed out!")
      return str(hostname)+" - Error:HOST NOT FOUND"
      
        
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


    if (len(stream)-10 == msglen) or (timeoutflag == 1):
        #print("full msg recvd:")
        if (timeoutflag == 1):
          # Sending error message
          #s1.send("Hostname - Error:HOST NOT FOUND".encode('utf-8'))
          return str(hostname)+" - Error:HOST NOT FOUND"
        else: #print(stream[10:])
          recieved_hostname=stream[10:]
          #print(recieved_hostname)
          print("ls got word from ts1:", recieved_hostname)
          # Sending back either A record to client
          return str(recieved_hostname)

        # Resetting buffer
        new_msg = True
        stream = ""



def queryTS2(s2,hostname):
  hostname = str(hostname)
  full = ("{:<10}".format(len(hostname))+hostname)

  #print(full)
  # Sending the word to TS1 server
  print("[LS]: LS sending hostname to TS2 through Socket:: " + str(hostname))
  # Sending hostname to LS server
  s2.send(full.encode("utf-8"))
  # Setting timeout interval
  s2.settimeout(7)
  timeoutflag = 0
  stream = ''
      # Initially setting new_msg flag to true
  new_msg = True
  while True:
    try:
      # Recieving header info of data sent from client
      data = s2.recv(20).decode('utf-8')
    except mysoc.timeout:
      # Could not find entry, thus timeout
      # Setting timeout flag to 1
      timeoutflag = 1
      print("timed out!")
      return str(hostname)+" - Error:HOST NOT FOUND"
      
        
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


    if (len(stream)-10 == msglen) or (timeoutflag == 1):
        #print("full msg recvd:")
        if (timeoutflag == 1):
          # Sending error message
          #s1.send("Hostname - Error:HOST NOT FOUND".encode('utf-8'))
          return str(hostname)+" - Error:HOST NOT FOUND"
        else: #print(stream[10:])
          recieved_hostname=stream[10:]
          #print(recieved_hostname)
          print("ls got word from ts1:", recieved_hostname)
          # Sending back either A record to client
          return str(recieved_hostname)

        # Resetting buffer
        new_msg = True
        stream = ""



# server task
def server():
  
    # Getting port in which LS listens to requests
    lsListenPort = int(sys.argv[1])

    # Socket to Client
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created on port "+ str(lsListenPort))
    except mysoc.error as err:
        print(format("socket open error ",err))
    
    server_binding=('',lsListenPort)
    ss.bind(server_binding)
    ss.listen(6)

    # Getting hostname of current machine
    host=mysoc.gethostname()
    print("[S]: LS Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: LS Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    print ("[S]: Got a connection request from a client at", addr)

    # Socket to TS1
    try:
        s1=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created on port "+ str(lsListenPort))
    except mysoc.error as err:
        print(format("socket open error ",err))

      # Socket to T2
    try:
        s2=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created on port "+ str(lsListenPort))
    except mysoc.error as err:
        print(format("socket open error ",err))



    ts1Hostname = mysoc.gethostbyname(sys.argv[2])
    ts1ListenPort =  int(sys.argv[3])
    ts2Hostname =  mysoc.gethostbyname(sys.argv[4])
    ts2ListenPort =  int(sys.argv[5])

    server_binding=(ts1Hostname,ts1ListenPort)
    s1.connect(server_binding)
    print("Connected to TS1")
    
    server_binding=(ts2Hostname,ts2ListenPort)
    s2.connect(server_binding)
    print("Connected to TS2")

    

    

  



    c =[]
    timeoutflag = 0
    while True:
      stream = ''
      # Initially setting new_msg flag to true
      new_msg = True
      while True:
        # Recieving header info of data sent from client
        
        
        data = csockid.recv(20).decode('utf-8')
        if new_msg:
            print("new msg len:",data[:10])
            print("msglen preview:",len(data[:10]))
            try:
              # Obtaining headersize from stream
              msglen = int(data[:10])
            except ValueError:
              break
            new_msg = False

        #print(f"full message length: {msglen}")
        
        stream += data

        ###print(len(stream))


        if (len(stream)-10 == msglen) or (timeoutflag == 1):
            #print("full msg recvd:")
            if (timeoutflag == 1):
              # Sending error message
              #csockid.send("Hostname - Error:HOST NOT FOUND".encode('utf-8'))
              print()
            else:
              recieved_hostname=stream[10:]
              print("got word:", recieved_hostname)
              s1word = queryTS1(s1,recieved_hostname)
              print(s1word)
              if ("Error:HOST NOT FOUND" in s1word):
                s2word = queryTS2(s2,recieved_hostname)
                csockid.send(s2word.encode("utf-8"))
              else: 
                csockid.send(s1word.encode("utf-8"))

              
              

              # Sending back either A record to client
              #csockid.send(recieved_hostname.encode('utf-8'))

            # Resetting buffer
            new_msg = True
            stream = ""



      return 
      


   # Close the server socket
    ss.close()
    exit()

server()
