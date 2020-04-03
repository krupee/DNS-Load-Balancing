1. Please write down the full names and netids of all your team members.
Zain Siddiqui (zas30) & Krupal Patel (kp766)

2. Briefly discuss how you implemented the LS functionality of tracking which TS responded to the query and timing out if neither TS responded.
Once the LS server receives a query from the client server, it sends the query to both of the TS servers. After sending the respective queries, the server waits for five seconds. If within these five seconds, the LS server receives a response then this response, including the A record and hostname of the respective TS server holding the record, is sent back to the Client server. If five seconds have passed without any response from the TS servers, then a timeout is achieved and the Client server receives an error message including the original hostname that was sent from the LS server. Ultimately, this functionality was achieved through a query function for each TS server defined in the LS server. This function handled the querying of both TS servers simultaneously and communicated with the Client server.

3. Are there known issues or functions that aren't working currently in your attached code? If so,
explain.
After testing the code with various test cases, there seems to be no known issues with regard to the functionality of the code. We both tested our code on multiple hosts and did sample testing other than the test already provided to us to assure our code was working correctly. 

4. What problems did you face developing code for this project?
The client file was pretty straightforward. For both TS1 and TS2 we did not have many problems because the logic was similar to that of the last project where we searched for the correct hostname in the DNS file for the corresponding TS file. The part where we faced the most problems was figuring out how to timeout on receive calls. We first tried to implement it without a timeout which would be very difficult because we need an indication that the TS failed and that we should move on to the next one. Creating a system that detected this was our main problem, but we solved it using timeout logic to create two recv calls and use time to indicate a success or failure on a TS.

5. What did you learn by working on this project?
We learned how to implement a server that takes in a connection from a client and establishes a connection with two other servers. We also obtained a better understanding of how sockets are used to connect multiple endpoints and relay data through a buffer stream. Furthermore, we learned how to handle situations where we might not receive any data back from a connection and correctly timeout. Ultimately, this project helped us understand how to be more flexible when creating an application that requires us to work with multiple connections and sending data in parallel.
