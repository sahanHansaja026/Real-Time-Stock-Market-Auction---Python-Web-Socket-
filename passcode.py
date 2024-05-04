import socket
def start_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 21
    s.connect((socket.gethostname(), port))
    #send pass code
    number_1 = input("Enter the code: ")

    n2 = number_1.encode()
    s.sendall(n2)
    print(number_1)
    s.close()
start_client()