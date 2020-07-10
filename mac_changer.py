#!/usr/bin/env python
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address, if problems execute it as sudo user")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address, mac format = 00:00:00:00:00:00")
    (options, _) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Specify an interface, use -h to get more information")
    if not options.mac:
        parser.error("[-] Specify a mac address, use -h to get more information")
    return options.interface, options.mac

def change_mac(i, m):
    print(f"[+] Changing MAC address for {i} to {m}")
    subprocess.call(["ifconfig", i, "down"])
    subprocess.call(["ifconfig", i, "hw", "ether", m])
    subprocess.call(["ifconfig", i, "up"])
    subprocess.call("ifconfig", shell=True)


interface, mac = get_arguments()
change_mac(interface, mac)