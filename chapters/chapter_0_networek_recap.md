# 🔐 Introduction to Cybersecurity
### BrainerX ComptaiSec+ — 2026-05-23

---

> **Course Duration:** 3 Hours  
> **Format:** Lecture + Practical Lab  
> **Prerequisites:** Basic networking knowledge, familiarity with Linux terminal  
> **Tools Required:** Linux/Kali Linux, Wireshark, Nmap, Browser with DevTools  

---

## 📋 Table of Contents

| # | Module | Duration |
|---|--------|----------|
| 1 | Introduction to Cybersecurity | 20 min |
| 2 | The OSI Model — Layers and Protocols | 30 min |
| 3 | The TCP/IP Model — Practical View | 25 min |
| 4 | Core Protocols: TCP, UDP, ICMP | 20 min |
| 5 | DNS — Domain Name System | 20 min |
| 6 | HTTP, HTTPS, and the SSL/TLS Handshake | 25 min |
| 7 | Lab 2 — Network Scanning with Nmap | 40 min |
| — | Review, Q&A, and Wrap-Up | 10 min |

---

## ⏱️ HOUR 1 — Foundations and Network Models

---

## Module 1 — Introduction to Cybersecurity (20 min)

### 1.1 What is Cybersecurity?

**Cybersecurity** is the practice of protecting systems, networks, programs, and data from digital attacks, unauthorized access, damage, or destruction. It encompasses technologies, processes, and practices designed to defend computers, servers, mobile devices, electronic systems, and data.

Modern cybersecurity operates across several domains:
- **Network Security** — protecting the infrastructure
- **Application Security** — securing software and apps
- **Information Security** — protecting data integrity and privacy
- **Operational Security** — processes and decisions for handling data
- **Endpoint Security** — securing individual devices
- **Cloud Security** — protecting cloud-based assets

---

### 1.2 The CIA Triad

The **CIA Triad** is the foundational model for information security:

```
          ┌─────────────────────────────────┐
          │         CIA TRIAD               │
          │                                 │
          │    C — Confidentiality          │
          │    I — Integrity                │
          │    A — Availability             │
          │                                 │
          └─────────────────────────────────┘
```

| Principle | Definition | Attack that violates it |
|-----------|-----------|------------------------|
| **Confidentiality** | Data is accessible only to authorized parties | Eavesdropping, data breach, MITM |
| **Integrity** | Data is accurate and has not been tampered with | Man-in-the-Middle, data injection |
| **Availability** | Systems and data are accessible when needed | Denial of Service (DoS), ransomware |

> 📌 give a real-world example that violates each principle before proceeding.

---

### 1.3 Types of Threats and Attackers

#### Threat Categories

| Threat Type | Description | Example |
|-------------|-------------|---------|
| **Malware** | Malicious software | Virus, Worm, Trojan, Ransomware |
| **Phishing** | Social engineering via fake messages | Fake bank email |
| **Man-in-the-Middle (MITM)** | Intercepting communication | ARP spoofing on LAN |
| **Denial of Service (DoS/DDoS)** | Overwhelming a service | Flooding a server |
| **SQL Injection** | Injecting malicious DB queries | Bypassing login forms |
| **Zero-Day Exploit** | Attack on unknown vulnerabilities | Stuxnet |
| **Insider Threat** | Attack from within | Disgruntled employee |

#### Types of Attackers (Threat Actors)

- 🟢 **White Hat** — Ethical hackers, authorized penetration testers
- ⚫ **Black Hat** — Malicious attackers with criminal intent
- 🩶 **Grey Hat** — Find vulnerabilities without permission, may or may not cause harm
- 🌐 **Nation-State** — Government-sponsored cyber warfare units
- 💰 **Cybercriminals** — Financially motivated organized groups
- 🧑‍💻 **Script Kiddies** — Inexperienced users using pre-built tools

---

### 1.4 The Attack Lifecycle (Cyber Kill Chain)

The **Lockheed Martin Cyber Kill Chain** describes the stages of a cyberattack:

```
  [1] Reconnaissance
         ↓
  [2] Weaponization
         ↓
  [3] Delivery
         ↓
  [4] Exploitation
         ↓
  [5] Installation
         ↓
  [6] Command & Control (C2)
         ↓
  [7] Actions on Objectives
```

Understanding this model helps defenders identify **where** and **when** to intervene.

---

![Cyber-Kill-Chain](./src/Cyber-Kill-Chain-7-stages-infographic.png)



---

### ✅ Module 1 — Review Questions

> **Q1.** Define the three components of the CIA Triad and give a real-world example for each.

> **Q2.** A hospital's patient database is encrypted by ransomware and becomes inaccessible. Which principle(s) of the CIA Triad are violated?

> **Q3.** What is the difference between a white hat and a grey hat hacker? Give an example scenario for each.

> **Q4.** In which phase of the Kill Chain does Nmap scanning fit? Justify your answer.

---

## Module 2 — The OSI Model (30 min)

### 2.1 Why Do We Need a Network Model?

Before the OSI model, different vendors built incompatible networking equipment. The **Open Systems Interconnection (OSI) model**, developed by the ISO in 1984, created a universal framework for how network communication should work — allowing devices from different manufacturers to communicate.

---

### 2.2 The 7 Layers of the OSI Model

```
┌─────┬─────────────────┬────────────────────────────────────────────┐
│ #   │ Layer Name      │ Function                                    │
├─────┼─────────────────┼────────────────────────────────────────────┤
│  7  │ Application     │ End-user interface (HTTP, FTP, SMTP, DNS)   │
│  6  │ Presentation    │ Data format, encryption, compression (SSL)  │
│  5  │ Session         │ Session management, authentication          │
│  4  │ Transport       │ End-to-end delivery, TCP/UDP, ports         │
│  3  │ Network         │ Routing, IP addressing, ICMP                │
│  2  │ Data Link       │ MAC addressing, framing, error detection    │
│  1  │ Physical        │ Cables, switches, bits, electrical signals  │
└─────┴─────────────────┴────────────────────────────────────────────┘
```

