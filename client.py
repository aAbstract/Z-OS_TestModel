
'''
Test Client That Implement ZCP client protocol

-----<ZCP-Protocol>-----
1 -> send client id <<clientid>_<network_role>>
2 -> encrypt the given signal from the server using his won public key
3 -> send the result of encryption to the server to valid the connection
4 -> perfom the required task on the network
-----</ZCP-Protocol>-----

'''
