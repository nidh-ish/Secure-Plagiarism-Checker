from server import *
from aes import *
from shuffle import *
from fpv import *
from winnowing import *
from time import *

class SecureCosineSimilarity:
    def __init__(self):
        self.globaltime = time()
    
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
            sttime = time()
            aes.circuit_offline([kl1.copy() , kl2.copy()], [lambda1.copy() , lambda2.copy()], S, outputs)
            S.complete_optimised_offline()
            etime = time()
            print("Offline aes starts -          ", sttime - self.globaltime)
            print("Offline aes ends -            ", etime - self.globaltime)
            print("offline aes                   ", - sttime + etime)
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
            sttime = time()
            aes.circuit_offline([kl1.copy() , km.copy()], [lambda1.copy() , m1.copy()], S, outputs)
            etime = time()
            print("Offline aes starts -          ", " "*30, sttime - self.globaltime)
            print("Offline aes ends -            ", " "*30, etime - self.globaltime)
            print("offline aes                   ", " "*30, - sttime + etime)
            sttime = time()
            aes.circuit_online([kl1.copy() , km.copy()], [lambda1.copy(), m1.copy()], S, outputs)
            etime = time()
            print("Online aes starts -           ", " "*30, sttime - self.globaltime)
            print("Online aes ends -             ", " "*30, etime - self.globaltime)
            print("online aes                    ", " "*30, - sttime + etime)
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
            sttime = time()
            aes.circuit_offline([kl2.copy() , km.copy()], [lambda2.copy() , m2.copy()], S, outputs)
            S.complete_optimised_offline()
            etime = time()
            print("Offline aes starts -          ", " "*30, " "*30, sttime - self.globaltime)
            print("Offline aes ends -            ", " "*30, " "*30, etime - self.globaltime)
            print("offline aes                   ", " "*30, " "*30, - sttime + etime)
            sttime = time()
            aes.circuit_online([kl2.copy() , km.copy()], [lambda2.copy() , m2.copy()], S, outputs)
            etime = time()
            print("Online aes starts -           ", " "*30, " "*30, sttime - self.globaltime)
            print("Online aes ends -             ", " "*30, " "*30, etime - self.globaltime)
            print("online aes                    ", " "*30, " "*30, - sttime + etime)
            return outputs

    def reconstructList(self, f: list[Share], S: Server):
        sttime = time()
        output = []
        for i in f:
            x = i.get()
            y = S.online_reconstruction(x[0], x[1])
            output.append(y)
        etime = time()
        print("List Reconstruction starts -  ", " "*30*S.id(), sttime - self.globaltime)
        print("List Reconstruction ends -    ", " "*30*S.id(), etime - self.globaltime)
        print("List Reconstruction           ", " "*30*S.id(), etime - sttime)
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

            # Running AES on the fingerprints
            print(S.id(), "Client 1 AES")
            encF1 = self.runAESonList(fingerprint1, key, S, aes)
            print(S.id(), "Client 2 AES")
            encF2 = self.runAESonList(fingerprint2, key, S, aes)

            # Shuffling Values and Encrypted Fingerprints
            sttime = time()
            temp1 = shuffle.shuffle_offline(61, encF1, values1, S)
            temp2 = shuffle.shuffle_offline(61, encF2, values2, S)
            shuffle.optimize_shuffle_offline(S)
            etime = time()
            print("offline shuffling starts -    ", " "*30*S.id(), sttime - self.globaltime)
            print("offline shuffling ends -      ", " "*30*S.id(), etime - self.globaltime)
            print("offline shuffling             ", " "*30*S.id(), - sttime + etime)
            sttime = time()
            temp1 = shuffle.shuffle_online(61, encF1, values1, S)
            temp2 = shuffle.shuffle_online(61, encF2, values2, S)
            etime = time()
            print("online shuffling starts -     ", " "*30*S.id(), sttime - self.globaltime)
            print("online shuffling ends -       ", " "*30*S.id(), etime - self.globaltime)
            print("online shuffling              ", " "*30*S.id(), - sttime + etime)
            encshufF1 = temp1[0]
            shufV1 = temp1[1]
            encshufF2 = temp2[0]
            shufV2 = temp2[1]

            # Reconstructing the Shuffled and Encrypted Fingerprints
            Z1 = self.reconstructList(encshufF1, S)
            Z2 = self.reconstructList(encshufF2, S)

            # Finding the indices of the common fingerprints
            commonindices = self.findCommonIndices(Z1, Z2)

            sttime = time()
            
            # Getting the numerator of CS using the common fingerprints
            Num = self.getNumerator(61, shufV1, shufV2, commonindices, S)
            floatnum = fpv.int2FPV(Num, S)
            tempcs = fpv.FPVMultiply(floatnum, Linv1, S)
            cs = fpv.FPVMultiply(tempcs, Linv2, S)
            csout = fpv.FPVonline_reconstruction2Float(cs, S)
            etime = time()
            print("fpv mpc starts -              ", sttime - self.globaltime)
            print("fpv mpc ends -                ", etime - self.globaltime)
            print("fpv mpc                       ", - sttime + etime)
            return csout

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
            
            # Running AES on the fingerprints
            print(S.id(), "Client 1 AES")
            encF1 = self.runAESonList(fingerprint1, key, S, aes)
            print(S.id(), "Client 2 AES")
            encF2 = self.runAESonList(fingerprint2, key, S, aes)

            # Shuffling Values and Encrypted Fingerprints
            sttime = time()
            temp1 = shuffle.shuffle_offline(61, encF1, values1, S)
            temp2 = shuffle.shuffle_offline(61, encF2, values2, S)
            shuffle.optimize_shuffle_offline(S)
            etime = time()
            print("offline shuffling starts -    ", " "*30*S.id(), sttime - self.globaltime)
            print("offline shuffling ends -      ", " "*30*S.id(), etime - self.globaltime)
            print("offline shuffling             ", " "*30*S.id(), - sttime + etime)
            sttime = time()
            temp1 = shuffle.shuffle_online(61, encF1, values1, S)
            temp2 = shuffle.shuffle_online(61, encF2, values2, S)
            etime = time()
            print("online shuffling starts -     ", " "*30*S.id(), sttime - self.globaltime)
            print("online shuffling ends -       ", " "*30*S.id(), etime - self.globaltime)
            print("online shuffling              ", " "*30*S.id(), - sttime + etime)
            encshufF1 = temp1[0]
            shufV1 = temp1[1]
            encshufF2 = temp2[0]
            shufV2 = temp2[1]
            
            # Reconstructing the Shuffled and Encrypted Fingerprints
            Z1 = self.reconstructList(encshufF1, S)
            Z2 = self.reconstructList(encshufF2, S)
            
            # Finding the indices of the common fingerprints
            commonindices = self.findCommonIndices(Z1, Z2)
            
            sttime = time()

            # Getting the numerator of CS using the common fingerprints
            Num = self.getNumerator(61, shufV1, shufV2, commonindices, S)
            floatnum = fpv.int2FPV(Num, S)
            tempcs = fpv.FPVMultiply(floatnum, Linv1, S)
            cs = fpv.FPVMultiply(tempcs, Linv2, S)
            csout = fpv.FPVonline_reconstruction2Float(cs, S)
            etime = time()
            print("fpv mpc starts -               ", " "*30, sttime - self.globaltime)
            print("fpv mpc ends -                 ", " "*30, etime - self.globaltime)
            print("fpv mpc                        ", " "*30, - sttime + etime)
            return csout

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

            # Running AES on the fingerprints
            print(S.id(), "Client 1 AES")
            encF1 = self.runAESonList(fingerprint1, key, S, aes)
            print(S.id(), "Client 2 AES")
            encF2 = self.runAESonList(fingerprint2, key, S, aes)

            # Shuffling Values and Encrypted Fingerprints
            sttime = time()
            shuffle.shuffle_offline(61, encF1, values1, S)
            shuffle.shuffle_offline(61, encF2, values2, S)
            shuffle.optimize_shuffle_offline(S)
            etime = time()
            print("offline shuffling starts -    ", " "*30*S.id(), sttime - self.globaltime)
            print("offline shuffling ends -      ", " "*30*S.id(), etime - self.globaltime)
            print("offline shuffling             ", " "*30*S.id(), - sttime + etime)
            sttime = time()
            temp1 = shuffle.shuffle_online(61, encF1, values1, S)
            temp2 = shuffle.shuffle_online(61, encF2, values2, S)
            etime = time()
            print("online shuffling starts -     ", " "*30*S.id(), sttime - self.globaltime)
            print("online shuffling ends -       ", " "*30*S.id(), etime - self.globaltime)
            print("online shuffling              ", " "*30*S.id(), - sttime + etime)
            encshufF1 = temp1[0]
            shufV1 = temp1[1]
            encshufF2 = temp2[0]
            shufV2 = temp2[1]
            
            # Reconstructing the Shuffled and Encrypted Fingerprints
            Z1 = self.reconstructList(encshufF1, S)
            Z2 = self.reconstructList(encshufF2, S)
            
            # Finding the indices of the common fingerprints
            commonindices = self.findCommonIndices(Z1, Z2)

            sttime = time()

            # Getting the numerator of CS using the common fingerprints
            Num = self.getNumerator(61, shufV1, shufV2, commonindices, S)
            floatnum = fpv.int2FPV(Num, S)
            tempcs = fpv.FPVMultiply(floatnum, Linv1, S)
            cs = fpv.FPVMultiply(tempcs, Linv2, S)
            csout = fpv.FPVonline_reconstruction2Float(cs, S)
            etime = time()
            print("fpv mpc starts -               ", " "*30, " "*30, sttime - self.globaltime)
            print("fpv mpc ends -                 ", " "*30, " "*30, etime - self.globaltime)
            print("fpv mpc                        ", " "*30, " "*30, - sttime + etime)
            return csout

    def Preprocess(self, program1, filename1, program2, filename2):
        gast = GenAST()
        gast.generate_ast(filename1, program1)
        gast2 = GenAST()
        gast2.generate_ast(filename2, program2)
        win = Winnowing()
        win.GentoFile(os.path.join("Program1", "program1"), os.path.join("Program2", "program2"))
    
    def Run(self, S: Server0 | Server1 | Server2):
        sttime = time()
        print("Sharing starts -              ", " "*30*S.id(), time() - self.globaltime)
        c1string = os.path.join("Client1", "Client1_Server") + str(S.id()) + "_v2.dat"
        c2string = os.path.join("Client2", "Client2_Server") + str(S.id()) + "_v2.dat"
        file0 = open(c1string, "r")
        f1, v1, IL1 = self.getSharesfromFile(file0)
        file0.close()
        file0 = open(c2string, "r")
        f2, v2, IL2 = self.getSharesfromFile(file0)
        file0.close()

        etime = time()
        print("Sharing ends -                ", " "*30*S.id(), time() - self.globaltime)
        print("Sharing                       ", " "*30*S.id(), etime - sttime)

        out = self.SecureCS(f1, f2, v1, v2, IL1, IL2, S)
        if S.id() == 0:
            sttime = time()
            with open("Output.dat", "w") as file:
                print(out)
                file.write(str(out))
            etime = time()
            print("output writing", - sttime + etime)
            
        return

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

    scs = SecureCosineSimilarity()

    filename1 = sys.argv[2]
    program_number1 = sys.argv[1]
    filename2 = sys.argv[4]
    program_number2 = sys.argv[3]
    print("AST Generation starts - ", time() - scs.globaltime)
    scs.Preprocess(program_number1, filename1, program_number2, filename2)
    print("AST Generation ends - ", time() - scs.globaltime)
    p0 = multiprocessing.Process(target=scs.Run, args=[S0])
    p1 = multiprocessing.Process(target=scs.Run, args=[S1])
    p2 = multiprocessing.Process(target=scs.Run, args=[S2])

    start_time = time()

    p0.start()
    p1.start()
    p2.start()

    p0.join()
    p1.join()
    p2.join()

    end_time = time()

    print(-start_time + end_time)