> 🧠 **Mnemonic (Top-Down):** "**A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing"

---

### 2.3 Layer-by-Layer Deep Dive

#### Layer 7 — Application Layer
- The **only layer** the end user directly interacts with
- Protocols: `HTTP`, `HTTPS`, `FTP`, `SMTP`, `POP3`, `IMAP`, `DNS`, `SNMP`, `SSH`, `Telnet`
- **PDU (Protocol Data Unit):** Data / Message

#### Layer 6 — Presentation Layer
- Handles **encoding, encryption, and compression**
- Translates data between application and network format
- Protocols/Standards: `SSL/TLS`, `JPEG`, `MPEG`, `ASCII`, `UTF-8`
- **PDU:** Data

#### Layer 5 — Session Layer
- Manages **sessions** (establishment, maintenance, termination)
- Handles **authentication** and **authorization**
- Protocols: `NetBIOS`, `RPC`, `PPTP`
- **PDU:** Data

#### Layer 4 — Transport Layer
- Provides **end-to-end** communication between processes
- **Port numbers** are defined at this layer
- **Flow control**, **error recovery**, **segmentation**
- Key protocols:
  - **TCP** (Transmission Control Protocol) — reliable, connection-oriented
  - **UDP** (User Datagram Protocol) — unreliable, connectionless, fast
- **PDU:** Segment (TCP) / Datagram (UDP)

#### Layer 3 — Network Layer
- Responsible for **logical addressing** and **routing**
- Determines the best path for data across networks
- Protocols: `IP (IPv4/IPv6)`, `ICMP`, `ARP`, `OSPF`, `BGP`
- **PDU:** Packet

#### Layer 2 — Data Link Layer
- Handles **physical addressing** (MAC address)
- Detects and corrects errors from Layer 1
- Two sublayers: **LLC** (Logical Link Control) and **MAC** (Media Access Control)
- Protocols: `Ethernet`, `Wi-Fi (802.11)`, `PPP`, `ARP`
- **PDU:** Frame

#### Layer 1 — Physical Layer
- Transmits raw **bits** over physical media
- Deals with: cables, fiber optics, radio frequencies, voltages
- Protocols/Standards: `USB`, `RS-232`, `Ethernet (physical)`, `DSL`, `Bluetooth`
- **PDU:** Bit

---

### 2.4 Data Encapsulation

As data travels **down** the OSI stack, each layer **wraps** the data with its own header (and sometimes trailer). This process is called **encapsulation**. The reverse happens on the receiving side (**decapsulation**).

```
Application   │ DATA                                         │
Presentation  │ DATA                                         │
Session       │ DATA                                         │
Transport     │ TCP/UDP Header │ DATA                        │
Network       │ IP Header │ TCP Header │ DATA                │
Data Link     │ Frame Header │ IP Hdr │ TCP Hdr │ DATA │ FCS│
Physical      │ 0101010101010101010101010101010101010101...  │
```

---

### 2.5 OSI vs Real-World — Where Attacks Happen

| Layer | Common Attack |
|-------|---------------|
| Application (7) | SQL Injection, XSS, HTTP Flood |
| Presentation (6) | SSL Stripping |
| Session (5) | Session Hijacking |
| Transport (4) | SYN Flood, Port Scanning |
| Network (3) | IP Spoofing, ICMP Flood |
| Data Link (2) | ARP Spoofing, MAC Flooding |
| Physical (1) | Cable tapping, Physical intrusion |

---

![](./src/0*s5-XKii40rAG0ykr)

---

### ✅ Module 2 — Review Questions

> **Q1.** At which OSI layer does a **router** primarily operate? What about a **switch**? A **hub**?

> **Q2.** A packet has a source IP address of `192.168.1.10` and destination IP `8.8.8.8`. At which OSI layer is this address information processed?

> **Q3.** Why is the Transport Layer important for cybersecurity? What specific information does it expose to an attacker?

> **Q4.** Match each protocol to its OSI layer: `HTTP`, `IP`, `TCP`, `SSL`, `Ethernet`, `DNS`, `ARP`.

> **Q5.** When a web browser sends a request to a web server, describe the encapsulation that occurs across the OSI layers.

---

## Module 3 — The TCP/IP Model (25 min)

### 3.1 TCP/IP vs OSI

The **TCP/IP model** (also called the **DoD model**) is the practical implementation used on the Internet. It collapses the 7-layer OSI model into **4 layers**:

```
     OSI Model                    TCP/IP Model
  ┌──────────────┐              ┌──────────────────┐
  │  Application │              │                  │
  ├──────────────┤     ────→    │   Application    │
  │ Presentation │              │   (HTTP, DNS,    │
  ├──────────────┤              │   FTP, SMTP...)  │
  │   Session    │              │                  │
  ├──────────────┤              ├──────────────────┤
  │  Transport   │     ────→    │   Transport      │
  │ (TCP / UDP)  │              │   (TCP / UDP)    │
  ├──────────────┤              ├──────────────────┤
  │   Network    │     ────→    │   Internet       │
  │     (IP)     │              │   (IP, ICMP)     │
  ├──────────────┤              ├──────────────────┤
  │  Data Link   │              │                  │
  ├──────────────┤     ────→    │  Network Access  │
  │   Physical   │              │  (Ethernet, Wi-Fi│
  └──────────────┘              └──────────────────┘
```

---

### 3.2 IPv4 Addressing

An **IPv4 address** is a 32-bit number written as four decimal octets separated by dots.

```
Example: 192.168.1.100
Binary:  11000000.10101000.00000001.01100100
```

#### IP Address Classes

| Class | Range | Default Subnet Mask | Usage |
|-------|-------|---------------------|-------|
| A | 1.0.0.0 – 126.255.255.255 | 255.0.0.0 /8 | Large networks |
| B | 128.0.0.0 – 191.255.255.255 | 255.255.0.0 /16 | Medium networks |
| C | 192.0.0.0 – 223.255.255.255 | 255.255.255.0 /24 | Small networks |

