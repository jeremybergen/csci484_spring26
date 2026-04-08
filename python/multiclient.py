from socket import *
import errno
import sys

HEADER_LENGTH=10

def main():
    username = input(f"Enter username: ")
    print(f"{len(username):<{HEADER_LENGTH}}{username}")
    quit()
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 1234))
        s.send(f"{len(username):<{HEADER_LENGTH}}{username}".encode())

        while True:
            message = input(f"{username}> ")
            if message:
                s.send(message.encode())
            
            try:
                while True:
                    recv_message = s.recv(1024).decode()
                    print(f"{recv_message}")
            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print(f"reading error: {str(e)}")
                    sys.exit()
                continue

if __name__ == "__main__":
    main()
    