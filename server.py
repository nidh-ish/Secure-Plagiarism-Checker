import random
import numpy as np
from bitarray import bitarray
from bitarray.util import *

class Server:
    def id(self):
        pass
    def nextp_randomness(self):
        pass
    def prevp_randomness(self):
        pass
    def common_randomness(self):
        pass
    def offline_AND(self):
        pass
    def offline_AND1(self):
        pass
    def online_AND(self):
        pass
    def offline_share(self):
        pass
    def online_share(self):
        pass
    def OR(self):
        pass


class Messenger:
    def __init__(self):
        self.__Q01 = []
        self.__Q10 = []

    # S0 calls to send message to S1
    def nextp_send(self, m):
        self.__Q01.append(m)
        
    # S1 calls to send message to S0
    def prevp_send(self, m):
        self.__Q10.append(m)

    # S0 calls to receive message from S1
    def nextp_receive(self):
        if len(self.__Q10) == 0:
            return None
        else:
            x = self.__Q10.pop(0)
            return x

    # S0 calls to receive message from S1
    def prevp_receive(self):
        if len(self.__Q01) == 0:
            return None
        else:
            x = self.__Q01.pop(0)
            return x


class Server0(Server):
    def __init__(self, initRandom01, initRandom02, initRandomCommon, mess_prev: Messenger, mess_next: Messenger) -> None:
        self.__initRandom01 = initRandom01
        self.__initRandom02 = initRandom02
        self.__initRandomCommon = initRandomCommon
        self.__mess_prev = mess_prev
        self.__mess_next = mess_next

    def id(self):
        return 0
    
    def OR(self, a, b):
        return [a[0] ^ b[0], a[1] ^ b[1]]

    def nextp_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandom01))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom01 = x
        return x

    def prevp_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandom02))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom02 = x
        return x

    def common_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandomCommon))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandomCommon = x
        return x
    
    def offline_AND(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))
        lambda_c1 = self.nextp_randomness(1)
        g1 = self.nextp_randomness(1)
        lambda_c2 = self.prevp_randomness(1)

        g2 = (a & b) ^ g1

        # Send g2 to Server2
        self.__mess_prev.prevp_send(g2)

        return lambda_c1 ^ lambda_c2
    
    def offline_AND1(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))

        lambda_c1 = self.nextp_randomness(1)
        g1 = self.nextp_randomness(1)
        lambda_c2 = self.prevp_randomness(1)

        g2 = (a & b) ^ g1

        # Send g2 to Server2
        self.__mess_prev.prevp_send(g2)

        return lambda_c1, lambda_c2
    
    def offline_share(self, sharingserver: int):
        if sharingserver == "0":
            lambda1 = self.nextp_randomness(1)
            lambda2 = self.prevp_randomness(1)
        
        if sharingserver == "1":
            lambda1 = self.nextp_randomness(1)
            lambda2 = self.common_randomness()
        
        if sharingserver == "2":
            lambda1 = self.common_randomness()
            lambda2 = self.prevp_randomness(1)

        return lambda1, lambda2

    def online_share(self, sharingserver: int, lambda1: bitarray, lambda2: bitarray, message: bitarray):
        if sharingserver == "0":
            m = lambda1 ^ lambda2 ^ message
            self.__mess_next.nextp_send(m)
            self.__mess_prev.prevp_send(m)