#### Private IP Ranges (RFC 1918)

| Range | CIDR |
|-------|------|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 |

> 🔑 **Security relevance:** Attackers scan private ranges during internal reconnaissance. Understanding CIDR notation is essential for interpreting Nmap scan ranges.

---

### 3.3 IPv6 Addressing

IPv6 was introduced to address **IPv4 exhaustion**. It uses **128-bit** addresses:

```
Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
Short:   2001:db8:85a3::8a2e:370:7334
```

IPv6 provides approximately **3.4 × 10³⁸** addresses — a practically unlimited pool.

---

### 3.4 Useful Network Commands

```bash
# Display your IP address and network interfaces
ip addr show
ifconfig          # older systems

# Test reachability (uses ICMP Echo Request)
ping 8.8.8.8
ping6 ::1         # IPv6 loopback test

# Trace the path to a host
traceroute 8.8.8.8
traceroute6 ipv6.google.com

# Display routing table
ip route show
route -n

# Show ARP table (IP → MAC mappings)
arp -a

# Show open ports and connections
netstat -tuln
ss -tuln

# DNS lookup
nslookup google.com
dig google.com
host google.com

# Display network interface statistics
ip -s link
```

---

### 3.5 The TCP Three-Way Handshake

Before any data can be exchanged over TCP, a **connection** must be established using a **three-way handshake**:

```
  Client                        Server
    │                              │
    │─── SYN (seq=x) ─────────────►│
    │                              │
    │◄── SYN-ACK (seq=y, ack=x+1) ─│
    │                              │
    │─── ACK (ack=y+1) ───────────►│
    │                              │
    │ ←─── DATA EXCHANGE ──────► │
    │                              │
    │─── FIN ─────────────────────►│
    │◄── FIN-ACK ──────────────────│
```

**TCP Flags and their meanings:**

| Flag | Meaning | Security Relevance |
|------|---------|-------------------|
| `SYN` | Synchronize — initiate connection | SYN Flood (DoS) |
| `ACK` | Acknowledge — confirm receipt | Used to map firewall rules |
| `FIN` | Finish — terminate connection | Used in stealthy scans |
| `RST` | Reset — abort connection | Port closed response |
| `PSH` | Push — send data immediately | Data delivery |
| `URG` | Urgent pointer | Rarely used |

> 🔑 **Nmap exploits** TCP flag behavior. A **SYN scan** (`-sS`) sends a SYN and analyzes the response — `SYN-ACK` means open, `RST` means closed.

---

### 3.6 TCP vs UDP — Comparison

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | Guaranteed delivery | Best effort |
| Ordering | In-order delivery | No ordering |
| Speed | Slower | Faster |
| Error recovery | Yes | No |
| Use cases | HTTP, HTTPS, SSH, FTP, SMTP | DNS, VoIP, Video Streaming, DHCP |
| Header size | 20–60 bytes | 8 bytes |

---

![](./src/what-is-a-tcp-3-way-handshake-process-tcp-header-b4e17a1675ac1e86.jpg)
![](./src/what-is-a-tcp-3-way-handshake-process-three-way-handshaking-establishing-connection-6a724e77ba96e241.jpg)

---

### ✅ Module 3 — Review Questions

> **Q1.** What is the purpose of the three-way handshake? What happens if the last ACK is never sent?

> **Q2.** A packet capture shows a host sending SYN packets to 1000 different ports on a target machine in 2 seconds with no completed handshakes. What type of scan or attack does this suggest?

> **Q3.** Why would an attacker prefer UDP scanning? What makes it harder to perform than TCP scanning?

> **Q4.** Convert the IP address `192.168.10.50` to binary. What is the network address if the subnet mask is `/24`?

> **Q5.** What is the difference between a public IP and a private IP? Why can't a private IP be routed on the Internet?

---

## ⏱️ HOUR 2 — Core Protocols and Cryptography

---

## Module 4 — Core Protocols: TCP, UDP, ICMP (20 min)

### 4.1 Port Numbers — The Language of Services

Ports are **16-bit numbers** (0–65535) that identify specific processes or services:

| Range | Type | Description |
|-------|------|-------------|
| 0 – 1023 | **Well-Known Ports** | Reserved for standard services |
| 1024 – 49151 | **Registered Ports** | Registered by software vendors |
| 49152 – 65535 | **Dynamic/Ephemeral Ports** | Temporary, used by clients |

#### Critical Well-Known Ports (Must Memorize)

| Port | Protocol | Service |
|------|----------|---------|
| 20, 21 | TCP | FTP (data, control) |
| 22 | TCP | SSH |
| 23 | TCP | Telnet (insecure!) |
| 25 | TCP | SMTP (email sending) |
| 53 | TCP/UDP | DNS |
| 67, 68 | UDP | DHCP |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 3306 | TCP | MySQL |
| 3389 | TCP | RDP (Remote Desktop) |
| 8080 | TCP | HTTP alternative |

> 🔑 **Security insight:** Open ports are an attack surface. An attacker scans ports to identify running services and match them to known vulnerabilities.

---

### 4.2 ICMP — Internet Control Message Protocol

ICMP is used for **error reporting and diagnostics**. It operates at the **Network Layer (Layer 3)** and has **no port numbers**.

#### Key ICMP Message Types

| Type | Code | Meaning |
|------|------|---------|
| 0 | 0 | Echo Reply (ping response) |
| 3 | 0–15 | Destination Unreachable |
| 5 | — | Redirect |
| 8 | 0 | Echo Request (ping) |
| 11 | 0 | Time Exceeded (used by traceroute) |

```bash
# Ping — send ICMP Echo Request
ping -c 4 8.8.8.8

# Ping with specific packet size
ping -s 1400 192.168.1.1

# Traceroute — exploits ICMP TTL Exceeded messages
traceroute 8.8.8.8
```

> 🔑 **Security use:** `ping sweep` (nmap -sP) uses ICMP to discover live hosts. Firewalls often **block ICMP** to prevent host discovery — this is why Nmap sometimes uses TCP/SYN pings as alternatives.

