import socket
from Crypto.Cipher import AES




def customPadding(messageToPad):
    while(len(messageToPad)%16!=0):
        messageToPad+="~"
    return  messageToPad


def encryption(messageToEncrypt):
    messageToEncrypt=customPadding(messageToEncrypt)
    obj = AES.new(secret_key, AES.MODE_CBC,Initialization_vector)
    return obj.encrypt(messageToEncrypt)



def decryption(ciphertext):
    obj2 = AES.new(secret_key, AES.MODE_CBC,Initialization_vector)
    return (obj2.decrypt(ciphertext).decode()).replace("~","")



def server():
    host = "127.0.0.1" #listen at all interfaces
    port = 9999
    
    mySocket = socket.socket()
    mySocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    mySocket.bind((host,port))

    mySocket.listen(1)#only 1 client can connect
    print("Listening for incoming connections")
    conn,addr = mySocket.accept()


    print('Connection from: {}'.format(addr))
    received_message = decryption(conn.recv(4096))

    sending_message= input("What should i send? ")

    while sending_message!= 'quit':
        conn.send(encryption(sending_message))
        received_message = decryption(conn.recv(4096))
        print(received_message)
        sending_message = input("What should i send? ")
       
    conn.close()
    print("Server shut down...")

if __name__ == "__main__":
    
    #secret_key = os.urandom(BLOCK_SIZE) i generated once and i will use that always
    secret_key=b'b\x90\xf7\x1d\\KY\xc3\xd7\x13\xf1\x90\xba\xe4HS\xe3\xce\x1cd\x8f\xdf\xda\xc8u\xa9B\x85-&<\xb7'
    Initialization_vector = 'This is a testIV'#IV must be 16 bytes long
    
    server()
