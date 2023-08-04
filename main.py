from server import *
from aes import *
from shuffle import *
from fpv import *

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
        return temp

class SecureCosineSimilarity:
    def findCommonIndices(self, A: list[bitarray], B: list[bitarray]) -> list[tuple[int, int]]:
        L = len(A)
        M = len(B)
        output = []
        for i in range(L):
            for j in range(M):
                if ba2hex(A[i]) == ba2hex(B[j]):
                    output.append((i, j))
        return output

    def getSharesfromFile(self, file) -> tuple[list[Share], list[Share], FPVShare]:
        line = file.readline()
        L = int(line)
        f = []
        # line = file.readline()
        # line = file.readline()
        for _ in range(L):
        # while line:
            line = file.readline()
            s = Share()
            x = line.split(" ")
            s.add(bitarray(x[0]))
            s.add(bitarray(x[1]))
            f.append(s)
        v = []
        for _ in range(L):
            line = file.readline()
            s = Share()
            x = line.split(" ")
            s.add(bitarray(x[0]))
            s.add(bitarray(x[1]))
            v.append(s)
        IL = []
        for i in range(4):
            line = file.readline()
            s = Share()
            x = line.split(" ")
            s.add(bitarray(x[0]))
            s.add(bitarray(x[1]))
            IL.append(s)
        ILS = FPVShare(IL[0], IL[1], IL[2], IL[3])
        return f, v, ILS

    def runAESonList(self, f: list[Share], k: Share, S: Server, aes: AES) -> list[Share]:
        outputs = []
        if S.id() == 0:
            kl1, kl2 = k.get()
            for fingerprint in f:
                s0 = Share()
                l1, l2 = fingerprint.get()
                aes.circuit([kl1 , kl2], [l1 , l2], S, s0)
                outputs.append(s0)
                print("0, AESdone")

        if S.id() == 1:
            kl1, km = k.get()
            outputs = []
            for fingerprint in f:
                s1 = Share()
                l1, m = fingerprint.get()
                aes.circuit([kl1 , km], [l1 , m], S, s1)
                outputs.append(s1)
                print("1, AESdone")

        if S.id() == 2:
            kl2, km = k.get()
            outputs = []
            for fingerprint in f:
                s2 = Share()
                l2, m = fingerprint.get()
                aes.circuit([kl2 , km], [l2 , m], S, s2)
                outputs.append(s2)
                print("2, AESdone")
        
        return outputs

    def reconstructList(self, f: list[Share], S: Server):
        output = []
        for i in f:
            x = i.get()
            y = S.online_reconstruction(x[0], x[1])
            output.append(y)
        return output

    def reconstructListF(self, f: list[Share], S: Server):
        output = []
        for i in f:
            x = i.get()
            y = S.online_reconstructionF(61, x[0], x[1])
            output.append(y)
        return output

    def generatezerovaluesF(self, P, L) -> tuple[list[bitarray], list[bitarray], list[bitarray]]:
        share1 = []
        for i in range(L):
            share = Share()
            x = bitarray("0"*P)
            y = bitarray("0"*P)
            share.add(x)
            share.add(y)
            share1.append(share)
        share2 = []
        for i in range(L):
            share = Share()
            x = bitarray("0"*P)
            y = bitarray("0"*P)
            share.add(x)
            share.add(y)
            share2.append(share)
        share3 = []
        for i in range(L):
            share = Share()
            x = bitarray("0"*P)
            y = bitarray("0"*P)
            share.add(x)
            share.add(y)
            share3.append(share)
        return share1, share2, share3

    def getNumerator(self, P: int, v1: list[Share], v2: list[Share], commonindices: list[tuple[int, int]], S: Server0 | Server1 | Server2):
        s0 = bitarray("0")
        s1 = bitarray("0")
        if S.id() == 0:
            for i in range(len(commonindices)):
                v1i = v1[commonindices[i][0]].get()
                v2i = v2[commonindices[i][1]].get()
                vi = S.offline_ANDF(P, S.addF(P, v1i[0], v1i[1]), S.addF(P, v2i[0], v2i[1]))
                s0 = S.addF(P, s0, vi[1])
                s1 = S.addF(P, s1, vi[2])
            p = S.online_reconstructionF(P, s0, s1)
            print(ba2int(p))
        else:
            for i in range(len(commonindices)):
                v1i = v1[commonindices[i][0]].get()
                v2i = v2[commonindices[i][1]].get()
                vi = S.offline_ANDF(P, v1i[0], v2i[0])
                s0 = S.addF(P, s0, vi)
            
            for i in range(len(commonindices)):
                v1i = v1[commonindices[i][0]].get()
                v2i = v2[commonindices[i][1]].get()
                vi = S.online_ANDF(P, v1i[1], v2i[1])
                s1 = S.addF(P, s1, vi)
            p = S.online_reconstructionF(P, s0, s1)
        Output = Share()
        Output.add(s0)
        Output.add(s1)
        return Output

    def SecureCS(self, fingerprint1: list[Share], fingerprint2: list[Share], values1: list[Share], values2: list[Share], Linv1: FPVShare, Linv2: FPVShare, S: Server0 | Server1 | Server2) -> float:
        aes = AES()
        shuffle = Shuffle()
        fpv = FPVArithmetic()
        if S.id() == 0:
            # Generating and sharing key for AES
            lambda1_key = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
            lambda2_key = bitarray(bin(random.getrandbits(128))[2:].zfill(128))

            S1messenger = S.getnextmessenger()
            S2messenger = S.getprevmessenger()

            S1messenger.nextp_send(lambda1_key)
            S2messenger.prevp_send(lambda2_key)
            key = Share()
            key.add(lambda1_key)
            key.add(lambda2_key)

            print(ba2hex(S.online_reconstruction(lambda1_key, lambda2_key)))

            # Running AES on the fingerprints
            encF1 = self.runAESonList(fingerprint1, key, S, aes)
            encF2 = self.runAESonList(fingerprint2, key, S, aes)

            # Shuffling Values and Encrypted Fingerprints
            temp1 = shuffle.shuffle(61, encF1, values1, S)
            temp2 = shuffle.shuffle(61, encF2, values2, S)
            encshufF1 = temp1[0]
            shufV1 = temp1[1]
            encshufF2 = temp2[0]
            shufV2 = temp2[1]

            # Reconstructing the Shuffled and Encrypted Fingerprints
            Z1 = self.reconstructList(encshufF1, S)
            Z2 = self.reconstructList(encshufF2, S)

            # Finding the indices of the common fingerprints
            commonindices = self.findCommonIndices(Z1, Z2)
            
            # Getting the numerator of CS using the common fingerprints
            Num = self.getNumerator(61, shufV1, shufV2, commonindices, S)
            floatnum = fpv.int2FPV(Num, S)
            tempcs = fpv.FPVMultiply(floatnum, Linv1, S)
            cs = fpv.FPVMultiply(tempcs, Linv2, S)
            csout = fpv.FPVonline_reconstruction2Float(cs, S)
            print(csout)

        if S.id() == 1:
            # Generating and sharing key for AES
            m_key = bitarray(bin(random.getrandbits(128))[2:].zfill(128))

            S2messenger = S.getnextmessenger()
            S0messenger = S.getprevmessenger()

            S2messenger.nextp_send(m_key)

            lambda1_key = S0messenger.prevp_receive()
            while lambda1_key == None:
                lambda1_key = S0messenger.prevp_receive()

            key = Share()
            key.add(lambda1_key)
            key.add(m_key)

            print(ba2hex(S.online_reconstruction(lambda1_key, m_key)))
            
            # Running AES on the fingerprints
            encF1 = self.runAESonList(fingerprint1, key, S, aes)
            encF2 = self.runAESonList(fingerprint2, key, S, aes)

            # Shuffling Values and Encrypted Fingerprints
            temp1 = shuffle.shuffle(61, encF1, values1, S)
            temp2 = shuffle.shuffle(61, encF2, values2, S)
            encshufF1 = temp1[0]
            shufV1 = temp1[1]
            encshufF2 = temp2[0]
            shufV2 = temp2[1]
            
            # Reconstructing the Shuffled and Encrypted Fingerprints
            Z1 = self.reconstructList(encshufF1, S)
            Z2 = self.reconstructList(encshufF2, S)
            
            # Finding the indices of the common fingerprints
            commonindices = self.findCommonIndices(Z1, Z2)
            
            # Getting the numerator of CS using the common fingerprints
            Num = self.getNumerator(61, shufV1, shufV2, commonindices, S)
            floatnum = fpv.int2FPV(Num, S)
            tempcs = fpv.FPVMultiply(floatnum, Linv1, S)
            cs = fpv.FPVMultiply(tempcs, Linv2, S)
            csout = fpv.FPVonline_reconstruction2Float(cs, S)

        if S.id() == 2:
            # Generating and sharing keys for AES
            S0messenger = S.getnextmessenger()
            S1messenger = S.getprevmessenger()
        
            lambda2_key = S0messenger.nextp_receive()
            while lambda2_key == None:
                lambda2_key = S0messenger.nextp_receive()
            
            m_key = S1messenger.prevp_receive()
            while m_key == None:
                m_key = S1messenger.prevp_receive()
            key = Share()
            key.add(lambda2_key)
            key.add(m_key)

            print(ba2hex(S.online_reconstruction(lambda2_key, m_key)))

            # Running AES on the fingerprints
            encF1 = self.runAESonList(fingerprint1, key, S, aes)
            encF2 = self.runAESonList(fingerprint2, key, S, aes)

            # Shuffling Values and Encrypted Fingerprints
            temp1 = shuffle.shuffle(61, encF1, values1, S)
            temp2 = shuffle.shuffle(61, encF2, values2, S)
            encshufF1 = temp1[0]
            shufV1 = temp1[1]
            encshufF2 = temp2[0]
            shufV2 = temp2[1]
            
            # Reconstructing the Shuffled and Encrypted Fingerprints
            Z1 = self.reconstructList(encshufF1, S)
            Z2 = self.reconstructList(encshufF2, S)
            
            # Finding the indices of the common fingerprints
            commonindices = self.findCommonIndices(Z1, Z2)

            # Getting the numerator of CS using the common fingerprints
            Num = self.getNumerator(61, shufV1, shufV2, commonindices, S)
            floatnum = fpv.int2FPV(Num, S)
            tempcs = fpv.FPVMultiply(floatnum, Linv1, S)
            cs = fpv.FPVMultiply(tempcs, Linv2, S)
            csout = fpv.FPVonline_reconstruction2Float(cs, S)

        return 0.0


