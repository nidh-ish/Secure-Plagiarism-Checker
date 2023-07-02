from server import *

# class ArrayOutput:
#     def __init__(self) -> None:
#         self.__list = multiprocessing.Queue()
    
#     def put(self, a: list[Share]) -> None:
#         self.__list.put(a)
    
#     def get(self) -> list[Share]:
#         x = self.__list.get()
#         self.__list.put(x)
#         return x

# class ArrayOutput:
#     def __init__(self) -> None:
#         self.__list = [0, 1]

#     def add(self, a: list[Share]) -> None:
#         self.__list.insert(0, a )
        
#     def retreive(self) -> list[Share]:
#         temp = self.__list
#         print(temp)
#         return temp

class encryptedFingerprintOutput:
    def __init__(self) -> None:
        self.__list = multiprocessing.Queue()

    def addShare(self, a: Share) -> None:
        self.__list.put(a)

    def getShares(self) -> list[Share]:
        temp = []
        while self.__list.empty() != True:
            i = self.__list.get()
            temp.append(i)
        for i in temp:
            self.__list.put(i)
        print(temp)
        return temp

def getSharesfromFile(f) -> list[Share]:
    line = f.readline()
    shares = []
    while line:
        s = Share()
        x = line.split(" ")
        s.add(bitarray(x[0]))
        s.add(bitarray(x[1]))
        shares.append(s)
        line = f.readline()
    return shares

class Shuffle:
    def __init__(self) -> None:
        pass

    def permute(self, A: list[bitarray], P: list[int]) -> list[bitarray]:
        n = len(P)
        for i in range(n):
            next = i
            while (P[next] >= 0):
                
                t = A[i]
                A[i] = A[P[next]]
                A[P[next]] = t
                
                temp = P[next]
                P[next] -= n
                next = temp
        return A

    def getrandompermutation(self, L):
        l1 = [i for i in range(L)]
        random.shuffle(l1)
        return l1
    
    def ArrayXOR(self, A: list[list[bitarray]]) -> list[bitarray]:
        outputArray = []
        for i in range(len(A[0])):
            output = bitarray("0"*128)
            for j in range(len(A)):
                output = output ^ A[j][i]
            outputArray.append(output)
        return outputArray

    def ArrayPrint(self, A: list[bitarray]):
        temp = []
        for i in A:
            temp.append(ba2hex(i))
        print(temp)
    
    def helper(self, Input: list[Share], S: Server, Serveri: int, Serverj: int, P: list[int], output: encryptedFingerprintOutput) -> None:
        L = len(Input)
        
        # Server 0's code
        if S.id() == 0:
        #Offline begins
            alpha = []
            beta = []
            lambdaIn1 = []
            lambdaIn2 = []
            lambdaOut1 = []
            lambdaOut2 = []

            for i in range(L):
                shares = Input[i].get()
                lambdaIn1.append(shares[0])
                lambdaIn2.append(shares[1])

            # Generate lambdaOut1 and lambdaOut2
            for _ in range(L):
                lambdaOut1.append(S.nextp_randomness(128))
            for _ in range(L):
                lambdaOut2.append(S.prevp_randomness(128))

            # Generate alpha and beta
            if Serveri == 0:
                if Serverj == 1:
                    for _ in range(L):
                        temp = S.nextp_randomness(128)
                        alpha.append(temp)
                        beta.append(bitarray("0"*128) ^ temp)
                if Serverj == 2:
                    for _ in range(L):
                        temp = S.prevp_randomness(128)
                        alpha.append(temp)
                        beta.append(bitarray("0"*128) ^ temp)

        #Online begins
            if Serveri == 0 and Serverj == 1:
                temp1 = self.permute(lambdaIn2.copy())
                
                mOutS2 = self.ArrayXOR([temp1, lambdaOut2, beta])

                S2messenger = S.getprevmessenger()
                S2messenger.prevp_send(mOutS2)

            if Serveri == 0 and Serverj == 2:
                temp1 = self.permute(lambdaIn1.copy())
                
                mOutS1 = self.ArrayXOR([temp1, lambdaOut1, beta])

                S1messenger = S.getnextmessenger()
                S1messenger.nextp_send(mOutS1)

            for i in range(L):
                share = Share()
                share.add(lambdaOut1[i])
                share.add(lambdaOut2[i])
                output.addShare(share)
            

        # Server 1's code
        if S.id() == 1:
        #Offline begins
            alpha = []
            lambdaIn1 = []
            mIn = []
            lambdaOut1 = []
            mOut = []

            for i in range(L):
                shares = Input[i].get()
                lambdaIn1.append(shares[0])
                mIn.append(shares[1])
                
            # Generate lambdaOut1
            for _ in range(L):
                lambdaOut1.append(S.prevp_randomness(128))
                
            # Generate alpha
            if Serveri == 0 and Serverj == 1:
                for _ in range(L):
                    temp = S.prevp_randomness(128)
                    alpha.append(temp)

        #Online begins
            if Serveri == 0 and Serverj == 1:
                temp1 = self.permute(lambdaIn1.copy())
                temp2 = self.permute(mIn.copy())
                mOutS1 = self.ArrayXOR([temp1, lambdaOut1, temp2, alpha])

                S2messenger = S.getnextmessenger()
                S2messenger.nextp_send(mOutS1)
                
                mOutS2 = S2messenger.nextp_receive()
                while mOutS2 == None:
                    mOutS2 = S2messenger.nextp_receive()
                mOut = self.ArrayXOR([mOutS1, mOutS2])

            if Serveri == 0 and Serverj == 2:
                S0messenger = S.getprevmessenger()
                S2messenger = S.getnextmessenger()
                
                mOutS1 = S0messenger.prevp_receive()
                while mOutS1 == None:
                    mOutS1 = S0messenger.prevp_receive()

                S2messenger.nextp_send(mOutS1)

                mOutS2 = S2messenger.nextp_receive()
                while mOutS2 == None:
                    mOutS2 = S2messenger.nextp_receive()
                mOut = self.ArrayXOR([mOutS1, mOutS2])

            if Serveri == 1 and Serverj == 2:
                temp1 = self.permute(lambdaIn1.copy(), P)
                temp2 = self.permute(mIn.copy(), P)
                mOutS1 = self.ArrayXOR([temp1, lambdaOut1.copy(), temp2])

                S2messenger = S.getnextmessenger()
                S2messenger.nextp_send(mOutS1)
                
                mOutS2 = S2messenger.nextp_receive()
                while mOutS2 == None:
                    mOutS2 = S2messenger.nextp_receive()
                mOut = self.ArrayXOR([mOutS1, mOutS2])
                
            for i in range(L):
                share = Share()
                share.add(lambdaOut1[i])
                share.add(mOut[i])
                output.addShare(share)
            

        # Server 2's code
        if S.id() == 2:
        #Offline begins
            alpha = []
            lambdaIn2 = []
            mIn = []
            lambdaOut2 = []
            mOut = []

            for i in range(L):
                shares = Input[i].get()
                lambdaIn2.append(shares[0])
                mIn.append(shares[1])

            # Generate lambdaOut2
            for _ in range(L):
                lambdaOut2.append(S.nextp_randomness(128))
            
            # Generate alpha
            if Serveri == 0 and Serverj == 2:
                for _ in range(L):
                    temp = S.nextp_randomness(128)
                    alpha.append(temp)
        
        #Online begins
            if Serveri == 0 and Serverj == 1:
                S0messenger = S.getnextmessenger()
                S1messenger = S.getprevmessenger()

                mOutS2 = S0messenger.nextp_receive()
                while mOutS2 == None:
                    mOutS2 = S0messenger.nextp_receive()

                S1messenger.prevp_send(mOutS2)

                mOutS1 = S1messenger.prevp_receive()
                while mOutS1 == None:
                    mOutS1 = S1messenger.prevp_receive()
                mOut = self.ArrayXOR([mOutS1, mOutS2])
                
            if Serveri == 0 and Serverj == 2:
                temp1 = self.permute(lambdaIn2.copy())
                temp2 = self.permute(mIn.copy())
                mOutS2 = self.ArrayXOR([temp1, lambdaOut2, temp2, alpha])

                S1messenger = S.getprevmessenger()
                S1messenger.prevp_send(mOutS2)
                
                mOutS1 = S1messenger.prevp_receive()
                while mOutS1 == None:
                    mOutS1 = S1messenger.prevp_receive()
                mOut = self.ArrayXOR([mOutS1, mOutS2])
                
            if Serveri == 1 and Serverj == 2:
                temp1 = self.permute(lambdaIn2.copy(), P)
                mOutS2 = self.ArrayXOR([temp1, lambdaOut2.copy()])

                S1messenger = S.getprevmessenger()
                S1messenger.prevp_send(mOutS2)
                                
                mOutS1 = S1messenger.prevp_receive()
                while mOutS1 == None:
                    mOutS1 = S1messenger.prevp_receive()
                mOut = self.ArrayXOR([mOutS1, mOutS2])

            for i in range(L):
                share = Share()
                share.add(lambdaOut2[i])
                share.add(mOut[i])
                output.addShare(share)

        # output.put(Output)
    
