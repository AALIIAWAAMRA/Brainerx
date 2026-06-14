# Chapter 1.0 — General Security Concepts

---

## Learning Objectives

By the end of this chapter, students will be able to:

1. Compare and contrast the four security control categories (Technical, Managerial, Operational, Physical) and six control types (Preventive, Deterrent, Detective, Corrective, Compensating, Directive).
2. Explain the CIA triad, non-repudiation, and the AAA framework, and describe how each applies in real-world security architecture.
3. Describe Zero Trust architecture, its control plane and data plane components, and why it replaces perimeter-based security.
4. Identify physical security mechanisms and explain their layered defensive role.
5. Explain how deception and disruption technologies are used to detect and study attackers.
6. Explain the importance of change management processes and their direct impact on the security posture of an organization.
7. Describe cryptographic solutions including PKI, symmetric and asymmetric encryption, hashing, digital signatures, and certificate management.

---

## Why This Chapter Matters

Security is not a product you buy — it is a discipline you design, implement, and continuously manage. Before you can defend a network, protect data, or respond to an incident, you need a coherent vocabulary and a mental model that lets you reason about security problems systematically.

This chapter builds that foundation. The concepts here — controls, CIA, Zero Trust, change management, cryptography — appear in every domain of cybersecurity. Whether you are hardening a server, designing a cloud architecture, writing a policy, or investigating a breach, you will trace your decisions back to principles introduced in this chapter.

Every concept covered here also maps directly to the CompTIA Security+ SY0-701 exam objectives.

---

## Section 1.1 — Compare and Contrast Various Types of Security Controls

### The Two Dimensions of Security Controls

Security controls are safeguards or countermeasures designed to avoid, detect, counteract, or minimize security risks. Every control has two dimensions:

- **Category** — *Who or what implements the control?* (Technical, Managerial, Operational, Physical)
- **Type** — *What is the control intended to do?* (Preventive, Deterrent, Detective, Corrective, Compensating, Directive)

Understanding both dimensions together allows you to reason about gaps and overlaps in a security program. A single control often spans multiple types. A locked server room door is both Preventive (it stops access) and Deterrent (it discourages attempts).

![](../src/Types-of-security-controls-1.jpg)

---

### Control Categories

#### Technical Controls

Technical controls are implemented through technology — hardware, software, firmware, or a combination. They are automated, consistent, and operate independently of human behavior once deployed.

**Examples:**
- Firewalls filtering network traffic
- Antivirus software scanning files
- Encryption protecting data at rest
- Multi-factor authentication (MFA) on a VPN
- Intrusion Detection Systems (IDS) monitoring network packets

> **Instructor note:** Students sometimes confuse "technical" with "digital." Remind them that a hardware token (like a YubiKey) is a technical control even though it is a physical object — the *enforcement mechanism* is technical (cryptographic handshake).

#### Managerial Controls

Managerial controls (also called administrative controls) are policy- and procedure-based. They govern *how* people and processes are expected to behave. They do not directly prevent an attack but establish the framework that makes other controls effective.

**Examples:**
- Acceptable Use Policies (AUP)
- Risk assessment processes
- Security awareness training programs
- Background checks for new employees
- Vendor management agreements

> **Instructor note:** A common student mistake is dismissing managerial controls as "soft" or less important. In reality, most security breaches involve human factors — phishing, insider threat, misconfiguration — that managerial controls directly address.

#### Operational Controls

Operational controls are day-to-day procedures carried out by people. They bridge the gap between policy (managerial) and technology (technical). Operational controls are as strong as the people executing them.

**Examples:**
- Security guards checking badges at entry points
- IT staff following a documented patch management process
- Help desk following an identity verification script before resetting passwords
- Incident response team executing a runbook during an alert
- Regular log review performed by a SOC analyst

#### Physical Controls

Physical controls protect the tangible, physical assets of an organization — hardware, buildings, and the people inside them.

**Examples:**
- Locked server rooms with biometric access
- Security cameras covering entry points
- Cable locks on laptops
- Bollards preventing vehicle ramming
- Environmental controls (HVAC, fire suppression)

---

### Control Types

#### Preventive Controls

Preventive controls stop an incident from occurring. They are proactive by design.

| Category | Preventive Example |
|---|---|
| Technical | Firewall blocking unauthorized ports |
| Managerial | Background checks before hiring |
| Operational | Security guard refusing entry without a badge |
| Physical | Locked door requiring keycard access |

#### Deterrent Controls

Deterrent controls discourage an attacker from attempting an action by making the cost or risk of the attempt unattractive. They do not technically stop an action — they rely on psychology.

**Examples:**
- "This network is monitored. Unauthorized access is a federal crime." warning banner
- Visible security cameras at the entrance of a data center
- A sign indicating a premises is alarmed
- Published disciplinary policies for policy violations

> **Instructor note:** Deterrents are only effective if potential attackers are aware of them *and* believe they are real. A fake camera dome may deter casual opportunists but will not stop a determined attacker who tests whether the camera is actually connected.

#### Detective Controls

Detective controls identify and record that an incident has occurred or is in progress. They do not prevent the incident — they generate visibility.

**Examples:**
- Security Information and Event Management (SIEM) systems correlating log data
- Intrusion Detection System (IDS) generating an alert on anomalous traffic
- Security cameras recording activity (note: same camera is *deterrent* when visible, *detective* when it records)
- File integrity monitoring tools detecting unauthorized changes to system files
- Audit logs capturing user access events

#### Corrective Controls

Corrective controls restore a system to its normal state after an incident has occurred. They are reactive by nature.

**Examples:**
- Restoring data from a verified backup after ransomware encryption
- Patching a vulnerability discovered after a breach
- Re-imaging a compromised endpoint
- Revoking a compromised certificate and issuing a new one
- Quarantining a malware-infected system and running remediation tools

#### Compensating Controls

Compensating controls are temporary or alternative controls that provide an equivalent level of protection when a primary control cannot be implemented. They are acceptable workarounds when the ideal solution is not feasible — but they must be formally documented and risk-accepted.

**Real-world scenario:** A legacy industrial control system (ICS) runs a critical manufacturing process. The vendor has not released a patch for a known vulnerability, and the system cannot be taken offline. The organization cannot apply the standard preventive control (patching). A compensating control would be to place the system on an isolated VLAN, monitor all traffic to and from it with an IDS, and require jump server access for any administrative sessions.

> **Instructor note:** Emphasize that a compensating control must be *documented, reviewed, and time-limited* where possible. It is not a permanent excuse to avoid fixing the underlying problem.

#### Directive Controls

Directive controls specify what actions individuals must (or must not) take. They direct behavior rather than enforcing it through technology.

**Examples:**
- An Acceptable Use Policy (AUP) directing employees on approved use of company devices
- A security policy directing that all sensitive data must be encrypted before emailing
- A regulatory requirement directing organizations to report breaches within 72 hours (GDPR)
- A standard operating procedure directing how change requests must be submitted

---

### Putting It Together: Defense in Depth

No single control is sufficient. The industry principle of *defense in depth* calls for layering multiple controls across categories and types so that the failure of one does not lead to a complete compromise.

**Example — Protecting a Data Center Server Room:**

| Layer | Control Category | Control Type |
|---|---|---|
| Fence around building perimeter | Physical | Preventive, Deterrent |
| Security guard at building entrance | Operational | Preventive, Detective |
| Keycard + PIN for server room | Physical / Technical | Preventive |
| CCTV inside server room | Physical / Technical | Detective, Deterrent |
| Audit log of all keycard entries | Technical | Detective |
| Policy requiring badge escort for visitors | Managerial | Directive |
| IDS on server room network segment | Technical | Detective |

---

## Section 1.2 — Fundamental Security Concepts

### The CIA Triad

The CIA triad is the foundational model of information security. Every security decision can be evaluated by how it affects one or more of these three properties.

![](../src/cia-header-banner-(1).tmb-banner.jpg)

#### Confidentiality

Confidentiality ensures that information is accessible only to those who are authorized to access it.

**Goal:** Prevent unauthorized disclosure.

**Mechanisms:** Encryption, access controls, data classification, need-to-know policies, MFA.

**Real-world threat:** A nurse at a hospital accesses celebrity patient records she has no clinical reason to view. Even if she doesn't share the information, confidentiality has been violated (unauthorized access, not necessarily unauthorized disclosure).

