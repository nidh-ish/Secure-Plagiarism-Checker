import random
import multiprocessing
from bitarray import bitarray
from bitarray.util import *

class Messenger:
    def __init__(self):
        self.__Q01 = multiprocessing.Queue()
        self.__Q10 = multiprocessing.Queue()

    # S0 calls to send message to S1
    def nextp_send(self, m):
        self.__Q01.put(m)
        
    # S1 calls to send message to S0
    def prevp_send(self, m):
        self.__Q10.put(m)

    # S0 calls to receive message from S1
    def nextp_receive(self):
        if not self.__Q10.empty():
            x = self.__Q10.get()
            return x
        return None

    # S0 calls to receive message from S1
    def prevp_receive(self):
        if not self.__Q01.empty():
            x = self.__Q01.get()
            return x
        return None

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
    def complete_optimised_offline(self):
        pass
    def flush_optimization(self):
        pass
    def online_AND(self):
        pass
    def online_AND1(self):
        pass
    def complete_optimised_online(self):
        pass
    def offline_share(self):
        pass
    def online_share(self):
        pass    
    def online_reconstruction(self):
        pass
    def OR(self):
        pass
    def getnextmessenger(self) -> Messenger:
        pass
    def getprevmessenger(self) -> Messenger:
        pass
    def offline_generateRandomShare(self):
        pass
    def online_generateRandomShare(self):
        pass
    def getList(self):
        pass
    def find_additive_inverse(self, P: int, a: bitarray):
        pass
    def addF(self, P: int, a: bitarray, b: bitarray):
        pass
    def multiplyF(self, P: int, a: bitarray, b: bitarray):
        pass
    def subtractF(self, P: int, a: bitarray, b: bitarray) -> bitarray:
        pass
    def nextp_randomnessF(self, P: int, len: int):
        pass
    def prevp_randomnessF(self, P: int, len: int) -> bitarray:
        pass
    def common_randomnessF(self, P: int, len: int) -> bitarray:
        pass
    def offline_ANDF(self, P: int, a: bitarray, b: bitarray):
        pass
    def online_ANDF(self, P: int, a: bitarray, b: bitarray):
        pass
    def online_reconstructionF(self, P: int, lambda1: bitarray, lambda2: bitarray):
        pass
    def offline_generateRandomShareF(self, P: int, L:int) -> bitarray:
        pass
    def online_generateRandomShareF(self, P: int, L:int) -> bitarray:
        pass
    def offline_shareF(self):
        pass
    def online_shareF(self):
        pass
    
class Share:
    def __init__(self) -> None:
        self.__list = multiprocessing.Queue()

    def add(self, m: bitarray):
        self.__list.put(m)
    
    def get(self) -> list[bitarray]:
        a = self.__list.get()
        b = self.__list.get()
        self.__list.put(a)
        self.__list.put(b)
        return [a, b]
    
    def flush(self):
        self.__list = multiprocessing.Queue()

