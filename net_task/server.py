import socket
from argparse import ArgumentParser

from core import create_words_dictionary, find_suitable_words


def main(dictionary_path='./dict.txt', port=9090):
    words_dictionary = []

    with open(dictionary_path, 'r') as dict_file:
        words_dictionary = create_words_dictionary(dict_file.readlines())

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('', port)
    sock.bind(server_address)
    sock.listen(1)

    prompt_len = 15

    while True:
        connection, _ = sock.accept()
        try:
            data = ""
            resp = ""
            while True:
                data = connection.recv(prompt_len + 1).strip().decode('utf-8')

                if data:
                    resp = find_suitable_words(data, words_dictionary)
                    resp_len = "{:05d}".format(len(resp))
                    resp_len = str.encode(resp_len)
                    resp = str.encode(resp)

                    connection.sendall(resp_len + resp)
        except TypeError as e:
            pass
        finally:
            connection.close()

if __name__ == "__main__":
    parser = ArgumentParser("User input prompt server")
    parser.add_argument("dictionary_path",
                        help="Path to the words dictionary file")
    parser.add_argument("port", type=int, help="Port number")
    args = parser.parse_args()
    main(**vars(args))