**Common controls:** AES-256 encryption for files at rest, TLS for data in transit, role-based access control (RBAC), data loss prevention (DLP) tools.

#### Integrity

Integrity ensures that information is accurate, consistent, and has not been altered by unauthorized parties.

**Goal:** Prevent unauthorized modification.

**Mechanisms:** Cryptographic hashing, digital signatures, file integrity monitoring, version control, checksums.

**Real-world example:** A bank transaction database must not allow any row to be modified after commitment without a corresponding audit entry. A SHA-256 hash of the database can detect whether any record has been altered since the last backup.

```bash
# Generate a SHA-256 hash of a file to verify integrity
sha256sum /etc/passwd
# Output: 3b4c5d6e7f... /etc/passwd

# Store the hash in a secure location, then later verify
sha256sum -c passwd.sha256
# Output: /etc/passwd: OK (if unchanged)
#         /etc/passwd: FAILED (if modified)
```

> **Instructor note:** Integrity does not mean the data is *correct* — it means the data has not been *altered without authorization*. A database can have perfectly intact but factually wrong records if the wrong data was entered correctly.

#### Availability

Availability ensures that systems and data are accessible when needed by authorized users.

**Goal:** Prevent denial of service.

**Mechanisms:** Redundancy, failover, load balancing, DDoS mitigation, backups, UPS systems, SLAs.

**Real-world threat:** A Distributed Denial of Service (DDoS) attack floods a bank's online portal with millions of fake requests, making it unavailable to legitimate customers. The data is not stolen or modified — availability alone is affected.

#### Balancing the Triad

The three properties sometimes conflict with each other:

- **Confidentiality vs. Availability:** Encrypting everything maximizes confidentiality but can degrade performance and access speed.
- **Integrity vs. Availability:** Requiring multi-party approval for every database write maximizes integrity but creates bottlenecks.
- **Security vs. Usability:** Every added security layer reduces ease of use.

Good security design is about finding the right balance for the context — a nuclear plant control system prioritizes integrity and availability over everything else; a public content delivery network prioritizes availability.

---

### Non-repudiation

Non-repudiation is the ability to prove that a specific entity performed a specific action, such that the entity cannot later deny having done it.

**Think of it like a certified letter:** when you sign for a delivery, both the sender and carrier have proof you received it. You cannot claim you never got it.

In information security, non-repudiation is achieved through:

- **Digital signatures** — a user signs a document with their private key, proving they authored or approved it (covered in Section 1.4)
- **Audit logs** — timestamped, tamper-evident records of who did what and when
- **PKI certificates** — binding an identity to a key pair

**Real-world importance:** An employee emails a signed contract to a vendor. The digital signature proves the email came from that employee's private key. The employee cannot later claim they never sent the contract.

---

### Authentication, Authorization, and Accounting (AAA)

The AAA framework governs how access to systems and resources is managed.

![](../src/AAA.jpg.webp)
#### Authentication — Proving Who You Are

Authentication is the process of verifying that an entity is who or what it claims to be.

**Authentication factors:**

| Factor Type | Description | Example |
|---|---|---|
| Something you know | A secret only you should know | Password, PIN, security question answer |
| Something you have | A physical or logical token | Smart card, hardware token (YubiKey), OTP app |
| Something you are | A biometric characteristic | Fingerprint, iris scan, facial recognition |
| Somewhere you are | Location-based constraint | GPS geofencing, IP-based access rules |
| Something you do | Behavioral pattern | Typing rhythm, gait analysis |

Multi-factor authentication (MFA) requires two or more of these factors. Using *two passwords* is not MFA — they are both "something you know" and thus the same factor type.

##### Authenticating People

People are authenticated using combinations of the above factors. The choice of factor depends on the threat model:

- A VPN login for a remote employee might require a password (something you know) + a TOTP code from an authenticator app (something you have).
- A biometric door lock at a high-security facility might require a fingerprint (something you are) + a PIN (something you know).

##### Authenticating Systems

Systems (servers, devices, applications) must also authenticate to each other. This is called *machine authentication* or *system authentication*.

**Methods:**
- **API keys** — a shared secret embedded in service-to-service API calls
- **Client certificates** — a PKI certificate installed on a device or server, proving its identity during a TLS handshake
- **Pre-shared keys (PSK)** — used in IPsec VPNs and Wi-Fi (WPA2-PSK)
- **SSH public key authentication** — the server verifies the client holds the private key matching an authorized public key

```bash
# Generate an SSH key pair for machine authentication
ssh-keygen -t ed25519 -C "webserver-prod-01" -f /etc/ssh/id_ed25519_webserver

# Copy the public key to an authorized_keys file on the target server
ssh-copy-id -i /etc/ssh/id_ed25519_webserver.pub user@target-server

# The machine now authenticates using its private key, no password needed
ssh -i /etc/ssh/id_ed25519_webserver user@target-server
```

#### Authorization — What You Are Allowed to Do

Authorization determines what an authenticated entity is permitted to do. Authentication answers "Who are you?" Authorization answers "What can you do?"

**Common authorization models:**

| Model | Description | Example |
|---|---|---|
| Discretionary Access Control (DAC) | Resource owner sets permissions | File owner grants read/write to specific users |
| Mandatory Access Control (MAC) | System enforces permissions based on labels | Top Secret clearance required for Top Secret files |
| Role-Based Access Control (RBAC) | Permissions assigned to roles, users assigned to roles | "Finance" role can access payroll DB; "HR" role cannot |
| Attribute-Based Access Control (ABAC) | Access decisions based on attributes of user, resource, and environment | Access allowed if: user.department = "Legal" AND resource.sensitivity = "Low" AND time = "BusinessHours" |
| Rule-Based Access Control | Access controlled by predefined rules (often in firewalls) | Firewall rule: allow TCP/443 from 10.0.0.0/8, deny all else |

> **Instructor note:** RBAC and ABAC are frequently confused. RBAC grants access based on *what role the user has*; ABAC grants access based on *contextual attributes* which can include the role, environment, device posture, time of day, and more. ABAC is more flexible and is the model underlying many Zero Trust implementations.

#### Accounting — Recording What Was Done

Accounting (also called *auditing*) is the recording of what an entity did, when, and from where. Without accounting, you cannot detect unauthorized access, investigate incidents, or prove compliance.

**Components of accounting:**
- **Audit logs** — records of login attempts, file access, configuration changes
- **SIEM systems** — aggregate and correlate logs from multiple sources
- **Non-repudiation evidence** — logs tied to cryptographic proof of identity

**A complete accounting entry should capture:**
- *Who* performed the action (authenticated identity)
- *What* action was taken (read, write, delete, login, logout)
- *When* (timestamp, preferably synchronized via NTP)
- *Where* (source IP, device, physical location)
- *Outcome* (success or failure)

---

### Gap Analysis

A gap analysis compares an organization's *current* security state to a *desired* or *required* state (such as a compliance framework like NIST CSF, ISO 27001, or PCI-DSS).

**The process:**
1. Define the target state (what controls *should* be in place)
2. Assess the current state (what controls *are* in place)
3. Identify the gaps (what is missing, insufficient, or incorrectly implemented)
4. Prioritize remediation based on risk

**Real-world example:** A healthcare organization performing a HIPAA audit discovers that while it has encryption on laptops (good), it has no formal policy for encrypting email containing PHI, and its audit log retention is 30 days instead of the required 6 years. These are the gaps — the analysis produces a remediation roadmap.

---

### Zero Trust

Zero Trust is a security framework and philosophy built on the principle: **"Never trust, always verify."**

Traditional perimeter-based security assumed that everything inside the corporate network was trusted and everything outside was untrusted. Zero Trust eliminates this assumption. Every user, every device, and every network connection is treated as potentially hostile — regardless of physical or network location.

**Core Zero Trust tenets:**
1. Verify explicitly — always authenticate and authorize based on all available data points (identity, location, device health, service, data classification)
2. Use least privilege access — limit user access with just-in-time and just-enough-access
3. Assume breach — minimize blast radius, segment access, verify end-to-end encryption

[IMAGE PLACEHOLDER: Zero Trust architecture diagram showing Control Plane (Policy Engine, Policy Administrator) and Data Plane (subjects, Policy Enforcement Points, resources) with arrows showing policy flow]

#### The Control Plane

The control plane contains the decision-making components of a Zero Trust architecture. It does not handle actual data traffic — it issues access decisions.

**Adaptive Identity**