class Server0(Server):
    def __init__(self, initRandom01, initRandom02, initRandomCommon, mess_prev: Messenger, mess_next: Messenger) -> None:
        self.__L = [[], [], [], [], []]
        self.__Sh = [[], []]
        self.__initRandom01 = initRandom01
        self.__initRandom02 = initRandom02
        self.__initRandomCommon = initRandomCommon
        self.messenger_prev = mess_prev
        self.messenger_next = mess_next
        self.timestamps = multiprocessing.Queue()

    def id(self):
        return 0
    
    # gcd of a and b
    def extended_gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a, 1, 0
        else:
            d, x, y = self.extended_gcd(b, a % b)
            return d, y, x - (a // b) * y

    # multiplicative inverse of a
    def find_multiplicative_inverse(self, P:int, a: bitarray) -> bitarray:
        a = ba2int(a)
        l = P
        p = 2**l - 1
        gcd, u, _ = self.extended_gcd(a, p)
        if gcd != 1:
            raise ValueError("Element has no inverse.")
        inverse = u % p
        inverse = int2ba(inverse, length=P)
        return inverse
    
    # additive inverse of a
    def find_additive_inverse(self, P: int, a: bitarray) -> bitarray:
        a = ba2int(a)
        p = 2**P - 1  
        additive_inverse = p - a
        additive_inverse = int2ba(additive_inverse, length=P)
        return additive_inverse
    
    # Calculate a + b in F
    def addF(self, P: int, a: bitarray, b: bitarray):
        a = ba2int(a)
        b = ba2int(b)
        temp = a+b
        p = 2**P - 1
        temp = temp % p
        temp = int2ba(temp, length=P)
        return temp
    
    # Calculate a*b in F
    def multiplyF(self, P: int, a: bitarray, b: bitarray):
        a = ba2int(a)
        b = ba2int(b)
        temp = a*b
        p = 2**P - 1
        temp = temp % p
        temp = int2ba(temp, length=P)
        return temp
    
    # Calculate b - a in F
    def subtractF(self, P: int, a: bitarray, b: bitarray) -> bitarray:
        p = 2**P - 1  
        temp = ba2int(self.find_additive_inverse(P, a))
        b = ba2int(b)
        c = (temp+b)%p
        c = int2ba(c, length=P)
        return c

    def nextp_randomnessF(self, P: int, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandom01))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom01 = x
        temp = ba2int(x[0:len])
        p = 2**P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def prevp_randomnessF(self, P: int, len: int):
        random.seed(ba2int(self.__initRandom02))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom02 = x
        temp = ba2int(x[0:len])
        p = 2**P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def common_randomnessF(self, P: int, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandomCommon))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandomCommon = x
        temp = ba2int(x[0:len])
        p = 2**P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp
    
    def offline_ANDF(self, P: int, a: bitarray, b: bitarray):
        lambda_c1 = self.nextp_randomnessF(P, P)
        g1 = self.nextp_randomnessF(P, P)
        lambda_c2 = self.prevp_randomnessF(P, P)
        temp = self.multiplyF(P, a, b)
        g2 = self.subtractF(P, g1, temp)

        # Send g2 to Server2
        self.messenger_prev.prevp_send(g2)

        temp = self.addF(P, lambda_c1, lambda_c2)

        return temp, lambda_c1, lambda_c2
    
    def online_reconstructionF(self, P: int, lambda1: bitarray, lambda2: bitarray) -> bitarray:
        self.messenger_next.nextp_send(lambda2)
        self.messenger_prev.prevp_send(lambda1)

        m = self.messenger_next.nextp_receive()
        while m == None:
            m = self.messenger_next.nextp_receive()

        lambdam = self.addF(P, lambda1, lambda2)

        return self.subtractF(P, lambdam, m)

    def OR(self, a, b):
        return [a[0] ^ b[0], a[1] ^ b[1]]

    def nextp_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandom01))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom01 = x
        return x[0:len]

    def prevp_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandom02))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom02 = x
        return x[0:len]

    def common_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandomCommon))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandomCommon = x
        return x[0:len]
    
    def offline_AND(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))
        lambda_c1 = self.nextp_randomness(1)
        g1 = self.nextp_randomness(1)
        lambda_c2 = self.prevp_randomness(1)

        g2 = (a & b) ^ g1

        # Send g2 to Server2
        self.messenger_prev.prevp_send(g2)
        self.__L[3].append(g2)

        return lambda_c1 ^ lambda_c2
    
    def offline_AND1(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))

        lambda_c1 = self.nextp_randomness(1)
        g1 = self.nextp_randomness(1)
        lambda_c2 = self.prevp_randomness(1)

        g2 = (a & b) ^ g1

        # Send g2 to Server2
        self.messenger_prev.prevp_send(g2)
        self.__L[3].append(g2)

        return lambda_c1, lambda_c2

    def multibit_optimised_offline_AND(self, a, b, l):
        lambda_c1 = self.nextp_randomness(l)
        g1 = self.nextp_randomness(l)
        lambda_c2 = self.prevp_randomness(l)

        g2 = (a & b) ^ g1

        # Send g2 to Server2
        self.__L[3].append(g2)

        return lambda_c1 ^ lambda_c2
    
    def multibit_optimised_offline_AND1(self, a, b, l):

        lambda_c1 = self.nextp_randomness(l)
        g1 = self.nextp_randomness(l)
        lambda_c2 = self.prevp_randomness(l)

        g2 = (a & b) ^ g1

        # Send g2 to Server2
        self.__L[3].append(g2)

        return lambda_c1, lambda_c2
    
    def complete_optimised_offline(self):
        self.messenger_prev.prevp_send(self.__L[3].copy())
        self.__L[3] = []

    def offline_share(self, sharingserver: int):
        if sharingserver == 0:
            lambda1 = self.nextp_randomness(1)
            lambda2 = self.prevp_randomness(1)
        
        if sharingserver == 1:
            lambda1 = self.nextp_randomness(1)
            lambda2 = self.common_randomness()
        
        if sharingserver == 2:
            lambda1 = self.common_randomness()
            lambda2 = self.prevp_randomness(1)

        return lambda1, lambda2

    def online_share(self, sharingserver: int, lambda1: bitarray | None, lambda2: bitarray | None, message: bitarray | None):
        if sharingserver == 0:
            m = lambda1 ^ lambda2 ^ message
            self.messenger_next.nextp_send(m)
            self.messenger_prev.prevp_send(m)

    def online_reconstruction(self, lambda1: bitarray, lambda2: bitarray) -> bitarray:
        self.messenger_next.nextp_send(lambda2)
        self.messenger_prev.prevp_send(lambda1)

        m = self.messenger_next.nextp_receive()
        while m == None:
            m = self.messenger_next.nextp_receive()

        return lambda1 ^ lambda2 ^ m

    def online_listreconstruction(self, lambda1: list[bitarray], lambda2: list[bitarray]) -> bitarray:
        self.messenger_next.nextp_send(lambda2)
        self.messenger_prev.prevp_send(lambda1)
        m = self.messenger_next.nextp_receive()
        while m == None:
            m = self.messenger_next.nextp_receive()
        output = []
        for i in range(len(lambda2)):
            output.append(lambda1[i] ^ lambda2[i] ^ m[i])
        return output
    
    def getnextmessenger(self) -> Messenger:
        return self.messenger_next

    def getprevmessenger(self) -> Messenger:
        return self.messenger_prev

    def offline_generateRandomShare(self, L:int) -> tuple[bitarray, bitarray]:
        lambda1 = self.nextp_randomness(L)
        lambda2 = self.prevp_randomness(L)
        return (lambda1, lambda2)
    
    def offline_generateRandomShareF(self, P: int, L:int) -> tuple[bitarray, bitarray]:
        lambda1 = self.nextp_randomnessF(P, L)
        lambda2 = self.prevp_randomnessF(P, L)
        return (lambda1, lambda2)
    
    def getList(self):
        return self.__L

    def offline_shareF(self, P: int, sharingserver: int):
        if sharingserver == 0:
            lambda1 = self.nextp_randomnessF(P, P)
            lambda2 = self.prevp_randomnessF(P, P)
            return lambda1, lambda2
        
        if sharingserver == 1:
            lambda1 = self.nextp_randomnessF(P, P)
            lambda2 = self.common_randomnessF(P, P)
            return lambda1, lambda2
        
        if sharingserver == 2:
            lambda1 = self.common_randomnessF(P, P)
            lambda2 = self.prevp_randomnessF(P, P)
            return lambda1, lambda2

    def online_shareF(self, P: int, sharingserver: int, lambda1: bitarray | None, lambda2: bitarray | None, message: bitarray | None):
        if sharingserver == 0:
            tempm = self.addF(P, lambda1, lambda2)
            m = self.addF(P, tempm, message)
            self.messenger_next.nextp_send(m)
            self.messenger_prev.prevp_send(m)

    def save_for_comm(self, arr: int, val: any):
        self.__Sh[arr].append(val)

    def get_saved(self, arr: int) -> any:
        return self.__Sh[arr].pop(0)

    def store_timestamp(self, time: float, string: str):
        self.timestamps.put((string, time))

    def print_timestamp(self):
        printout = []
        while not self.timestamps.empty():
            x = self.timestamps.get()
            printout.append(x)
        print(self.id() , ": ", printout, ",")

