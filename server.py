#THIS IS SERVER#
#create and modify M.M.S.Hansaja#
# import the socket and pickle modules
import socket
import threading
#port address
def handle_client(clientsocket):
            #GET USER id
            user_id = clientsocket.recv(1024).decode()      
            data="valid user id"
            #send validity of user id
            dat=data.encode()
            clientsocket.send(dat) 
            import sys
            # import time
            import datetime
            e = datetime.datetime.now()
            print ("Date :: ",e.strftime("%d/%m/%Y"))
            print ("Time :: ",e.strftime("%I:%M:%S %p"))
            print("user id was:::",user_id)
            e = datetime.datetime.now()
            p= (e.strftime("%I.%M"))
            print (e.strftime("%a, %b %d, %Y"))
            date=p
            ti=date.encode()
            clientsocket.send(ti)

# send 10 random stock deatails to client
                #import csv file reader
            import csv
            #import random
            import random
            # read stocks. csv
            with open(r'C:\Users\sahan\OneDrive\Desktop\New folder\stocks.csv', mode='r') as file:
                csv_reader = csv.DictReader(file)
                rows = list(csv_reader)
                random.shuffle(rows)

                selected_rows = rows[:10]  # Assuming `rows` is a valid list of rows

                stock_data = ""
                for row in selected_rows:
                    s1 = "Security: " + row['Security']
                    s2 = "Symbol: " + row['Symbol']
                    s3 = "Price: " + row['Price']
                    s4 = "Profit: " + row['Profit']
                    s5 = "-----------------------------------"
                    stock_data += s1 + "\n" + s2 + "\n" + s3 + "\n" + s4 + "\n" + s5 + "\n"

                stock_data = stock_data.encode()
                clientsocket.sendall(stock_data)  # Using sendall() instead of send()
#write name ,symbol and bit in clint.csv file

            print("ok")
                    
            import csv

            header = ['name', 'symbol', 'bit']   
            #append client .csv file
            with open(r'C:\Users\sahan\OneDrive\Desktop\New folder\client.csv', mode='a') as file:
                csv_writer = csv.writer(file)
                name = clientsocket.recv(1024).decode()# get name from client
                symbol = clientsocket.recv(1024).decode()# get symbol from client
                if symbol == symbol:# check symbol validity
                    import csv
                    found = False
#get security code of that symbol from stocks.csv fie
                    with open(r'C:\Users\sahan\OneDrive\Desktop\New folder\stocks.csv', mode='r') as file:# read stock.csv file
                        csv_reader = csv.DictReader(file)
                        for row in csv_reader:
                            if row['Symbol'] == symbol:
                                print(f"Security: {row['Security']}")
                                found = True
                                #send security to the client
                                kl = str(row['Security'])
                                sec = kl.encode()
                                clientsocket.send(sec)
                    # if not valid symbol prosess this
                    if not found:
                        kl = "Symbol not found"
                        sec = kl.encode()
                        clientsocket.send(sec)
                else:
                    print("ERROR")
        # write bit in client.csv file
            with open(r'C:\Users\sahan\OneDrive\Desktop\New folder\client.csv', mode='a') as file:
                csv_writer = csv.writer(file)     
                #receve bit       
                bit = clientsocket.recv(1024).decode()
                if file.tell() == 0:
                    csv_writer.writerow(header)
                    #write name,symbol, bit
                csv_writer.writerow([name, symbol, bit])


            data_4=str(bit)
            bit_4=data_4.encode()
            clientsocket.send(bit_4)

            import pandas as pd
            df = pd.read_csv(r'C:\Users\sahan\OneDrive\Desktop\New folder\client.csv')
            max_bit = df['bit'].max()
            data_1=str(max_bit)
            max_b=data_1.encode()
            clientsocket.send(max_b)

            
            import time
            duration = 300
            start_time = time.time()
            while time.time() - start_time < duration:
    #clint bit again recive to client
                new_bit = clientsocket.recv(1024).decode()
    #get max bit from the client.csv file
                import csv
                with open(r'C:\Users\sahan\OneDrive\Desktop\New folder\client.csv', mode='r') as file:# read client.csv
                    csv_reader = csv.DictReader(file)
                    rows = list(csv_reader)

                for row in rows:
                    if row['name'] == name and row['symbol'] == symbol:
                        row['bit'] = new_bit
                        break

                # Write the updated rows back to the CSV file
    #again update row after the new bit
                # Write the updated rows back to the CSV file
                #include file part of client.csv
                with open(r'C:\Users\sahan\OneDrive\Desktop\New folder\client.csv', mode='w', newline='') as file:
                    fieldnames = ['name', 'symbol', 'bit']
                    #send max bit to client
                    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
                    csv_writer.writeheader()#file write
                    csv_writer.writerows(rows)

                print("Bit value updated successfully.") 
    #send maximum bit
                
                import pandas as pd
                df = pd.read_csv(r'C:\Users\sahan\OneDrive\Desktop\New folder\client.csv')
                max_bit = df['bit'].max()#file part of client.csv
                data_1=str(max_bit)
                max_b=data_1.encode()
                clientsocket.send(max_b)           

            clientsocket.close()

#socket connection
    
def start_server():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 2022
        s.bind(('', port))#get port address
        s.listen(1)
        print("Server listening on port", port)

        while True:
            clientsocket, address = s.accept()
            print("New client connected:", address)

            client_thread = threading.Thread(target=handle_client, args=(clientsocket,))
            client_thread.start()

start_server()