Adaptive identity means that the identity of a user or device is not treated as binary (authenticated or not). Instead, trust is continuously evaluated based on context:

- Is the user logging in from their usual location, or from a new country?
- Is the device compliant with corporate security policy (patched, running EDR)?
- Is the request occurring at an unusual time?
- Has this account recently failed multiple authentication attempts?

When risk signals are detected, the system adapts: it might require step-up authentication, limit what the user can do, or deny access entirely.

**Threat Scope Reduction**

Threat scope reduction means minimizing the attack surface and the blast radius of a potential compromise. Strategies include:

- Microsegmentation — dividing the network into small segments so that a compromise in one does not automatically grant access to others
- Least privilege access — users and systems have only the access they need for the task at hand
- Just-in-time (JIT) access — privilege is granted only when needed and automatically revoked after a time limit

**Policy-Driven Access Control**

All access decisions are driven by explicitly defined policies, not by network location. The policy engine evaluates each access request against current policies and context.

**Policy Administrator**

The Policy Administrator is the component that communicates access decisions to the enforcement points. It acts as the bridge between the decision (Policy Engine) and enforcement (Policy Enforcement Point). When the Policy Engine decides to allow or deny access, the Policy Administrator signals the appropriate Policy Enforcement Point.

**Policy Engine**

The Policy Engine is the core decision-maker in Zero Trust. It evaluates:
- User identity and authentication strength
- Device compliance status
- The sensitivity of the resource being requested
- Environmental context (time, location, network)
- Threat intelligence feeds

It then grants, denies, or revokes access according to policy.

#### The Data Plane

The data plane is where actual user-to-resource communication occurs. The data plane does not make decisions — it enforces them.

**Implicit Trust Zones**

Traditional networks had explicit trust zones (inside = trusted, outside = untrusted). Zero Trust replaces these with *context-based* trust. There are no permanently trusted zones — every request is evaluated individually. The concept of "implicit trust zones" acknowledges that some degree of segmentation still exists in real implementations (e.g., a microsegment hosting database servers), but trust within that zone is never assumed — it must be verified for each session.

**Subject/System**

The subject is the entity requesting access — a human user, a service account, or an automated system. The system refers to devices or applications acting on behalf of subjects. In Zero Trust, both subjects and systems must authenticate and be evaluated.

**Policy Enforcement Point (PEP)**

The Policy Enforcement Point is the gatekeeper that sits between the subject and the resource. It receives access decisions from the Policy Administrator and enforces them. A PEP can be:
- A next-generation firewall
- An API gateway
- A reverse proxy
- An identity-aware proxy (e.g., Google BeyondCorp)
- An endpoint agent

---

### Physical Security

Physical security is the first line of defense. If an attacker gains physical access to hardware, most technical controls can be bypassed.

[IMAGE PLACEHOLDER: Physical security layers diagram — outer perimeter (fence, bollards) → building entry (vestibule, guard) → interior (badge readers, cameras) → server room (biometric lock, sensors)]

#### Bollards

Bollards are short, sturdy vertical posts installed in front of buildings or critical infrastructure to prevent vehicle-borne attacks (ramming). They are a preventive physical control against vehicle-as-weapon threats.

**Example:** Bollards are standard in front of government buildings, data centers, and public gathering spaces to prevent a vehicle from driving through the façade.

#### Access Control Vestibule

An access control vestibule (also called a mantrap) is a small room with two sets of interlocking doors. A person must pass through the outer door and authenticate before the inner door unlocks. This prevents *tailgating* — unauthorized individuals following an authorized person through a secure door.

**Example:** Many data centers use a vestibule at the main entrance: you badge into the outer door, wait while the outer door closes and your credentials are verified, then the inner door unlocks.

#### Fencing

Fencing establishes a physical perimeter. It is a deterrent (visible barrier), a preventive control (physical obstacle), and it forces entry through controlled access points.

Different fence heights convey different security levels:
- 3–4 feet: defines boundary, deters casual entry
- 6–7 feet: difficult to climb casually
- 8+ feet with barbed wire or anti-climb toppings: serious barrier against determined intruders

#### Video Surveillance

Video surveillance (CCTV) serves multiple control types simultaneously:
- **Deterrent** — visible cameras discourage attacks
- **Detective** — cameras record incidents for later review
- **Forensic evidence** — recordings are used in investigations and prosecutions

Modern systems include analytics capabilities: motion detection, facial recognition, license plate reading, and behavioral anomaly detection.

#### Security Guard

Security guards provide a human, adaptive presence that no automated system can fully replicate. They can:
- Verify identities
- Observe contextual behavior and respond
- Escort authorized visitors
- Respond immediately to incidents

Guards are an operational control and can be preventive, deterrent, detective, and corrective simultaneously — the most versatile control type.

#### Access Badge

Access badges (smart cards, proximity cards, RFID badges) combine identification and access control. They:
- Identify the holder (printed photo)
- Authenticate the holder to electronic lock systems
- Generate audit logs of entry/exit events

**Best practice:** Badges should require a PIN or biometric to activate, so a lost or stolen badge cannot be used without the second factor.

#### Lighting

Adequate lighting reduces concealment opportunities for intruders and improves video surveillance image quality. It is both a deterrent (no cover of darkness) and a detective control enhancement (better camera footage).

**Parking lots, building perimeters, and loading docks** are the highest-priority areas for security lighting.

#### Sensors

Sensors detect physical intrusion or presence. They are primarily detective controls, often feeding into alarm systems or access control systems.

**Infrared (IR) Sensors**

Passive infrared (PIR) sensors detect changes in infrared radiation — the heat emitted by a human body moving through the sensor's field of view. Common in alarm systems and automatic lighting.

**Limitation:** Can be fooled by slow movement or thermal shielding. Not suitable as a sole detection method in high-security environments.

**Pressure Sensors**

Pressure sensors detect weight applied to a surface — typically a floor mat or pad. When someone steps on the sensor, an alarm triggers. Used under server room floors, in exhibit cases, or beneath safes.

**Microwave Sensors**

Microwave sensors emit microwave pulses and detect changes in the reflected signal caused by movement. They cover larger areas than IR sensors and can detect through walls. Used in high-security perimeter detection.

**Limitation:** Can generate false positives from vibration, HVAC systems, or small animals.

**Ultrasonic Sensors**

Ultrasonic sensors emit high-frequency sound waves and measure the time for reflections to return. Movement in the field changes the return time, triggering an alert. Used in interior spaces, vehicle detection, and some access control applications.

---

### Deception and Disruption Technology

Deception technology deliberately presents false targets to attackers. The goal is to detect intrusion attempts, study attacker behavior, and waste attacker time and resources on fake assets.

> **Instructor note:** Deception technology is one of the most intellectually interesting areas of security because it flips the dynamic — instead of just defending, the defender creates a trap and watches the attacker spring it.

#### Honeypot

A honeypot is a system intentionally designed to look like a legitimate, valuable target but which has no real production value. Any interaction with a honeypot is inherently suspicious.

**Purpose:**
- Detect intrusions that bypass perimeter defenses
- Study attacker tools, techniques, and procedures (TTPs)
- Slow down attackers who invest effort in a fake target

**Example:** A financial services company sets up a fake "admin portal" server on an internal VLAN. The server is not part of any real workflow. When an attacker who has compromised the network scans for admin portals and connects to it, the SOC receives an immediate high-confidence alert — any connection to a honeypot is unauthorized by definition.

> **Instructor note:** Students often ask "Is running a honeypot legal?" The answer is nuanced. Operating a honeypot on your own network is generally legal. However, allowing an attacker to *continue* attacking from it (to gather intelligence) and then using that data in court involves legal and ethical questions about entrapment and evidence handling. These are important advanced topics.

#### Honeynet

A honeynet is a network of interconnected honeypot systems designed to simulate an entire environment — multiple servers, network devices, even simulated user activity. It is more convincing than a single honeypot and allows researchers to observe lateral movement.

**Example:** A cybersecurity research organization operates a honeynet that simulates an industrial control system network complete with fake PLCs, HMIs, and historian servers. When nation-state actors probe the internet for ICS systems, they find and interact with the honeynet instead of a real facility. The researchers observe the TTPs and publish threat intelligence.

#### Honeyfile

A honeyfile is a fake file planted in a location where an attacker who has gained access might look. The file has a compelling name (e.g., `passwords_2024.xlsx`, `CEO_compensation.docx`) but contains no real sensitive data. Accessing the honeyfile triggers an alert.

