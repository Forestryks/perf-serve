from typing import List
import netifaces


def get_local_ips() -> List[str]:
    ips = []
    for interface in netifaces.interfaces():
        for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
            ips.append(link['addr'])
    return ips
