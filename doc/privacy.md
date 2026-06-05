``` bash
sudo anonsurf start
```
this will change the iptables rule of the system to catch any 
external connection and forwored mondatory via TOR networek
this enclude (*os updates , web browsering , DNS packet ...*)

### how install anaonsurf

```
git clone https://github.com/Und3rf10w/kali-anonsurf.git
cd kali-anonsurf
sudo ./installer.sh
```


### very important

```
عندما تقوم بتشغيل الأداة، فإنها لا تكتفي بفتح نفق عبر Tor فحسب، بل تقوم بتطبيق قواعد جدار حماية صارمة جداً (iptables) تمنع أي نوع من أنواع الاتصال المباشر (Cleartext/Direct connection) خارج هذا النفق.

إليك تفسير ما يحدث مع الأدوات والمتصفحات التي ذكرتها:

1. المتصفحات الخارجية (مثل Chrome أو Firefox العادي)
الأداة تمنعها أو تغلقها لأن هذه المتصفحات تقوم افتراضياً بعمليات ربط وتخزين مؤقت (Caching) وقد ترسل طلبات DNS بشكل مباشر خارج شبكة Tor (وهو ما يسمى DNS Leak). تعطل الأداة هذه المنافذ لإجبارك على استخدام متصفح معزول تماماً ومعد مسبقاً للـ Proxies مثل Tor Browser لضمان عدم تسريب بصمة جهازك الرقمية.

2. أدوات الشبكة والمنافذ (hping3, curl, host, nmap)
هنا تكمن نقطة حساسة جداً لعملك في اختبار الاختراق (Penetration Testing):

بروتوكول TCP: أدوات مثل curl أو wget ستعمل معك بشرط أن تدعم حزم SOCKS5 أو إذا قامت الأداة بتحويل حزم TCP بنجاح.

بروتوكول UDP و ICMP (الـ Ping): شبكة Tor لا تدعم بروتوكولات UDP و ICMP على الإطلاق، هي مصممة فقط لحمل حركة مرور TCP.

النتيجة: أدوات مثل hping3 (عند إرسال حزم مخصصة أو SYN scans عنيفة)، أو أمر ping العادي، أو طلبات البحث عن النطاقات host/nslookup التي تعتمد على UDP، ستفشل بالكامل وتتوقف. جدار الحماية يمنعها تماماً بدلاً من أن يسمح لها بالخروج بشكل مكشوف (بدون Tor) فتكشف هويتك.
```


# Technical Note: Proxychains vs Proxychains4 & Protocol Architecture

This note documents the evolutionary differences between the legacy `proxychains` and the modern `proxychains4` (ProxyChains-NG) wrappers, alongside a deep architectural breakdown of SOCKS4 vs SOCKS5 proxy protocols.

---

## 1. Proxychains (Legacy) vs Proxychains4 (Next Gen)

The tool name suffix indicates the software version and rewrite history, which directly impacts stability and security during offensive operations.

| Metric / Feature | Proxychains (Legacy v3.x) | Proxychains4 (Next Generation v4.x) |
| :--- | :--- | :--- |
| **Status** | Unmaintained / Abandoned (Since ~2006) | Actively Maintained (ProxyChains-NG) |
| **Codebase** | Old C architecture, prone to memory leaks | Rewritten from scratch for stability |
| **IPv6 Support** | Broken / IPv4 Only | Full Native IPv6 Support |
| **Thread Safety** | Non-thread-safe (Crashes under multi-threading) | Thread-safe (Handles asynchronous connections) |
| **Configuration File**| `/etc/proxychains.conf` | `/etc/proxychains4.conf` |
| **Hooking Method** | Old `LD_PRELOAD` hacks | Modern `libproxychains4.so` injection |

### Operational Breakdown of the Differences

#### A. Multi-Threading & Tool Stability

* **Legacy Proxychains:** If you run a high-threaded scanner or directory brute-forcer (like `gobuster`, `dirb`, or custom multi-threaded Python exploits), the legacy tool fails to handle concurrent connection hooks. It frequently throws `Segmentation Faults` or freezes.
* **Proxychains4:** Engineered specifically to handle multi-threaded applications. It safely intercepts and queues socket calls from multiple threads simultaneously, making it reliable for heavy automated infrastructure scanning.

