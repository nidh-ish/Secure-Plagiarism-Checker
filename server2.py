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
        # if self.__Q01.qsize() >= 2:
        #     print("   prevp", self.__Q01.qsize(), end="")
        
    # S1 calls to send message to S0
    def prevp_send(self, m):
        self.__Q10.put(m)
        # if self.__Q10.qsize() >= 2:
        #     print("   prevp", self.__Q10.qsize(), end="")

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

    def printQueuesStatus(self):
        print(self.__Q01.qsize(), self.__Q10.qsize())

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
    def online_AND1(self):
        pass
    def offline_share(self):
        pass
    def online_share(self):
        pass    
    def online_reconstruction(self):
        pass
    def OR(self):
        pass
    def printMessengers(self):
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
    def nextp_randomnessF(self, len: int):
        pass
    def prevp_randomnessF(self, len: int) -> bitarray:
        pass
    def common_randomnessF(self, len: int) -> bitarray:
        pass
    def offline_ANDF(self, a: bitarray, b: bitarray):
        pass
    def online_ANDF(self, a: bitarray, b: bitarray):
        pass
    def online_reconstructionF(self, lambda1: bitarray, lambda2: bitarray):
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
        self.__initRandom01 = initRandom01
        self.__initRandom02 = initRandom02
        self.__initRandomCommon = initRandomCommon
        self.messenger_prev = mess_prev
        self.messenger_next = mess_next
        self.P = 7

    def id(self):
        return 0
    
    def find_additive_inverse(self, a: bitarray) -> bitarray:
        a = ba2int(a)
        p = 2**self.P - 1  
        additive_inverse = p - a
        additive_inverse = int2ba(additive_inverse, length=self.P)
        return additive_inverse
    
    # Calculate a + b in F
    def addF(self, a: bitarray, b: bitarray):
        a = ba2int(a)
        b = ba2int(b)
        temp = a+b
        p = 2**self.P - 1
        temp = temp % p
        temp = int2ba(temp, length=self.P)
        return temp
    
    # Calculate a*b in F
    def multiplyF(self, a: bitarray, b: bitarray):
        a = ba2int(a)
        b = ba2int(b)
        temp = a*b
        p = 2**self.P - 1
        temp = temp % p
        temp = int2ba(temp, length=self.P)
        return temp
    
    # Calculate b - a in F
    def subtractF(self, a: bitarray, b: bitarray) -> bitarray:
        p = 2**self.P - 1  
        temp = ba2int(self.find_additive_inverse(a))
        b = ba2int(b)
        c = (temp+b)%p
        c = int2ba(c, length=self.P)
        return c

    def nextp_randomnessF(self, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandom01))
        x = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
        self.__initRandom01 = x
        temp = ba2int(x[0:len])
        p = 2**self.P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def prevp_randomnessF(self, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandom02))
        x = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
        self.__initRandom02 = x
        temp = ba2int(x[0:len])
        p = 2**self.P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def common_randomnessF(self, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandomCommon))
        x = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
        self.__initRandomCommon = x
        temp = ba2int(x[0:len])
        p = 2**self.P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp
    
    def offline_ANDF(self, a: bitarray, b: bitarray):
        lambda_c1 = self.nextp_randomnessF(self.P)
        g1 = self.nextp_randomnessF(self.P)
        lambda_c2 = self.prevp_randomnessF(self.P)
        temp = self.multiplyF(a, b)
        g2 = self.subtractF(g1, temp)

        # Send g2 to Server2
        self.messenger_prev.prevp_send(g2)

        temp = self.addF(lambda_c1, lambda_c2)

        return temp, lambda_c1, lambda_c2
    
    def online_reconstructionF(self, lambda1: bitarray, lambda2: bitarray) -> bitarray:
        self.messenger_next.nextp_send(lambda2)
        self.messenger_prev.prevp_send(lambda1)

        m = self.messenger_next.nextp_receive()
        while m == None:
            m = self.messenger_next.nextp_receive()

        lambdam = self.addF(lambda1, lambda2)

        return self.subtractF(lambdam, m)

    def offline_generateRandomShare(self, L:int) -> tuple[bitarray, bitarray]:
        lambda1 = self.nextp_randomness(L)
        lambda2 = self.prevp_randomness(L)
        return (lambda1, lambda2)

