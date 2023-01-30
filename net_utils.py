import requests
from requests_toolbelt.adapters import source


def make_request(local_addr: str, url: str, timeout: int = 5):
    with requests.Session() as session:
        session.mount('http://', source.SourceAddressAdapter(local_addr))
        session.mount('https://', source.SourceAddressAdapter(local_addr))
        return session.get(url, timeout=timeout)


# TODO: don't load full body
def check_reachable_by_local_addr(local_addr: str, port: str):
    url = f"http://{local_addr}:{port}/"
    print(f"checking {local_addr}, url {url}")
    make_request(local_addr, url, timeout=1)
