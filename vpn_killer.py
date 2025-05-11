import psutil
import os
import time

# Change this to the name of your VPN process (e.g., openvpn, nordvpn, expressvpn)
VPN_PROCESS_NAMES = ["openvpn", "nordvpn", "expressvpn", "windscribe"]

def is_vpn_connected():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and any(vpn.lower() in proc.info['name'].lower() for vpn in VPN_PROCESS_NAMES):
            return True
    return False

def kill_network():
    os.system('netsh interface set interface name="Wi-Fi" admin=disable')
    os.system('netsh interface set interface name="Ethernet" admin=disable')
    print("[!!] VPN disconnected. Network disabled.")

print("[*] Monitoring VPN...")
while True:
    if not is_vpn_connected():
        kill_network()
        break
    time.sleep(5)