class Server1(Server):
    def __init__(self, initRandom10, initRandom12, initRandomCommon, mess_prev: Messenger, mess_next: Messenger) -> None:
        self.__L = [[], [], [], [], []]
        self.__initRandom10 = initRandom10
        self.__initRandom12 = initRandom12
        self.__initRandomCommon = initRandomCommon
        self.messenger_prev = mess_prev
        self.messenger_next = mess_next
        self.P = 7

    def id(self):
        return 1
    
    def find_additive_inverse(self, a: bitarray) -> bitarray:
        a = ba2int(a)
        p = 2**self.P - 1  
        additive_inverse = p - a
        additive_inverse = int2ba(additive_inverse, length=self.P)
        return additive_inverse
    
    # Calculate a + b in F
    def addF(self, a: bitarray, b: bitarray):
        a = ba2int(a)
        b = ba2int(b)
        temp = a+b
        p = 2**self.P - 1
        temp = temp % p
        temp = int2ba(temp, length=self.P)
        return temp
    
    # Calculate a*b in F
    def multiplyF(self, a: bitarray, b: bitarray):
        a = ba2int(a)
        b = ba2int(b)
        temp = a*b
        p = 2**self.P - 1
        temp = temp % p
        temp = int2ba(temp, length=self.P)
        return temp
    
    # Calculate b - a in F
    def subtractF(self, a: bitarray, b: bitarray) -> bitarray:
        p = 2**self.P - 1  
        temp = ba2int(self.find_additive_inverse(a))
        b = ba2int(b)
        c = (temp+b)%p
        c = int2ba(c, length=self.P)
        return c
    
    def nextp_randomnessF(self, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandom12))
        x = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
        self.__initRandom12 = x
        temp = ba2int(x[0:len])
        p = 2**self.P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def prevp_randomnessF(self, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandom10))
        x = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
        self.__initRandom10 = x
        temp = ba2int(x[0:len])
        p = 2**self.P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def common_randomnessF(self, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandomCommon))
        x = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
        self.__initRandomCommon = x
        temp = ba2int(x[0:len])
        p = 2**self.P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp
    
    def offline_ANDF(self, a: bitarray, b: bitarray):
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c1 = self.prevp_randomnessF(self.P)
        self.__L[2].append(lambda_c1)

        g1 = self.prevp_randomnessF(self.P)
        self.__L[3].append(g1)
        return lambda_c1

    def online_ANDF(self, a: bitarray, b: bitarray):

        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)

        m1temp1 = self.subtractF(self.multiplyF(a, temp1), bitarray("0"*self.P))
        m1temp2 = self.subtractF(self.multiplyF(b, temp2), m1temp1)
        m1temp3 = self.addF(m1temp2, temp3)
        m1 = self.addF(m1temp3, temp4)

        # Send m1 to Server2
        self.messenger_next.nextp_send(m1)

        # Receive m2 from Server2
        m2 = self.messenger_next.nextp_receive()
        while m2 == None:
            m2 = self.messenger_next.nextp_receive()

        return self.addF(m1, m2)
    
    def online_reconstructionF(self, lambda1: bitarray, m: bitarray) -> bitarray:
        self.messenger_prev.prevp_send(m)

        lambda2 = self.messenger_prev.prevp_receive()
        while lambda2 == None:
            lambda2 = self.messenger_prev.prevp_receive()

        lambdam = self.addF(lambda1, lambda2)

        return self.subtractF(lambdam, m)

    def offline_generateRandomShare(self, L:int) -> bitarray:
        lambda1 = self.prevp_randomness(L)
        return lambda1
    
    def online_generateRandomShare(self, L:int) -> bitarray:
        m = self.nextp_randomness(L)
        return m

