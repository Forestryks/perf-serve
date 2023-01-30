from pathlib import Path
import requests
from server import start_server
from time import sleep
from perf_script import run_perf_script
from args import Args, parse_args
from interfaces import get_local_ips
from net_utils import check_reachable_by_local_addr


def serve(args: Args, perf_script_output: Path):
    return start_server(perf_script_output, args.address, args.port)

    # my_ip = get_my_ip()
    # data_url = f"http://{my_ip}:{http_server.server_address[1]}/"
    # print(f"Public: {data_url}")
    # print(f"Url: https://profiler.forestryks.org/from-url/{urllib.parse.quote(data_url, safe='')}")


def get_my_ip() -> str:
    return requests.get('https://api.ipify.org').text


def check_file_exists(path: Path):
    if not path.exists():
        print(f"Cannot find {path}")
        exit(1)


def find_possible_urls(port: int):
    ips = get_local_ips()
    for ip in ips:
        check_reachable_by_local_addr(ip, port)
        # print(ip)


def main():
    args = parse_args()
    check_file_exists(args.path)

    perf_script_output = run_perf_script(args.path)
    http_server = start_server(Path(perf_script_output.name), args.address, args.port)

    find_possible_urls(http_server.server_address[1])

    while True:
        sleep(1)


if __name__ == "__main__":
    main()

# TODO: detect and display more ips
# TODO: detect closed ports
# TODO: easy installation
# TODO: better logs and output
# TODO: use hyperlinks formatting when possible
