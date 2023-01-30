from typing import List
import netifaces


def get_local_ips() -> List[str]:
    ips = []
    for interface in netifaces.interfaces():
        ifaddresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET not in ifaddresses:
            continue
        for link in ifaddresses[netifaces.AF_INET]:
            ips.append(link['addr'])
    return ips