if __name__ == "__main__":
    shuffle = Shuffle()

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

    
    file0 = open("Client1_Server0.dat", "r")
    f0 = getSharesfromFile(file0)
    file0.close()
    file1 = open("Client1_Server1.dat", "r")
    f1 = getSharesfromFile(file1)
    file1.close()
    file2 = open("Client1_Server2.dat", "r")
    f2 = getSharesfromFile(file2)
    file2.close()

    permutation = shuffle.getrandompermutation(10)
    # out0 = ArrayOutput()
    # out1 = ArrayOutput()
    # out2 = ArrayOutput()
    out0 = encryptedFingerprintOutput()
    out1 = encryptedFingerprintOutput()
    out2 = encryptedFingerprintOutput()

    p0 = multiprocessing.Process(target=shuffle.helper, args=(f0, S0, 1, 2, permutation, out0))
    p1 = multiprocessing.Process(target=shuffle.helper, args=(f1, S1, 1, 2, permutation, out1))
    p2 = multiprocessing.Process(target=shuffle.helper, args=(f2, S2, 1, 2, permutation, out2))

    p0.start()
    p1.start()
    p2.start()
    p0.join()
    p1.join()
    p2.join()
    output0 = out0.getShares()
    output1 = out1.getShares()
    output2 = out2.getShares()
    print1 = []
    print2 = []
    for i in range(len(f0)):
        x = output1[i].get()
        y = output2[i].get()
        print1.append(ba2hex(x[0] ^ x[1] ^ y[0]))

    
    for i in range(len(f0)):
        x = output0[i].get()
        y = output1[i].get()
        print2.append(ba2hex(x[0] ^ x[1] ^ y[1]))

    print(print1)
    print(print2)