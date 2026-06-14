# Deauthentication Attack Workflow Guide (Step-by-Step)

This guide explains how to prepare an external wireless network adapter, identify a target wireless network, and then launch a network-wide deauthentication attack using the `aireplay-ng` tool.

---

# Step 1: Prepare the System and Enable Monitor Mode

Before starting, any operating system services (such as `NetworkManager`) that may attempt to control the external wireless adapter and force it back into Managed Mode should be stopped.

## Commands

```bash
# 1. Terminate interfering processes and services
sudo airmon-ng check kill

# 2. Temporarily disable the wireless interface
sudo ip link set wlan1 down

# 3. Switch the adapter into Monitor Mode
sudo iw config wlan1 mode monitor

# 4. Re-enable the wireless interface
sudo ip link set wlan1 up
```

## Detailed Explanation

### Monitor Mode

Monitor Mode allows a wireless network adapter to listen to all wireless frames transmitted over the air, even if those frames are not addressed to the local machine. It also enables packet injection capabilities without requiring association with a wireless network.

### `airmon-ng check kill`

This is a critical step because system services may detect the adapter operating in Monitor Mode and automatically switch it back to Managed Mode. Such behavior can cause later operations to fail and may generate errors such as:

```text
Device or resource busy
```

---

# Step 2: Reconnaissance and Target Discovery

In this phase, nearby wireless networks are observed to determine the router's MAC address (`BSSID`) and operating channel (`CH`).

## Command

```bash
sudo airodump-ng wlan1
```

## Detailed Explanation

When executed, the adapter automatically hops between wireless channels to collect information about nearby networks.

### Record the Following Information

From the upper table displayed by `airodump-ng`, identify the target network and note:

* **BSSID** (Example: `B8:DD:71:D5:9D:AC`)
* **CH (Channel Number)** (Example: `7`)

### Important Note

After collecting the required information, stop the scan immediately by pressing:

```text
Ctrl + C
```

If the scanning process continues running, the adapter will keep hopping between channels and will not remain synchronized with the target network.

---

# Step 3: Lock the Adapter to the Target Channel

After stopping the scan, configure the adapter to remain fixed on the target network's channel.

## Command

```bash
sudo iwconfig wlan1 channel 7
```

## Detailed Explanation

The wireless adapter and the target access point must operate on the same channel.

If deauthentication frames are transmitted while the adapter is tuned to a different channel than the target access point, the frames will not reach the intended destination, and tools such as `aireplay-ng` may display warnings indicating a channel mismatch.

---

# Step 4: Launch a Continuous Broadcast Deauthentication Attack

The following command initiates a continuous deauthentication attack against all devices associated with the target wireless network.

## Command

```bash
sudo aireplay-ng --deauth 0 -a B8:DD:71:D5:9D:AC -D --ignore-negative-one wlan1
```

## Parameter Breakdown

| Parameter               | Function and Explanation                                                                                                                                                                |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sudo`                  | Executes the command with root privileges, allowing direct access to wireless hardware functionality.                                                                                   |
| `--deauth 0`            | Specifies a deauthentication operation. The value `0` indicates continuous transmission without a predefined limit. The operation continues until manually interrupted with `Ctrl + C`. |
| `-a B8:DD:71:D5:9D:AC`  | Specifies the BSSID (MAC address) of the target access point.                                                                                                                           |
| Absence of `-c`         | Because no client MAC address is specified, the operation targets the broadcast destination (`FF:FF:FF:FF:FF:FF`), affecting all associated clients.                                    |
| `-D`                    | Short form of `--disable-subsequences`. Instructs the tool to avoid automatic channel adjustments and remain on the configured channel.                                                 |
| `--ignore-negative-one` | Bypasses a common Linux driver issue in which the adapter is incorrectly reported as operating on channel `-1`.                                                                         |
| `wlan1`                 | Specifies the wireless interface being used.                                                                                                                                            |

---

# How the Attack Works (Conceptual Overview)

1. Traditional Wi-Fi networks (including WPA2 and earlier standards) rely on management frames to coordinate communications between access points and client devices.

2. The attack tool generates spoofed management frames that appear to originate from the access point and instruct client devices to terminate their current association.

3. Client devices receiving these frames may disconnect and attempt to reconnect repeatedly while the transmission continues.

---
