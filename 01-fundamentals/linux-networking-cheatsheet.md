#  Linux Networking Cheatsheet

A quick-reference guide for essential Linux networking commands used in troubleshooting, system administration, and security analysis.

---

##  1. Interface & IP Configuration

| Command | Description |
| :--- | :--- |
| `ip a` or `ip addr` | Show all network interfaces and assigned IP addresses |
| `ip link show` | Display link-layer information (MAC addresses, interface state) |
| `ip -s link` | Show network interface statistics (packets sent/received/dropped) |
| `ip route show` or `ip r` | Display the current routing table |
| `ifconfig` | *(Legacy)* Display interface configuration |

---

## 📡 2. Connectivity & Routing Tests

| Command | Description |
| :--- | :--- |
| `ping <ip_or_domain>` | Test ICMP network connectivity to a host |
| `ping -c 4 <ip>` | Send exactly 4 ICMP echo requests |
| `traceroute <domain>` | Trace the hop-by-hop packet route to a target domain |
| `tracepath <domain>` | Trace path to target and report MTU size |
| `ip route add default via <gateway_ip>` | Set the default gateway |

---

##  3. Active Connections & Listening Ports

| Command | Description |
| :--- | :--- |
| `ss -tuln` | List listening TCP/UDP ports with numerical addresses (Fast) |
| `ss -tulnp` | List listening TCP/UDP ports showing associated process names/PIDs |
| `netstat -tulnp` | *(Legacy)* List active listening sockets and process IDs |
| `lsof -i :<port>` | Identify which process is running on a specific port |

---

##  4. DNS & Name Resolution

| Command | Description |
| :--- | :--- |
| `dig <domain>` | Perform a detailed DNS query for a domain |
| `dig <domain> MX` | Query specific DNS record types (A, MX, NS, TXT) |
| `dig +short <domain>` | Return only the target IP address |
| `nslookup <domain>` | Query internet name servers interactively |
| `host <domain>` | Quick lookup of IP or domain name |
| `cat /etc/resolv.conf` | Display configured local DNS nameservers |
| `cat /etc/hosts` | View local static IP-to-hostname mappings |

---

##  5. Traffic Analysis & Packet Capture

| Command | Description |
| :--- | :--- |
| `tcpdump -i eth0` | Capture all packet traffic on interface `eth0` |
| `tcpdump -i eth0 port 80` | Capture traffic on a specific port (HTTP) |
| `tcpdump -i eth0 -w capture.pcap` | Save captured network traffic to a PCAP file |
| `tcpdump -r capture.pcap` | Read and analyze a saved PCAP file |

---

##  6. Firewall & Security Operations

| Command | Description |
| :--- | :--- |
| `sudo ufw status` | Check status of Uncomplicated Firewall (UFW) |
| `sudo ufw allow 22/tcp` | Allow incoming SSH traffic |
| `sudo ufw deny 80` | Block incoming HTTP traffic |
| `sudo iptables -L -v` | List all Active `iptables` firewall rules verbosely |
| `sudo nft list ruleset` | List active `nftables` rulesets |

---

##  7. File Transfer & Remote Access

| Command | Description |
| :--- | :--- |
| `curl -I <url>` | Fetch HTTP headers from a URL |
| `curl -O <url>` | Download a file via URL retaining original filename |
| `wget <url>` | Download files directly from the web |
| `ssh user@<ip>` | Connect to remote server via SSH |
| `scp file.txt user@<ip>:/path/` | Securely copy local file to remote server |
| `nc -zv <ip> <port>` | Check if a specific remote port is open using Netcat |
