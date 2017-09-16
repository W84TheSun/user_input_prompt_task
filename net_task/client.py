import socket
from argparse import ArgumentParser


def main(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (hostname, port)
    sock.connect(server_address)

    while True:
        user_input = input()
        cmd, prompt = user_input.split()
        if cmd == 'get':
            sock.send(prompt)

            guesses = sock.recv().strip()
            print(guesses)
            print(" ")
        else:
            print("Unknown command. Use Ctrl+C to exit.")


if __name__ == "__main__":
    parser = ArgumentParser("User input prompt server")
    parser.add_argument("hostname",
                        help="Server IP address or hostname")
    parser.add_argument("port", type=int, help="Port number")
    args = parser.parse_args()
    main(**vars(args))
