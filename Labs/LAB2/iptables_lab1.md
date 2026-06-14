# LAB 1 — Introduction to Stateless Firewalls Using iptables

---

| Field | Details |
|---|---|
| **Course** | CompTIA Security+ |
| **Lab Number** | LAB 1 |
| **Lab Title** | Introduction to Stateless Firewalls Using iptables |
| **Instructor** | Nidhal Lahcen |
| **Organization** | BrainerX |
| **Estimated Duration** | 90 – 120 minutes |
| **Difficulty Level** | Beginner – Intermediate |

---

## Prerequisites

Before starting this lab, students should have:

- Basic understanding of TCP/IP networking (IP addresses, ports, protocols)
- Familiarity with the Linux command line (navigating directories, running commands as root)
- Basic knowledge of network services (FTP, SSH, Telnet, HTTP)
- Access to a Linux virtual machine (Metasploitable recommended) and an attacker machine (Kali Linux recommended)
- Understanding of what a port scanner does (e.g., nmap)

---

## Learning Objectives

By the end of this lab, students will be able to:

1. Explain what a firewall is and why organizations need one
2. Describe the difference between hardware and software firewalls
3. Explain what a stateless (packet-filtering) firewall is and how it processes packets
4. Identify the three main iptables tables: **filter**, **nat**, and **mangle**
5. Identify and explain the three main iptables chains: **INPUT**, **OUTPUT**, and **FORWARD**
6. Write and apply iptables rules using the correct syntax
7. Set default policies (DROP / ACCEPT) on iptables chains
8. Apply ACCEPT and REJECT actions to specific ports and protocols
9. Verify active firewall rules using `iptables -L`
10. Understand the security impact of firewall rule ordering
11. Flush (reset) iptables rules to a clean state
12. Explain the limitations of stateless packet filtering

---

## Introduction

Every organization that connects to the Internet faces a fundamental security problem: without any controls, anyone on the Internet can attempt to communicate with any machine inside the network, and internal users can connect to any external service they want.

A **firewall** is the solution to this problem. It sits between two networks — typically between an internal corporate network and the Internet — and acts as a mandatory checkpoint. Every packet that enters or leaves the network must pass through the firewall. The firewall then decides, based on a set of rules called a **security policy**, whether to allow or block that packet.

In this lab, we focus on **stateless firewalls** — the oldest and most foundational type of firewall. A stateless firewall inspects each network packet individually, comparing it against a list of rules based on IP addresses, ports, and protocols. It does not remember anything about previous packets or ongoing connections.

On Linux systems, the built-in firewall engine is called **Netfilter**. The command-line tool used to configure Netfilter is called **iptables**. In this lab, you will learn to use iptables to build and manage firewall rules that protect a Linux machine from network scans and attacks.

> **Real-world context:** Even though modern firewalls have evolved far beyond stateless filtering, understanding stateless firewalls is essential for any security professional. The concepts of chains, tables, rules, and policies introduced here form the foundation of all firewall technologies you will encounter throughout your career.

---

## Theory Section

### 1. What Is a Firewall?

#### Definition

A firewall is a network security device — hardware, software, or both — that monitors and controls incoming and outgoing network traffic based on a set of predefined security rules. It is positioned between two networks (such as a corporate LAN and the Internet) and creates a mandatory passage that all traffic must cross.

#### Why It Matters

Without a firewall, every employee can connect to any external service, and every person on the Internet can attempt to connect to any machine inside your network. This creates an enormous attack surface. The firewall reduces this attack surface by enforcing a security policy.

#### Real-World Use Case

A company places a firewall between its internal network and the Internet. The firewall is configured to allow employees to browse the web (HTTP/HTTPS) and receive emails (POP/IMAP), but block all other incoming connections from external sources.

#### Security Impact

A correctly configured firewall prevents unauthorized access to internal systems, limits the damage an attacker can do even if they reach the network perimeter, and provides a single control point for enforcing security policy.

#### Common Mistakes

- Leaving the default policy as ACCEPT (allowing all traffic by default)
- Writing rules that are too broad, accidentally permitting dangerous services
- Placing more general rules before more specific ones, causing specific rules to never be evaluated

#### Exam Tips (CompTIA Security+)

- Firewalls operate primarily at OSI **layers 3** (Network — IP filtering), **4** (Transport — port filtering), and **7** (Application — protocol/content filtering)
- Know the difference between a **host-based firewall** (software on a single machine) and a **network firewall** (hardware/software protecting an entire network)

---

### 2. Why Organizations Need Firewalls

#### Definition

Without a firewall, the internal network is fully exposed to the Internet. Any external party can attempt connections to any service running on any internal machine. Employees can also connect to any external destination, including malicious sites.

#### Why It Matters

A firewall enforces the organization's **security policy** — the set of rules that define what traffic is allowed and what is blocked. It limits both inbound threats (attackers from the Internet) and outbound risks (employees connecting to dangerous external services or data being exfiltrated).

