import socket as mysoc
import sys


#client task
def client():
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print(format("socket open error ",err))
  #python client.py rsHostname rsListenPort tsListenPort
  
  # Defining the port on which you want to connect to the LS server
    lsport = int(sys.argv[2])
  # Defining hostname for LS server
    ls_hostName = mysoc.gethostbyname(sys.argv[1])
    ## For testing purposes
    #rs_hostName = mysoc.gethostbyname(mysoc.gethostname())
    #print(rs_hostName)

  # Connecting to the LS server
    server_binding=(ls_hostName,lsport)
    cs.connect(server_binding)

    rmsgs = []
    hns = []
    

  # Reading PROJ2-HNS.txt file and storing each line as an element in the Hostnames list
    hns = [line.rstrip('\n') for line in open('PROJ2-HNS.txt')]
    i=0
  # Writing returned records to RESOLVED.txt file
    f = open("RESOLVED.txt","w+")

    while i in range(len(hns)):
      #print(i)
    # Creating a header in order to specify number of characters in each line to server
      full = ("{:<10}".format(len(hns[i]))+hns[i])
      #print(full)
    # Sending the word to server
      print("[C]: Client sending hostname through Socket:: ",hns[i])
      # Sending hostname to LS server
      cs.send(full.encode())

    # Receiving data back from the server
      data_from_server = cs.recv(1024).decode('utf-8')
      print("data from server: "+ str(data_from_server))

    # Splitting data into a list
      data_list = data_from_server.split(" ")

    # Checking if data recieved is an A record or Hostname - Error:HOST NOT FOUND
      if (data_list[2] == "A"):
        # Is A record, can write data to output file
        f.write(str(data_from_server)+"\n")
      else:
        # Is an error, can write data to output file
        f.write(str(data_from_server)+"\n")   
        
        
   
      i = i+1

# closing the client socket
    cs.close()
    exit()

#def tlsSocketConnections():



client()