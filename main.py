from server import *
from aes import *
from shuffle import *
from fpv import *
from winnowing import *
from time import *
import winsound

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

    def getSharesfromFile(self, filename) -> tuple[list[Share], list[Share], FPVShare]:
        f = []
        v = []
        IL = []
        with open(filename, "r") as file:
            line = file.readline()
            L = int(line)
            for _ in range(L):
            # while line:
                line = file.readline()
                s = Share()
                x = line.split(" ")
                s.add(bitarray(x[0]))
                s.add(bitarray(x[1]))
                f.append(s)
            for _ in range(L):
                line = file.readline()
                s = Share()
                x = line.split(" ")
                s.add(bitarray(x[0]))
                s.add(bitarray(x[1]))
                v.append(s)
            for i in range(4):
                line = file.readline()
                s = Share()
                x = line.split(" ")
                s.add(bitarray(x[0]))
                s.add(bitarray(x[1]))
                IL.append(s)
        ILS = FPVShare(IL[0], IL[1], IL[2], IL[3])
        return f, v, ILS

    def runAESonList(self, f: list[Share], k: Share, S: Server0 | Server1 | Server2, aes: AES) -> list[Share]:
        
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
            # print("Offline aes starts -          ", sttime - self.globaltime)
            # print("Offline aes ends -            ", etime - self.globaltime)
            # print("offline aes                   ", - sttime + etime)
            S.store_timestamp(sttime - self.globaltime, "Offline aes starts - ")
            S.store_timestamp(etime - self.globaltime, "Offline aes ends - ")
            S.store_timestamp(- sttime + etime, "Offline aes - ")
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
            # print("Offline aes starts -          ", " "*30, sttime - self.globaltime)
            # print("Offline aes ends -            ", " "*30, etime - self.globaltime)
            # print("offline aes                   ", " "*30, - sttime + etime)
            S.store_timestamp(sttime - self.globaltime, "Offline aes starts - ")
            S.store_timestamp(etime - self.globaltime, "Offline aes ends - ")
            S.store_timestamp(- sttime + etime, "Offline aes - ")
            sttime = time()
            aes.circuit_online([kl1.copy() , km.copy()], [lambda1.copy(), m1.copy()], S, outputs)
            etime = time()
            # print("Online aes starts -           ", " "*30, sttime - self.globaltime)
            # print("Online aes ends -             ", " "*30, etime - self.globaltime)
            # print("Online aes                    ", " "*30, - sttime + etime)
            S.store_timestamp(sttime - self.globaltime, "Online aes starts - ")
            S.store_timestamp(etime - self.globaltime, "Online aes ends - ")
            S.store_timestamp(- sttime + etime, "Online aes - ")
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
            # print("Offline aes starts -          ", " "*30, " "*30, sttime - self.globaltime)
            # print("Offline aes ends -            ", " "*30, " "*30, etime - self.globaltime)
            # print("offline aes                   ", " "*30, " "*30, - sttime + etime)
            S.store_timestamp(sttime - self.globaltime, "Offline aes starts - ")
            S.store_timestamp(etime - self.globaltime, "Offline aes ends - ")
            S.store_timestamp(- sttime + etime, "Offline aes - ")
            sttime = time()
            aes.circuit_online([kl2.copy() , km.copy()], [lambda2.copy() , m2.copy()], S, outputs)
            etime = time()
            # print("Online aes starts -           ", " "*30, " "*30, sttime - self.globaltime)
            # print("Online aes ends -             ", " "*30, " "*30, etime - self.globaltime)
            # print("online aes                    ", " "*30, " "*30, - sttime + etime)
            S.store_timestamp(sttime - self.globaltime, "Online aes starts - ")
            S.store_timestamp(etime - self.globaltime, "Online aes ends - ")
            S.store_timestamp(- sttime + etime, "Online aes - ")
            return outputs

    def reconstructList(self, f: list[Share], S: Server0 | Server1 | Server2):
        s1 = []
        s2 = []
        output = []
        for i in f:
            x = i.get()
            s1.append(x[0])
            s2.append(x[1])
        return  S.online_listreconstruction(s1, s2)

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
            
            L = len(fingerprint1)
            fingerprints = []
            for i in range(len(fingerprint1)):
                fingerprints.append(fingerprint1[i])
            for i in range(len(fingerprint2)):
                fingerprints.append(fingerprint2[i])
            encF = self.runAESonList(fingerprints, key, S, aes)
            encF1 = encF[:L]
            encF2 = encF[L:]
            # Shuffling Values and Encrypted Fingerprints
            sttime = time()
            temp1 = shuffle.shuffle_offline(61, encF1, values1, S)
            temp2 = shuffle.shuffle_offline(61, encF2, values2, S)
            shuffle.optimize_shuffle_offline(S)
            etime = time()
            S.store_timestamp(sttime - self.globaltime, "Offline shuffling starts - ")
            S.store_timestamp(etime - self.globaltime, "Offline shuffling ends - ")
            S.store_timestamp(- sttime + etime, "Offline shuffling - ")
            sttime = time()
            temp1 = shuffle.shuffle_online(61, encF1, values1, S)
            temp2 = shuffle.shuffle_online(61, encF2, values2, S)
            etime = time()
            S.store_timestamp(sttime - self.globaltime, "Online shuffling starts - ")
            S.store_timestamp(etime - self.globaltime, "Online shuffling ends - ")
            S.store_timestamp(- sttime + etime, "Online shuffling - ")
            encshufF1 = temp1[0]
            shufV1 = temp1[1]
            encshufF2 = temp2[0]
            shufV2 = temp2[1]
            
            sttime = time()

            # Reconstructing the Shuffled and Encrypted Fingerprints
            Z1 = self.reconstructList(encshufF1, S)
            Z2 = self.reconstructList(encshufF2, S)
            etime = time()
            S.store_timestamp(sttime - self.globaltime, "List Reconstruction starts - ")
            S.store_timestamp(etime - self.globaltime, "List Reconstruction ends - ")
            S.store_timestamp(- sttime + etime, "List Reconstruction - ")

            # Finding the indices of the common fingerprints
            commonindices = self.findCommonIndices(Z1, Z2)           
            
            # Getting the numerator of CS using the common fingerprints
            Num = self.getNumerator(61, shufV1, shufV2, commonindices, S)
            sttime1 = time()
            floatnum = fpv.int2FPV(Num, S)
            tempcs = fpv.FPVMultiply(floatnum, Linv1, S)
            cs = fpv.FPVMultiply(tempcs, Linv2, S)
            csout = fpv.FPVonline_reconstruction2Float(cs, S)
            etime1 = time()
            S.store_timestamp(sttime1 - self.globaltime, "fpv mpc starts - ")
            S.store_timestamp(etime1 - self.globaltime, "fpv mpc ends - ")
            S.store_timestamp(- sttime1 + etime1, "fpv mpc - ")
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
            
            L = len(fingerprint1)
            fingerprints = []
            for i in range(len(fingerprint1)):
                fingerprints.append(fingerprint1[i])
            for i in range(len(fingerprint2)):
                fingerprints.append(fingerprint2[i])
            encF = self.runAESonList(fingerprints, key, S, aes)
            encF1 = encF[:L]
            encF2 = encF[L:]

            # Shuffling Values and Encrypted Fingerprints
            sttime = time()
            temp1 = shuffle.shuffle_offline(61, encF1, values1, S)
            temp2 = shuffle.shuffle_offline(61, encF2, values2, S)
            shuffle.optimize_shuffle_offline(S)
            etime = time()
            S.store_timestamp(sttime - self.globaltime, "Offline shuffling starts - ")
            S.store_timestamp(etime - self.globaltime, "Offline shuffling ends - ")
            S.store_timestamp(- sttime + etime, "Offline shuffling - ")
            sttime = time()
            temp1 = shuffle.shuffle_online(61, encF1, values1, S)
            temp2 = shuffle.shuffle_online(61, encF2, values2, S)
            etime = time()
            S.store_timestamp(sttime - self.globaltime, "Online shuffling starts - ")
            S.store_timestamp(etime - self.globaltime, "Online shuffling ends - ")
            S.store_timestamp(- sttime + etime, "Online shuffling - ")
            encshufF1 = temp1[0]
            shufV1 = temp1[1]
            encshufF2 = temp2[0]
            shufV2 = temp2[1]
            
            sttime = time()
            
            # Reconstructing the Shuffled and Encrypted Fingerprints
            Z1 = self.reconstructList(encshufF1, S)
            Z2 = self.reconstructList(encshufF2, S)
            etime = time()
            S.store_timestamp(sttime - self.globaltime, "List Reconstruction starts - ")
            S.store_timestamp(etime - self.globaltime, "List Reconstruction ends - ")
            S.store_timestamp(- sttime + etime, "List Reconstruction - ")
            
            # Finding the indices of the common fingerprints
            commonindices = self.findCommonIndices(Z1, Z2)
            
            # Getting the numerator of CS using the common fingerprints
            Num = self.getNumerator(61, shufV1, shufV2, commonindices, S)
            
            sttime = time()
            floatnum = fpv.int2FPV(Num, S)
            tempcs = fpv.FPVMultiply(floatnum, Linv1, S)
            cs = fpv.FPVMultiply(tempcs, Linv2, S)
            csout = fpv.FPVonline_reconstruction2Float(cs, S)
            etime = time()
            S.store_timestamp(sttime - self.globaltime, "fpv mpc starts - ")
            S.store_timestamp(etime - self.globaltime, "fpv mpc ends - ")
            S.store_timestamp(- sttime + etime, "fpv mpc - ")
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
            
            L = len(fingerprint1)
            fingerprints = []
            for i in range(len(fingerprint1)):
                fingerprints.append(fingerprint1[i])
            for i in range(len(fingerprint2)):
                fingerprints.append(fingerprint2[i])
            encF = self.runAESonList(fingerprints, key, S, aes)
            encF1 = encF[:L]
            encF2 = encF[L:]

            # Shuffling Values and Encrypted Fingerprints
            sttime = time()
            shuffle.shuffle_offline(61, encF1, values1, S)
            shuffle.shuffle_offline(61, encF2, values2, S)
            shuffle.optimize_shuffle_offline(S)
            etime = time()
            S.store_timestamp(sttime - self.globaltime, "Offline shuffling starts - ")
            S.store_timestamp(etime - self.globaltime, "Offline shuffling ends - ")
            S.store_timestamp(- sttime + etime, "Offline shuffling - ")
            sttime = time()
            temp1 = shuffle.shuffle_online(61, encF1, values1, S)
            temp2 = shuffle.shuffle_online(61, encF2, values2, S)
            etime = time()
            S.store_timestamp(sttime - self.globaltime, "Online shuffling starts - ")
            S.store_timestamp(etime - self.globaltime, "Online shuffling ends - ")
            S.store_timestamp(- sttime + etime, "Online shuffling - ")
            encshufF1 = temp1[0]
            shufV1 = temp1[1]
            encshufF2 = temp2[0]
            shufV2 = temp2[1]
            
            sttime = time()
            
            # Reconstructing the Shuffled and Encrypted Fingerprints
            Z1 = self.reconstructList(encshufF1, S)
            Z2 = self.reconstructList(encshufF2, S)
            etime = time()
            S.store_timestamp(sttime - self.globaltime, "List Reconstruction starts - ")
            S.store_timestamp(etime - self.globaltime, "List Reconstruction ends - ")
            S.store_timestamp(- sttime + etime, "List Reconstruction - ")
            
            # Finding the indices of the common fingerprints
            commonindices = self.findCommonIndices(Z1, Z2)


            # Getting the numerator of CS using the common fingerprints
            Num = self.getNumerator(61, shufV1, shufV2, commonindices, S)
            sttime = time()
            floatnum = fpv.int2FPV(Num, S)
            
            tempcs = fpv.FPVMultiply(floatnum, Linv1, S)
            cs = fpv.FPVMultiply(tempcs, Linv2, S)
            csout = fpv.FPVonline_reconstruction2Float(cs, S)
            etime = time()
            S.store_timestamp(sttime - self.globaltime, "fpv mpc starts - ")
            S.store_timestamp(etime - self.globaltime, "fpv mpc ends - ")
            S.store_timestamp(- sttime + etime, "fpv mpc - ")
            return csout

    def Preprocess(self, program1, filename1, program2, filename2):
        gast = GenAST()
        gast.generate_ast(filename1, program1)
        f = open(filename1, "r")
        l1 = len(f.readlines())
        f.close()
        f = open(filename2, "r")
        l2 = len(f.readlines())
        f.close()
        print("\"Code1Len\": " + str(l1) + ",")
        print("\"Code2Len\": " + str(l2) + ",")
        gast2 = GenAST()
        gast2.generate_ast(filename2, program2)
        win = Winnowing()
        cs = win.GentoFile(os.path.join("Program1", "program1"), os.path.join("Program2", "program2"))
        print("\"Plaintext Similarity\": " + str(cs) + ",")
    
    def Run(self, S: Server0 | Server1 | Server2, output: multiprocessing.Queue):
        sttime = time()
        S.store_timestamp(time() - self.globaltime, "Share reading starts - ")
        c1string = os.path.join("Client1", "Client1_Server") + str(S.id()) + "_v2.dat"
        c2string = os.path.join("Client2", "Client2_Server") + str(S.id()) + "_v2.dat"
        f1, v1, IL1 = self.getSharesfromFile(c1string)
        f2, v2, IL2 = self.getSharesfromFile(c2string)
        etime = time()
        S.store_timestamp(time() - self.globaltime, "Share reading ends - ")
        S.store_timestamp(etime - sttime, "Share reading - ")

        out = self.SecureCS(f1, f2, v1, v2, IL1, IL2, S)
        output.put(out)          
        return

