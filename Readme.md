# 🔍 ReconX

 Automated Reconnaissance Framework for Bug Bounty Hunters & Security Researchers

ReconX is a modular Python-based reconnaissance automation tool designed to streamline subdomain enumeration, DNS resolution, and structured output organization for platforms like Bugcrowd, HackerOne, and custom VDP/BPP programs.

---

## ⚡ Features

- 🚀 Automated subdomain enumeration (subfinder / external tools support)
- 🌐 DNS resolution of discovered subdomains
- 📁 Organized output structure by platform & program type
- ⚙️ Async-based execution for better performance
- 🧩 Modular architecture (easy to extend)
- 📊 Clean and structured recon results
- 🔧 CLI-based workflow for fast usage

---

## 🧠 Why ReconX?

Manual recon is slow and unorganized. ReconX solves this by:

- Automating repetitive recon steps
- Structuring results per target & platform
- Making bug bounty workflow faster and scalable

---

## 📁 Project Structure

── config
│── __init__.py
│── settings.py
├── core
│ ├── config.py
│ ├── health.py
│ ├── __init__.py
│ ├── logger.py
│ ├── pipeline.py
│ ├── probe.py
│ ├── resolver.py
│ ├── runner.py
│ ├── subdomain.py
│ └── utils.py
├── data
│ ├── resolvers.txt
│ └── wordlists
├── main.py
├── modules
│ ├── brute
│ ├── dns_brute.py
│ ├── __init__.py
│ ├── passive
│ ├── resolver
│ └── validator
├── output
├── Readme.md
├── requirement.txt
└── structure.md




---

## ⚙️ Installation

### 1. Clone Repository
```bash
git clone https://github.com/Balramch/ReconX.git
cd ReconX
```

## Install Python Dependencies
```
pip install -r requirements.txt

```
🚀 Usage
Basic Command
```
python3 main.py -d example.com -p bugcrowd -t bpp
```
📌 Arguments
```
Flag	Description
-d	Target domain
-p	Platform (bugcrowd / hackerone / others)
-t	Program type (bpp / vdp / private)
```


📂 Output Example
output/
└── bugcrowd/
    └── bpp/
        └── example_com/
            ├── subs.txt
            ├── resolved.txt


🧪 Example Output
==================================================
        ReconX - Recon Automation Tool
==================================================
Target       : bugcrowd.com
Platform     : bugcrowd
Program Type : bpp
--------------------------------------------------
[*] Subdomain Enumeration Started
[*] Resolving Subdomains
[+] Found: 124 subdomains
[+] Resolved: 98 live domains





👨‍💻 Author

Balram Chaudhary
Security Researcher | Bug Bounty Hunter | DevSecOps Enthusiast

📜 Disclaimer

This tool is built for educational and authorized security testing only.

Do not use against systems without explicit permission.