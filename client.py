import socket
import urllib.request
from Crypto.Cipher import AES
import time



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




def client():

    #Creating the socket passing the ip and port as parameters and trying to connect
    host = "127.0.0.1"
    port = 4444
    mySocket = socket.socket()
    mySocket.connect((host,port))
    #connection established

    #sending the ip
    #external ip: urllib.request.urlopen('http://ident.me').read().decode('utf8')
    sending_message = "Hello"
    sending_message = encryption(sending_message)
    mySocket.send(sending_message)
    
    received_message = decryption(mySocket.recv(4096))
    print(received_message)
    while(received_message!="quit"):

        sending_message = encryption(received_message)
        mySocket.send(sending_message)

    
        received_message=decryption(mySocket.recv(4096))
        print(received_message)





if __name__ == "__main__":

    #secret_key = os.urandom(BLOCK_SIZE) i generated once and i will use that always
    secret_key=b'b\x90\xf7\x1d\\KY\xc3\xd7\x13\xf1\x90\xba\xe4HS\xe3\xce\x1cd\x8f\xdf\xda\xc8u\xa9B\x85-&<\xb7'
    Initialization_vector = 'This is a testIV'#IV must be 16 bytes long
    
    while True:
       try:
            client()
       except:
            print("could not connect")
            time.sleep(60) # sleep for 60 seconds before retrying to connect
