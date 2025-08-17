# WiFi Security Testing Tool (Terminal-Based)

This tool is designed for **educational and authorized use only**. It performs WPA handshake capture and password testing using a wordlist. Intended for cybersecurity training, penetration testing labs, and personal network audits.

## 🧠 Features

- Monitor mode activation
- Network scanning (SSID, BSSID, channel)
- WPA handshake capture
- Real password testing via wordlist (aircrack-ng)
- Step-by-step terminal interface

## ⚠️ Legal Disclaimer

This tool must **only be used on networks you own or have explicit permission to test**. Unauthorized use against third-party networks is illegal and violates computer crime laws in most countries.

## 🔧 Requirements

- Linux (Kali Linux recommended)
- Python 3.8+
- Installed tools: `airmon-ng`, `airodump-ng`, `aircrack-ng`
- Wi-Fi adapter that supports monitor mode
- Wordlist file (e.g., `rockyou.txt`)

## 🚀 Installation

```bash
sudo apt update
sudo apt install aircrack-ng
git clone https://github.com/Friday7772/WPAForge.git
cd WPAForge
sudo python3 WPAForge.py
