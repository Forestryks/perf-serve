from pathlib import Path
from server import start_server
from time import sleep
from perf_script import run_perf_script
from args import parse_args
from interfaces import get_local_ips
import urllib.parse
import requests


def check_file_exists(path: Path):
    if not path.exists():
        print(f"Cannot find {path}")
        exit(1)


def make_link(label: str, url: str):
    escape_mask = '\033]8;;{}\033\\{}\033]8;;\033\\'
    return escape_mask.format(url, label)


def get_my_ip() -> str:
    return requests.get('https://api.ipify.org').text


def display_url_via_ip(ip: str, port: int, prefix: str, name: str):
    data_url = f"http://{ip}:{port}/"
    url = f"https://profiler.forestryks.org/from-url/{urllib.parse.quote(data_url, safe='')}"
    link = make_link(name, url)
    print(f"{prefix} {link}")


def display_possible_urls(port: int):
    display_url_via_ip(get_my_ip(), port, "🚀", "via public ip")
    print("Other variants:")
    ips = get_local_ips()
    for ip in ips:
        display_url_via_ip(ip, port, "➤", f"via {ip}")


def main():
    args = parse_args()
    check_file_exists(args.path)

    perf_script_output = run_perf_script(args.path)
    http_server = start_server(Path(perf_script_output.name), args.address, args.port)

    display_possible_urls(http_server.server_address[1])

    while True:
        sleep(1)


if __name__ == "__main__":
    main()

# TODO: detect closed ports
# TODO: easy installation
# TODO: better logs and output
# TODO: detect that hyperlinks are not supported