#### Real-World Use Case

A bank must prevent anyone from the Internet from directly reaching its internal database servers. It also must prevent employees from sending sensitive data to unauthorized external services. A firewall, positioned at the network boundary, enforces both of these requirements.

#### Security Impact

Without a firewall, an attacker who discovers your public IP address can probe every port on every internal machine directly. With a firewall, the attacker sees only what the firewall explicitly permits.

#### Common Mistakes

- Treating a firewall as the only security control (defense in depth requires multiple layers)
- Failing to update firewall rules when network services change

#### Exam Tips (CompTIA Security+)

- A firewall is a **preventive control**
- Firewalls alone cannot protect against threats that originate from inside the network, or encrypted attacks that pass through allowed ports

---

### 3. Hardware Firewalls vs. Software Firewalls

#### Definition

A **hardware firewall** is a dedicated physical appliance that sits at the network boundary, between the router and the internal network. A **software firewall** is a program installed on an individual machine that filters traffic entering or leaving that machine.

#### Why It Matters

In enterprise environments, organizations typically deploy both: hardware firewalls at the network perimeter to protect the entire organization, and software firewalls on individual machines to provide an additional layer of protection in case an attacker bypasses the perimeter.

#### Real-World Use Case

A company installs a Fortinet FortiGate or Cisco ASA hardware appliance at the edge of its network. Each workstation also runs a host-based software firewall (such as iptables on Linux or Windows Defender Firewall on Windows) to protect against lateral movement if an attacker gets inside the network.

#### Security Impact

Hardware firewalls provide centralized protection for all devices on the network. Software firewalls provide per-machine granularity. Together, they implement the principle of **defense in depth**.

#### Exam Tips (CompTIA Security+)

- Examples of hardware firewall vendors: Fortinet, Palo Alto, Cisco, Check Point, Stormshield
- iptables is a **software/host-based firewall** on Linux
- Know that firewalls can be deployed as a **single central firewall**, as **multiple firewalls**, or with a **DMZ (Demilitarized Zone)** architecture

---

### 4. Firewall Architectures

#### 4.1 Single Central Firewall

A single firewall is positioned between the LAN (internal network) and the WAN (Internet). Filtering occurs at OSI layers 3 and 4. This is the least expensive architecture, suitable for organizations that do not expose any internal servers directly to the Internet.

#### 4.2 Multiple Firewalls

One firewall sits between the LAN and WAN, and an additional firewall separates two different internal network segments. This architecture allows a sensitive internal network (e.g., a finance network) to be protected from other internal networks — not just from external threats.

#### 4.3 Demilitarized Zone (DMZ)

A DMZ allows specific servers (such as web, mail, and FTP servers) to be accessible from the Internet, while keeping the internal network protected. An additional firewall is placed between the DMZ servers and the internal network. This means:

- External users can reach the DMZ servers
- DMZ servers cannot directly reach the internal network
- Even if a DMZ server is compromised, the attacker cannot access internal machines

> **Key point:** In a DMZ, filtering is done by opening only the specific ports required for each service (e.g., port 80 for HTTP, port 443 for HTTPS).

---

### 5. Security Policy

#### Definition

A security policy (in the context of firewalls) is the set of filtering rules defined before configuring the firewall. It is the first step in building a secure firewall configuration. The security policy translates the organization's business needs into specific firewall rules.

#### Why It Matters

A poorly defined security policy leads to a poorly configured firewall, which exposes the organization to security risks. The security policy must balance security with operational functionality — if you block too much, business operations are disrupted; if you block too little, attackers can exploit open services.

#### The Two Approaches

| Approach | Description | Recommended? |
|---|---|---|
| Allow all, block dangerous | Default is ACCEPT; specific dangerous services are blocked | ❌ Not recommended |
| Block all, allow necessary | Default is DROP/REJECT; only required services are explicitly allowed | ✅ Recommended |

The second approach (default deny / least privilege) is the security best practice. It ensures that unknown or newly discovered services are blocked by default.

#### Real-World Examples of Security Policy Translation

| Business Need | Firewall Rule |
|---|---|
| Employees need to browse the Internet | Open outbound ports 80 (HTTP) and 443 (HTTPS) |
| Users need to access email | Open outbound ports for POP (110) and IMAP (143) |
| External customers need to reach the web server | Open inbound port 80 and/or 443 to the web server |
| Prevent SSH access from the Internet | Block inbound port 22 from all external sources |

#### Exam Tips (CompTIA Security+)

- The principle of **least privilege** applied to firewalls = block everything, then allow only what is necessary
- Security policy drives all firewall configuration decisions

---

### 6. Stateless Firewalls (Packet Filtering)

#### Definition

A stateless firewall, also called a **packet-filtering firewall**, is the oldest type of firewall. It inspects each network packet **independently**, comparing the packet's header information (source IP, destination IP, source port, destination port, protocol) against a predefined list of rules called an **ACL (Access Control List)**. The firewall makes a decision for each packet without any knowledge of previous packets or ongoing connections.