class Server1(Server):
    def __init__(self, initRandom10, initRandom12, initRandomCommon, mess_prev: Messenger, mess_next: Messenger) -> None:
        self.__L = [[], [], [], [], []]
        self.__Sh = [[], []]
        self.__initRandom10 = initRandom10
        self.__initRandom12 = initRandom12
        self.__initRandomCommon = initRandomCommon
        self.messenger_prev = mess_prev
        self.messenger_next = mess_next
        self.timestamps = multiprocessing.Queue()

    def id(self):
        return 1
    
    # gcd of a and b
    def extended_gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a, 1, 0
        else:
            d, x, y = self.extended_gcd(b, a % b)
            return d, y, x - (a // b) * y

    # multiplicative inverse of a
    def find_multiplicative_inverse(self, P:int, a: bitarray) -> bitarray:
        a = ba2int(a)
        l = P
        p = 2**l - 1
        gcd, u, _ = self.extended_gcd(a, p)
        if gcd != 1:
            raise ValueError("Element has no inverse.")
        inverse = u % p
        inverse = int2ba(inverse, length=P)
        return inverse
    
    # additive inverse of a
    def find_additive_inverse(self, P: int, a: bitarray) -> bitarray:
        a = ba2int(a)
        p = 2**P - 1  
        additive_inverse = p - a
        additive_inverse = int2ba(additive_inverse, length=P)
        return additive_inverse
    
    # Calculate a + b in F
    def addF(self, P: int, a: bitarray, b: bitarray):
        a = ba2int(a)
        b = ba2int(b)
        temp = a+b
        p = 2**P - 1
        temp = temp % p
        temp = int2ba(temp, length=P)
        return temp
    
    # Calculate a*b in F
    def multiplyF(self, P: int, a: bitarray, b: bitarray):
        a = ba2int(a)
        b = ba2int(b)
        temp = a*b
        p = 2**P - 1
        temp = temp % p
        temp = int2ba(temp, length=P)
        return temp
    
    # Calculate b - a in F
    def subtractF(self, P: int, a: bitarray, b: bitarray) -> bitarray:
        p = 2**P - 1  
        temp = ba2int(self.find_additive_inverse(P, a))
        b = ba2int(b)
        c = (temp+b)%p
        c = int2ba(c, length=P)
        return c
    
    def nextp_randomnessF(self, P: int, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandom12))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom12 = x
        temp = ba2int(x[0:len])
        p = 2**P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def prevp_randomnessF(self, P: int, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandom10))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom10 = x
        temp = ba2int(x[0:len])
        p = 2**P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def common_randomnessF(self, P: int, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandomCommon))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandomCommon = x
        temp = ba2int(x[0:len])
        p = 2**P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp
    
    def offline_ANDF(self, P: int, a: bitarray, b: bitarray):
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c1 = self.prevp_randomnessF(P, P)
        self.__L[2].append(lambda_c1)

        g1 = self.prevp_randomnessF(P, P)
        self.__L[3].append(g1)
        return lambda_c1

    def online_ANDF(self, P: int, a: bitarray, b: bitarray):

        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)

        m1temp1 = self.subtractF(P, self.multiplyF(P, a, temp1), bitarray("0"*P))
        m1temp2 = self.subtractF(P, self.multiplyF(P, b, temp2), m1temp1)
        m1temp3 = self.addF(P, m1temp2, temp3)
        m1 = self.addF(P, m1temp3, temp4)

        # Send m1 to Server2
        self.messenger_next.nextp_send(m1)

        # Receive m2 from Server2
        m2 = self.messenger_next.nextp_receive()
        while m2 == None:
            m2 = self.messenger_next.nextp_receive()

        return self.addF(P, m1, m2)
    
    def online_reconstructionF(self, P: int, lambda1: bitarray, m: bitarray) -> bitarray:
        self.messenger_prev.prevp_send(m)

        lambda2 = self.messenger_prev.prevp_receive()
        while lambda2 == None:
            lambda2 = self.messenger_prev.prevp_receive()

        lambdam = self.addF(P, lambda1, lambda2)

        return self.subtractF(P, lambdam, m)

    def OR(self, a, b):
        return [a[0] ^ b[0]]

    def nextp_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandom12))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom12 = x
        return x[0:len]

    def prevp_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandom10))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom10 = x
        return x[0:len]

    def common_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandomCommon))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandomCommon = x
        return x[0:len]
    
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

    def multibit_optimised_offline_AND(self, a, b, l):
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c1 = self.prevp_randomness(l)
        self.__L[2].append(lambda_c1)

        g1 = self.prevp_randomness(l)
        self.__L[3].append(g1)
        return lambda_c1

    def multibit_optimised_offline_AND1(self, a, b, l):
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c1 = self.prevp_randomness(l)
        self.__L[2].append(lambda_c1)

        g1 = self.prevp_randomness(l)
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
        self.messenger_next.nextp_send(m1)

        # Receive m2 from Server2
        m2 = self.messenger_next.nextp_receive()
        while m2 == None:
            m2 = self.messenger_next.nextp_receive()

        return m1 ^ m2
    
    def online_AND1(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))
        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)

        m1 = (a & temp1) ^ (b & temp2) ^ temp3 ^ temp4

        # Send m1 to Server2
        self.messenger_next.nextp_send(m1)

        # Receive m2 from Server2
        m2 = self.messenger_next.nextp_receive()
        while m2 == None:
            m2 = self.messenger_next.nextp_receive()

        return [m1 ^ m2]
    
    def multibit_optimised_online_AND(self, a, b):
        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)

        m1 = (a & temp1) ^ (b & temp2) ^ temp3 ^ temp4

        return m1
    
    def multibit_optimised_online_AND1(self, a, b):
        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)

        m1 = (a & temp1) ^ (b & temp2) ^ temp3 ^ temp4

        return [m1]
    
    def complete_optimised_online(self, m1: list[bitarray]) -> list[bitarray]:
        # send m2 to Server1
        self.messenger_next.nextp_send(m1)

        # receive m1 from Server0
        m2 = self.messenger_next.nextp_receive()
        while m2 == None:
            m2 = self.messenger_next.nextp_receive()

        return m2

    def offline_share(self, sharingserver: int):
        if sharingserver == 0:
            lambda1 = self.prevp_randomness(1)
            return lambda1
        if sharingserver == 1:
            lambda1 = self.prevp_randomness(1)
            lambda2 = self.common_randomness()
            return lambda1, lambda2
        if sharingserver == 2:
            lambda1 = self.common_randomness()
            return lambda1

    def online_share(self, sharingserver: int, lambda1: bitarray | None, lambda2: bitarray | None, message: bitarray | None) -> bitarray:
        if sharingserver == 0:
            m = self.messenger_prev.prevp_receive()
            while m == None:
                m = self.messenger_prev.prevp_receive()
        
        if sharingserver == 1:
            m = lambda1 ^ lambda2 ^ message
            self.messenger_next.nextp_send(m)

        if sharingserver == 2:
            m = self.messenger_next.nextp_receive()
            while m == None:
                m = self.messenger_next.nextp_receive()
        
        return m
    
    def online_reconstruction(self, lambda1: bitarray, m: bitarray) -> bitarray:
        self.messenger_prev.prevp_send(m)

        lambda2 = self.messenger_prev.prevp_receive()
        while lambda2 == None:
            lambda2 = self.messenger_prev.prevp_receive()

        return lambda1 ^ lambda2 ^ m

    def online_listreconstruction(self, lambda1: list[bitarray], m: list[bitarray]) -> bitarray:
        self.messenger_prev.prevp_send(m)

        lambda2 = self.messenger_prev.prevp_receive()
        while lambda2 == None:
            lambda2 = self.messenger_prev.prevp_receive()

        output = []
        for i in range(len(lambda2)):
            output.append(lambda1[i] ^ lambda2[i] ^ m[i])
        return output
    
    def getnextmessenger(self) -> Messenger:
        return self.messenger_next

    def getprevmessenger(self) -> Messenger:
        return self.messenger_prev

    def offline_generateRandomShare(self, L:int) -> bitarray:
        lambda1 = self.prevp_randomness(L)
        return lambda1
    
    def online_generateRandomShare(self, L:int) -> bitarray:
        m = self.nextp_randomness(L)
        return m
 
    def offline_generateRandomShareF(self, P: int, L:int) -> bitarray:
        lambda1 = self.prevp_randomnessF(P, L)
        return lambda1
    
    def online_generateRandomShareF(self, P: int, L:int) -> bitarray:
        m = self.nextp_randomnessF(P, L)
        return m   

    def getList(self):
        return self.__L

    def offline_shareF(self, P: int, sharingserver: int):
        if sharingserver == 0:
            lambda1 = self.prevp_randomnessF(P, P)
            return lambda1
        if sharingserver == 1:
            lambda1 = self.prevp_randomnessF(P, P)
            lambda2 = self.common_randomnessF(P, P)
            return lambda1, lambda2
        if sharingserver == 2:
            lambda1 = self.common_randomnessF(P, P)
            return lambda1

    def online_shareF(self, P: int, sharingserver: int, lambda1: bitarray | None, lambda2: bitarray | None, message: bitarray | None) -> bitarray:
        if sharingserver == 0:
            m = self.messenger_prev.prevp_receive()
            while m == None:
                m = self.messenger_prev.prevp_receive()
            return m
        
        if sharingserver == 1:
            tempm = self.addF(P, lambda1, lambda2)
            m = self.addF(P, tempm, message)
            self.messenger_next.nextp_send(m)
            return m

        if sharingserver == 2:
            m = self.messenger_next.nextp_receive()
            while m == None:
                m = self.messenger_next.nextp_receive()
            return m

    def save_for_comm(self, arr: int, val: any):
        self.__Sh[arr].append(val)

    def get_saved(self, arr: int) -> any:
        return self.__Sh[arr].pop(0)

    def store_timestamp(self, time: float, string: str):
        self.timestamps.put((string, time))

    def print_timestamp(self):
        printout = []
        while not self.timestamps.empty():
            x = self.timestamps.get()
            printout.append(x)
        print(self.id() , ": ", printout, ",")

