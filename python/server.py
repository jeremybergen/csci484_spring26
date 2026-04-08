import socket

def main():
    # with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", 1234))
        s.listen()
        conn, addr = s.accept()
        print(f"conn:{conn}, addr:{addr}")
        # data = conn.recv(1024)
        # print(f"Received: {data.decode()}")
        # conn.send(data)
        with open("server.out", "+rb") as fin:
            data = fin.read()
            conn.send(data)
    # s.close()

if __name__ == "__main__":
    main()