#### B. The IPv6 Blindspot (OPSEC Risk)

* If an application running under legacy `proxychains` attempts to connect to a target that resolves to an IPv6 address, the tool cannot hook the connection. The operating system will either drop the packet or, worse, route it via the host's default **cleartext IPv6 gateway**, completely exposing your real IP address.
* `proxychains4` handles IPv6 hooks seamlessly, mapping or tunneling them safely according to the proxy chain specifications.

---

## 2. Proxy Protocols Supported by Each Version

Both tools act as hook layers that force software traffic through predefined proxies, but their protocol engines differ:

### Proxychains (Legacy) Supported Proxies

* **HTTP / HTTPS** (Connect method only)
* **SOCKS4**
* **SOCKS5** (Basic implementation, lacks stable DNS/Auth chaining)

### Proxychains4 Supported Proxies

* **HTTP / HTTPS** (Enhanced CONNECT tunnel support)
* **SOCKS4** (Legacy backward compatibility)
* **SOCKS5** (Full implementation including secure remote DNS resolution and robust authentication handling)

---

## 3. High-Level Protocol Comparison Matrix: SOCKS4 vs SOCKS5

| Feature / Metric | SOCKS4 | SOCKS5 |
| :--- | :--- | :--- |
| **OSI Layer** | Layer 5 (Session Layer) | Layer 5 (Session Layer) |
| **Supported Transport Protocols** | TCP Only | TCP & UDP (via UDP Associate) |
| **Authentication Methods** | None (Ident-based User-ID only) | Null, Username/Password, GSS-API |
| **DNS Resolution Location** | Client-Side (Leaky) | Server-Side / Proxy-Side (Secure) |
| **IPv6 Support** | No (IPv4 Only) | Yes (Full Native Support) |
| **RFC Specification** | None (Unofficial Memo) | RFC 1928 (IETF Standard) |

---

## 4. Deep Dive: Architectural Protocol Differences

### A. Transport Layer Capabilities (TCP vs UDP)

* **SOCKS4:** Hardcoded to support **TCP streams only**. It is completely blind to UDP packets. Any tool trying to utilize UDP (like fast DNS queries, VoIP, or custom C2 channels) will break or bypass the proxy entirely.
* **SOCKS5:** Introduces the `UDP ASSOCIATE` command. When a client wants to send UDP data, it establishes a TCP control connection to the SOCKS5 server, which opens a dedicated UDP port to handle and forward the UDP datagrams.

### B. The DNS Resolution Problem (Critical for OPSEC)

In offensive security and anonymity, *where* a domain name is resolved into an IP address determines your protection status.

* **SOCKS4 (The Leak Trap):**
    The client application must resolve `target.com` to an IP address **before** initiating the SOCKS4 connection block.
    $$\text{Client} \xrightarrow{\text{Plaintext DNS Request}} \text{Local ISP DNS} \rightarrow \text{Leaks Identity}$$

* **SOCKS5 (Remote Resolution):**
    The client can pass the raw domain name string directly inside the SOCKS5 request packet (Address Type `0x03`). The proxy server (or the Tor Exit Node) performs the DNS resolution on its end.
    $$\text{Client} \xrightarrow{\text{Encrypted SOCKS5 Tunnel}} \text{Proxy/Tor Node} \xrightarrow{\text{DNS Request}} \text{Target}$$

### C. Authentication Framework

* **SOCKS4:** Relies on an outdated "User-ID" field within the connection header. It does not challenge the client for a password, making it useless for access control over untrusted networks.
* **SOCKS5:** Features a sub-negotiation phase. Upon connection, the client sends a list of supported authentication methods. The server selects one:
  * `0x00`: No Authentication Required (Null).
  * `0x02`: Username/Password (RFC 1929).

---

## 5. Packet Header Anatomy

### SOCKS4 Request Packet Structure (Fixed Size)

```text
+----+----+----+----+----+----+----+----+----+----+....+----+
| VN | CD | DSTPORT |      DSTIP        | USERID      |NULL|
+----+----+----+----+----+----+----+----+----+----+....+----+
  1    1       2              4           Variable      1   (Bytes)
