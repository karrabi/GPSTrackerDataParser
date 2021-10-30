import socket
import datetime
from Decoder import DecodeData
import struct 
import binascii

TCP_IP = '51.38.66.1'
TCP_PORT = 9000
BUFFER_SIZE = 1024
param = []


def convert_data_to_ints(data, big_endian=True):
    int_count = len(data) // 4  # Assuming uint is 4 bytes long !!!
    fmt = ">" if big_endian else "<"
    fmt += "I" * int_count
    return struct.unpack(fmt, data[:int_count * 4])
    
    

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
                # print('server time: ', srv_time)
                # databyte = bytes.fromhex(data)
                # print('1')
                print(data)
                b = bytearray(data)
                # print('2')
                # print(b)
                dataString  = binascii.hexlify(b)
                # print('3')
                # print(dataString)
                # print('4')
                print(dataString.decode())
                decodedData, resp = DecodeData(data=dataString.decode(), server_time=srv_time, type='Received')
                print('from {} received [{}] Packet: {}'.format(addr[1], decodedData[0]['Decoded']['Protocol Description'], dataString.decode()))
                # print(decodedData)
                # print(decodedData[0]['Decoded']['Protocol Description'])
                print('responsed:' + resp )
                # print(resp.encode())
                # print(binascii.unhexlify(resp.encode()))
                conn.sendto(binascii.unhexlify(resp.encode()), addr)
                print('')
                print('')
                print('')
                print('')