class Server2(Server):
    def __init__(self, initRandom20, initRandom21, initRandomCommon, mess_prev: Messenger, mess_next: Messenger) -> None:
        self.__L = [[], [], [], [], []]
        self.__initRandom20 = initRandom20
        self.__initRandom21 = initRandom21
        self.__initRandomCommon = initRandomCommon
        self.messenger_prev = mess_prev
        self.messenger_next = mess_next
        self.P = 7

    def id(self):
        return 2 
    
    def find_additive_inverse(self, a: bitarray) -> bitarray:
        a = ba2int(a)
        p = 2**self.P - 1  
        additive_inverse = p - a
        additive_inverse = int2ba(additive_inverse, length=self.P)
        return additive_inverse
    
    # Calculate a + b in F
    def addF(self, a: bitarray, b: bitarray):
        a = ba2int(a)
        b = ba2int(b)
        temp = a+b
        p = 2**self.P - 1
        temp = temp % p
        temp = int2ba(temp, length=self.P)
        return temp
    
    # Calculate a*b in F
    def multiplyF(self, a: bitarray, b: bitarray):
        a = ba2int(a)
        b = ba2int(b)
        temp = a*b
        p = 2**self.P - 1
        temp = temp % p
        temp = int2ba(temp, length=self.P)
        return temp
    
    # Calculate b - a in F
    def subtractF(self, a: bitarray, b: bitarray) -> bitarray:
        p = 2**self.P - 1  
        temp = ba2int(self.find_additive_inverse(a))
        b = ba2int(b)
        c = (temp+b)%p
        c = int2ba(c, length=self.P)
        return c
    
    def nextp_randomnessF(self, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandom20))
        x = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
        self.__initRandom20 = x
        temp = ba2int(x[0:len])
        p = 2**self.P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def prevp_randomnessF(self, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandom21))
        x = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
        self.__initRandom21 = x
        temp = ba2int(x[0:len])
        p = 2**self.P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def common_randomnessF(self, len: int) -> bitarray:
        random.seed(ba2int(self.__initRandomCommon))
        x = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
        self.__initRandomCommon = x
        temp = ba2int(x[0:len])
        p = 2**self.P-1
        temp = temp%p
        temp = int2ba(temp, length=len)
        return temp

    def offline_ANDF(self, a: bitarray, b: bitarray):
        self.__L[0].append(a)
        self.__L[1].append(b)

        lambda_c2 = self.nextp_randomnessF(self.P)
        self.__L[2].append(lambda_c2)

        # receive g2 from Server0
        g2 = self.messenger_next.nextp_receive()
        while g2 == None:
            g2 = self.messenger_next.nextp_receive()
        
        self.__L[3].append(g2)
        
        return lambda_c2

    def online_ANDF(self, a: bitarray, b: bitarray):
        temp1 = self.__L[1].pop(0)
        temp2 = self.__L[0].pop(0)
        temp3 = self.__L[2].pop(0)
        temp4 = self.__L[3].pop(0)

        m2temp1 = self.subtractF(self.multiplyF(a, temp1), self.multiplyF(a, b))
        m2temp2 = self.subtractF(self.multiplyF(b, temp2), m2temp1)
        m2temp3 = self.addF(m2temp2, temp3)
        m2 = self.addF(m2temp3, temp4)

        # Send m2 to Server1
        self.messenger_prev.prevp_send(m2)

        # Receive m1 from Server1
        m1 = self.messenger_prev.prevp_receive()
        while m1 == None:
            m1 = self.messenger_prev.prevp_receive()

        return self.addF(m1, m2)
    
    def online_reconstructionF(self, lambda2: bitarray, m: bitarray) -> bitarray:
        lambda1 = self.messenger_next.nextp_receive()
        while lambda1 == None:
            lambda1 = self.messenger_next.nextp_receive()

        lambdam = self.addF(lambda1, lambda2)

        return self.subtractF(lambdam, m)
    
    def offline_generateRandomShare(self, L:int) -> bitarray:
        lambda2 = self.nextp_randomness(L)
        return lambda2
    
    def online_generateRandomShare(self, L:int) -> bitarray:
        m = self.prevp_randomness(L)
        return m

