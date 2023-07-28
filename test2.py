from server import *
from aes import *


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

def runAESonList(f: list[Share], k: Share, S: Server, aes: AES, output: encryptedFingerprintOutput) -> None:
    if S.id() == 0:
        kl1, kl2 = k.get()
        outputs = []
        for fingerprint in f:
            s0 = Share()
            l1, l2 = fingerprint.get()
            aes.circuit([kl1 , kl2], [l1 , l2], S, s0)
            outputs.append(s0)
            s0 = s0.get()
            output.addShare(s0)
            S.printMessengers()
            print("0, AESdone")

    if S.id() == 1:
        kl1, km = k.get()
        outputs = []
        for fingerprint in f:
            s1 = Share()
            l1, m = fingerprint.get()
            print( ba2hex(kl1), "\n",ba2hex(km))
            aes.circuit([kl1 , km], [l1 , m], S, s1)
            outputs.append(s1)
            s1 = s1.get()
            output.addShare(s1)
            S.printMessengers()
            print("1, AESdone")

    if S.id() == 2:
        kl2, km = k.get()
        outputs = []
        for fingerprint in f:
            s2 = Share()
            l2, m = fingerprint.get()
            print(ba2hex(kl2), "\n",ba2hex(km))
            aes.circuit([kl2 , km], [l2 , m], S, s2)
            outputs.append(s2)
            s2 = s2.get()
            output.addShare(s2)
            S.printMessengers()
            print("2, AESdone")


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

    l1 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    l2 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    inp = bitarray("01010100011101110110111100100000010011110110111001100101001000000100111001101001011011100110010100100000010101000111011101101111")
    m = l1 ^ l2 ^ inp 

    # input_fin0 = [[l1], [l2]]
    # input_fin1 = [[l1], [m]]
    # input_fin2 = [[l2], [m]]
    f0 = []
    f1 = []
    f2 = []
    for i in range(2):
        s0 = Share()
        s1 = Share()
        s2 = Share()
        s0.add(l1)
        s0.add(l2)
        s1.add(l1)
        s1.add(m)
        s2.add(l2)
        s2.add(m)
        f0.append(s0)
        f1.append(s1)
        f2.append(s2)
        

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

    o0 = encryptedFingerprintOutput()
    o1 = encryptedFingerprintOutput()
    o2 = encryptedFingerprintOutput()

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

    p0 = multiprocessing.Process(target=runAESonList, args=(f0, keyshare0, S0, aes, o0))
    p1 = multiprocessing.Process(target=runAESonList, args=(f1, keyshare1, S1, aes, o1))
    p2 = multiprocessing.Process(target=runAESonList, args=(f2, keyshare2, S2, aes, o2))

    p0.start()
    p1.start()
    p2.start()

    p0.join()
    p1.join()
    p2.join()

    out0 = o0.getShares()
    out1 = o1.getShares()
    out2 = o2.getShares()

    # print(out0)

    for i in range(len(out0)):
        share0 = out0[i]
        share1 = out1[i]
        share2 = out2[i]
        print(ba2hex(share1[0] ^ share2[0] ^ share1[1]))
    # o0 = s0.get()
    # o1 = s1.get()
    # o2 = s2.get()


    # print("AES input: ", ba2hex(inp))
    # print("AES key: ", ba2hex(sk))
    # print("AES output: ", ba2hex(o0[0] ^ o0[1] ^ o1[1]))
    # Run the online phase 