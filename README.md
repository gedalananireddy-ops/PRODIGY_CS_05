# PRODIGY_CS_05
Task-05: Network Packet Analyzer (Educational Packet Sniffer)
⚠️ IMPORTANT DISCLAIMER
This project is developed strictly for educational and ethical purposes.

Use this tool only on networks you own or where you have explicit authorization
Unauthorized packet sniffing may violate privacy laws and cybersecurity regulations
The author is not responsible for misuse of this tool
📌 Project Overview
This is a basic network packet analyzer (packet sniffer) written in Python.
It captures live network traffic and displays:

Source IP address
Destination IP address
Network protocol (TCP / UDP / ICMP)
Payload data (limited and safely decoded)
This project helps learners understand:

How packet sniffers work
Network protocols
Why encryption (HTTPS, TLS) is important
Defensive network security concepts
✨ Features
Live packet capture
Protocol detection (TCP, UDP, ICMP)
Payload inspection (first few bytes only)
Clean termination using CTRL + C
No packet modification or injection
No persistence or stealth behavior
🛠️ Requirements
Python 3.8 or higher
Administrator / Root privileges
Visual Studio Code (recommended)
Internet access (only for installing dependencies)
📦 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/network-packet-analyzer.git
cd network-packet-analyzer
2️⃣ Open in VS Code
code .

3️⃣ Create a Virtual Environment (Recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate
4️⃣ Install Dependencies
pip install scapy

▶️ How to Run the Packet Analyzer

⚠️ Administrator / Root privileges required

Windows

Open VS Code as Administrator

Run:

python packet_sniffer.py
🧪 Example Output
============================================================
Source IP      : 192.168.1.10
Destination IP : 142.250.182.14
Protocol       : TCP
Payload        : GET / HTTP/1.1

🔍 How It Works

Captures packets from the network interface

Checks for IP packets

Identifies protocol (TCP / UDP / ICMP)

Extracts source and destination IP addresses

Displays payload data safely (limited bytes)

Continues until manually stopped

🛡️ Ethical Use & Learning Objectives

This tool is intended for:

Cybersecurity students

Ethical hacking labs

Network analysis practice

Defensive security research

❌ Not intended for:

Surveillance

Spying on users

Data theft

Man-in-the-middle attacks