def TestANDF(a: list[bitarray], b: list[bitarray], S: Server0 | Server1 | Server2):
    if S.id() == 0:
        out = S.offline_ANDF(S.addF(a[0], a[1]), S.addF(b[0], b[1]))
        lam = out[0]
        lam1 = out[1]
        lam2 = out[2]
        output = S.online_reconstructionF(lam1, lam2)
        print("0", lam1, lam2)
        print("0", output, ba2int(output))
    elif S.id() == 1:
        offout = S.offline_ANDF(a[0], b[0])
        onlout = S.online_ANDF(a[1], b[1])
        output = S.online_reconstructionF(offout, onlout)
        print("1", offout, onlout)
        print("1", output, ba2int(output))
    elif S.id() == 2:
        offout = S.offline_ANDF(a[0], b[0])
        onlout = S.online_ANDF(a[1], b[1])
        output = S.online_reconstructionF(offout, onlout)
        print("2", offout, onlout)
        print("2", output, ba2int(output))
    


if __name__ == "__main__":
    
    # Messenger between Server0 and Server1
    M01 = Messenger()
    # Messenger between Server0 and Server2
    M02 = Messenger()
    # Messenger between Server1 and Server2
    M12 = Messenger()

    # Generate random value for Server0 and Server1
    r01 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))

    # Generate random value for Server0 and Server2
    r02 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))

    # Generate random value for Server1 and Server2
    r12 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))

    # Generate random value for Server0, Server1, and Server2
    r_common = bitarray(bin(random.getrandbits(128))[2:].zfill(128))

    # Instantiate the servers
    S0 = Server0(r01, r02, r_common, M02, M01)
    S1 = Server1(r01, r12, r_common, M01, M12)
    S2 = Server2(r02, r12, r_common, M12, M02)

    l1 = bitarray(bin(random.getrandbits(128))[2:].zfill(7))
    l2 = bitarray(bin(random.getrandbits(128))[2:].zfill(7))
    inp = bitarray("1011011")
    m = int2ba((ba2int(inp) + ba2int(l1) + ba2int(l2))%(2**7-1), length=7)   

    k1 = bitarray(bin(random.getrandbits(128))[2:].zfill(7))
    k2 = bitarray(bin(random.getrandbits(128))[2:].zfill(7))
    sk = bitarray("0101001")
    mk = int2ba((ba2int(sk) + ba2int(k1) + ba2int(k2))%(2**7-1), length=7)

    manager = multiprocessing.Manager()
    d = manager.dict()

    s0 = Share()
    s1 = Share()
    s2 = Share()

    p0 = multiprocessing.Process(target=TestANDF, args=([l1, l2], [k1, k2], S0,))
    p1 = multiprocessing.Process(target=TestANDF, args=([l1, m], [k1, mk], S1))
    p2 = multiprocessing.Process(target=TestANDF, args=([l2, m], [k2, mk], S2))

    p0.start()
    p1.start()
    p2.start()

    p0.join()
    p1.join()
    p2.join()

    # out0 = o0.getShares()
    # out1 = o1.getShares()
    # out2 = o2.getShares()

    # print(out0)

    # o0 = s0.get()
    # o1 = s1.get()
    # o2 = s2.get()


    # print("AES input: ", ba2hex(inp))
    # print("AES key: ", ba2hex(sk))
    # print("AES output: ", ba2hex(o0[0] ^ o0[1] ^ o1[1]))
    # Run the online phase 