if __name__=='__main__':
    
    filename1 = sys.argv[2]
    program_number1 = sys.argv[1]
    filename2 = sys.argv[4]
    program_number2 = sys.argv[3]
    print(f"\"o{filename1}{filename2}\": {{")

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


    sttime = time()
    # print("AST Generation starts - ", time() - scs.globaltime)
    scs.Preprocess(program_number1, filename1, program_number2, filename2)
    etime = time()
    # print("AST Generation ends - ", time() - scs.globaltime)
    S0.store_timestamp(sttime - scs.globaltime, "AST Generation starts - ")
    S1.store_timestamp(sttime - scs.globaltime, "AST Generation starts - ")
    S2.store_timestamp(sttime - scs.globaltime, "AST Generation starts - ")
    S0.store_timestamp(etime - scs.globaltime, "AST Generation ends - ")
    S1.store_timestamp(etime - scs.globaltime, "AST Generation ends - ")
    S2.store_timestamp(etime - scs.globaltime, "AST Generation ends - ")
    
    S0.store_timestamp(etime - sttime, "AST Generation - ")
    S1.store_timestamp(etime - sttime, "AST Generation - ")
    S2.store_timestamp(etime - sttime, "AST Generation - ")
    out0 = multiprocessing.Queue()
    out1 = multiprocessing.Queue()
    out2 = multiprocessing.Queue()
    p0 = multiprocessing.Process(target=scs.Run, args=[S0, out0])
    p1 = multiprocessing.Process(target=scs.Run, args=[S1, out1])
    p2 = multiprocessing.Process(target=scs.Run, args=[S2, out2])

    start_time = time()

    p0.start()
    p1.start()
    p2.start()

    p0.join()
    p1.join()
    p2.join()

    end_time = time()

    # print(-start_time + end_time)
    # S0.store_timestamp(-start_time + end_time, "Total runtime - ")
    # S1.store_timestamp(-start_time + end_time, "Total runtime - ")
    # S2.store_timestamp(-start_time + end_time, "Total runtime - ")
    S0.print_timestamp()
    S1.print_timestamp()
    S2.print_timestamp()
    # print(out0.qsize(), out1.qsize(), out2.qsize())
    print("\"Total runtime - \": " + str(-start_time + end_time) + ",")
    print("\"Secure Similarity\": " + str(out0.get()) + ",")

    print("},")
    # winsound.Beep(4000, 100)