from server import *
from aes import *
from fpv import * 
import os

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

def getSharesfromFile(file) -> tuple[list[Share], list[Share], FPVShare]:
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

def runAESonList(f: list[Share], k: Share, S: Server, aes: AES) -> list[Share]:
    
    if S.id() == 0:
        # Offline begins
        lambda1 = []
        lambda2 = []
        outputs = []
        for fingerprint in f:
            s0 = Share()
            l1, l2 = fingerprint.get()
            lambda1.append(l1)
            lambda2.append(l2)
            outputs.append(s0)
        kl1, kl2 = k.get()
        offline_output = aes.circuit_offline([kl1.copy() , kl2.copy()], [lambda1.copy() , lambda2.copy()], S, outputs)
        print("0, AESdone offline")
        S.complete_optimised_offline()
        # Online begins
        for i in range(len(outputs)):
            s = outputs[i].get()
            x = S.online_reconstruction(s[0], s[1])
            print(ba2hex(x))
        return outputs

    if S.id() == 1:
        # Offline begins
        kl1, km = k.get()
        lambda1 = []
        m1 = []
        outputs = []
        for fingerprint in f:
            s1 = Share()
            l1, m = fingerprint.get()
            lambda1.append(l1)
            m1.append(m)
            outputs.append(s1)

        offline_output = aes.circuit_offline([kl1.copy() , km.copy()], [lambda1.copy() , m1.copy()], S, outputs)
        print("1, AESdone offline")
        online_output = aes.circuit_online([kl1.copy() , km.copy()], [lambda1.copy(), m1.copy()], S, outputs)
        print("1, AESdone online")
        for i in range(len(outputs)):
            s = outputs[i].get()
            x = S.online_reconstruction(s[0], s[1])
        return outputs

    if S.id() == 2:
        # Offline begins
        lambda2 = []
        m2 = []
        outputs = []
        for fingerprint in f:
            s2 = Share()
            l2, m = fingerprint.get()
            lambda2.append(l2)
            m2.append(m)
            outputs.append(s2)
        kl2, km = k.get()

        offline_output = aes.circuit_offline([kl2.copy() , km.copy()], [lambda2.copy() , m2.copy()], S, outputs)
        print("2, AESdone offline")
        S.complete_optimised_offline()

        # Online begins

        online_output = aes.circuit_online([kl2.copy() , km.copy()], [lambda2.copy() , m2.copy()], S, outputs)
        print("2, AESdone online")
        for i in range(len(outputs)):
            s = outputs[i].get()
            x = S.online_reconstruction(s[0], s[1])
        return outputs

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

    # l1 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    # l2 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    # inp = bitarray("01010100011101110110111100100000010011110110111001100101001000000100111001101001011011100110010100100000010101000111011101101111")
    # m = l1 ^ l2 ^ inp 

    # input_fin0 = [[l1], [l2]]
    # input_fin1 = [[l1], [m]]
    # input_fin2 = [[l2], [m]]
    # f0 = []
    # f1 = []
    # f2 = []
    # for i in range(2):
    #     s0 = Share()
    #     s1 = Share()
    #     s2 = Share()
    #     s0.add(l1)
    #     s0.add(l2)
    #     s1.add(l1)
    #     s1.add(m)
    #     s2.add(l2)
    #     s2.add(m)
    #     f0.append(s0)
    #     f1.append(s1)
    #     f2.append(s2)
    c1string = os.path.join("Client1_Server") + str(0) + "_v2.dat"
    c2string = os.path.join("Client1_Server") + str(1) + "_v2.dat"
    c3string = os.path.join("Client1_Server") + str(2) + "_v2.dat"
    file0 = open(c1string, "r")
    f10, v10, IL10 = getSharesfromFile(file0)
    file0.close()
    file0 = open(c2string, "r")
    f11, v11, IL11 = getSharesfromFile(file0)
    file0.close()
    file0 = open(c3string, "r")
    f12, v12, IL12 = getSharesfromFile(file0)
    file0.close()

    
    c1string = os.path.join("Client2_Server") + str(0) + "_v2.dat"
    c2string = os.path.join("Client2_Server") + str(1) + "_v2.dat"
    c3string = os.path.join("Client2_Server") + str(2) + "_v2.dat"
    file0 = open(c1string, "r")
    f20, v20, IL20 = getSharesfromFile(file0)
    file0.close()
    file0 = open(c2string, "r")
    f21, v21, IL21 = getSharesfromFile(file0)
    file0.close()
    file0 = open(c3string, "r")
    f22, v22, IL22 = getSharesfromFile(file0)
    file0.close()

    k1 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    k2 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    sk = bitarray("01010100011010000110000101110100011100110010000001101101011110010010000001001011011101010110111001100111001000000100011001110101")
    mk = k1 ^ k2 ^ sk

    # key_0 = [[k1], [k2]]
    # key_1 = [[k1], [mk]]
    # key_2 = [[k2], [mk]]

    keyshare0 = Share()
    keyshare1 = Share()
    keyshare2 = Share()
    keyshare0.add(k1)
    keyshare0.add(k2)
    keyshare1.add(k1)
    keyshare1.add(mk)
    keyshare2.add(k2)
    keyshare2.add(mk)

    offline_circuit = []

    aes = AES()
    # print("original l1: ", ba2hex(l1))
    # print("original l2: ", ba2hex(l2))
    # Run the offline phase for each dimension of the fingerprint (128)

    manager = multiprocessing.Manager()
    d = manager.dict()

    s0 = Share()
    s1 = Share()
    s2 = Share()

    p0 = multiprocessing.Process(target=runAESonList, args=(f10, keyshare0, S0, aes))
    p1 = multiprocessing.Process(target=runAESonList, args=(f11, keyshare1, S1, aes))
    p2 = multiprocessing.Process(target=runAESonList, args=(f12, keyshare2, S2, aes))

    p0.start()
    p1.start()
    p2.start()

    p0.join()
    p1.join()
    p2.join()

    # p0 = multiprocessing.Process(target=runAESonList, args=(f20, keyshare0, S0, aes))
    # p1 = multiprocessing.Process(target=runAESonList, args=(f21, keyshare1, S1, aes))
    # p2 = multiprocessing.Process(target=runAESonList, args=(f22, keyshare2, S2, aes))

    # p0.start()
    # p1.start()
    # p2.start()

    # p0.join()
    # p1.join()
    # p2.join()

    # out0 = o0.getShares()
    # out1 = o1.getShares()
    # out2 = o2.getShares()

    # # print(out0)

    # for i in range(len(out0)):
    #     share0 = out0[i]
    #     share1 = out1[i]
    #     share2 = out2[i]
    #     print(ba2hex(share1[0] ^ share2[0] ^ share1[1]))
    # o0 = s0.get()
    # o1 = s1.get()
    # o2 = s2.get()

    # print("AES input: ", ba2hex(inp))
    # print("AES key: ", ba2hex(sk))
    # print("AES output: ", ba2hex(o0[0] ^ o0[1] ^ o1[1]))
    # Run the online phase 