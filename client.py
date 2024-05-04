#socket connection
import socket
import time
def start_client():#definition
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 2022
    s.connect((socket.gethostname(), port))
    print('*'*5,'-'*5,'this is client','-'*5,'*'*5)
    user_id = input("Enter your user id: ")
    s.sendall(user_id.encode())

    # validity of user id from server
    date = s.recv(1024)
    date = date.decode()
    print(date)

    #receiveing time from server
    data = s.recv(1024)
    data = data.decode()
    print("time was::::: ",data)
    print('---------------------')


    #receiveing stocks deatails
    stock_1 = s.recv(1024)
    stock_1 = stock_1.decode()
    print(stock_1)

    #input client name
    name = input("Enter the name: ")
    #send client name
    n2 = name.encode()
    s.sendall(n2)

    #input symbol
    symbol = input("Enter the symbol: ")
    #send symbol
    n3=symbol.encode()
    s.sendall(n3)

    #receiveing Security
    sec = s.recv(1024)
    sec = sec.decode()
    print("Security was:::",sec)
    # trading for timeing and bit
    #this programe exit after 60 seconds
    import threading
    def get_user_input():
        print("..........Executing the program after 60 seconds!..........")
        bit = input("Enter the bit: ")# bit input

        #send this bit to server
        n4=bit.encode()
        s.sendall(n4)

     #timeing codes   
    timer = threading.Timer(60.0, lambda: print("Time's up!"))
    try:
        timer.start()
        get_user_input()
    finally:
        timer.cancel()
#5 minutes count down
    duration = 300
    start_time = time.time()
 
#old bit receiveing
    obit= s.recv(1024)
    obit = obit.decode()
    #print old bit
    print(obit)

    print("..........END the program after 5 minutes !..........")
#receiveing max bit from server
    datamax= s.recv(1024)
    datamax = datamax.decode()
    print("max bit was:::",datamax)

    while time.time() - start_time < duration:
        print("max bit was:::",datamax)
        new_bit = input("Enter new bit value: ") #new bit input
        nb=new_bit.encode()#new bit send to server
        s.sendall(nb) 

        obit=new_bit
    #receiveing max bit again this is updated max bit
        datamax= s.recv(1024)
        datamax = datamax.decode()
        while True:
            if float(datamax)>float(obit):#condition

                    print("now max bit was::::",datamax)#print it
                    break


            else:   
                    print("your bit was now maximimem bit\n")
                    break
    print("Countdown complete!")
    print("Thank you join us!")
    print("end")

    s.close()# client socket drop/stop
start_client()