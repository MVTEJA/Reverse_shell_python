import socket
import sys


# Createing a Socket to connect two computers
def Creating_Socket():
    try:
        global Host_name
        global Port_No
        global S1
        Host_name = ""
        Port_No = 9999
        S1 = socket.socket()

    except socket.error as message1:
        print("Error in Creating Socket: " + str(message1))


# Through this function I'm Binding the socket to listen for the connections
def bind_socket():
    try:
        global Host_name
        global Port_No
        global S1
        print("Binding the Port: " + str(Port_No))

        S1.bind((Host_name, Port_No))
        S1.listen(5)

    except socket.error as message1:
        print("Socket Binding error" + str(message1) + "\n" + "Retrying...")
        bind_socket()


# Using thsi fucntion I'm Establishing connection with a client (The Socket should be listening)

def socket_accept():
    Connection_Details, Socket_Address = S1.accept()
    print("Connection established between Client and Server ! |" + " IP Address " + Socket_Address[0] + " | Port No" + str(Socket_Address[1]))
    send_commands(Connection_Details)
    Connection_Details.close()

# Sending commands to the client
def send_commands(Connection_Details):

    # To establish a persistent connection bcaz in the above function after the command has been sent through the send_commands the connection closes
    while True:
        input_command = input()
        if input_command == 'quit':
            Connection_Details.close()
            S1.close()
            sys.exit()
        if len(str.encode(input_command)) > 0:
            Connection_Details.send(str.encode(input_command))
            client_response = str(Connection_Details.recv(1024),"utf-8")
            print(client_response, end="")


def main():
    Creating_Socket()
    bind_socket()
    socket_accept()


main()