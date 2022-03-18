import socket
import pickle


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    s.connect((host, port))

    lst = ["QAZ", "WSX", "EDC", "RFV", "TGB"]
    s.send(pickle.dumps(lst))

    msg = s.recv(1024)
    print(pickle.loads(msg))

    s.close()
