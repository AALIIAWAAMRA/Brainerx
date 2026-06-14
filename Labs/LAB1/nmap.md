# wha is nmap ?
```
- nmap is short for networek mapper it open source linux commande-line tool that is ised to scan ip @ and port in networek and detecet installed application
- nmap allowes admins to find wich devices are runing on their networek discover open ports and services  and detect vlunrabilities
```

## what is a port scan 

```
port scan is a technique attacker use to discover open or week doors in 
networek 
```

### port scan technique

1) pings scan ==>  sends a verious numner of ICMP request in an attempt to get resppons 
2) vanillascan ==> attempt to connect to all ports from 65,536 is send synchornize (SYN) flag
when it recive  SYN-ACK response it respponde with ACK 
3) SYN scan ==> also called half open scan it send SYN flag to target and wait for a SYN-ACK reponse in the case of response the nmap dosen't reply with ACK 
flag wich means the TCP connection dosen't logged
4) XMAS scan ==> it called chrismas scan because nmap rise 3 flag at same time 
FIN , PSH , URG  (in wirsharek it appear litted like the chrsmas tree )
the purpose it to send unlogical packet (not logical to request and at the same time urget  the recive of  packet   eand also push it  )
   ```
   how actualy nmap recognise the port status 
      - if the port is closed the target OS will reply with RST packet 
      - if the port is open the OS will ignore the packet and dosen't reply 
   ```
5) the nmap will send the TCP packet continu only one packet FIN 
the purpose send unexpectd  packet to know the bahvioure of the port 
   ```
   how actualy nmap recognise the port status 
      - if the port is closed the target OS will reply with RST packet 
      - if the port is open the OS will ignore the packet and dosen't reply 
   ```
## Note
   XMAS and FIN scan fill in windows OS because windows 
   dosen't floow this part of the standrand RFC 793 
6) FTP bounes scna  ==>  in the normal case whn you whant to scan port of a target the pacet exit your device striat forwared to the target pc if there is a firewall or 
IDS it will log your ip or even drop the packet before rich the target 
but in  FTP bounes you will not directly connect with target  instead you will lock for FTP server (FTP Proxy ) and then ask him to scan and attack the target 
```
   nmap -b username:password@FTP_Server_IP:Port Target_IP
```
7) Sweep Scan ==> -sn instead of scan single host it scan sevreal host 
   - if you are at the LAN it will send ARP request 
   - if you are in external networek he will send 
      1) ICMP echo request
      2) ICMP timestamp request 
      3) TCP SYN 
      4) TCP ACK


---------
scaning TCP and UDP 

some times you need to scan TCP and UDP the default scan is TCP 
but you can scan both bY :
   nmap -sT -sU target_ip


-------------
TLS Fingerprinting ==> help me in  create a digital fingerprint to the server or the client 
based on TLS features (server Hello , certifcat , cipher suite) in order to know the technology , the hiden servicce , the versions ....
most comuun TLS Fingerprinting is a JA3 Fingerprinting it convert  client hello to hash 

exaple 769,47-53-5-10,... to e7d705a3286e19ea42f587b344ee6865

this hash might lead to know is it  Chrome , Firefox , Curl , Malware , Metasploit 

JA3S is for the srever and it focus in server hello 


-----------------

## TCP Headers  (FLAGS)


1) SYN (synchronize) => initaite a connection 
SYN is a TCP packet  sent to another coumputer to request establish connection 
between them

2) URG (urgent) => packet to be processed immedaitly
data inside segment with flag URG =1  is forword to application layer immeditly 
even if there more data to be given to application layer  ( notify the reciver to process the urgent packet before procesing all the packet)

3) ACK => acknolgemnt recive data 
indicate that data has been recived sucessfly 

4) PSH => Transmits data immidetly 
the TCP push flag is used to indicate that the reciveing device shold deliver the data to the reciving application as soon as possible  rather then buffering it 

5) FIN =>  Closes a connection 
TCP packet are sent to close a connection . 

6) RST  => Aborts (cut) Connection in reponse to an error
a packet with "Rest" flag are  sent to cut a connection 