class Server1(Server):
    def __init__(self, initRandom10, initRandom12, initRandomCommon, mess_prev: Messenger, mess_next: Messenger) -> None:
        self.__L = [[], [], [], []]
        self.__initRandom10 = initRandom10
        self.__initRandom12 = initRandom12
        self.__initRandomCommon = initRandomCommon
        self.__mess_prev = mess_prev
        self.__mess_next = mess_next

    def id(self):
        return 1
    
    def OR(self, a, b):
        return [a[0] ^ b[0]]

    def nextp_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandom12))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom12 = x
        return x

    def prevp_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandom10))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom10 = x
        return x

    def common_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandomCommon))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandomCommon = x
        return x
    
    def offline_AND(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c1 = self.prevp_randomness(1)
        self.__L[2].append(lambda_c1)

        g1 = self.prevp_randomness(1)
        self.__L[3].append(g1)
        return lambda_c1

    def offline_AND1(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c1 = self.prevp_randomness(1)
        self.__L[2].append(lambda_c1)

        g1 = self.prevp_randomness(1)
        self.__L[3].append(g1)
        
        return [lambda_c1]

    def online_AND(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))
        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)

        m1 = (a & temp1) ^ (b & temp2) ^ temp3 ^ temp4

        # Send m1 to Server2
        self.__mess_next.nextp_send(m1)

        # Receive m2 from Server2
        m2 = self.__mess_next.nextp_receive()
        while m2 != None:
            m2 = self.__mess_next.nextp_receive()

        return m1 ^ m2
    
    def offline_share(self, sharingserver: int):
        if sharingserver == "0":
            lambda1 = self.prevp_randomness(1)
            return lambda1
        if sharingserver == "1":
            lambda1 = self.prevp_randomness(1)
            lambda2 = self.common_randomness()
            return lambda1, lambda2
        if sharingserver == "2":
            lambda1 = self.common_randomness()
            return lambda1

    def online_share(self, sharingserver: int, lambda1: bitarray, lambda2: bitarray, message: bitarray) -> bitarray:
        if sharingserver == "0":
            m = self.__mess_prev.prevp_receive()
            while m != None:
                m = self.__mess_prev.prevp_receive()
        
        if sharingserver == "1":
            m = lambda1 ^ lambda2 ^ message
            self.__mess_next.nextp_send(m)

        if sharingserver == "2":
            m = self.__mess_next.nextp_receive()
            while m != None:
                m = self.__mess_next.nextp_receive()
        
        return m


class Server2(Server):
    def __init__(self, initRandom20, initRandom21, initRandomCommon, mess_prev: Messenger, mess_next: Messenger) -> None:
        self.__L = [[], [], [], []]
        self.__initRandom20 = initRandom20
        self.__initRandom21 = initRandom21
        self.__initRandomCommon = initRandomCommon
        self.__mess_prev = mess_prev
        self.__mess_next = mess_next

    def id(self):
        return 2 
    
    def OR(self, a, b):
        return [a[0] ^ b[0]]

    def nextp_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandom20))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom20 = x
        return x

    def prevp_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandom21))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom21 = x
        return x

    def common_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandomCommon))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandomCommon = x
        return x

    def offline_AND(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c2 = self.nextp_randomness(1)
        self.__L[2].append(lambda_c2)

        # receive g2 from Server0
        g2 = self.__mess_next.nextp_receive()
        while g2 != None:
            g2 = self.__mess_next.nextp_receive()
        
        self.__L[3].append(g2)
        
        return lambda_c2

    def offline_AND1(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c2 = self.nextp_randomness(1)
        self.__L[2].append(lambda_c2)

        # receive g2 from Server0
        g2 = self.__mess_next.nextp_receive()
        while g2 != None:
            g2 = self.__mess_next.nextp_receive()
        
        self.__L[3].append(g2)
        
        return [lambda_c2]

    def online_AND(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))
        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)

        m2 = (a & b) ^ (a & temp1) ^ (b & temp2) ^ temp3 ^ temp4

        # Send m2 to Server1
        self.__mess_prev.prevp_send(m2)

        # Receive m1 from Server1
        m1 = self.__mess_prev.prevp_receive()
        while m1 != None:
            m1 = self.__mess_prev.prevp_receive()

        return m1 ^ m2
    
    def offline_share(self, sharingserver: int):
        if sharingserver == "0":
            lambda2 = self.nextp_randomness(1)
            return lambda2
        if sharingserver == "1":
            lambda2 = self.common_randomness()
            return lambda2
        if sharingserver == "2":
            lambda1 = self.common_randomness()
            lambda2 = self.nextp_randomness(1)
            return lambda1, lambda2

    def online_share(self, sharingserver: int, lambda1: bitarray, lambda2: bitarray, message: bitarray) -> bitarray:
        if sharingserver == "0":
            m = self.__mess_next.nextp_receive()
            while m != None:
                m = self.__mess_next.nextp_receive()
        if sharingserver == "1":
            m = self.__mess_prev.prevp_receive()
            while m != None:
                m = self.__mess_prev.prevp_receive()
        if sharingserver == "2":
            m = lambda1 + lambda2 + message
        return m