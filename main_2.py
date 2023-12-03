import argparse
import socket
from pathlib import Path
from threading import Thread

STATUS_200 = "HTTP/1.1 200 OK\r\n"
STATUS_404 = "HTTP/1.1 404 Not Found\r\n\r\n"


def handle_request(sock):
    data = sock.recv(1024)
    method, path = get_path(data)

    headers = data.decode().strip("\r\n").split("\r\n")[1:]
    response = ""
    if path == "/user-agent":
        agent = ""
        for header in headers:
            if header.startswith("User-Agent"):
                agent = header.split(":")[-1].strip()

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {len(agent)}\r\n\r\n"
            f"{agent}\r\n"
        )
    elif path.startswith("/echo/"):
        param = path[len("/echo/") :]
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {len(param)}\r\n\r\n"
            f"{param}\r\n"
        )

    elif path.startswith("/files/"):
        parser = argparse.ArgumentParser()
        parser.add_argument("--directory", help="The directory to serve file from")
        args = parser.parse_args()

        search_dir_path = args.directory and Path(args.directory)
        filename = path[len("/files/") :]
        file_path = None
        if search_dir_path:
            file_path = search_dir_path / filename

        if method == "GET":
            if not file_path or not file_path.is_file():
                response = STATUS_404
            else:
                with open(file_path, "r") as fp:
                    content = fp.read()

                response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: application/octet-stream\r\n"
                    f"Content-Length: {len(content)}\r\n\r\n"
                    f"{content}\r\n"
                )
        else:
            if not file_path:
                response = STATUS_404
            else:
                body = data.decode().strip("\r\n").split("\r\n")[-1]
                with open(file_path, "w") as fp:
                    content = fp.write(body)
                response = "HTTP/1.1 201\r\n\r\n"

    elif path == "/":
        response = STATUS_200 + "\r\n"
    else:
        response = STATUS_404

    sock.send(response.encode())
    sock.close()


def get_path(data):
    request = data.decode().split("\r\n")
    head = request[0]
    method, path = head.split(" ")[0:2]
    return method, path


def main():
    print("Starting http server::")
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        sock, _ = server_socket.accept()
        new_thread = Thread(target=handle_request, args=(sock,))
        new_thread.start()


if __name__ == "__main__":
    main()