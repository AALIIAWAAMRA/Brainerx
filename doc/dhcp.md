The Dynamic Host Configuration Protocol (DHCP) operates using a structured four-step process often remembered by the acronym **DORA**: **D**iscover, **O**ffer, **R**equest, and **A**cknowledge. This workflow relies on UDP broadcast and unicast messages to automatically assign an IP address to a client.

Here is the complete step-by-step workflow of a successful DHCP connection.

---

### The DORA Workflow

#### 1. Discover (`DHCPDISCOVER`)

When a device (client) connects to a network, it does not have an IP address, subnet mask, or gateway. It begins by broadcasting a discovery message to find any available DHCP servers on the network.

* **Source IP:** `0.0.0.0` (Since the client doesn't have an IP yet)
* **Destination IP:** `255.255.255.255` (Network-wide broadcast)
* **Ports Used:** Source Port `68` $\rightarrow$ Destination Port `67`

#### 2. Offer (`DHCPOFFER`)

Any DHCP server that receives the discovery message checks its pool of available IP addresses and reserves one for the client. The server then sends an offer message containing the proposed configuration.

* **Source IP:** DHCP Server IP (e.g., `192.168.1.1`)
* **Destination IP:** `255.255.255.255` (Broadcast) or the client's Hardware/MAC address (Unicast, depending on the server configuration).
* **Payload:** Contains the offered IP address (e.g., `192.168.1.50`), Subnet Mask, Lease Time, Default Gateway, and DNS Server IPs.
* **Ports Used:** Source Port `67` $\rightarrow$ Destination Port `68`

#### 3. Request (`DHCPREQUEST`)

The client receives the offer. If multiple DHCP servers sent offers, the client typically accepts the first one it receives. It then broadcasts a request message formally asking to lease that specific IP address.

* **Source IP:** `0.0.0.0`
* **Destination IP:** `255.255.255.255` (Broadcast)
* **Why Broadcast?** This informs the chosen server that its offer was accepted, while simultaneously signaling to any other DHCP servers that their offers were declined, allowing them to release their reserved IPs back into their pools.

#### 4. Acknowledgment (`DHCPACK`)

The chosen DHCP server receives the request, finalizes the lease in its database, and sends an acknowledgment packet to the client confirming the assignment.

* **Source IP:** DHCP Server IP
* **Destination IP:** `255.255.255.255` or Client MAC
* **Result:** Upon receiving this packet, the client configures its network interface with the assigned IP settings, and it can now officially communicate on the network.

---

### Subsequent States: Renewal and Release

The connection workflow doesn't completely end at `DHCPACK`. Because IP addresses are leased rather than given permanently, two other important phases exist:

* **DHCP Renewal (`DHCPREQUEST` at 50% Lease Time):** When **50%** of the lease time expires (known as $T1$), the client sends a *unicast* `DHCPREQUEST` directly to the server that granted the lease to ask for an extension. If the server responds with a `DHCPACK`, the timer resets. If no response is received, the client tries again at **87.5%** of the lease time ($T2$) via a *broadcast* to find *any* available DHCP server.
* **DHCP Release (`DHCPRELEASE`):** When a device gracefully disconnects from the network (e.g., shutting down safely or manually releasing the IP via command line), it sends a unicast `DHCPRELEASE` message to the server, freeing up that IP address immediately for other devices.