---

### 4.3 ARP — Address Resolution Protocol

**ARP** maps an IP address to a **MAC address** on the local network (Layer 2–3 boundary).

```
  Who has 192.168.1.1?  (ARP Request — broadcast)
  ─────────────────────────────────────────►  FF:FF:FF:FF:FF:FF

  192.168.1.1 is at AA:BB:CC:DD:EE:FF  (ARP Reply — unicast)
  ◄─────────────────────────────────────────
```

```bash
# View ARP cache
arp -a

# Send ARP request manually
arping 192.168.1.1
```

> 🔑 **ARP Spoofing:** An attacker sends fake ARP replies to associate their MAC with the gateway IP — allowing **Man-in-the-Middle** attacks. This is a critical Layer 2 attack vector.

---

### 🖼️ IMAGE PLACEHOLDER 4

```
┌─────────────────────────────────────────────────────────┐
│                    [ IMAGE HERE ]                        │
│                                                         │
│   Suggested: Wireshark capture of ARP exchange /        │
│   Port table visual / ICMP ping diagram                 │
│                                                         │
│   Recommended size: 800 × 400 px                        │
└─────────────────────────────────────────────────────────┘
```

---

## Module 5 — DNS — Domain Name System (20 min)

### 5.1 What is DNS?

**DNS (Domain Name System)** is the "phone book" of the Internet. It translates human-readable **domain names** (e.g., `google.com`) into **IP addresses** (e.g., `142.250.185.46`).

- Operates on **port 53**
- Uses **UDP** for queries (≤512 bytes), **TCP** for zone transfers and large responses
- Hierarchical and distributed architecture

---

### 5.2 DNS Resolution Process

When you type `www.google.com` in your browser:

```
  Browser                  Resolver            Root NS        TLD NS         Auth NS
     │                        │                   │               │              │
     │── "www.google.com?" ──►│                   │               │              │
     │                        │── "google.com?" ─►│               │              │
     │                        │◄─ ".com NS is X" ─│               │              │
     │                        │── "google.com?" ──────────────────►│              │
     │                        │◄─ "google.com NS is Y" ────────────│              │
     │                        │── "www.google.com?" ───────────────────────────►│
     │                        │◄─ "142.250.185.46" ────────────────────────────│
     │◄── "142.250.185.46" ───│                   │               │              │
```

**Resolution Chain:**
1. **Local Cache** → check browser/OS cache
2. **Recursive Resolver** → your ISP or configured DNS (e.g., `8.8.8.8`)
3. **Root Name Server** → 13 root server clusters (labeled A–M)
4. **TLD Name Server** → responsible for `.com`, `.org`, `.dz`, etc.
5. **Authoritative Name Server** → the final answer

---

### 5.3 DNS Record Types

| Record | Full Name | Purpose | Example |
|--------|-----------|---------|---------|
| **A** | Address | Maps hostname → IPv4 | `google.com → 142.250.185.46` |
| **AAAA** | IPv6 Address | Maps hostname → IPv6 | `google.com → 2607:f8b0::` |
| **MX** | Mail Exchange | Mail server for domain | `google.com → smtp.google.com` |
| **CNAME** | Canonical Name | Alias for another domain | `www.google.com → google.com` |
| **NS** | Name Server | Authoritative DNS servers | `google.com → ns1.google.com` |
| **TXT** | Text | SPF, DKIM, verification | `"v=spf1 include:..."` |
| **PTR** | Pointer | Reverse DNS (IP → name) | `8.8.8.8 → dns.google` |
| **SOA** | Start of Authority | Zone administration info | — |

---

### 5.4 DNS Commands

```bash
# Basic DNS lookup (A record)
nslookup google.com

# Query specific record type
dig google.com MX
dig google.com NS
dig google.com TXT
dig google.com AAAA

# Query a specific DNS server
dig @8.8.8.8 google.com

# Reverse DNS lookup (PTR record)
dig -x 8.8.8.8

# Full DNS resolution trace
dig +trace google.com

# Query all record types
dig google.com ANY

# Simple host lookup
host google.com
host -t MX google.com

# Test DNS on Windows
nslookup -type=MX google.com 8.8.8.8
```

---

### 5.5 DNS Security Issues

#### DNS Attacks

| Attack | Description |
|--------|-------------|
| **DNS Spoofing / Cache Poisoning** | Injecting false DNS records into a resolver's cache |
| **DNS Hijacking** | Redirecting DNS queries to a malicious server |
| **DNS Amplification (DDoS)** | Using open resolvers to amplify attack traffic |
| **DNS Zone Transfer Attack** | Unauthorized transfer of all DNS records (`AXFR`) |
| **DNS Tunneling** | Encoding data inside DNS queries/responses to bypass firewalls |

```bash
# Attempt a zone transfer (only works if misconfigured)
dig @ns1.target.com target.com AXFR

# Check if a server allows recursive queries (amplification risk)
dig @target-dns.com google.com
```

> ⚠️ **Warning:** Only perform these on domains/servers you have explicit permission to test.

#### DNS Security Extensions (DNSSEC)
**DNSSEC** adds cryptographic signatures to DNS records to verify authenticity and prevent spoofing.

---

![](./src/dns.png)

---

### ✅ Module 5 — Review Questions

> **Q1.** What happens if a DNS server is unreachable? How does this affect web browsing even if the web server itself is working perfectly?

> **Q2.** What is the difference between a **recursive resolver** and an **authoritative name server**?

> **Q3.** Using `dig`, how would you find the mail server for the domain `univ-batna2.dz`? Write the exact command.

> **Q4.** Explain how **DNS cache poisoning** works. What is the impact on a user's machine?

> **Q5.** Why is a **DNS zone transfer** a security risk? What information can an attacker gain from it?

---

## Module 6 — HTTP, HTTPS, and the SSL/TLS Handshake (25 min)

### 6.1 HTTP — HyperText Transfer Protocol

