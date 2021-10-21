import socket
import datetime
from Decoder import DecodeData

TCP_IP = '127.0.0.1'
TCP_PORT = 9000
BUFFER_SIZE = 1024
param = []


def Listen():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((TCP_IP, TCP_PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                srv_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                decodedData, resp = DecodeData(data=data.decode(), server_time=srv_time, type='Received')
                print('from {} received [{}] Packet: {}'.format(addr[1], decodedData[0]['Decoded']['Protocol Description'], data.decode()))
                # print(decodedData)
                # print(decodedData[0]['Decoded']['Protocol Description'])
                conn.sendto(resp.encode(), addr)