#### Why It Matters

Stateless firewalls are fast and efficient because they do not need to maintain any memory of past traffic. They operate at OSI layers 3 and 4, making them effective at blocking unauthorized IP addresses and ports.

#### How It Works — Step by Step

1. A packet arrives at the firewall
2. The firewall reads the packet's header: source IP, destination IP, protocol, source port, destination port
3. The firewall compares this information against its rule list, starting from the first rule
4. The first rule that matches the packet is applied (ACCEPT, DROP, or REJECT)
5. If no rule matches, the default policy is applied
6. The firewall makes no record of this decision — the next packet starts the same process from scratch

#### Advantages

- Fast processing — no session table to maintain
- Simple to understand and configure
- Low resource consumption
- Effective at blocking known bad IP addresses and ports

#### Disadvantages

- Does not track connection state — cannot distinguish a legitimate reply from a new, unsolicited connection
- Vulnerable to IP spoofing attacks
- Cannot inspect packet content (payload)
- Complex rule sets required to handle bidirectional traffic correctly (must explicitly allow return traffic)
- Becoming increasingly obsolete for production use

#### The Return Traffic Problem

This is the most important limitation of stateless firewalls. Consider a scenario where you allow internal users to initiate outbound connections (e.g., web browsing on port 80). When the web server responds, the response packet comes from an external IP address to an internal IP address. A stateless firewall sees this as a new, unsolicited **inbound** connection, and if inbound connections are blocked, it drops the response — breaking the connection.

**Solution in stateless firewalls:** Explicitly add a rule to allow inbound packets that have the TCP ACK flag set (indicating they are part of an established connection, not a new connection initiation). This is an imperfect workaround that stateful firewalls solve properly by maintaining a connection state table.

#### Common Mistakes

- Blocking outbound traffic but not adding a rule to allow the return (ACK) traffic
- Not understanding that rule order is critical — the first matching rule wins

#### Exam Tips (CompTIA Security+)

- Stateless = packet-by-packet, no memory of connections
- Stateful = maintains a connection table, knows if a packet belongs to an established session
- ACL = Access Control List = the rule list used by a stateless firewall

---

### 7. Stateful Firewalls (for comparison)

#### Definition

A stateful firewall tracks the **state** of network connections. It maintains a state table that records information about every active connection (source IP, destination IP, ports, TCP flags, sequence numbers). When a new packet arrives, the firewall checks not just the packet header, but also whether this packet is part of a known, established connection.

#### Advantages Over Stateless

- Automatically allows return traffic for permitted outbound connections
- Can detect certain DoS attacks by monitoring connection state
- Fewer rules required to manage bidirectional traffic

#### Limitations

- The state table has a finite size — a flood of connection requests (SYN flood) can exhaust the table (DoS attack)
- Cannot perform deep content inspection (requires next-generation features like DPI)

---

### 8. Application-Layer Firewalls (Proxy Firewalls)

#### Definition

An application-layer firewall (also called a **proxy firewall**) operates at OSI layer 7. Instead of simply reading packet headers, it reads the actual content of packets. It uses a module called **DPI (Deep Packet Inspection)** to analyze packet payloads.

Each application protocol has a dedicated proxy process. For example, FTP traffic is handled by an FTP proxy, which checks whether the FTP commands conform to the FTP protocol specification. This means the firewall filters the **protocol behavior**, not just the port number.

#### How Signature-Based Filtering Works

Firewall vendors analyze known attacks (viruses, spam, exploits) and create **signatures** — unique patterns that identify each attack. These signatures are stored in the firewall's database. The proxy firewall compares all traffic against these signatures and blocks traffic that matches a known attack pattern.

#### Limitation

The vendor must continuously update the signature database, because attackers change their techniques and the signatures change accordingly.

#### Key Benefit Over Other Types

- Hides real internal IP addresses effectively
- Can inspect and filter based on actual application data, not just ports

---

## iptables Fundamentals

### Overview

**Netfilter** is the firewall framework built into the Linux kernel. It provides the hooks and mechanisms for packet inspection and filtering.

**iptables** is the command-line interface (the "language") used to define and manage the rules that Netfilter enforces. Think of Netfilter as the engine and iptables as the control panel.

iptables is a **stateless packet-filtering firewall** operating at OSI layers 3 (IP) and 4 (TCP/UDP).

---

### Tables

iptables organizes rules into **tables**, each serving a different purpose:

| Table | Purpose |
|---|---|
| **filter** | The main firewall table. Controls which packets are accepted or dropped. This is the default table when no `-t` option is specified. |
| **nat** | Network Address Translation. Modifies source or destination IP addresses to change packet routing (e.g., masquerading, port forwarding). |
| **mangle** | Modifies packet header fields. For example, modifying the TTL (Time To Live) field to extend a packet's lifetime on the network. |
| **raw** | Evaluates packets as a group/session rather than individually. Used for connection tracking exemptions. |

