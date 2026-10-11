#  [Platform Name] - [Room / Challenge Name]

- **Platform:** [TryHackMe / Hack The Box / OverTheWire / PicoCTF]
- **Difficulty:** [Easy / Medium / Hard / Insane]
- **Date Completed:** [YYYY-MM-DD]
- **Target IP / URL:** `10.10.x.x`
- **Topics / Tags:** `#nmap` `#web` `#privilege-escalation` `#linux`

---

##  Executive Summary
Briefly summarize the challenge. What was the main objective? What vulnerabilities were discovered, and what was the high-level path to gaining root/administrator access?

---

##  1. Reconnaissance & Enumeration

### Port Scanning (Nmap)
Run an Nmap scan to identify open ports and services:
```bash
nmap -sC -sV -T4 -p- 10.10.x.x