class Server2(Server):
    def __init__(self, initRandom20, initRandom21, initRandomCommon, mess_prev: Messenger, mess_next: Messenger) -> None:
        self.__L = [[], [], [], [], []]
        self.__Sh = [[], []]
        self.__initRandom20 = initRandom20
        self.__initRandom21 = initRandom21
        self.__initRandomCommon = initRandomCommon
        self.messenger_prev = mess_prev
        self.messenger_next = mess_next
        self.timestamps = multiprocessing.Queue()

    def id(self):
        return 2 
    
    # gcd of a and b
    def extended_gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a, 1, 0
        else:
            d, x, y = self.extended_gcd(b, a % b)
            return d, y, x - (a // b) * y

    # multiplicative inverse of a
    def find_multiplicative_inverse(self, P:int, a: bitarray) -> bitarray:
        a = ba2int(a)
        l = P
        p = 2**l - 1
        gcd, u, _ = self.extended_gcd(a, p)
        if gcd != 1:
            raise ValueError("Element has no inverse.")
        inverse = u % p
        inverse = int2ba(inverse, length=P)
        return inverse
    
    # additive inverse of a
    def find_additive_inverse(self, P: int, a: bitarray) -> bitarray:
        a = ba2int(a)
        p = 2**P - 1  
        additive_inverse = p - a
        additive_inverse = int2ba(additive_inverse, length=P)
        return additive_inverse
    
    # Calculate a + b in F
    def addF(self, P: int, a: bitarray, b: bitarray):
        a = ba2int(a)
        b = ba2int(b)
        temp = a+b
        p = 2**P - 1
        temp = temp % p
        temp = int2ba(temp, length=P)
        return temp
    
    # Calculate a*b in F
    def multiplyF(self, P: int, a: bitarray, b: bitarray):
        a = ba2int(a)
        b = ba2int(b)
        temp = a*b
        p = 2**P - 1
        temp = temp % p
        temp = int2ba(temp, length=P)
        return temp
    
    # Calculate b - a in F
    def subtractF(self, P: int, a: bitarray, b: bitarray) -> bitarray:
        p = 2**P - 1  
        temp = ba2int(self.find_additive_inverse(P, a))
        b = ba2int(b)
        c = (temp+b)%p
        c = int2ba(c, length=P)
        return c
    
    def nextp_randomnessF(self, P: int, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandom20))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom20 = x
        temp = ba2int(x[0:len])
        p = 2**P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def prevp_randomnessF(self, P: int, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandom21))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom21 = x
        temp = ba2int(x[0:len])
        p = 2**P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def common_randomnessF(self, P: int, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandomCommon))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandomCommon = x
        temp = ba2int(x[0:len])
        p = 2**P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def offline_ANDF(self, P: int, a: bitarray, b: bitarray):
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c2 = self.nextp_randomnessF(P, P)
        self.__L[2].append(lambda_c2)

        # receive g2 from Server0
        g2 = self.messenger_next.nextp_receive()
        while g2 == None:
            g2 = self.messenger_next.nextp_receive()
        
        self.__L[3].append(g2)
        
        return lambda_c2

    def online_ANDF(self, P: int, a: bitarray, b: bitarray):
        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)
            
        m2temp1 = self.subtractF(P, self.multiplyF(P, a, temp1), self.multiplyF(P, a, b))
        m2temp2 = self.subtractF(P, self.multiplyF(P, b, temp2), m2temp1)
        m2temp3 = self.addF(P, m2temp2, temp3)
        m2 = self.addF(P, m2temp3, temp4)

        # Send m2 to Server1
        self.messenger_prev.prevp_send(m2)

        # Receive m1 from Server1
        m1 = self.messenger_prev.prevp_receive()
        while m1 == None:
            m1 = self.messenger_prev.prevp_receive()

        return self.addF(P, m1, m2)

    def online_reconstructionF(self, P: int, lambda2: bitarray, m: bitarray) -> bitarray:
        lambda1 = self.messenger_next.nextp_receive()
        while lambda1 == None:
            lambda1 = self.messenger_next.nextp_receive()

        lambdam = self.addF(P, lambda1, lambda2)

        return self.subtractF(P, lambdam, m)
    
    def OR(self, a, b):
        return [a[0] ^ b[0]]

    def nextp_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandom20))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom20 = x
        return x[0:len]

    def prevp_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandom21))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandom21 = x
        return x[0:len]

    def common_randomness(self, len) -> bitarray:
        random.seed(ba2int(self.__initRandomCommon))
        x = bitarray(bin(random.getrandbits(len))[2:].zfill(len))
        self.__initRandomCommon = x
        return x[0:len]

    def offline_AND(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c2 = self.nextp_randomness(1)
        self.__L[2].append(lambda_c2)

        # receive g2 from Server0
        g2 = self.messenger_next.nextp_receive()
        while g2 == None:
            g2 = self.messenger_next.nextp_receive()
        
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
        g2 = self.messenger_next.nextp_receive()
        while g2 == None:
            g2 = self.messenger_next.nextp_receive()
        
        self.__L[3].append(g2)
        
        return [lambda_c2]

    def multibit_optimised_offline_AND(self, a, b, l):
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c2 = self.nextp_randomness(l)
        self.__L[2].append(lambda_c2)
        
        return lambda_c2

    def multibit_optimised_offline_AND1(self, a, b, l):
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c2 = self.nextp_randomness(l)
        self.__L[2].append(lambda_c2)
        
        return [lambda_c2]

    def complete_optimised_offline(self):
        # receive g2 from Server0
        g2 = self.messenger_next.nextp_receive()
        while g2 == None:
            g2 = self.messenger_next.nextp_receive()
        self.__L[3] = g2

    def online_AND(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))
        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)

        m2 = (a & b) ^ (a & temp1) ^ (b & temp2) ^ temp3 ^ temp4

        # Send m2 to Server1
        self.messenger_prev.prevp_send(m2)

        # Receive m1 from Server1
        m1 = self.messenger_prev.prevp_receive()
        while m1 == None:
            m1 = self.messenger_prev.prevp_receive()

        return m1 ^ m2
    
    def online_AND1(self, a, b):
        a = bitarray(str(a))
        b = bitarray(str(b))
        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)

        m2 = (a & b) ^ (a & temp1) ^ (b & temp2) ^ temp3 ^ temp4

        # Send m2 to Server1
        self.messenger_prev.prevp_send(m2)

        # Receive m1 from Server1
        m1 = self.messenger_prev.prevp_receive()
        while m1 == None:
            m1 = self.messenger_prev.prevp_receive()

        return [m1 ^ m2]
    
    def multibit_optimised_online_AND(self, a, b):
        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)

        m2 = (a & b) ^ (a & temp1) ^ (b & temp2) ^ temp3 ^ temp4

        return m2
    
    def multibit_optimised_online_AND1(self, a, b):
        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)

        m2 = (a & b) ^ (a & temp1) ^ (b & temp2) ^ temp3 ^ temp4

        return [m2]
    
    def complete_optimised_online(self, m2: list[bitarray]) -> list[bitarray]:
        # send m2 to Server1
        self.messenger_prev.prevp_send(m2)

        # receive m1 from Server0
        m1 = self.messenger_prev.prevp_receive()
        while m1 == None:
            m1 = self.messenger_prev.prevp_receive()

        return m1

    def offline_share(self, sharingserver: int):
        if sharingserver == 0:
            lambda2 = self.nextp_randomness(1)
            return lambda2
        if sharingserver == 1:
            lambda2 = self.common_randomness(1)
            return lambda2
        if sharingserver == 2:
            lambda1 = self.common_randomness(1)
            lambda2 = self.nextp_randomness(1)
            return lambda1, lambda2

    def online_share(self, sharingserver: int, lambda1: bitarray | None, lambda2: bitarray | None, message: bitarray | None) -> bitarray:
        if sharingserver == 0:
            m = self.messenger_next.nextp_receive()
            while m == None:
                m = self.messenger_next.nextp_receive()
            return m
        if sharingserver == 1:
            m = self.messenger_prev.prevp_receive()
            while m == None:
                m = self.messenger_prev.prevp_receive()
            return m
        if sharingserver == 2:
            m = lambda1 ^ lambda2 ^ message
            self.messenger_next.nextp_send(m)
            return m
        
    def online_reconstruction(self, lambda2: bitarray, m: bitarray) -> bitarray:
        lambda1 = self.messenger_next.nextp_receive()
        while lambda1 == None:
            lambda1 = self.messenger_next.nextp_receive()

        return lambda1 ^ lambda2 ^ m
    
    def online_listreconstruction(self, lambda2: list[bitarray], m: list[bitarray]) -> bitarray:
        lambda1 = self.messenger_next.nextp_receive()
        while lambda1 == None:
            lambda1 = self.messenger_next.nextp_receive()

        output = []
        for i in range(len(lambda2)):
            output.append(lambda1[i] ^ lambda2[i] ^ m[i])
        return output
    
    def getnextmessenger(self) -> Messenger:
        return self.messenger_next

    def getprevmessenger(self) -> Messenger:
        return self.messenger_prev
    
    def offline_generateRandomShare(self, L:int) -> bitarray:
        lambda2 = self.nextp_randomness(L)
        return lambda2
    
    def online_generateRandomShare(self, L:int) -> bitarray:
        m = self.prevp_randomness(L)
        return m
    
    def offline_generateRandomShareF(self, P: int, L:int) -> bitarray:
        lambda2 = self.nextp_randomnessF(P, L)
        return lambda2
    
    def online_generateRandomShareF(self, P: int, L:int) -> bitarray:
        m = self.prevp_randomnessF(P, L)
        return m
    
    def getList(self):
        return self.__L

    def offline_shareF(self, P: int, sharingserver: int):
        if sharingserver == 0:
            lambda2 = self.nextp_randomnessF(P, P)
            return lambda2
        if sharingserver == 1:
            lambda2 = self.common_randomnessF(P, P)
            return lambda2
        if sharingserver == 2:
            lambda1 = self.common_randomnessF(P, P)
            lambda2 = self.nextp_randomnessF(P, P)
            return lambda1, lambda2

    def online_shareF(self, P: int, sharingserver: int, lambda1: bitarray | None, lambda2: bitarray | None, message: bitarray | None) -> bitarray:
        m = None
        if sharingserver == 0:
            m = self.messenger_next.nextp_receive()
            while m == None:
                m = self.messenger_next.nextp_receive()
            return m
        if sharingserver == 1:
            m = self.messenger_prev.prevp_receive()
            while m == None:
                m = self.messenger_prev.prevp_receive()
            return m
        if sharingserver == 2:
            tempm = self.addF(P, lambda1, lambda2)
            m = self.addF(P, tempm, message)
            self.messenger_prev.prevp_send(m)
            return m
    
    def flush_optimization(self):
        self.__L[3] = []

    def save_for_comm(self, arr: int, val: any):
        self.__Sh[arr].append(val)

    def get_saved(self, arr: int) -> any:
        return self.__Sh[arr].pop(0)

    def store_timestamp(self, time: float, string: str):
        self.timestamps.put((string, time))

    def print_timestamp(self):
        printout = []
        while not self.timestamps.empty():
            x = self.timestamps.get()
            printout.append(x)
        print(self.id() , ": ", printout, ",")