> In this lab, we focus primarily on the **filter** table, which is the actual firewall.

---

### Chains

Within each table, rules are organized into **chains**. A chain is a list of rules that is evaluated sequentially for each packet. iptables has three built-in chains in the filter table:

#### INPUT Chain

Handles all packets **arriving at the local machine** that are destined for a process running on that machine.

- A packet sent to this machine's IP address travels through the INPUT chain
- If not rejected, the packet is delivered to the local process (service/application)

#### OUTPUT Chain

Handles all packets **generated by the local machine** that are leaving the machine.

- A process on this machine sends a connection request — that packet goes through OUTPUT
- Example: this machine initiates an HTTP request to a web server

#### FORWARD Chain

Handles packets that **pass through this machine** but are neither originated by it nor destined for it. This applies when the machine acts as a router or gateway.

- A packet arrives on one network interface, is routed, and leaves through another interface
- The packet travels through FORWARD — not INPUT, because this machine is not the destination

> **Key concept for the exam:** A packet arriving at a router goes through FORWARD (on the router) and then INPUT (on the destination machine). It does NOT go through INPUT on the router.

#### Packet Flow Diagram

```
                        Incoming Packet
                               │
                               ▼
                    ┌─────────────────┐
                    │    Routing      │
                    │   Decision      │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │                             │
              ▼                             ▼
     Destined for THIS machine       Destined for ANOTHER machine
              │                             │
              ▼                             ▼
        ┌──────────┐                 ┌──────────────┐
        │  INPUT   │                 │   FORWARD    │
        │  Chain   │                 │    Chain     │
        └────┬─────┘                 └──────┬───────┘
             │                             │
             ▼                             ▼
      Local Process                  Post-Routing
             │
             ▼
        ┌──────────┐
        │  OUTPUT  │
        │  Chain   │
        └──────────┘
             │
             ▼
      Outgoing Packet
```

---

### Rule Matching and Actions

Each rule in a chain specifies **matching criteria** and an **action** (called a **target**). When a packet matches a rule's criteria, iptables applies the target action.

#### Actions (Targets)

| Action | Behavior |
|---|---|
| **ACCEPT** | Allow the packet to proceed to its destination |
| **DROP** | Silently discard the packet. The sender receives no notification. |
| **REJECT** | Discard the packet AND send an error message (TCP RST or ICMP port-unreachable) back to the sender |

> **DROP vs REJECT:** DROP is stealthier — the sender doesn't know why there is no response (could be a timeout). REJECT is friendlier — the sender immediately knows the connection was refused. For external-facing security, DROP is often preferred because it gives attackers less information.

---

### iptables Rule Syntax

The full syntax for adding a rule to iptables is:

```
iptables -A <chain> -i <input_interface> -o <output_interface> -p <protocol> -s <source_IP> -d <destination_IP> --sport <source_port> --dport <destination_port> -j <action>
```

#### Parameter Reference

| Parameter | Meaning | Example |
|---|---|---|
| `-A <chain>` | Append a rule to the specified chain | `-A INPUT` |
| `-i <interface>` | Match packets arriving on this interface | `-i eth0` |
| `-o <interface>` | Match packets leaving on this interface | `-o eth1` |
| `-p <protocol>` | Match this protocol | `-p tcp` or `-p udp` or `-p icmp` |
| `-s <source>` | Match this source IP address or network | `-s 192.168.1.0/24` |
| `-d <destination>` | Match this destination IP address or network | `-d 10.10.3.0/24` |
| `--sport <port>` | Match this source port | `--sport 1024` |
| `--dport <port>` | Match this destination port | `--dport 80` |
| `-j <action>` | Jump to this action if matched | `-j ACCEPT` or `-j DROP` or `-j REJECT` |
| `!` (negation) | Match anything EXCEPT the specified value | `--dport ! 443` |

> **Note:** Not all parameters are required in every rule. You only specify the parameters you want to match. Unspecified parameters match all values.

---

### Rule Order — Critical Concept

iptables evaluates rules **sequentially**, starting from the first rule in the chain. The **first rule that matches a packet is applied**, and no further rules are evaluated for that packet.

This means:

- **Specific rules must come before general rules**
- A broad ACCEPT rule placed before a DROP rule will allow traffic that should have been blocked
- A DROP rule placed before an ACCEPT rule for a specific port will block that port

#### Example of Correct Rule Order

```
Rule 1:  ACCEPT  any traffic destined to 1.2.3.4 on port 25 (email server)
Rule 2:  ACCEPT  any traffic from internal users to any destination
Rule 3:  DROP    everything else
```

If rules 1 and 2 were reversed, internal users could connect anywhere (matching Rule 1 as the broader rule) and the specific email server rule would still work. But if Rule 3 were placed first, all traffic would be dropped before reaching Rule 1 or Rule 2.

---

### Default Policy

The **default policy** is the action applied to a packet when it does not match any rule in the chain. Setting a default policy is equivalent to adding a catch-all rule at the very end of the chain.