**Example:** A security team places a file named `customer_database_backup.zip` in the documents folder of a shared drive. A canary token embedded in the file phones home if it is opened. If an alert fires, the team knows an attacker (or malicious insider) has accessed that folder.

#### Honeytoken

A honeytoken is a credential, token, or piece of data that has no legitimate use case — it exists purely as a trap. If the honeytoken is ever used, it signals compromise.

**Examples:**
- A fake AWS access key pair published nowhere legitimate — if it appears in API calls, credentials were stolen
- A fake domain admin account that is never used by IT — if it logs in, an attacker has obtained and is using credentials
- A fake API token embedded in a configuration file in source code — if it makes API calls, a developer has accidentally exposed credentials or a threat actor has exfiltrated the repo

```python
# Example: Simple honeytoken detection concept
# In a real implementation, the canary token service
# would send an alert to your SOC when this URL is fetched

import hashlib

# Generate a unique honeytoken
secret = "prod-db-backup-archive-2024"
token = hashlib.sha256(secret.encode()).hexdigest()[:16]
print(f"Honeytoken: {token}")
# Embed this token in a fake document or config file
# If it ever appears in logs, API calls, or is used for auth — it's a breach indicator
```

---

## Section 1.3 — The Importance of Change Management Processes and the Impact to Security

### Why Change Management Matters for Security

A significant percentage of security incidents are caused not by sophisticated attacks, but by **poorly managed changes** to IT systems. A misconfigured firewall rule, a dependency broken by a software update, or a patch applied without testing can introduce vulnerabilities or cause outages.

Change management is the formal process by which changes to IT systems are proposed, reviewed, approved, implemented, tested, and documented. It directly protects the CIA triad:

- A firewall rule change that opens an unintended port threatens **Confidentiality** and **Integrity**
- A failed update that crashes a critical service threatens **Availability**
- An undocumented change that modifies access controls threatens **Accountability**

> **Instructor note:** Ask students to recall a real incident where a change caused a security breach or outage. Examples: the 2021 Facebook outage (BGP config change), the 2012 Knight Capital trading loss ($440M in 45 minutes due to a software deployment error). These make the abstract concrete.

---

### Business Processes Impacting Security Operations

#### Approval Process

No change should be implemented without formal approval. The approval process ensures that a qualified decision-maker has reviewed the change's scope, risk, and impact before it is applied.

**Typical approval levels:**
- Minor/standard changes (low risk, well-understood) — pre-approved or fast-tracked
- Significant changes — reviewed by a Change Advisory Board (CAB)
- Emergency changes — expedited approval with post-implementation review

**Security impact:** Without an approval process, a system administrator could make unauthorized changes — intentionally (insider threat) or accidentally — with no oversight.

#### Ownership

Every change must have a named *owner* — an individual who is accountable for the change's success. Ownership eliminates the diffusion of responsibility that leads to errors going unaddressed.

**Example:** A developer submits a change to open a new port on a web application firewall. The change owner is the developer's team lead, who is accountable if the change creates a vulnerability.

#### Stakeholders

Stakeholders are all parties who have an interest in the outcome of the change. A firewall rule change may have stakeholders from:
- Networking (who owns the firewall)
- Security (who must review the rule)
- The application team (who needs the port open)
- Compliance (who must verify the rule does not violate policy)

Identifying stakeholders early prevents the "silent dependency" problem — a change that seems straightforward until someone discovers it breaks something they depend on.

#### Impact Analysis

Before a change is approved, its potential impact must be assessed:
- What systems does this change affect directly?
- What systems depend on the affected systems?
- What is the worst-case impact if the change fails?
- What is the risk if the change introduces a vulnerability?

**Security-specific impact analysis questions:**
- Does this change modify firewall rules, ACLs, or authentication settings?
- Does this change introduce new software with unknown dependencies?
- Does this change modify cryptographic settings or certificate configurations?

#### Test Results

Changes should be tested in a non-production environment before deployment. Test results document that the change was validated and functioned as expected.

**Security implications of skipping testing:**
- An untested patch may break authentication, leaving users locked out or — worse — disabling authentication entirely
- An untested firewall rule may inadvertently expose a service to the public internet

#### Backout Plan

A backout plan (rollback plan) is the predefined set of steps to revert a change if it causes problems. No change should be approved without a documented backout plan.

**Example backout plan for a database patch:**
1. Stop the application servers connected to the database
2. Restore the database from the pre-patch snapshot taken at T-30 minutes
3. Verify database integrity and application connectivity
4. Notify stakeholders of the rollback
5. Schedule a post-incident review

> **Instructor note:** Students sometimes think "we can always roll back" is a strategy. Emphasize that rollback must be *documented and tested* before the change — not improvised during a crisis at 2:00 AM.

#### Maintenance Window

A maintenance window is a scheduled period of time during which changes can be made to systems — typically during low-usage hours to minimize user impact.

**Security relevance:** Emergency changes outside of maintenance windows are a red flag. If someone is modifying firewall rules or user accounts outside an approved window, it may indicate unauthorized activity. Deviations should generate alerts and require post-hoc documentation.

#### Standard Operating Procedure (SOP)

An SOP is a documented, step-by-step procedure for carrying out a common or repetitive task. SOPs ensure that tasks are performed consistently regardless of who executes them.

**Security benefit:** An SOP for provisioning new user accounts ensures that the process always includes assigning the correct minimum permissions, logging the account creation, and notifying the user's manager — not just whatever the admin feels like doing today.

---

### Technical Implications of Change Management

#### Allow Lists and Deny Lists

Allow lists (formerly whitelists) and deny lists (formerly blacklists) control what is permitted or prohibited in a system. Changes to these lists have immediate security implications.

- Adding an IP to an **allow list** opens access — potentially to an attacker using that IP
- Removing an IP from a **deny list** may re-enable a blocked threat
- Changes to application allow lists (e.g., allowed software to execute) can enable malware if a malicious executable is added

**These changes require explicit approval and must be version controlled.**

#### Restricted Activities

Some changes are flagged as restricted and require elevated approval or specialized review. Examples:
- Disabling MFA or modifying authentication settings
- Modifying firewall rules that expose services to the internet
- Granting domain admin or root-level access
- Modifying audit logging settings (an attacker may try to disable logging to hide their tracks)

#### Downtime

Many changes require system downtime. Unplanned downtime is an availability failure. Planned downtime must be:
- Communicated to stakeholders in advance
- Scheduled during approved maintenance windows
- Minimized to the scope necessary

**Security impact:** Extended or unexpected downtime can be the result of a failed change *or* an attack disguised as a maintenance activity. Distinguishing between them requires good logging and change tracking.

#### Service Restart and Application Restart

After a change, services or applications may need to be restarted. This can be disruptive and must be planned.

**Security consideration:** Some configuration changes — particularly to security software like firewalls, IDS agents, or endpoint protection — do not take effect until a restart. Applying a patch and not restarting leaves the vulnerability temporarily open and the patch unapplied in memory.

#### Legacy Applications

Legacy applications present special challenges in change management:

- They may not support modern authentication, encryption, or patching mechanisms
- Their documentation may be incomplete or lost
- They may depend on deprecated OS versions or unsupported libraries
- Their vendors may no longer exist

**Example:** A hospital runs a legacy radiology application that requires an unencrypted database connection and runs only on Windows Server 2008. Patching it is not possible without breaking functionality. This requires a compensating control strategy (network isolation, strict monitoring) and a formal risk acceptance, documented through the change management process.

#### Dependencies

Modern systems have complex dependency chains. A change to one component can break another that depends on it.

**Example:** A security team updates the TLS library on an application server to remove support for TLS 1.0. Unknown to the team, a critical third-party payment processor still uses TLS 1.0. After the update, payment processing fails. A dependency analysis before the change would have identified this.

**Best practice:** Maintain a Configuration Management Database (CMDB) that maps systems and their dependencies. Use it during impact analysis before every significant change.

---

### Documentation

#### Updating Diagrams

Network and architecture diagrams must be kept current. An outdated diagram can lead to:
- Security teams not knowing a system exists (shadow IT)
- Incident responders misunderstanding the blast radius of a compromise
- Firewall rules that reference systems that no longer exist

After every change that modifies network topology, system placement, or data flows, the corresponding diagrams must be updated.

#### Updating Policies and Procedures

