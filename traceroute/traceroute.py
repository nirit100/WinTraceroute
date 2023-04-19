import sys
from abc import ABC, abstractmethod
from scapy.all import IP, UDP, sr1


def trace_udp(host:str, 
          udp_length=2,
          max_ttl:int=30,
          num_per_fleet:int=3,
          timeout:int=5,
          port:int=33434):
    data:str = get_junk(udp_length)
    responses = list()
    for ttl in range(1, max_ttl):
        for pckno in range(num_per_fleet):
            packet = IP(dst='host', ttl=ttl) / \
                     UDP(dport=port) / \
                     data
            response = sr1(packet, timeout=timeout)
            responses.append(response)
            
            
def get_junk(length=2):
    ret = "42" * length
    if length%2 != 0:
        ret += "!"
    return ret