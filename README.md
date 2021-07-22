# project-tools
flask script for GUI-based Nmap execution

Nmap: A popular reconnaisance tool, which allows user to scan a target IP with various types of scans like TCP (syn) scan, TCP connect scan, UDP scan, SCTP INIT scan, FIN scan, NULL scan, Xmas scan etc.

In this project we have 
  1. SYN-ACK Scan
  2. UDP Scan
  3. Comprehensive Scan
  4. Regular Scan
  5. Ping Scan

The basic execution requires to setup the flask virtual environment.
Then run $output.py. The program will be executed in the terminal itself.
Once the execution starts, you will be asked to enter the target IP address. After that select the option number for the type of scan, and wait for the output. 

**Note: 1. Depending upon your internet speed, system performance and the type of scan you have chosen, the time for the scan will vary. But approx. 3-4 minutes maximum waiting              time has been observed.
        2. The scans won't work properly if the target system has active firewall.
        3. Using this scan against any private target without legal permission is a punishable offence, so follow proper protocols to use it.
        
Future scope: To implement OS detection scan in this model.