Changes to systems often require updates to the policies and procedures that govern them. Examples:
- A new authentication system requires updates to the Acceptable Use Policy
- A new cloud storage service requires a new Data Classification and Handling Policy
- A migrated application requires an updated disaster recovery runbook

---

### Version Control

Version control systems (like Git) track changes to code, configuration files, scripts, and documentation over time.

**Security benefits of version control:**
- **Auditability** — every change is recorded with who made it, when, and why
- **Rollback** — you can revert to any previous state
- **Diff analysis** — you can see exactly what changed between versions
- **Access control** — you can restrict who can commit to production branches

```bash
# Initialize a repository for firewall configuration files
git init /etc/firewall-configs

# Stage and commit a change to a firewall rule file
git add rules.conf
git commit -m "Add allow rule for payment processor IP 203.0.113.45 - CAB-2024-0412"

# View the change history
git log --oneline

# See what changed in the last commit
git diff HEAD~1 HEAD rules.conf
```

> **Instructor note:** Emphasize that the commit message in the example references a Change Advisory Board (CAB) ticket number. This is best practice — every committed change to a configuration file should be traceable to an approved change request.

---

## Section 1.4 — The Importance of Appropriate Cryptographic Solutions

### Why Cryptography Matters

Cryptography is the mathematical foundation of nearly every security mechanism in use today. Without it, there is no confidentiality in transit, no integrity verification, no authenticated identity, and no non-repudiation. It is the technology that makes the modern internet function securely.

> **Instructor note:** Before diving into cryptography, calibrate the class. Students who have never seen modular arithmetic or prime numbers may struggle with the mathematical intuition. Reassure them: the exam tests *conceptual understanding*, not the ability to implement RSA from scratch.

---

### Public Key Infrastructure (PKI)

PKI is the framework of hardware, software, policies, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates and manage public-key encryption.

[IMAGE PLACEHOLDER: PKI certificate chain diagram — Root CA → Intermediate CA → End-entity certificate, showing the chain of trust]

#### Public Key

A public key is one half of an asymmetric key pair. It is designed to be shared freely. Anyone can encrypt data *to* you using your public key, and only your private key can decrypt it. Your public key is embedded in your digital certificate and distributed to others.

#### Private Key

A private key is the other half of the asymmetric key pair. It must be kept absolutely secret — possession of the private key *is* possession of the identity. Loss or compromise of a private key requires immediate revocation of the corresponding certificate and generation of a new key pair.

**Analogy:** Your public key is like your email address — share it freely so people can send you messages. Your private key is like the password to that email account — never share it.

#### Key Escrow

Key escrow is the practice of storing a copy of a cryptographic key with a trusted third party. This allows for key recovery if the primary holder loses access.

**Controversy:** Law enforcement agencies (FBI, NSA) have advocated for mandatory key escrow so that they can decrypt communications during investigations. The security community largely opposes mandatory escrow because:
- The escrow system itself becomes a high-value target
- There is no way to guarantee the escrow is only accessed lawfully
- Weakening encryption weakens it for everyone, including against malicious actors

---

### Encryption

Encryption is the process of transforming readable data (plaintext) into an unreadable format (ciphertext) using an algorithm and a key. Only authorized parties with the correct key can reverse the process (decryption).

#### Encryption Levels

Encryption can be applied at different granularities depending on the threat model and performance requirements.

| Level | Description | Example |
|---|---|---|
| Full-disk encryption (FDE) | Encrypts the entire storage device | BitLocker (Windows), FileVault (macOS) |
| Partition encryption | Encrypts specific partitions | LUKS on Linux |
| Volume encryption | Encrypts logical volumes | VeraCrypt volumes |
| File encryption | Encrypts individual files | GnuPG (GPG), EFS on Windows |
| Database encryption | Encrypts the entire database | Transparent Data Encryption (TDE) in SQL Server |
| Record encryption | Encrypts individual fields/records | Encrypting only SSN and credit card number columns |

```bash
# Encrypt a file using GPG (symmetric)
gpg --symmetric --cipher-algo AES256 sensitive_report.pdf
# Prompts for a passphrase; produces sensitive_report.pdf.gpg

# Decrypt the file
gpg --decrypt sensitive_report.pdf.gpg > sensitive_report.pdf
```

```bash
# Check if a disk is encrypted with BitLocker (Windows - run in cmd/PowerShell)
manage-bde -status C:
```

**Record-level encryption** is the most granular and most expensive option. It is used when you need to protect specific fields (e.g., SSNs, payment card numbers) while leaving other fields available for queries and processing.

#### Transport/Communication Encryption

Transport encryption protects data *in motion* — while it travels across a network. The most common protocol is **TLS (Transport Layer Security)**, which secures HTTPS, SMTPS, IMAPS, and many other protocols.

```bash
# Examine the TLS certificate presented by a server
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null \
  | openssl x509 -noout -text | grep -E "Subject:|Issuer:|Not After"
```

> **Instructor note:** Distinguish between *encryption in transit* (TLS) and *encryption at rest* (FDE/file encryption). Data can be encrypted in transit and stored unencrypted at rest, or vice versa. Good security requires both.

#### Asymmetric Encryption

Asymmetric encryption uses a key pair — a public key and a private key. What one key encrypts, only the other can decrypt.

**Use cases:**
- **Secure key exchange** — Alice encrypts a symmetric session key with Bob's public key; only Bob's private key can decrypt it
- **Digital signatures** — Alice signs a document with her private key; anyone with her public key can verify the signature
- **Certificate-based authentication** — a server proves its identity by demonstrating possession of the private key corresponding to the certificate

**Common asymmetric algorithms:**
- **RSA** — widely used; key lengths of 2048 or 4096 bits recommended
- **ECC (Elliptic Curve Cryptography)** — provides equivalent security to RSA at much shorter key lengths; preferred for mobile and IoT
- **Diffie-Hellman (DH) / ECDH** — key exchange algorithm (does not encrypt data directly)

**Limitation:** Asymmetric encryption is computationally expensive. It is not used to encrypt bulk data — it is used to securely exchange symmetric keys, which then do the bulk encryption.

#### Symmetric Encryption

Symmetric encryption uses the *same key* for both encryption and decryption. It is fast and suitable for encrypting large amounts of data.

**Common symmetric algorithms:**

| Algorithm | Key Size | Notes |
|---|---|---|
| AES-128 | 128-bit | Strong; widely used in consumer devices |
| AES-256 | 256-bit | Recommended for sensitive/government data |
| 3DES | 112-bit effective | Legacy; avoid in new systems |
| ChaCha20 | 256-bit | Modern; used in TLS 1.3 and WireGuard |

```python
# Symmetric encryption example using Python's cryptography library
from cryptography.fernet import Fernet

# Generate a symmetric key
key = Fernet.generate_key()
print(f"Key: {key.decode()}")  # This key must be kept secret

# Create a Fernet cipher (uses AES-128-CBC under the hood)
cipher = Fernet(key)

# Encrypt plaintext
plaintext = b"Sensitive HR data: salary=85000"
ciphertext = cipher.encrypt(plaintext)
print(f"Ciphertext: {ciphertext}")

# Decrypt ciphertext (same key required)
decrypted = cipher.decrypt(ciphertext)
print(f"Decrypted: {decrypted.decode()}")
```

**The key distribution problem:** Symmetric encryption requires both parties to have the same key. How do you share that key securely over an insecure channel? This is where **key exchange** comes in.

#### Key Exchange

Key exchange protocols allow two parties to derive a shared secret over an insecure channel without ever transmitting the secret itself.

**Diffie-Hellman (DH):** The foundational key exchange protocol. Two parties each generate a public/private DH key pair. They exchange public keys over an insecure channel. Each party can then independently compute the same shared secret using their private key and the other party's public key — but an eavesdropper who sees only the public keys cannot compute the secret.

**ECDH (Elliptic Curve DH):** The same concept using elliptic curve mathematics. More efficient than classical DH for the same security level.

**Perfect Forward Secrecy (PFS):** Modern implementations generate a fresh DH key pair for each session (ephemeral keys). Even if the server's long-term private key is later compromised, past sessions cannot be decrypted. TLS 1.3 mandates PFS.

#### Cryptographic Algorithms

