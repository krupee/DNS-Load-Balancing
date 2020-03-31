1. Please write down the full names and netids of all your team members.
Zain Siddiqui (zas30) & Krupal Patel (kp766)

2. Briefly discuss how you implemented the LS functionality of tracking which TS responded to the
query and timing out if neither TS responded.
Implemented a query function for each TS server in LS that does a recv call on each TS server and waits.

3. Are there known issues or functions that aren't working currently in your attached code? If so,
explain.
After testing the code with various test cases, there seems to be no known issues with regard to the functionality of the code.

4. What problems did you face developing code for this project?
Figuring out how to timeout on recieve call.

5. What did you learn by working on this project?
Learned how to implement a server that takes in a connection from a client and establishes a connection with two other servers. Obtained a better understanding of how sockets are used to connect multiple endpoints and relay data through a buffer stream.