**HTTP** is the foundation of data communication on the Web. It is a **stateless, text-based** request-response protocol operating at Layer 7.

#### HTTP Request Structure

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Connection: keep-alive

[Optional Request Body]
```

#### HTTP Response Structure

```
HTTP/1.1 200 OK
Date: Mon, 01 Jan 2026 12:00:00 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 3456
Server: Apache/2.4.51

[Response Body — HTML content]
```

#### HTTP Methods

| Method | Description | Security Risk |
|--------|-------------|---------------|
| `GET` | Retrieve a resource | Parameters exposed in URL |
| `POST` | Submit data to server | Can send large/hidden data |
| `PUT` | Update a resource | May allow unauthorized modification |
| `DELETE` | Delete a resource | Destructive if unprotected |
| `HEAD` | Like GET but no body | Used in fingerprinting |
| `OPTIONS` | What methods are allowed | Reveals server capabilities |

#### HTTP Status Codes

| Code | Meaning | Security Note |
|------|---------|---------------|
| 200 | OK | Success |
| 301/302 | Redirect | Can be abused (redirect attacks) |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Authorization failure |
| 404 | Not Found | Reveals resource existence |
| 500 | Internal Server Error | May leak stack traces |

---

### 6.2 The Problem with HTTP

HTTP transmits data **in plaintext**. This means anyone between the client and server can read the data:

```
  You ───── [your data in clear text] ────► Web Server
              ↑
              Attacker intercepts here
              (Wi-Fi sniffing, MITM)
```

> 🔑 Never send passwords, credit card numbers, or sensitive data over plain HTTP.

---

### 6.3 HTTPS and TLS/SSL

**HTTPS (HTTP Secure)** is HTTP combined with **TLS (Transport Layer Security)** — the modern replacement for the older **SSL (Secure Sockets Layer)**.

HTTPS provides:
- **Encryption** — data is unreadable to interceptors
- **Authentication** — verifies the server's identity via certificates
- **Integrity** — ensures data was not modified in transit

> 📌 **Note:** Despite common usage, SSL is deprecated. Modern systems use **TLS 1.2** or **TLS 1.3**. The terms "SSL" and "TLS" are often used interchangeably in everyday conversation.

---

### 6.4 Digital Certificates and PKI

A **TLS/SSL certificate** is a digital document that:
- Proves the server's identity
- Contains the server's **public key**
- Is signed by a **Certificate Authority (CA)** that your browser trusts

```
Certificate Contents:
├── Subject (domain name)
├── Issuer (Certificate Authority)
├── Validity period (Not Before / Not After)
├── Public Key
├── Digital Signature (signed by CA)
└── Subject Alternative Names (SANs)
```

**Chain of Trust:**
```
  Root CA (trusted by OS/browser)
      └── Intermediate CA
              └── Server Certificate (e.g., *.google.com)
