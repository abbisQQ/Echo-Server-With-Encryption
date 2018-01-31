# Echo-Server-With-Encryption
  This time our echo server is using encryption to secure the messages we send.
We use AES encryption, padding the message in multipliers of 16 before we send it over.

  AES or Advanced Encryption Standards (also known as Rijndael) is one of the most widely used methods for encrypting and decrypting sensitive information.

  AES is a block cipher.  This means that the number of bytes that it encrypts is fixed.   AES can currently encrypt 
blocks of 16 bytes at a time; no other block sizes are presently a part of the AES standard.  If the bytes being 
encrypted are larger than the specified block then AES is executed concurrently.  This also means that AES has to 
encrypt a minimum of 16 bytes.  If the plain text is smaller than 16 bytes then it must be padded. 
Simply said the block is a reference to the bytes that are processed by the algorithm.   