| Algorithm | Type | Purpose | Status |
|---|---|---|---|
| AES | Symmetric | Bulk encryption | Current standard |
| RSA | Asymmetric | Key exchange, digital signatures | Use 2048+ bit keys |
| ECC / ECDSA | Asymmetric | Digital signatures, key exchange | Preferred for modern systems |
| SHA-256 / SHA-3 | Hash | Integrity verification | Current standard |
| MD5 | Hash | Integrity verification | Broken — avoid |
| SHA-1 | Hash | Integrity verification | Deprecated — avoid |
| HMAC | MAC | Message authentication with symmetric key | Current standard |
| DH / ECDH | Key exchange | Deriving shared secrets | Use ECDH for new systems |

#### Key Length

Key length directly affects the security of an encrypted system. Longer keys provide more security but require more computation. The "right" key length is determined by how long the data needs to remain protected and the computational power available to attackers.

**Current NIST recommendations:**
- Symmetric encryption: 128-bit minimum; 256-bit for high-security
- RSA: 2048-bit minimum; 3072 or 4096 for new systems
- ECC: 256-bit minimum (equivalent to RSA-3072)
- Hash functions: SHA-256 minimum

> **Instructor note:** Explain that "breaking" AES-256 by brute force would require more energy than the sun produces in its lifetime with current computing technology. The real threats are implementation flaws, weak key generation, and key management failures — not the algorithm itself.

---

### Cryptographic Tools

#### Trusted Platform Module (TPM)

A TPM is a secure cryptoprocessor chip embedded in a computer's motherboard (or implemented in firmware). It provides:
- Hardware-based secure key generation and storage
- Platform integrity measurement (measuring boot components and storing them in Platform Configuration Registers)
- Remote attestation (proving to a remote server that the device has not been tampered with)
- Support for full-disk encryption (BitLocker uses TPM to seal the volume encryption key)

**Practical significance:** Without a TPM, BitLocker requires a PIN or USB key at every boot. With a TPM, BitLocker can unseal the key automatically — but only if the boot process measurements match the expected values. If someone tampers with the bootloader, the measurements change, and the TPM refuses to release the key.

#### Hardware Security Module (HSM)

An HSM is a dedicated hardware device (or cloud service) that performs cryptographic operations and stores cryptographic keys in a tamper-resistant environment.

**Key properties:**
- Keys never leave the HSM in plaintext
- Tampering with the device causes it to zeroize (erase) its keys
- Used by Certificate Authorities, banks, payment processors, and any organization that needs to protect high-value keys

**Examples:** Thales Luna HSM, AWS CloudHSM, YubiHSM.

**Difference from TPM:** A TPM is embedded in a single device for that device's use. An HSM is a standalone device (or service) that can serve many applications and typically handles higher volumes of cryptographic operations.

#### Key Management System (KMS)

A Key Management System is software (or a cloud service) that manages the full lifecycle of cryptographic keys:
- Generation
- Distribution
- Storage
- Rotation (generating new keys and re-encrypting data)
- Revocation and deletion

**Examples:** HashiCorp Vault, AWS KMS, Azure Key Vault, Google Cloud KMS.

**Why key management matters:** The strongest encryption is worthless if the keys are stored in a plaintext configuration file next to the data they encrypt. KMS solves this by providing secure, access-controlled key storage and centralized rotation.

#### Secure Enclave

A secure enclave is an isolated, hardware-enforced memory region within a processor that protects code and data from the rest of the system — including from the operating system and hypervisor.

**Examples:**
- Apple Secure Enclave (used in iPhones to protect biometric data and encryption keys)
- Intel Software Guard Extensions (SGX)
- AMD Secure Encrypted Virtualization (SEV)

**Use case:** A mobile banking app stores the user's biometric templates in the secure enclave. Even if the operating system is compromised by malware, the biometric data and keys inside the enclave cannot be accessed.

---

### Obfuscation

Obfuscation techniques conceal sensitive data without necessarily encrypting it. They are typically used to protect data while preserving its format or usability.

#### Steganography

Steganography is the practice of hiding secret data *within* non-secret data. Unlike encryption (which hides the *content*), steganography hides the *existence* of the message.

**Example:** A message can be hidden in a JPEG image by altering the least significant bit (LSB) of pixel color values. The visual difference is imperceptible, but the hidden bits form a readable message to someone who knows where to look.

**Security use case:** Watermarking documents with invisible identifiers to detect leaks — if the document is found outside the organization, the watermark identifies the source of the leak.

```python
# Conceptual illustration of LSB steganography
# (Not a complete implementation — illustrative only)

# A pixel's red channel value: 200 = binary 11001000
# We can change the last bit (LSB) without visible change:
# 11001000 (200) → 11001001 (201) — stores a "1" bit
# 11001000 (200) → 11001000 (200) — stores a "0" bit

def embed_bit(pixel_value, bit):
    """Embed a single bit in the LSB of a pixel value."""
    return (pixel_value & 0xFE) | bit  # Clear LSB then set to our bit

print(embed_bit(200, 1))  # Output: 201
print(embed_bit(200, 0))  # Output: 200
```

#### Tokenization

Tokenization replaces sensitive data with a non-sensitive placeholder (a token). The mapping between the token and the original data is stored in a secure *token vault*. The token itself has no mathematical relationship to the original data — it cannot be reversed without access to the vault.

**Example:** A payment system stores a credit card number `4111-1111-1111-1111` in its database as the token `tok_a8b9c2d3`. The actual card number is stored only in the token vault (often operated by a PCI-DSS-compliant third party). If the database is breached, the attacker gets tokens, not card numbers.

**Difference from encryption:** Encrypted data can be decrypted with the key. Tokenized data can only be "decrypted" by querying the vault — there is no algorithm that maps token → original value.

#### Data Masking

Data masking replaces real values with realistic-looking but fictitious data. It is commonly used for:
- Populating test and development environments with non-production data
- Displaying partially hidden data (e.g., `****-****-****-4242` for a credit card)

**Static data masking:** Creates a permanent masked copy of the dataset for use in non-production environments.

**Dynamic data masking:** Applies masking at query time, based on the user's role. A call center agent sees `****-****-1234` while a fraud analyst sees the full number.

---

### Hashing

Hashing is a one-way mathematical function that takes an input of any size and produces a fixed-size output (hash, digest, fingerprint). The same input always produces the same output; any change to the input — even a single bit — produces a completely different output.

**Properties of a cryptographic hash function:**
- **Deterministic** — same input → same hash every time
- **One-way** — cannot reverse the hash to get the input
- **Avalanche effect** — small input changes cause dramatic output changes
- **Collision resistant** — it should be computationally infeasible to find two different inputs that produce the same hash

**Use cases:**
- Verifying file integrity (download verification)
- Storing passwords (never store plaintext passwords — store their hashes)
- Digital signatures (sign the hash of a document, not the document itself)
- Blockchain transaction records

```bash
# Hash a file with SHA-256
sha256sum document.pdf

# Hash a string directly
echo -n "password123" | sha256sum
# Output: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f

# Note: this hash is well-known — never use "password123"
```

```python
import hashlib

# Hash a password with SHA-256 (for illustration only — use bcrypt/scrypt in production)
password = "password123"
digest = hashlib.sha256(password.encode()).hexdigest()
print(f"SHA-256 hash: {digest}")

# Hash a file
with open("document.pdf", "rb") as f:
    file_hash = hashlib.sha256(f.read()).hexdigest()
print(f"File hash: {file_hash}")
```

**Common hash algorithms:**

| Algorithm | Output Length | Status |
|---|---|---|
| MD5 | 128-bit (32 hex chars) | Broken — collision attacks feasible |
| SHA-1 | 160-bit (40 hex chars) | Deprecated — collision attacks feasible |
| SHA-256 | 256-bit (64 hex chars) | Current standard |
| SHA-3-256 | 256-bit | Modern alternative; different construction from SHA-2 |
| BLAKE3 | Variable | Very fast; used in modern applications |

---

### Salting

Salting solves a fundamental problem with hashing passwords: if two users have the same password, they produce the same hash. An attacker who obtains a hash database can precompute hashes for common passwords (*rainbow table attack*) and instantly look up matches.

A **salt** is a random value that is generated for each user and appended (or prepended) to the password before hashing. Because every user's salt is unique, even identical passwords produce different hashes.

