#!/usr/bin/env python
ip_addr = input("Gimme an IP: ")
ip_addr = (ip_addr.split("."))

print(ip_addr)

ip_addr[-1] = '0'

print(ip_addr[0], ip_addr[1], ip_addr[2], ip_addr[3])

print(bin(int(ip_addr[0])), bin(int(ip_addr[1])), bin(int(ip_addr[2])), bin(int(ip_addr[3])))
