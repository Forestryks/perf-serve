from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import argparse


class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, served_file: Path, *args, **kwargs) -> None:
        self.served_file = served_file
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        with self.served_file.open() as f:
            self.wfile.write(bytes(f.read(), "utf8"))


@dataclass
class Config:
    path: Path
    address: str
    port: int


def serve(config: Config):
    server_address = (config.address, config.port)
    http_server = HTTPServer(server_address, lambda *args, **kwargs: RequestHandler(config.path, *args, **kwargs))
    print(f"Server running on {http_server.server_address[0]}:{http_server.server_address[1]}")
    http_server.serve_forever()


def check_file_exists(path: Path):
    if not path.exists():
        print("cannot find specified file")
        exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--address", help="set address to serve on, defaults to 0.0.0.0", default="0.0.0.0", type=str)
    parser.add_argument("--port", help="set port to serve on, defaults to random", default=0, type=int)
    parser.add_argument("file", help="path to file to serve", type=Path)
    args = parser.parse_args()

    config = Config(args.file, args.address, args.port)
    check_file_exists(args.file)
    serve(config)


if __name__ == "__main__":
    main()