```python
import hashlib
import os

# Generate a random salt for each user
salt = os.urandom(32)  # 32 bytes of cryptographically random data

password = "password123"
# Combine salt + password before hashing
salted_password = salt + password.encode()
password_hash = hashlib.sha256(salted_password).hexdigest()

print(f"Salt: {salt.hex()}")
print(f"Hash: {password_hash}")
# Store BOTH the salt and the hash in the database
# When the user logs in, retrieve their salt, apply it, hash the attempt, and compare
```

> **Instructor note:** Salting protects against precomputed attacks (rainbow tables) but does not protect against a targeted brute-force attack against a *specific* account. For password storage, always use purpose-built password hashing algorithms like **bcrypt**, **scrypt**, or **Argon2** — they are slow by design (which is what you want for password hashing) and include salting automatically.

---

### Digital Signatures

A digital signature is a cryptographic mechanism that provides **authentication**, **integrity**, and **non-repudiation** for digital messages or documents.

**How it works:**
1. The sender computes a hash of the message
2. The sender encrypts the hash with their **private key** (this produces the signature)
3. The sender transmits the message + signature
4. The recipient decrypts the signature with the sender's **public key**, recovering the hash
5. The recipient independently computes the hash of the message
6. If the two hashes match, the signature is valid: the message has not been modified, and it was signed by the holder of the private key

[IMAGE PLACEHOLDER: Digital signature process diagram — sender hashes message, encrypts hash with private key → transmits message + signature → receiver decrypts signature with public key, verifies hash match]

```bash
# Sign a file with GPG
gpg --detach-sign --armor document.pdf
# Produces document.pdf.asc (the signature file)

# Verify the signature
gpg --verify document.pdf.asc document.pdf
# Output: Good signature from "Alice Smith <alice@example.com>"
```

> **Instructor note:** A very common exam distractor: "Alice encrypts the document with her private key." Clarify: Alice does NOT encrypt the whole document with her private key (that would be slow and wasteful). She encrypts the *hash* of the document. The resulting signature proves she signed it, not that the content is confidential.

---

### Key Stretching

Key stretching takes a weak input (like a human-chosen password) and transforms it into a stronger, longer key through repeated hashing or other computational operations. The goal is to make brute-force attacks more expensive by making each guess take longer.

**How it works:** Instead of hashing a password once (which takes microseconds), key stretching applies the hash function thousands or millions of times. An attacker who wants to test a billion passwords must wait billions of hash iterations — instead of billions of microseconds, it might take years.

**Algorithms designed for key stretching:**
- **bcrypt** — intentionally slow; includes a cost factor you can increase over time
- **scrypt** — memory-hard; requires large amounts of RAM to compute, making GPU/ASIC attacks expensive
- **Argon2** — winner of the Password Hashing Competition; recommended for new systems
- **PBKDF2** — used in WPA2 Wi-Fi and many legacy systems

---

### Blockchain

A blockchain is a distributed, append-only ledger where records (blocks) are linked cryptographically. Each block contains:
- The data of the transactions in that block
- A cryptographic hash of the block's data
- The hash of the *previous* block (creating the chain)
- A timestamp and other metadata

Altering any block would change its hash, which would invalidate every subsequent block's reference to it — making tampering immediately detectable.

**Security properties:**
- **Integrity** — any modification to historical data is cryptographically detectable
- **Transparency** — on public blockchains, all transactions are visible to all participants
- **Decentralization** — no single point of control or failure

**Security applications beyond cryptocurrency:**
- Certificate transparency logs (public record of all issued TLS certificates — detects fraudulently issued certificates)
- Supply chain provenance tracking
- Immutable audit logs

#### Open Public Ledger

The open public ledger concept means that all transactions on a public blockchain are visible to any participant. This achieves transparency and enables independent verification — anyone can verify that a transaction occurred without trusting a central authority.

**Certificate Transparency (CT):** Browsers increasingly require that TLS certificates be logged to public CT logs (open public ledgers) before they are trusted. This prevents certificate authorities from secretly issuing fraudulent certificates for domains they don't control — any such certificate would appear in the public log and could be detected.

---

### Certificates

A digital certificate is a digitally signed document that binds a public key to an identity. It is the foundation of PKI.

[IMAGE PLACEHOLDER: X.509 certificate structure showing Subject, Issuer, Public Key, Validity Period, Extensions, and Signature fields]

#### Certificate Authorities (CAs)

A Certificate Authority is a trusted entity that issues and signs digital certificates. When a CA signs a certificate, it vouches for the binding between the public key and the identity in the certificate.

**CA hierarchy:**
- **Root CA** — the ultimate trust anchor; its certificate is self-signed; stored in OS and browser trust stores
- **Intermediate CA** — signed by the Root CA; issues end-entity certificates; the Root CA is kept offline to protect it
- **End-entity certificate** — issued to a specific server, user, or device; used in actual communication

#### Certificate Revocation Lists (CRLs)

A CRL is a signed list published by a CA containing the serial numbers of certificates it has revoked. Certificates may be revoked because:
- The private key was compromised
- The certificate holder's identity changed (name, organization)
- The certificate was issued in error

**Limitation:** CRLs can become large and are updated on a schedule — there is a window between revocation and the client downloading the updated CRL during which a revoked certificate may still be accepted.

#### Online Certificate Status Protocol (OCSP)

OCSP is a real-time protocol that allows a client to query a CA's OCSP responder to check whether a specific certificate is currently valid or revoked.

**Advantage over CRL:** Real-time response for a specific certificate, rather than downloading the entire revocation list.