```

---

### 6.5 The TLS Handshake — Step by Step

The TLS handshake negotiates **encryption parameters** and **authenticates** the server before any data is exchanged.

#### TLS 1.2 Handshake (Classic)

```
  Client                                      Server
    │                                              │
    │──── ClientHello ─────────────────────────────►│
    │  (TLS version, cipher suites, client random) │
    │                                              │
    │◄─── ServerHello ─────────────────────────────│
    │  (chosen cipher, server random, session ID)  │
    │                                              │
    │◄─── Certificate ─────────────────────────────│
    │  (server's public key + CA signature)        │
    │                                              │
    │◄─── ServerHelloDone ─────────────────────────│
    │                                              │
    │ [Client verifies certificate against CA]     │
    │                                              │
    │──── ClientKeyExchange ───────────────────────►│
    │  (pre-master secret, encrypted with server   │
    │   public key)                                │
    │                                              │
    │──── ChangeCipherSpec ────────────────────────►│
    │  (switching to encrypted communication)      │
    │                                              │
    │──── Finished (encrypted) ────────────────────►│
    │                                              │
    │◄─── ChangeCipherSpec ────────────────────────│
    │◄─── Finished (encrypted) ────────────────────│
    │                                              │
    │ ════ Encrypted Application Data (HTTP) ════ │
```

#### TLS 1.3 Handshake (Modern — Faster)

TLS 1.3 reduces the handshake to **1 round-trip** (vs 2 in TLS 1.2) and improves security by removing obsolete cipher suites.

```
  Client                                    Server
    │                                          │
    │──── ClientHello + Key Share ─────────────►│
    │  (key share allows server to compute      │
    │   session keys immediately)               │
    │                                          │
    │◄─── ServerHello + Key Share ─────────────│
    │◄─── Certificate (encrypted) ─────────────│
    │◄─── Finished (encrypted) ────────────────│
    │                                          │
    │──── Finished ────────────────────────────►│
    │                                          │
    │ ════ Encrypted Application Data ════════ │
```

---

### 6.6 Cipher Suites

A **cipher suite** defines the cryptographic algorithms used for a TLS session:

```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
 │     │     │      │    │      │
 │     │     │      │    │      └── Hash for MAC
 │     │     │      │    └───────── Mode (GCM)
 │     │     │      └────────────── Encryption (AES 256)
 │     │     └───────────────────── Auth (RSA)
 │     └─────────────────────────── Key Exchange (ECDHE)
 └───────────────────────────────── Protocol
```

---

### 6.7 Commands for TLS/HTTPS Analysis

```bash
# Check a website's TLS certificate
openssl s_client -connect google.com:443

# View certificate details
openssl s_client -connect google.com:443 | openssl x509 -text -noout

# Check supported TLS versions
nmap --script ssl-enum-ciphers -p 443 target.com

# Test TLS version and cipher support
nmap -sV --version-intensity 5 -p 443 target.com

# Check for weak SSL/TLS configurations
nmap --script ssl-heartbleed -p 443 target.com

# Curl with verbose TLS info
curl -v https://google.com 2>&1 | grep -A5 "TLS"

# Test specific TLS version
openssl s_client -tls1_2 -connect target.com:443
openssl s_client -tls1_3 -connect target.com:443
```

---

### 6.8 Common TLS/HTTPS Attacks

| Attack | Description | Mitigation |
|--------|-------------|-----------|
| **SSL Stripping** | Downgrade HTTPS to HTTP | HSTS (HTTP Strict Transport Security) |
| **BEAST** | Exploit CBC mode in TLS 1.0 | Use TLS 1.2+ |
| **POODLE** | Exploit SSL 3.0 | Disable SSL 3.0 |
| **Heartbleed (CVE-2014-0160)** | Memory leak via malformed heartbeat | Patch OpenSSL |
| **MITM with Fake Cert** | Rogue CA issues fraudulent cert | Certificate Pinning |
| **FREAK/Logjam** | Force weak export-grade crypto | Disable export ciphers |

---

![](./src/tls1.3.png)

---

### ✅ Module 6 — Review Questions

> **Q1.** What are the three guarantees that HTTPS provides over plain HTTP? Explain each one.

> **Q2.** In the TLS 1.2 handshake, what is the purpose of the **pre-master secret**? Who generates it and how is it securely transmitted?

> **Q3.** Why is **TLS 1.3** considered more secure and faster than TLS 1.2?

> **Q4.** A user connects to `http://banking-site.com` (no HTTPS). An attacker on the same Wi-Fi performs an **SSL stripping attack**. Describe step-by-step what happens.

> **Q5.** What is a **Certificate Authority (CA)**? What is the risk if a CA is compromised? Can you name a real-world example of a CA compromise?

> **Q6.** Using `openssl`, write the command to check the TLS certificate of `univ-batna2.dz`. What information would you expect to see?

---

## ⏱️ HOUR 3 — Network Scanning with Nmap

---

## Module 7 — Lab 2: Network Scanning with Nmap (40 min)

### 7.1 What is Nmap?

**Nmap (Network Mapper)** is an open-source network scanner used to discover hosts, services, operating systems, and open ports on a network. It is an essential tool for:

- **Administrators** — auditing network security posture
- **Penetration testers** — reconnaissance and enumeration
- **Attackers** — mapping targets (reconnaissance phase of Kill Chain)

**Alternatives:** Superscan, Angry IP Scanner, Masscan (high-speed), Zmap

**GUI:** **Zenmap** provides a graphical interface for Nmap, but this lab uses the command line.

**Test domain provided by Nmap:** `scanme.nmap.org`

> ⚠️ **Legal Warning:** You are **strictly prohibited** from scanning IP addresses or domains you do not own or have explicit written permission to scan. Unauthorized network scanning is a criminal offense in most jurisdictions.

---

### 7.2 How Nmap Works — Under the Hood

Nmap sends **crafted packets** and analyzes **responses** to determine:

| What Nmap Sends | What Nmap Learns |
|----------------|-----------------|
| ICMP Echo Request | Is the host alive? |
| TCP SYN to port | Is the port open/closed/filtered? |
| TCP SYN + service probe | What service version is running? |
| OS detection packets | What operating system is running? |
| Script-specific packets | What specific vulnerabilities exist? |

---

### 7.3 Nmap — Port States

Nmap reports six possible port states:

| State | Meaning | Why it happens |
|-------|---------|----------------|
| **open** | Application actively accepts connections | Service is listening |
| **closed** | Port accessible but no application listening | RST received |
| **filtered** | Nmap can't determine state | Firewall/filter drops packets |
| **unfiltered** | Accessible, state unknown | ACK scan result |
| **open\|filtered** | Either open or filtered, can't tell | No response to probe |
| **closed\|filtered** | Either closed or filtered, can't tell | Idle scan result |

---

### 7.4 Nmap Commands — Explained and Analyzed

---

#### 📌 Part 1 — Host Discovery

```bash
# Ping scan — discover live hosts (no port scan)
nmap -sP <victim IP>

# Example:
nmap -sP 192.168.1.1
```

**What it does:** Sends ICMP Echo Request, TCP SYN to port 443, TCP ACK to port 80, and ICMP Timestamp. Reports which hosts respond.

**Attacker value:** Maps all active hosts on a subnet to build a target list. First step in network reconnaissance.

```bash
# Scan another host on the same network
nmap -sP <another IP on the network>

# Scan an entire subnet
nmap -sP 192.168.1.0/24
nmap -sP 192.168.1.*
nmap -sP 192.168.1.1-100
```

---

#### 📌 Part 2 — Port Scanning Techniques

```bash
# SYN Scan (Stealth Scan) — requires root
nmap -sS <victim IP>

# Example:
sudo nmap -sS 192.168.1.100
```

**What it does:** Sends a TCP SYN to each port. If it receives:
- `SYN-ACK` → port is **open** (sends RST to avoid completing handshake)
- `RST` → port is **closed**
- No response → port is **filtered**

**Why it's called "stealth":** The three-way handshake is **never completed**, so older systems/IDS may not log it as a full connection.

**Attacker value:** Quickly identifies open ports without leaving full connection logs.

```bash
# Service/Version Detection
nmap -sV <victim IP>
```

**What it does:** After finding open ports, sends **service probes** and compares responses to its database to identify the running service and its **exact version**.

**Attacker value:** Knowing the exact version allows the attacker to search for **known CVEs** (e.g., Apache 2.4.49 → CVE-2021-41773).

---

#### 📌 Part 3 — Targeted Scanning

```bash
# Scan specific ports only
nmap -p 80,443 <victim IP>
```

**What it does:** Only scans ports 80 (HTTP) and 443 (HTTPS) instead of the default 1000 ports.

**Attacker value:** Faster, more focused scanning. Useful when only web services are relevant.

```bash
# Version detection on specific ports
nmap -sV -p 80,443 <victim IP>
```

**What it does:** Combines version detection with targeted port scanning. Identifies whether the web server is Apache, Nginx, IIS, etc., and its version.

**Attacker value:** Version fingerprinting enables targeted exploit selection.

```bash
# Aggressive scan (OS detection + version + scripts + traceroute)
nmap -sV -p 80,443 <victim IP> -A
```

**What it does:**  
- `-A` enables: **OS detection** (`-O`), **version detection** (`-sV`), **script scanning** (`-sC`), and **traceroute** (`--traceroute`)

**Attacker value:** Maximum information gathering in one command — OS, services, versions, and even running scripts that probe for vulnerabilities.

> 🔑 The `-A` flag is the most powerful and also the most **noisy** — easily detected by IDS/IPS.

---

#### 📌 Part 4 — Output and Additional Options

```bash
# Save output to a text file
nmap -sV -p 80,443 <victim IP> > scan.txt

# Save in all formats (normal, XML, grepable)
nmap -sV -p 80,443 <victim IP> -oA scan_results

# View the saved results
cat scan.txt
```

```bash
# IPv6 scanning
nmap -6 <victim IPv6>

# Example:
nmap -6 ::1
```

**What it does:** Performs Nmap scanning over IPv6. As IPv6 adoption grows, IPv6 scanning is increasingly important.

```bash
# Script scan — run default NSE scripts
nmap -sC -p 80 <victim IP>
```

**What it does:** Runs the **Nmap Scripting Engine (NSE)** default scripts against port 80. Scripts can detect: HTTP headers, robots.txt, authentication methods, potential vulnerabilities.

---

### 7.5 Advanced Nmap Techniques

```bash
# OS Detection
sudo nmap -O <victim IP>

# Detect firewall/IDS evasion — fragment packets
nmap -f <victim IP>

# Use decoys to hide your IP
nmap -D RND:10 <victim IP>

# Slow scan to evade detection
nmap -T0 <victim IP>          # Paranoid (slowest)
nmap -T1 <victim IP>          # Sneaky
nmap -T3 <victim IP>          # Normal (default)
nmap -T5 <victim IP>          # Insane (fastest, noisy)

# Scan UDP ports (slow but important)
sudo nmap -sU <victim IP>

# Detect specific vulnerabilities with NSE
nmap --script vuln <victim IP>
nmap --script ssl-heartbleed -p 443 <victim IP>
nmap --script http-sql-injection -p 80 <victim IP>

# Banner grabbing
nmap -sV --version-intensity 9 <victim IP>

# Bypass firewall using FIN scan
sudo nmap -sF <victim IP>

# Null scan (no flags)
sudo nmap -sN <victim IP>
```

---

### 7.6 Nmap Scan Types — Summary Table

| Scan Type | Flag | Requires Root? | Noise Level | Use Case |
|-----------|------|---------------|------------|---------|
| Ping Scan | `-sP` | No | Low | Host discovery |
| SYN Scan | `-sS` | Yes | Medium | Default stealth port scan |
| Connect Scan | `-sT` | No | High | When SYN not possible |
| UDP Scan | `-sU` | Yes | Low | Find UDP services |
| Version Scan | `-sV` | No | Medium | Service identification |
| OS Detection | `-O` | Yes | Medium | OS fingerprinting |
| Script Scan | `-sC` | No | High | Vulnerability detection |
| Aggressive | `-A` | No | Very High | All-in-one |
| FIN Scan | `-sF` | Yes | Very Low | Firewall bypass |

---

### 7.7 Scan Multiple Targets

```bash
# Scan a range of IPs
nmap 192.168.12.1-100

# Scan using wildcard
nmap 192.168.12.*

# Scan entire subnet
nmap 192.168.12.0/24

# Scan multiple specific IPs
nmap 192.168.1.1 192.168.1.5 192.168.1.10

# Scan from a file containing IPs
nmap -iL targets.txt
```

---

### 7.8 Interpreting Nmap Output

A typical Nmap output looks like this:

```
Starting Nmap 7.94 ( https://nmap.org )
Nmap scan report for 192.168.1.100
Host is up (0.00089s latency).

PORT    STATE  SERVICE    VERSION
22/tcp  open   ssh        OpenSSH 8.2p1 Ubuntu
80/tcp  open   http       Apache httpd 2.4.41
443/tcp open   ssl/https  Apache httpd 2.4.41
3306/tcp closed mysql

OS details: Linux 4.15 - 5.6
```

**Reading the results:**
- `22/tcp open ssh OpenSSH 8.2p1` → SSH running, check for vulnerabilities specific to this version
- `80/tcp open http Apache 2.4.41` → Search CVE database for Apache 2.4.41 vulnerabilities
- `3306/tcp closed mysql` → MySQL installed but not accepting remote connections
- OS detection → helps choose OS-specific exploits

---

### 🖼️ IMAGE PLACEHOLDER 7

```
┌─────────────────────────────────────────────────────────┐
│                    [ IMAGE HERE ]                        │
│                                                         │
│   Suggested: Nmap terminal output screenshot /          │
│   Zenmap GUI screenshot / Nmap scan types diagram       │
│                                                         │
│   Recommended size: 900 × 600 px                        │
└─────────────────────────────────────────────────────────┘
```

---

### 🖼️ IMAGE PLACEHOLDER 8 — Lab File Attachment

```
┌─────────────────────────────────────────────────────────┐
│                    [ LAB FILE HERE ]                     │
│                                                         │
│   Attach: Lab 2 - nmap.pdf                              │
│                                                         │
│   Students will use this lab sheet to run all           │
│   commands on their assigned victim VM or               │
│   scanme.nmap.org                                        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

### ✅ Module 7 — Lab Questions

> **Q1.** Run `nmap -sP 192.168.X.X/24` on your lab network. How many hosts are alive? List their IP addresses and MAC addresses.

> **Q2.** Run a SYN scan (`-sS`) on the victim VM. List every open port, its service, and one potential security risk for each.

> **Q3.** Run `nmap -sV -p 22,80,443 <victim>`. What exact versions are reported? Search the CVE database (https://cve.mitre.org) and report any known vulnerabilities.

> **Q4.** What is the difference in output between `nmap -p 80 <victim>` and `nmap -sV -p 80 <victim>`? Why is version detection important?

> **Q5.** Run `nmap -A <victim>`. What operating system does Nmap detect? How confident is the detection (match percentage)?

> **Q6.** Save an Nmap scan result to a file called `lab2_scan.txt`. Show the command used and the first 10 lines of the output.

> **Q7.** Why does the `-sS` SYN scan require root privileges? What happens if you run it as a regular user?

> **Q8.** You see `filtered` next to a port. What does this likely indicate about the network configuration? How could an attacker try to bypass this?

---

### 7.9 Defending Against Nmap Scans

Understanding scanning is also about knowing how to **detect and defend**:

| Defense | How it Works |
|---------|-------------|
| **Firewall with stateful inspection** | Drops unsolicited SYN packets from unknown sources |
| **IDS/IPS (e.g., Snort, Suricata)** | Detects port scan patterns and alerts/blocks |
| **Port knocking** | Ports only open after a secret sequence of packets |
| **Disabling ICMP** | Prevents ping sweeps (but not TCP-based host discovery) |
| **Service minimization** | Close all unused ports — reduce attack surface |
| **Honeypots** | Fake open ports that alert when accessed |
| **Rate limiting** | Block IPs that exceed a connection threshold |

```bash
# Detect Nmap scans with Snort rule (example)
alert tcp any any -> $HOME_NET any (msg:"Nmap SYN Scan"; flags:S; threshold:type both,track by_src,count 20,seconds 2; sid:1000001;)

# Check iptables for current rules
iptables -L -n -v

# Block ICMP (ping)
iptables -A INPUT -p icmp --icmp-type echo-request -j DROP

# Log port scan attempts
iptables -A INPUT -p tcp --syn -m recent --name portscan --set
iptables -A INPUT -p tcp --syn -m recent --name portscan --rcheck --seconds 60 --hitcount 5 -j DROP
```

---

## 🔁 Final Review and Wrap-Up (10 min)

### Complete Topic Map

```
Introduction to Cybersecurity
│
├── CIA Triad (Confidentiality, Integrity, Availability)
├── Threat Actors (White/Grey/Black Hat)
├── Cyber Kill Chain
│
├── OSI Model (7 Layers)
│   ├── Physical → Data Link → Network → Transport
│   └── Session → Presentation → Application
│
├── TCP/IP Model (4 Layers)
│   ├── IPv4/IPv6 Addressing
│   ├── TCP Three-Way Handshake
│   └── TCP vs UDP
│
├── Core Protocols
│   ├── ICMP (ping, traceroute)
│   ├── ARP (IP → MAC, spoofing)
│   └── Port Numbers (Well-Known Ports)
│
├── DNS
│   ├── Resolution Process (Recursive → TLD → Auth)
│   ├── Record Types (A, AAAA, MX, CNAME, NS, PTR)
│   └── Attacks (Spoofing, Hijacking, Zone Transfer)
│
├── HTTP/HTTPS
│   ├── HTTP Methods and Status Codes
│   ├── TLS 1.2 and TLS 1.3 Handshake
│   ├── Certificates and PKI
│   └── Attacks (SSL Stripping, Heartbleed, POODLE)
│
└── Nmap (Network Scanning)
    ├── Port States (open, closed, filtered...)
    ├── Scan Types (-sP, -sS, -sV, -A, -sC, -O)
    ├── Target Ranges (/24, *.*, 1-100)
    └── Defense (Firewalls, IDS, Rate Limiting)
```

---

### 🔑 Key Takeaways

1. **Every open port is a potential attack surface** — minimize services running on production systems.
2. **HTTP is insecure** — always use HTTPS with modern TLS (1.2 or 1.3) for any sensitive communication.
3. **DNS is foundational but fragile** — DNS poisoning can silently redirect users to malicious sites.
4. **Reconnaissance is the first step of any attack** — Nmap is what attackers use; understanding it helps defenders.
5. **The OSI model maps attacks to layers** — knowing which layer an attack targets helps select the right defense.

---

### 📝 Final Comprehensive Questions

> **Q1.** A user visits `http://mail.company.com` and enters their credentials. An attacker on the same LAN intercepts the traffic. Describe the full attack chain using the concepts from this course (ARP, MITM, HTTP, TLS).

> **Q2.** You are hired as a penetration tester. Your first task is to map the internal network `10.0.0.0/24`. Write the complete sequence of Nmap commands you would use from initial host discovery to service version enumeration, and explain why you chose each command.

> **Q3.** A web server returns `nmap -sV` result: `443/tcp open ssl/https Apache/2.4.29`. Search CVE databases and explain what you would investigate next.

> **Q4.** Map the TLS handshake process to the OSI model — at which layer does each step operate? Which OSI layer is most relevant to TLS?

> **Q5.** Draw and label a complete diagram showing: a client browser making an HTTPS request — include DNS resolution, TCP handshake, TLS handshake, and HTTP data exchange. Label which protocol is active at each step.

---

### 📚 Recommended Resources

| Resource | URL | Notes |
|----------|-----|-------|
| Nmap Official Docs | https://nmap.org/docs.html | Complete reference |
| CVE Database | https://cve.mitre.org | Vulnerability lookup |
| Wireshark | https://www.wireshark.org | Packet capture analysis |
| OWASP Top 10 | https://owasp.org/top10 | Web application risks |
| TryHackMe | https://tryhackme.com | Hands-on practice |
| Hack The Box | https://hackthebox.com | CTF challenges |
| SSL Labs | https://ssllabs.com/ssltest | Test HTTPS config |
| DNS Lookup | https://dnschecker.org | DNS record lookup |

---

### 🛠️ Lab Environment Setup

```bash
# Install Nmap (if not already installed)
sudo apt install nmap -y

# Install Wireshark
sudo apt install wireshark -y

# Install dig and nslookup
sudo apt install dnsutils -y

# Install OpenSSL
sudo apt install openssl -y

# Verify installations
nmap --version
wireshark --version
dig -v
openssl version
```

---
