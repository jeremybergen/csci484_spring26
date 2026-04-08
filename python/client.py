import socket


def main() -> None:
    # with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 1234))
        with open("client.out", "+wb") as fout:
            # data = s.recvall()
            while True:
                data = s.recv(1024)
                if not data:
                    break
                fout.write(data)
        # s.send("Hello".encode())
        # recvData = s.recv(1024)
        # print(f"Received: {recvData.decode()}")


if __name__ == "__main__":
    main()