**OCSP Stapling:** The server periodically fetches its own OCSP response and includes ("staples") it in the TLS handshake. This improves performance (no additional round trip to the OCSP responder) and privacy (the CA doesn't learn who is connecting to the server).

```bash
# Check the OCSP status of a certificate
openssl s_client -connect example.com:443 -status 2>/dev/null | grep -A 10 "OCSP Response"
```

#### Self-Signed Certificates

A self-signed certificate is signed by the same entity it identifies — there is no third-party CA vouching for it. Browsers will display a warning when encountering a self-signed certificate because there is no chain of trust.

**Appropriate uses:**
- Internal development and testing environments
- Internal services where all clients can be configured to trust the specific certificate manually

**Inappropriate uses:** Any public-facing service where users cannot be expected to manually trust the certificate.

#### Third-Party Certificates

Third-party certificates are issued by a trusted CA whose root certificate is already in the OS/browser trust store. End users will see no warnings, and the connection is trusted automatically.

**Examples:** DigiCert, Sectigo, Let's Encrypt (free and automated), GlobalSign.

#### Root of Trust

The root of trust is the foundation of the PKI trust chain — the Root CA whose certificate is self-signed and whose trustworthiness is assumed rather than proven cryptographically. Operating systems and browsers ship with a list of trusted Root CA certificates (the trust store). If a Root CA is compromised, every certificate it has ever signed becomes potentially untrustworthy.

#### Certificate Signing Request (CSR) Generation

Before a CA will issue a certificate, the requester generates a CSR — a formal request that includes:
- The public key to be certified
- The identity information (Common Name, Organization, etc.)
- The requested Subject Alternative Names (SANs — the domain names the certificate should cover)
- A digital signature by the corresponding private key (proving the requester holds the private key)

```bash
# Generate a private key and CSR for a web server
openssl req -newkey rsa:2048 -nodes -keyout server.key \
  -out server.csr \
  -subj "/C=US/ST=California/O=Example Corp/CN=www.example.com"

# View the contents of the CSR
openssl req -text -noout -in server.csr
```

The CSR is submitted to the CA. The CA verifies the requester's identity (domain validation, organization validation, or extended validation), then signs the certificate and returns it.

#### Wildcard Certificates

A wildcard certificate covers a domain and all of its immediate subdomains. The wildcard character `*` replaces the leftmost label.

**Example:** `*.example.com` covers:
- `www.example.com`
- `mail.example.com`
- `api.example.com`
- Any other single-level subdomain

**Does NOT cover:**
- `example.com` (the apex domain itself — requires SAN entry)
- `sub.api.example.com` (two levels deep)

**Security consideration:** If the private key for a wildcard certificate is compromised, *all* covered subdomains are at risk. Wildcard certificates require careful key management and should be rotated immediately upon any indication of compromise.

```bash
# Generate a CSR for a wildcard certificate
openssl req -newkey rsa:2048 -nodes -keyout wildcard.key \
  -out wildcard.csr \
  -subj "/C=US/O=Example Corp/CN=*.example.com"
```

---

## Key Takeaways

- Security controls have two dimensions: **category** (Technical, Managerial, Operational, Physical) and **type** (Preventive, Deterrent, Detective, Corrective, Compensating, Directive). Defense in depth uses multiple controls across both dimensions.
- The **CIA triad** (Confidentiality, Integrity, Availability) is the foundational model for evaluating security decisions. Every control protects one or more of these properties.
- **AAA** (Authentication, Authorization, Accounting) governs how access is granted and recorded. Authentication verifies identity; authorization determines permitted actions; accounting records what was done.
- **Zero Trust** eliminates implicit trust based on network location. The control plane (Policy Engine, Policy Administrator) makes access decisions; the data plane (Policy Enforcement Points) enforces them.
- Physical security is the first layer of defense. Layered physical controls — bollards, vestibules, fencing, surveillance, guards, sensors — protect against physical access attacks.
- **Deception technologies** (honeypots, honeynets, honeyfiles, honeytokens) detect intrusions and study attackers with high-fidelity alerts.
- **Change management** is a critical security process. Poorly managed changes are a leading cause of security incidents. Every change needs approval, an owner, impact analysis, testing, a backout plan, and documentation.
- **Cryptography** underpins confidentiality (encryption), integrity (hashing), authentication (digital signatures, PKI), and non-repudiation (digital signatures).
- **PKI** creates a chain of trust through CAs, certificates, and key pairs. Certificate management (issuance, revocation via CRL/OCSP, renewal) is as important as the cryptography itself.
- Use **purpose-built algorithms** for each task: AES-256 for symmetric encryption, RSA-2048+ or ECC-256+ for asymmetric, SHA-256 for hashing, bcrypt/Argon2 for password hashing.

---

## Review Questions

1. A company cannot patch a legacy application due to vendor constraints. They isolate it on a dedicated VLAN with strict monitoring. What type of security control is this isolation strategy, and what category does it belong to?

2. An organization's intrusion detection system generates an alert when a file named `admin_passwords.xlsx` is opened on a shared drive. The file contains no real data. What deception technology is this, and what control type does it represent?

3. Explain the difference between authentication and authorization. Give an example of a situation where a user is successfully authenticated but not authorized to perform an action.

4. A bank's website uses TLS 1.3. Explain the role of the Policy Enforcement Point in a Zero Trust architecture in the context of a customer accessing their online banking portal.

5. What is the difference between a compensating control and a corrective control? Provide a real-world example of each.

6. A systems administrator changes a firewall rule at 11:00 PM on a Saturday without submitting a change request. The next morning, a critical application is unreachable. What change management failures occurred, and what should have been in place?

7. Explain why MD5 is no longer acceptable as a cryptographic hash function for security purposes.

8. A user complains that they receive a browser warning when accessing the internal HR portal. The HR portal uses a self-signed certificate. Explain what the warning means and describe two alternative solutions.

9. How does salting protect against rainbow table attacks? Why is salting alone insufficient for password storage in high-security systems?

10. An organization is implementing Zero Trust architecture. Describe the role of the Policy Engine and how adaptive identity improves security compared to static authentication.

---

## Short Practical Lab Ideas

**Lab 1: Control Classification Exercise**
Present students with a list of 20 real-world security measures. Have students independently classify each by category and type, then compare and discuss disagreements. Example: "Security camera in server room" — is it Technical, Physical, or both? What types does it serve?

**Lab 2: Hashing and Integrity Verification**
Students download a known file and its published SHA-256 hash. They compute the hash themselves using `sha256sum` (Linux/macOS) or `certutil -hashfile` (Windows) and verify it matches. They then modify the file by one byte and observe that the hash changes completely.

**Lab 3: GPG Encryption and Signing**
Students generate a GPG key pair, export their public key to a classmate, encrypt a message with the classmate's public key, and verify that only the classmate can decrypt it. Then students sign a document and verify the signature. Lab reinforces the distinction between encryption (confidentiality) and signing (non-repudiation).

**Lab 4: TLS Certificate Inspection**
Using `openssl s_client`, students connect to several websites and inspect their certificates: Common Name, Subject Alternative Names, issuer chain, validity dates, key type, and revocation information. Students identify one with OCSP stapling and one without.

**Lab 5: Change Management Simulation**
Present students with a simulated change request form and a fictional IT environment. Students must complete: impact analysis, stakeholder identification, test plan, backout procedure, and maintenance window selection. Class debrief discusses what happens if each step is skipped.

**Lab 6: Honeytoken Deployment Concept**
Students create a fake credential file with a canary token (using a free service like canarytokens.org), place it in a simulated shared drive, and observe the alert generated when it is accessed. Discuss how this would be deployed in a real environment.

---

## Mini Quiz with Answers

**Q1.** Which control type is MOST focused on discouraging an attacker from attempting an action?

- A) Corrective
- B) Compensating
- C) Deterrent ✅
- D) Detective

*Explanation: Deterrent controls discourage attacks through psychological means (visible cameras, warning banners) without technically preventing them.*

---

**Q2.** An organization discovers that their antivirus missed a malware infection. They restore the affected system from a clean backup. What control type is the restoration?

- A) Detective
- B) Preventive
- C) Compensating
- D) Corrective ✅

*Explanation: Restoring a system to a known-good state after an incident is a corrective control.*

---

**Q3.** Which component of Zero Trust architecture is responsible for making the access decision?

- A) Policy Enforcement Point
- B) Policy Administrator
- C) Policy Engine ✅
- D) Subject

*Explanation: The Policy Engine evaluates the request against policies and context, then makes the grant/deny decision. The Policy Administrator communicates the decision to enforcement points.*

---

**Q4.** Which of the following BEST describes the relationship between a public key and a private key?

- A) Both keys can encrypt and decrypt the same data
- B) Data encrypted with the public key can only be decrypted with the private key ✅
- C) Data encrypted with the private key can only be decrypted with the public key
- D) The keys are identical copies stored in different locations

*Explanation: In asymmetric encryption, the keys are mathematically paired but functionally opposite. Data encrypted with the public key can only be decrypted with the paired private key. (Note: when signing, the private key is used to encrypt the hash, and the public key is used to verify — the same asymmetric relationship applies.)*

---

**Q5.** A company cannot deploy MFA on a legacy payroll system due to technical limitations. They implement additional monitoring and require all access to go through a dedicated jump server. What type of control is this?

- A) Corrective
- B) Compensating ✅
- C) Directive
- D) Detective

*Explanation: A compensating control is an alternative safeguard that provides equivalent protection when the primary control cannot be implemented.*

---

**Q6.** Which of the following is the BEST reason to use salting when storing passwords?

- A) It makes the password longer before hashing
- B) It prevents two users with the same password from having the same hash ✅
- C) It encrypts the password before storage
- D) It allows the original password to be recovered for verification

*Explanation: Salting adds a unique random value per user, so even identical passwords produce different hashes. This defeats precomputed rainbow table attacks.*

---

**Q7.** An organization uses a fake server that mimics a production database but contains no real data, placed on the internal network to detect lateral movement. What is this called?

- A) Honeyfile
- B) Honeytoken
- C) Honeypot ✅
- D) Honeynet

*Explanation: A honeypot is a single system designed to look like a real target but which has no legitimate use — any interaction with it signals an intruder.*

---

**Q8.** A change was made to a web application firewall that inadvertently exposed an internal API to the internet. Which change management process would have MOST directly prevented this?

- A) Backout plan
- B) Maintenance window scheduling
- C) Impact analysis ✅
- D) Version control

*Explanation: Impact analysis evaluates what a change affects, including unintended side effects. A thorough impact analysis would have identified that the rule change could expose internal services.*

---

**Q9.** Which technology allows a server to include its own OCSP response in the TLS handshake, eliminating the need for the client to contact the CA directly?

- A) CRL distribution point
- B) Certificate pinning
- C) OCSP stapling ✅
- D) Certificate transparency

*Explanation: OCSP stapling allows the server to pre-fetch and cache its OCSP response, then provide it to clients during the TLS handshake. This improves performance and privacy.*

---

**Q10.** A security administrator wants to hide a sensitive message inside an image file so that even the existence of the message is concealed. Which technique should they use?

- A) Tokenization
- B) Encryption
- C) Data masking
- D) Steganography ✅

*Explanation: Steganography hides the existence of a message by embedding it within a carrier file (such as an image). Encryption hides the content but reveals that encrypted content exists.*

---

*End of Chapter 1.0 — General Security Concepts*