```
iptables -P INPUT DROP      # Drop all inbound packets not matched by a rule
iptables -P OUTPUT DROP     # Drop all outbound packets not matched by a rule
iptables -P FORWARD DROP    # Drop all forwarded packets not matched by a rule
```

> **Best practice:** Set the default policy to DROP (deny all by default), then explicitly allow only the traffic you need. This implements the **least privilege / default deny** principle.

---

### Flushing (Resetting) Rules

To remove all rules from a chain (reset to empty):

```bash
iptables -F INPUT
iptables -F OUTPUT
iptables -F FORWARD
```

> **Note:** Flushing removes all rules but does **not** change the default policy. If the default policy is DROP and you flush all rules, all traffic will be dropped. This is an important operational consideration.

---

## Practical Demonstration

This section walks through every command used in the lab, with detailed explanations of what each command does, what result to expect, and why it matters from a security perspective.

---

### Step 1 — Listing Current Firewall Rules

#### 1.1 — View filter table rules (default)

```bash
iptables -L
```

**Explanation:** Lists all rules in all chains of the default **filter** table (INPUT, FORWARD, OUTPUT). If no rules have been added, each chain shows "policy ACCEPT" (default policy) and no rules.

**Expected Result:**

```
Chain INPUT (policy ACCEPT)
target     prot opt source               destination

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
```

**Security Purpose:** Verify the current state of the firewall before making changes. Also useful for auditing — confirming that expected rules are in place.

---

#### 1.2 — View NAT table rules

```bash
iptables -L -t nat
```

**Explanation:** The `-t nat` flag specifies the **nat** table instead of the default filter table. The nat table contains rules for NAT (Network Address Translation), including PREROUTING and POSTROUTING chains.

**Expected Result:** Shows chains specific to the nat table (PREROUTING, INPUT, OUTPUT, POSTROUTING). Usually empty in a basic lab environment.

**Security Purpose:** Understand NAT rules that may redirect or masquerade traffic — important when diagnosing unexpected traffic flows.

---

#### 1.3 — View mangle table rules

```bash
iptables -L -t mangle
```

**Explanation:** The `-t mangle` flag specifies the **mangle** table. This table is used to modify packet header fields, such as TTL (Time To Live).

**Expected Result:** Shows mangle table chains. Usually empty in a basic lab environment.

**Difference Summary:**

| Command | Table Shown | Typical Use |
|---|---|---|
| `iptables -L` | filter | Packet allow/deny decisions |
| `iptables -L -t nat` | nat | Address translation rules |
| `iptables -L -t mangle` | mangle | Packet header modification |

---

### Step 2 — Running a Baseline Network Scan

Before applying any firewall rules, run a network scan from Kali Linux to establish a baseline of open ports on the Metasploitable machine.

```bash
nmap -sV <victim_IP>
```

**Explanation:** `nmap -sV` performs a service version detection scan. It probes open ports and attempts to identify the service and version running on each port.

**Expected Result:** A list of open ports including (among others):

- **Port 21** — FTP (open)
- **Port 22** — SSH (open)
- **Port 23** — Telnet (open)

**Security Purpose:** Establish a baseline. Document which ports are open before any firewall rules are applied. After applying rules, you will re-run this scan to observe the effect of each rule.

---

### Step 3 — Setting a Default DROP Policy on FORWARD

```bash
iptables -P FORWARD DROP
```

**Explanation:** Sets the default policy for the FORWARD chain to DROP. Any packet that passes through this machine (intended for another destination) that does not match an explicit rule will be silently dropped.

**Expected Result of `iptables -L` after this command:**

```
Chain INPUT (policy ACCEPT)
target     prot opt source               destination

Chain FORWARD (policy DROP)
target     prot opt source               destination

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
```

**Re-run nmap from Kali:**

```bash
nmap -sV <victim_IP>
```

**Expected Observation:** The scan results are **unchanged**. Ports 21, 22, and 23 still appear open.

**Why?** The nmap scan is targeting the Metasploitable machine directly. The packets are destined **for** the Metasploitable machine, so they go through the **INPUT** chain — not the FORWARD chain. The FORWARD chain only affects packets that are passing **through** the machine to another destination. Since we only changed FORWARD, the direct scan results are unaffected.

**Security Purpose:** Demonstrates the difference between INPUT and FORWARD chains. A machine that is not acting as a router is not affected by FORWARD rules when it is the direct target of traffic.

---

### Step 4 — Setting a Default DROP Policy on INPUT

```bash
iptables -P INPUT DROP
```

**Explanation:** Sets the default policy for the INPUT chain to DROP. All packets arriving at this machine that do not match an explicit ACCEPT rule will be silently discarded.

**Re-run nmap from Kali:**

```bash
nmap -sV <victim_IP>
```

**Expected Observation:** Nmap reports all ports as **filtered** (no response received). No open ports are shown.

