import sys
from abc import ABC, abstractmethod
from scapy.all import IP, UDP, sr1


def trace_udp(host:str,
              udp_length=2,
              min_ttl:int=1,
              max_ttl:int=30,
              num_per_fleet:int=3,
              timeout:int=5,
              port:int=33434,
              source:str=None):
    data:str = get_junk(udp_length)
    responses = list()
    for ttl in range(min_ttl, max_ttl+1):
        for pckno in range(num_per_fleet):
            packet = make_packet(host, source, ttl, port, data)
            response = sr1(packet, timeout=timeout)
            responses.append(response)
            #print(response) # TODO: interpret response


def make_packet(host:str, source:str, ttl:int, port:int, data):
    if source != None:
        packet = IP(dst=host, src=source, ttl=ttl) / \
                 UDP(dport=port) / \
                 data
    else:
        packet = IP(dst=host, ttl=ttl) / \
                 UDP(dport=port) / \
                 data
    return packet

def get_junk(length=2):
    ret = "42" * length
    if length%2 != 0:
        ret += "!"
    return ret
