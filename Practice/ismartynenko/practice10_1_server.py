import socket
import pickle


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    s.bind((host, port))
    s.listen(1)

    dic = {"QAZ": "Абель", "WSX": "Толкачев", "EDC": "Эймс", "RFV": "Поляков", "TGB": "Соломатин"}
    decrypt = []

    while True:
        conn, _ = s.accept()
        msg = conn.recv(1024)
        for i in pickle.loads(msg):
            decrypt.append(dic[i])

        conn.send(pickle.dumps(decrypt))
        conn.close()