if __name__=='__main__':
    
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

    # Get key Shares
    # k1 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    # k2 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    # sk = bitarray("01010100011010000110000101110100011100110010000001101101011110010010000001001011011101010110111001100111001000000100011001110101")
    # mk = k1 ^ k2 ^ sk
    # keyshare0 = Share()
    # keyshare1 = Share()
    # keyshare2 = Share()
    # keyshare0.add(k1)
    # keyshare0.add(k2)
    # keyshare1.add(k1)
    # keyshare1.add(mk)
    # keyshare2.add(k2)
    # keyshare2.add(mk)

    scs = SecureCosineSimilarity()

    # Get fingerprint Shares for Client 1
    file0 = open("Client1_Server0_v2.dat", "r")
    f01, v01, IL01 = scs.getSharesfromFile(file0)
    file0.close()
    file1 = open("Client1_Server1_v2.dat", "r")
    f11, v11, IL11 = scs.getSharesfromFile(file1)
    file1.close()
    file2 = open("Client1_Server2_v2.dat", "r")
    f21, v21, IL21 = scs.getSharesfromFile(file2)
    file2.close()

    # Get fingerprint Shares for Client 1
    file0 = open("Client2_Server0_v2.dat", "r")
    f02, v02, IL02 = scs.getSharesfromFile(file0)
    file0.close()
    file1 = open("Client2_Server1_v2.dat", "r")
    f12, v12, IL12 = scs.getSharesfromFile(file1)
    file1.close()
    file2 = open("Client2_Server2_v2.dat", "r")
    f22, v22, IL22 = scs.getSharesfromFile(file2)
    file2.close()

    offline_circuit = []

    aes = AES()

    manager = multiprocessing.Manager()
    d = manager.dict()

    s0 = Share()
    s1 = Share()
    s2 = Share()

    p0 = multiprocessing.Process(target=scs.SecureCS, args=(f01, f02, v01, v02, IL01, IL02, S0))
    p1 = multiprocessing.Process(target=scs.SecureCS, args=(f11, f12, v11, v12, IL11, IL12, S1))
    p2 = multiprocessing.Process(target=scs.SecureCS, args=(f21, f22, v21, v22, IL21, IL22, S2))

    p0.start()
    p1.start()
    p2.start()

    p0.join()
    p1.join()
    p2.join()
