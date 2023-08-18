from server import *

def getSharesfromFileF(f) -> list[Share]:
    line = f.readline()
    shares = []
    while line:
        s = Share()
        x = line.split(" ")
        s.add(bitarray(x[0])[0:6])
        s.add(bitarray(x[1])[0:6])
        shares.append(s)
        line = f.readline()
    return shares

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

    def permute(self, A: list[bitarray], Permutation: list[int]) -> list[bitarray]:
        n = len(Permutation)
        for i in range(n):
            next = i
            while (Permutation[next] >= 0):
                
                t = A[i]
                A[i] = A[Permutation[next]]
                A[Permutation[next]] = t
                
                temp = Permutation[next]
                Permutation[next] -= n
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

    def ArrayAddF(self, P: int, A: list[bitarray], B: list[bitarray],  S: Server0 | Server1 | Server2) -> list[bitarray]:
        outputArray = []
        for i in range(len(A)):
            outputArray.append(S.addF(P, A[i], B[i]))
        return outputArray

    def ArraySubtractF(self, P: int, A: list[bitarray], B: list[bitarray],  S: Server0 | Server1 | Server2) -> list[bitarray]:
        outputArray = []
        for i in range(len(A)):
            outputArray.append(S.subtractF(P, A[i], B[i]))
        return outputArray

    def ArrayPrint(self, A: list[bitarray]):
        temp = []
        for i in A:
            temp.append(ba2hex(i))
    
    def helper(self, Input: list[Share], S: Server0 | Server1 | Server2, Serveri: int, Serverj: int, Permutation: list[int] | None) -> list[Share]:
        L = len(Input)
        Output = []
        
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
                temp1 = self.permute(lambdaIn2.copy(), Permutation.copy())
                mOutS2 = self.ArrayXOR([temp1, lambdaOut2, beta])
                S.save_for_comm(1, mOutS2)

            if Serveri == 0 and Serverj == 2:
                temp1 = self.permute(lambdaIn1.copy(), Permutation.copy())
                mOutS1 = self.ArrayXOR([temp1, lambdaOut1, beta])
                S.save_for_comm(1, mOutS1)

            for i in range(L):
                share = Share()
                share.add(lambdaOut1[i])
                share.add(lambdaOut2[i])
                Output.append(share)

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
                temp1 = self.permute(lambdaIn1.copy(), Permutation.copy())
                temp2 = self.permute(mIn.copy(), Permutation.copy())
                mOutS1 = self.ArrayXOR([temp1, lambdaOut1, temp2, alpha])
                S.save_for_comm(1, mOutS1)

            if Serveri == 1 and Serverj == 2:
                temp1 = self.permute(lambdaIn1.copy(), Permutation.copy())
                temp2 = self.permute(mIn.copy(), Permutation.copy())
                mOutS1 = self.ArrayXOR([temp1, lambdaOut1.copy(), temp2])
                S.save_for_comm(1, mOutS1)
                
            for i in range(L):
                share = Share()
                share.add(lambdaOut1[i])
                Output.append(share)

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
            if Serveri == 0 and Serverj == 2:
                temp1 = self.permute(lambdaIn2.copy(), Permutation.copy())
                temp2 = self.permute(mIn.copy(), Permutation.copy())
                mOutS2 = self.ArrayXOR([temp1, lambdaOut2, temp2, alpha])
                S.save_for_comm(1, mOutS2)
                
            if Serveri == 1 and Serverj == 2:
                temp1 = self.permute(lambdaIn2.copy(), Permutation.copy())
                mOutS2 = self.ArrayXOR([temp1, lambdaOut2.copy()])
                S.save_for_comm(1, mOutS2)

            for i in range(L):
                share = Share()
                share.add(lambdaOut2[i])
                Output.append(share)
        return Output
    
    def helperF(self, P: int ,Input: list[Share], S: Server0 | Server1 | Server2, Serveri: int, Serverj: int, Permutation: list[int] | None) -> list[Share]:
        L = len(Input)
        Output = []
        
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
                lambdaOut1.append(S.nextp_randomnessF(P, P-1))
            for _ in range(L):
                lambdaOut2.append(S.prevp_randomnessF(P, P-1))

            # Generate alpha and beta
            if Serveri == 0:
                if Serverj == 1:
                    for _ in range(L):
                        temp = S.nextp_randomnessF(P, P-1)
                        alpha.append(temp)
                        beta.append(S.find_additive_inverse(P, temp))
                if Serverj == 2:
                    for _ in range(L):
                        temp = S.prevp_randomnessF(P, P-1)
                        alpha.append(temp)
                        beta.append(S.find_additive_inverse(P, temp))

        #Online begins
            if Serveri == 0 and Serverj == 1:
                temp1 = self.permute(lambdaIn2.copy(), Permutation.copy())
                temp2 = self.ArrayAddF(P, beta, lambdaOut2, S)
                mOutS2 = self.ArraySubtractF(P, temp1, temp2, S)
                S.save_for_comm(1, mOutS2)

            if Serveri == 0 and Serverj == 2:
                temp1 = self.permute(lambdaIn1.copy(), Permutation.copy())
                temp2 = self.ArrayAddF(P, beta, lambdaOut1, S)
                mOutS1 = self.ArraySubtractF(P, temp1, temp2, S)
                S.save_for_comm(1, mOutS1)

            for i in range(L):
                share = Share()
                share.add(lambdaOut1[i])
                share.add(lambdaOut2[i])
                Output.append(share)

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
                lambdaOut1.append(S.prevp_randomnessF(P, P-1))
                
            # Generate alpha
            if Serveri == 0 and Serverj == 1:
                for _ in range(L):
                    temp = S.prevp_randomnessF(P, P-1)
                    alpha.append(temp)

        #Online begins
            if Serveri == 0 and Serverj == 1:
                temp1 = self.permute(lambdaIn1.copy(), Permutation.copy())
                temp2 = self.permute(mIn.copy(), Permutation.copy())
                temp3 = self.ArrayAddF(P, temp2, lambdaOut1, S)
                temp4 = self.ArrayAddF(P, temp3, alpha, S)
                mOutS1 = self.ArraySubtractF(P, temp1, temp4, S)
                S.save_for_comm(1, mOutS1)

            if Serveri == 1 and Serverj == 2:
                temp1 = self.permute(lambdaIn1.copy(), Permutation.copy())
                temp2 = self.permute(mIn.copy(), Permutation.copy())
                temp3 = self.ArrayAddF(P, temp2, lambdaOut1, S)
                mOutS1 = self.ArraySubtractF(P, temp1, temp3, S)
                S.save_for_comm(1, mOutS1)
                
            for i in range(L):
                share = Share()
                share.add(lambdaOut1[i])
                Output.append(share)

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
                lambdaOut2.append(S.nextp_randomnessF(P, P-1))
            
            # Generate alpha
            if Serveri == 0 and Serverj == 2:
                for _ in range(L):
                    temp = S.nextp_randomnessF(P, P-1)
                    alpha.append(temp)
        
        #Online begins
            if Serveri == 0 and Serverj == 2:
                temp1 = self.permute(lambdaIn2.copy(), Permutation.copy())
                temp2 = self.permute(mIn.copy(), Permutation.copy())
                temp3 = self.ArrayAddF(P, temp2, lambdaOut2, S)
                temp4 = self.ArrayAddF(P, temp3, alpha, S)
                mOutS2 = self.ArraySubtractF(P, temp1, temp4, S)
                S.save_for_comm(1, mOutS2)
                
            if Serveri == 1 and Serverj == 2:
                temp1 = self.permute(lambdaIn2.copy(), Permutation.copy())
                mOutS2 = self.ArraySubtractF(P, temp1, lambdaOut2, S)
                S.save_for_comm(1, mOutS2)

            for i in range(L):
                share = Share()
                share.add(lambdaOut2[i])
                Output.append(share)
        return Output
    
    def optimizeHelpers(self, P: int, S: Server0 | Server1 | Server2, Serveri: int, Serverj: int, Output: list[Share], OutputF: list[Share]):
        if S.id() == 0:
            if Serveri == 0 and Serverj == 1:
                p = S.get_saved(1)
                p2 = S.get_saved(1)
                S2messenger = S.getprevmessenger()
                S2messenger.prevp_send((p, p2))

            if Serveri == 0 and Serverj == 2:
                p = S.get_saved(1)
                p2 = S.get_saved(1)
                S1messenger = S.getnextmessenger()
                S1messenger.nextp_send((p, p2))

        if S.id() == 1:
            if Serveri == 0 and Serverj == 1:
                mOutS1 = S.get_saved(1)
                mOutS1F = S.get_saved(1)
                S2messenger = S.getnextmessenger()
                S2messenger.nextp_send((mOutS1, mOutS1F))

                mOutS = S2messenger.nextp_receive()
                while mOutS == None:
                    mOutS = S2messenger.nextp_receive()
                
                mOutS2, mOutS2F = mOutS[0] ,mOutS[1]

                mOut = self.ArrayXOR([mOutS1, mOutS2])
                mOutF = self.ArrayAddF(P, mOutS1F, mOutS2F, S)

            if Serveri == 0 and Serverj == 2:
                S0messenger = S.getprevmessenger()
                S2messenger = S.getnextmessenger()
                
                RmOutS1 = S0messenger.prevp_receive()
                while RmOutS1 == None:
                    RmOutS1 = S0messenger.prevp_receive()
                mOutS1, mOutS1F = RmOutS1[0], RmOutS1[1]

                S2messenger.nextp_send((mOutS1, mOutS1F))

                RmOutS2 = S2messenger.nextp_receive()
                while RmOutS2 == None:
                    RmOutS2 = S2messenger.nextp_receive()
                mOutS2, mOutS2F = RmOutS2[0], RmOutS2[1]
                
                mOut = self.ArrayXOR([mOutS1, mOutS2])
                mOutF = self.ArrayAddF(P, mOutS1F, mOutS2F, S)

            if Serveri == 1 and Serverj == 2:
                S2messenger = S.getnextmessenger()
                mOutS1 = S.get_saved(1)

                mOutS1F = S.get_saved(1)
                S2messenger.nextp_send((mOutS1, mOutS1F))
                
                RmOutS2 = S2messenger.nextp_receive()
                while RmOutS2 == None:
                    RmOutS2 = S2messenger.nextp_receive()
                mOutS2, mOutS2F = RmOutS2[0], RmOutS2[1]
                    
                mOutF = self.ArrayAddF(P, mOutS1F, mOutS2F, S)
                mOut = self.ArrayXOR([mOutS1, mOutS2])
                

            for i in range(len(mOut)):
                share = Output[i]
                share.add(mOut[i])
                shareF = OutputF[i]
                shareF.add(mOutF[i])
                
        if S.id() == 2:
            if Serveri == 0 and Serverj == 1:
                S0messenger = S.getnextmessenger()
                S1messenger = S.getprevmessenger()

                RmOutS2 = S0messenger.nextp_receive()
                while RmOutS2 == None:
                    RmOutS2 = S0messenger.nextp_receive()
                mOutS2, mOutS2F = RmOutS2[0], RmOutS2[1]

                S1messenger.prevp_send((mOutS2, mOutS2F))

                RmOutS1 = S1messenger.prevp_receive()
                while RmOutS1 == None:
                    RmOutS1 = S1messenger.prevp_receive()
                mOutS1, mOutS1F = RmOutS1[0], RmOutS1[1]

                mOut = self.ArrayXOR([mOutS1, mOutS2])
                mOutF = self.ArrayAddF(P, mOutS1F, mOutS2F, S)

            if Serveri == 0 and Serverj == 2:
                S1messenger = S.getprevmessenger()
                mOutS2 = S.get_saved(1)
                mOutS2F = S.get_saved(1)
                S1messenger.prevp_send((mOutS2, mOutS2F))

                RmOutS1 = S1messenger.prevp_receive()
                while RmOutS1 == None:
                    RmOutS1 = S1messenger.prevp_receive()
                mOutS1, mOutS1F = RmOutS1[0], RmOutS1[1]

                mOut = self.ArrayXOR([mOutS1, mOutS2])
                mOutF = self.ArrayAddF(P, mOutS1F, mOutS2F, S)

            if Serveri == 1 and Serverj == 2:
                S1messenger = S.getprevmessenger()
                
                mOutS2 = S.get_saved(1)

                
                mOutS2F = S.get_saved(1)
                S1messenger.prevp_send((mOutS2, mOutS2F))

                RmOutS1 = S1messenger.prevp_receive()
                while RmOutS1 == None:
                    RmOutS1 = S1messenger.prevp_receive()
                mOutS1, mOutS1F = RmOutS1[0], RmOutS1[1]

                mOut = self.ArrayXOR([mOutS1, mOutS2])
                mOutF = self.ArrayAddF(P, mOutS1F, mOutS2F, S)

            for i in range(len(mOut)):
                share = Output[i]
                share.add(mOut[i])
                shareF = OutputF[i]
                shareF.add(mOutF[i])

    def shuffle_offline(self, P:int, Input1: list[Share], Input2: list[Share], S: Server0 | Server1 | Server2):
        L = len(Input1)
        Output1 = []
        Output2 = []
        if S.id() == 0:
        #Offline begins
            sigma01 = self.getrandompermutation(L)
            sigma02 = self.getrandompermutation(L)

            # S1messenger = S.getnextmessenger()
            # S2messenger = S.getprevmessenger()

            # S1messenger.nextp_send(sigma01)
            # S2messenger.prevp_send(sigma02)

            S.save_for_comm(0, sigma01)
            S.save_for_comm(0, sigma02)

        if S.id() == 1:
        #Offline begins
            sigma12 = self.getrandompermutation(L)
            
            S0messenger = S.getprevmessenger()
            S2messenger = S.getnextmessenger()

            S.save_for_comm(0, sigma12)

            # S2messenger.nextp_send(sigma12)
            # sigma01 = S0messenger.prevp_receive()
            # while sigma01 == None:
            #     sigma01 = S0messenger.prevp_receive()

        if S.id() == 2:
        #Offline begins
            # S0messenger = S.getnextmessenger()
            # S1messenger = S.getprevmessenger()

            # sigma12 = S1messenger.prevp_receive()
            # while sigma12 == None:
            #     sigma12 = S1messenger.prevp_receive()

            # sigma02 = S0messenger.nextp_receive()
            # while sigma02 == None:
            #     sigma02 = S0messenger.nextp_receive()
            pass

    def optimize_shuffle_offline(self, S: Server0 | Server1 | Server2):
        if S.id() == 0:
        #Offline begins
            sigma011 = S.get_saved(0)
            sigma021 = S.get_saved(0)
            sigma012 = S.get_saved(0)
            sigma022 = S.get_saved(0)
            
            S1messenger = S.getnextmessenger()
            S2messenger = S.getprevmessenger()

            S1messenger.nextp_send((sigma011, sigma012))
            S2messenger.prevp_send((sigma021, sigma022))
            
            S.save_for_comm(0, sigma011)
            S.save_for_comm(0, sigma021)
            S.save_for_comm(0, sigma012)
            S.save_for_comm(0, sigma022)


        if S.id() == 1:
        #Offline begins
            
            S0messenger = S.getprevmessenger()
            S2messenger = S.getnextmessenger()

            sigma121 = S.get_saved(0)
            sigma122 = S.get_saved(0)

            S2messenger.nextp_send((sigma121, sigma122))

            Rsigma01 = S0messenger.prevp_receive()
            while Rsigma01 == None:
                Rsigma01 = S0messenger.prevp_receive()
            sigma011, sigma012 = Rsigma01[0], Rsigma01[1]

            S.save_for_comm(0, sigma011)
            S.save_for_comm(0, sigma121)
            S.save_for_comm(0, sigma012)
            S.save_for_comm(0, sigma122)


        if S.id() == 2:
        #Offline begins
            S0messenger = S.getnextmessenger()
            S1messenger = S.getprevmessenger()

            Rsigma12 = S1messenger.prevp_receive()
            while Rsigma12 == None:
                Rsigma12 = S1messenger.prevp_receive()
            sigma121, sigma122 = Rsigma12[0], Rsigma12[1]

            Rsigma02 = S0messenger.nextp_receive()
            while Rsigma02 == None:
                Rsigma02 = S0messenger.nextp_receive()
            sigma021, sigma022 = Rsigma02[0], Rsigma02[1]

            S.save_for_comm(0, sigma021)
            S.save_for_comm(0, sigma121)
            S.save_for_comm(0, sigma022)
            S.save_for_comm(0, sigma122)    
            
    def shuffle_online(self, P:int, Input1: list[Share], Input2: list[Share], S: Server0 | Server1 | Server2) -> tuple[list[Share], list[Share]]:
        L = len(Input1)
        Output1 = []
        Output2 = []
        if S.id() == 0:

            sigma01 = S.get_saved(0)
            sigma02 = S.get_saved(0)

        #Online begins
            temp11 = self.helper(Input1, S, 0, 1, sigma01.copy())
            temp12 = self.helperF(P, Input2, S, 0, 1, sigma01.copy())
            self.optimizeHelpers(P, S, 0, 1, temp11, temp12)
            temp21 = self.helper(temp11, S, 1, 2, None)
            temp22 = self.helperF(P, temp12, S, 1, 2, None)
            self.optimizeHelpers(P, S, 1, 2, temp21, temp22)
            Output1 = self.helper(temp21, S, 0, 2, sigma02.copy())
            Output2 = self.helperF(P, temp22, S, 0, 2, sigma02.copy())
            self.optimizeHelpers(P, S, 0, 2, Output1, Output2)

        if S.id() == 1:
            sigma01 = S.get_saved(0)
            sigma12 = S.get_saved(0)

        #Online begins
            temp11 = self.helper(Input1, S, 0, 1, sigma01.copy())
            temp12 = self.helperF(P, Input2, S, 0, 1, sigma01.copy())
            self.optimizeHelpers(P, S, 0, 1, temp11, temp12)
            temp21 = self.helper(temp11, S, 1, 2, sigma12.copy())
            temp22 = self.helperF(P, temp12, S, 1, 2, sigma12.copy())
            self.optimizeHelpers(P, S, 1, 2, temp21, temp22)
            Output1 = self.helper(temp21, S, 0, 2, None)
            Output2 = self.helperF(P, temp22, S, 0, 2, None)
            self.optimizeHelpers(P, S, 0, 2, Output1, Output2)

        if S.id() == 2: 
            sigma02 = S.get_saved(0)
            sigma12 = S.get_saved(0)

        #Online begins
            temp11 = self.helper(Input1, S, 0, 1, None)
            temp12 = self.helperF(P, Input2, S, 0, 1, None)
            self.optimizeHelpers(P, S, 0, 1, temp11, temp12)
            temp21 = self.helper(temp11, S, 1, 2, sigma12.copy())
            temp22 = self.helperF(P, temp12, S, 1, 2, sigma12.copy())
            self.optimizeHelpers(P, S, 1, 2, temp21, temp22)
            Output1 = self.helper(temp21, S, 0, 2, sigma02.copy())
            Output2 = self.helperF(P, temp22, S, 0, 2, sigma02.copy())
            self.optimizeHelpers(P, S, 0, 2, Output1, Output2)
        return Output1, Output2

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

    
    file0 = open("Client2_Server0.dat", "r")
    f0 = getSharesfromFile(file0)
    file0.seek(0)
    v0 = getSharesfromFileF(file0)
    file0.close()
    file1 = open("Client2_Server1.dat", "r")
    f1 = getSharesfromFile(file1)
    file1.seek(0)
    v1 = getSharesfromFileF(file1)
    file1.close()
    file2 = open("Client2_Server2.dat", "r")
    f2 = getSharesfromFile(file2)
    file2.seek(0)
    v2 = getSharesfromFileF(file2)
    file2.close()
      
    p0 = multiprocessing.Process(target=shuffle.shuffle, args=(7, f0, v0, S0))
    p1 = multiprocessing.Process(target=shuffle.shuffle, args=(7, f1, v1, S1))
    p2 = multiprocessing.Process(target=shuffle.shuffle, args=(7, f2, v2, S2))

    p0.start()
    p1.start()
    p2.start()
    p0.join()
    p1.join()
    p2.join()