**Why?** With INPUT defaulting to DROP and no ACCEPT rules in place, every packet from the Kali machine is discarded before it reaches any service. The services are still running on Metasploitable — they just cannot receive any packets from outside because the firewall drops all incoming traffic before it gets to them.

**Security Purpose:** Demonstrates the power of a default DROP policy. A machine is effectively invisible to network scanners when INPUT is set to DROP with no exceptions. This is the foundation of a "deny all, permit by exception" security posture.

---

### Step 5 — Allowing Specific Ports (Whitelisting)

Now we will selectively open specific ports while keeping the default DROP policy. We allow ports 80, 53, 8180, and 445.

```bash
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

**Explanation:** Appends a rule to the INPUT chain. It matches TCP packets destined for port 80 (HTTP) and accepts them.

```bash
iptables -A INPUT -p tcp --dport 53 -j ACCEPT
```

**Explanation:** Allows incoming TCP packets to port 53 (DNS).

```bash
iptables -A INPUT -p tcp --dport 8180 -j ACCEPT
```

**Explanation:** Allows incoming TCP packets to port 8180 (Apache Tomcat web interface on Metasploitable).

```bash
iptables -A INPUT -p tcp --dport 445 -j ACCEPT
```

**Explanation:** Allows incoming TCP packets to port 445 (SMB — Windows file sharing / Samba).

**Verify rules were added:**

```bash
iptables -L
```

**Expected Result:**

```
Chain INPUT (policy DROP)
target     prot opt source               destination
ACCEPT     tcp  --  anywhere             anywhere    tcp dpt:http
ACCEPT     tcp  --  anywhere             anywhere    tcp dpt:domain
ACCEPT     tcp  --  anywhere             anywhere    tcp dpt:8180
ACCEPT     tcp  --  anywhere             anywhere    tcp dpt:microsoft-ds
```

**Re-run nmap from Kali:**

```bash
nmap -sV <victim_IP>
```

**Expected Observation:** Only ports 80, 53, 8180, and 445 appear as **open**. All other ports (including 21, 22, 23) appear as **filtered**.

**Why?** The four ACCEPT rules explicitly allow traffic on those four ports. All other traffic hits the default DROP policy and is discarded. The nmap scanner receives responses on ports 80, 53, 8180, and 445, but gets no responses on all other ports.

**Security Purpose:** This is the correct approach to firewall configuration — default deny with explicit exceptions for required services only.

---

### Step 6 — Switching to Default ACCEPT with Specific Port Blocking (Blacklisting)

Now we demonstrate the alternative (and weaker) approach: allow everything by default and block specific ports.

First, change the INPUT default policy back to ACCEPT:

```bash
iptables -P INPUT ACCEPT
```

**Explanation:** Sets the default INPUT policy back to ACCEPT. All traffic is allowed unless explicitly blocked.

Now block specific ports — 21 (FTP), 22 (SSH), and 23 (Telnet):

```bash
iptables -A INPUT -p tcp --dport 21 -j REJECT
```

**Explanation:** Appends a rule to reject all TCP packets destined for port 21 (FTP). Unlike DROP, REJECT sends an error response back to the sender.

```bash
iptables -A INPUT -p tcp --dport 22 -j REJECT
```

**Explanation:** Rejects TCP packets to port 22 (SSH).

```bash
iptables -A INPUT -p tcp --dport 23 -j REJECT
```

**Explanation:** Rejects TCP packets to port 23 (Telnet).

**Re-run nmap from Kali:**

```bash
nmap -sV <victim_IP>
```

**Expected Observation:** Ports 21, 22, and 23 now appear as **closed** (because REJECT sends back an RST/ICMP error). All other ports remain open.

**Security Discussion:** This blacklist approach is weaker because you must explicitly block every dangerous port. If a new service starts on an unblocked port, it is immediately exposed. The whitelist approach (default DROP) is more secure because new services are blocked by default.

---

### Step 7 — Blocking All Remaining TCP and UDP Traffic

```bash
iptables -A INPUT -p tcp -j REJECT
iptables -A INPUT -i eth0 -p udp -j REJECT
```

**Explanation:**

- Rule 1: Appends a rule to reject all remaining TCP packets that haven't been matched by earlier rules
- Rule 2: Appends a rule to reject all UDP packets arriving on the `eth0` interface

**Re-run nmap from Kali:**

```bash
nmap -sV <victim_IP>
```

**Expected Observation:** All ports are now **closed** or **filtered**, depending on rule order with respect to the earlier ACCEPT rules. No services appear accessible.

**Security Purpose:** Demonstrates how a catch-all REJECT rule at the end of the chain can block all traffic not explicitly permitted by earlier rules — achieving a similar effect to a default DROP policy, but using an explicit rule rather than the policy mechanism.

---

### Step 8 — Flushing All Rules

To reset the firewall to a clean state (remove all rules without changing the default policy):

```bash
iptables -F INPUT
iptables -F OUTPUT
iptables -F FORWARD
```

**Explanation:** `-F` (flush) removes all rules from the specified chain. This does not affect the default policy.

**Security Warning:** If your default policy is DROP and you flush all rules, all traffic will be blocked, including legitimate administrative connections (SSH). Always plan your rule changes carefully in production environments.

---

### Summary of iptables Commands

| Command | Purpose |
|---|---|
| `iptables -L` | List all rules in the filter table |
| `iptables -L -t nat` | List all rules in the nat table |
| `iptables -L -t mangle` | List all rules in the mangle table |
| `iptables -P INPUT DROP` | Set default INPUT policy to DROP |
| `iptables -P FORWARD DROP` | Set default FORWARD policy to DROP |
| `iptables -P INPUT ACCEPT` | Set default INPUT policy to ACCEPT |
| `iptables -A INPUT -p tcp --dport 80 -j ACCEPT` | Allow inbound TCP traffic on port 80 |
| `iptables -A INPUT -p tcp --dport 22 -j REJECT` | Reject inbound TCP traffic on port 22 |
| `iptables -A INPUT -p tcp -j REJECT` | Reject all remaining inbound TCP traffic |
| `iptables -A INPUT -i eth0 -p udp -j REJECT` | Reject all UDP traffic on eth0 |
| `iptables -F INPUT` | Flush (remove) all rules from INPUT chain |
| `iptables -F OUTPUT` | Flush (remove) all rules from OUTPUT chain |
| `iptables -F FORWARD` | Flush (remove) all rules from FORWARD chain |

---

## Lab Exercises

Complete the following exercises in order. Document your observations and answers.

---

### Exercise 1 — Baseline Inspection

**On Metasploitable (as root):**

1. Run `iptables -L` and record the output.
2. Run `iptables -L -t nat` and record the output.
3. Run `iptables -L -t mangle` and record the output.

**Questions:**

a) What is the default policy for INPUT, FORWARD, and OUTPUT in the filter table before any changes?

b) What is the main difference between the three commands above?

c) Which table would you use if you wanted to change the source IP address of outbound packets?

---

### Exercise 2 — Port Scanning Baseline

**On Kali Linux:**

1. Run `nmap -sV <Metasploitable_IP>` and record all open ports.

**Questions:**

a) What is the state (open/closed/filtered) of ports 21, 22, and 23?

b) What service is running on each of these three ports?

c) Why is it a security concern to have these ports open?

---

### Exercise 3 — FORWARD Chain Policy

**On Metasploitable (as root):**

1. Run `iptables -P FORWARD DROP`
2. Run `iptables -L` to confirm the change

**On Kali Linux:**

1. Re-run `nmap -sV <Metasploitable_IP>`

**Questions:**

a) Did the nmap scan results change after setting FORWARD to DROP? Why or why not?

b) In what scenario would setting FORWARD to DROP affect scan results?

---

### Exercise 4 — INPUT Chain Policy

**On Metasploitable (as root):**

1. Run `iptables -P INPUT DROP`

**On Kali Linux:**

1. Re-run `nmap -sV <Metasploitable_IP>`

**Questions:**

a) What happened to the scan results? Describe what nmap reports.

b) Are the services (FTP, SSH, Telnet) still running on Metasploitable? How do you know?

c) Why does setting INPUT to DROP cause the scan to show no open ports?

---

### Exercise 5 — Whitelisting Specific Ports

**On Metasploitable (as root), with INPUT policy still set to DROP:**

1. Add ACCEPT rules for ports 80, 53, 8180, and 445 (TCP)
2. Run `iptables -L` and confirm four rules appear in INPUT

**On Kali Linux:**

1. Re-run `nmap -sV <Metasploitable_IP>`

**Questions:**

a) Which ports does nmap now show as open?

b) What is the state of ports 21, 22, and 23?

c) Explain why only the four specified ports are accessible even though Metasploitable has many more services running.

---

### Exercise 6 — Blacklisting Specific Ports

**On Metasploitable (as root):**

1. Set INPUT policy back to ACCEPT: `iptables -P INPUT ACCEPT`
2. Add REJECT rules for ports 21, 22, and 23

**On Kali Linux:**

1. Re-run `nmap -sV <Metasploitable_IP>`

**Questions:**

a) What is the state of ports 21, 22, and 23 now?

b) Compare the output to Exercise 4 (default DROP). What is the difference in how blocked ports appear?

c) Which approach is more secure — whitelist (default DROP + allow) or blacklist (default ACCEPT + block)? Why?

---

### Exercise 7 — Security Impact Assessment

After completing all exercises, attempt the following attacks from Kali Linux against Metasploitable (with the configuration from Exercise 5 active — default DROP, only ports 80, 53, 8180, 445 open).

**Attack 1 — Telnet connection attempt:**

```bash
telnet <Metasploitable_IP>
```

**Questions:**

a) What is the result of the Telnet connection attempt?

b) Why is this the expected result?

**Attack 2 — FTP exploit attempt (reference prior labs on port 21 vulnerabilities):**

Attempt to exploit the FTP vulnerability on port 21.

**Questions:**

a) What is the result?

b) Why did the firewall prevent this attack?

c) What does this tell you about the relationship between open ports and vulnerability exposure?

---

## Key Concepts Summary

| Concept | Summary |
|---|---|
| **Firewall** | A mandatory checkpoint between networks that enforces a security policy |
| **Security Policy** | A set of rules based on business needs that defines what traffic is allowed |
| **Default Deny** | Block all traffic by default; explicitly allow only what is needed (recommended) |
| **Default Allow** | Allow all traffic by default; explicitly block dangerous traffic (not recommended) |
| **Stateless Firewall** | Inspects each packet independently; no memory of connections; uses ACLs |
| **Netfilter** | The Linux kernel firewall framework |
| **iptables** | The command-line interface for configuring Netfilter rules |
| **filter table** | The iptables table that controls packet allow/deny decisions |
| **nat table** | The iptables table that handles Network Address Translation |
| **mangle table** | The iptables table that handles packet header modification |
| **INPUT chain** | Rules applied to packets destined for the local machine |
| **OUTPUT chain** | Rules applied to packets originating from the local machine |
| **FORWARD chain** | Rules applied to packets passing through the machine |
| **ACCEPT** | Allow the packet |
| **DROP** | Silently discard the packet |
| **REJECT** | Discard the packet and notify the sender |
| **Default Policy** | Action taken when no rule matches (set with `-P`) |
| **Flush** | Remove all rules from a chain (using `-F`) |
| **Rule Order** | Specific rules must precede general rules; first match wins |

---

## CompTIA Security+ Exam Prep

The following points directly support Security+ exam objectives:

1. **Stateless vs. Stateful:** Know that stateless firewalls process packets independently (no session awareness). Stateful firewalls maintain a connection state table and can recognize return traffic automatically.

2. **Firewall placement:** Firewalls should be placed between networks (next to a router), acting as a mandatory passage for all traffic between the segments.

3. **OSI Layers:** Stateless filtering = layers 3 and 4. Application proxy = layer 7.

4. **Least Privilege for Firewalls:** Default DENY (block everything, allow only what is needed) is the security best practice.

5. **DMZ:** A DMZ allows servers to be accessible from the Internet without exposing the internal network. An additional firewall sits between the DMZ and the internal LAN.

6. **Defense in Depth:** Use both hardware firewalls at the network perimeter and software (host-based) firewalls on individual machines.

7. **ACL:** Access Control List — the rule list used by stateless firewalls. Rules are evaluated in order; first match wins.

8. **DROP vs. REJECT:** DROP is stealthier (attacker gets no feedback). REJECT sends an error message back.

9. **Return Traffic Problem:** Stateless firewalls require explicit rules to allow return (ACK) traffic for outbound connections — a limitation solved by stateful firewalls.

---

## Glossary

| Term | Definition |
|---|---|
| **ACL** | Access Control List — a list of permit/deny rules used by stateless firewalls |
| **Chain** | A named list of iptables rules evaluated in order for matching packets |
| **Default Policy** | The action taken when a packet matches no rule in a chain |
| **DMZ** | Demilitarized Zone — a netwok segment between the Internet and the internal network, hosting publicly accessible servers |
| **DPI** | Deep Packet Inspection — inspection of packet content (payload), not just headers |
| **DROP** | Silently discard a packet; no notification to sender |
| **Firewall** | A security device that controls traffic between networks based on rules |
| **Flush** | Remove all rules from an iptables chain |
| **FORWARD** | The iptables chain for packets passing through the machine to another destination |
| **INPUT** | The iptables chain for packets arriving at the local machine |
| **iptables** | The command-line interface for configuring the Linux Netfilter firewall |
| **LAN** | Local Area Network — an internal organizational network |
| **Mangle** | iptables table for modifying packet header fields (e.g., TTL) |
| **NAT** | Network Address Translation — modifying source/destination IP addresses |
| **Netfilter** | The firewall engine built into the Linux kernel |
| **OUTPUT** | The iptables chain for packets sent from the local machine |
| **Policy** | The default action for a chain when no rules match |
| **Proxy Firewall** | Application-layer firewall that inspects packet content |
| **REJECT** | Discard a packet and send an error response to the sender |
| **Security Policy** | A set of organizational rules that drive firewall configuration |
| **Signature** | A unique pattern used to identify a known attack in an application-layer firewall |
| **Stateful Firewall** | A firewall that tracks connection state and can recognize established sessions |
| **Stateless Firewall** | A firewall that inspects each packet independently, with no connection memory |
| **Table** | An iptables organizational structure grouping related chains and rules |
| **TTL** | Time To Live — a packet header field controlling how many hops a packet can traverse |
| **WAN** | Wide Area Network — the Internet or an external network |

---

*End of LAB 1 — Introduction to Stateless Firewalls Using iptables*

*BrainerX | CompTIA Security+ | Instructor: Nidhal Lahcen*
