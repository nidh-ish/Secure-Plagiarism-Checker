from server import * 

class AES:

    def __init__(self):
        pass

    def ShiftRow(self, input: bitarray(128)) -> bitarray(128):
        
        output = bitarray(128)
        
        output[0:8] = input[0:8]
        output[8:16] = input[40:48]
        output[16:24] = input[80:88]
        output[24:32] = input[120:128]

        output[32:40] = input[32:40]
        output[40:48] = input[72:80]
        output[48:56] = input[112:120]
        output[56:64] = input[24:32]

        output[64:72] = input[64:72]
        output[72:80] = input[104:112]
        output[80:88] = input[16:24]
        output[88:96] = input[56:64]

        output[96:104] = input[96:104]
        output[104:112] = input[8:16]
        output[112:120] = input[48:56]
        output[120:128] = input[88:96]

        return output

    def times(self, input: bitarray(8)) -> bitarray(8):
        output = input << 1
        a = [bitarray("00000000"), bitarray("00011011")]
        output = output ^ a[ba2int(input >> 7)]
        return output

    def MixColumn(self, input: bitarray(128)) -> bitarray(128):
        output = bitarray(128)
        
        output[0:8] = self.times(input[0:8]) ^ self.times(input[8:16]) ^ (input[8:16]) ^ (input[16:24]) ^ (input[24:32])
        output[8:16] = (input[0:8]) ^ self.times(input[8:16]) ^ self.times(input[16:24]) ^ (input[16:24]) ^ (input[24:32])
        output[16:24] = (input[0:8]) ^ input[8:16] ^ self.times(input[16:24]) ^ self.times(input[24:32]) ^ (input[24:32])
        output[24:32] = self.times(input[0:8]) ^ (input[0:8]) ^ input[8:16] ^ (input[16:24]) ^ self.times(input[24:32])

        output[32:40] = self.times(input[32:40]) ^ self.times(input[40:48]) ^ (input[40:48]) ^ (input[48:56]) ^ (input[56:64])
        output[40:48] = (input[32:40]) ^ self.times(input[40:48]) ^ self.times(input[48:56]) ^ (input[48:56]) ^ (input[56:64])
        output[48:56] = (input[32:40]) ^ input[40:48] ^ self.times(input[48:56]) ^ self.times(input[56:64]) ^ (input[56:64])
        output[56:64] = self.times(input[32:40]) ^ (input[32:40]) ^ input[40:48] ^ (input[48:56]) ^ self.times(input[56:64])

        output[64:72] = self.times(input[64:72]) ^ self.times(input[72:80]) ^ (input[72:80]) ^ (input[80:88]) ^ (input[88:96])
        output[72:80] = (input[64:72]) ^ self.times(input[72:80]) ^ self.times(input[80:88]) ^ (input[80:88]) ^ (input[88:96])
        output[80:88] = (input[64:72]) ^ input[72:80] ^ self.times(input[80:88]) ^ self.times(input[88:96]) ^ (input[88:96])
        output[88:96] = self.times(input[64:72]) ^ (input[64:72]) ^ input[72:80] ^ (input[80:88]) ^ self.times(input[88:96])

        output[96:104] = self.times(input[96:104]) ^ self.times(input[104:112]) ^ (input[104:112]) ^ (input[112:120]) ^ (input[120:128])
        output[104:112] = (input[96:104]) ^ self.times(input[104:112]) ^ self.times(input[112:120]) ^ (input[112:120]) ^ (input[120:128])
        output[112:120] = (input[96:104]) ^ input[104:112] ^ self.times(input[112:120]) ^ self.times(input[120:128]) ^ (input[120:128])
        output[120:128] = self.times(input[96:104]) ^ (input[96:104]) ^ input[104:112] ^ (input[112:120]) ^ self.times(input[120:128])

        return output

    def Optimized_SBox_offline(self, fingerprints: list[bitarray], keyinput: bitarray, AND, AND1, OR, Serv: Server0 | Server1 | Server2):

        f = len(fingerprints)

        size = 16 * f + 4

        input = []
        for i in range(8):
            l = 0
            temp = bitarray(size)
            for j in range(f):
                for k in range(16):
                    temp[l] = fingerprints[j][8*k + i]
                    l += 1
            for j in range(4):
                temp[l] = keyinput[8*j + i]
                l += 1
            input.append(temp)

        t = []
        m = []
        out1 = []
        out2 = []
        keyout1 = bitarray(32)
        keyout2 = bitarray(32)

        for i in range(28):
            t.append(bitarray(size))
        for i in range(64):
            m.append(bitarray(size))
        for i in range(8):
            out1.append(bitarray(size))
            out2.append(bitarray(size))

        L = [[]]*30
        S = [[]]*8
        M = [[]]*18
        output = [[]]*8

        # Top linear layer
        t[1] = input[0] ^ input[3] 
        t[2] = input[0] ^ input[5]
        t[3] = input[0] ^ input[6]
        t[4] = input[3] ^ input[5]
        t[5] = input[4] ^ input[6]
        t[6] = t[1] ^ t[5]
        t[7] = input[1] ^ input[2]
        t[8] = input[7] ^ t[6]
        t[9] = input[7] ^ t[7]
        t[10] = t[6] ^ t[7]
        t[11] = input[1] ^ input[5]
        t[12] = input[2] ^ input[5]
        t[13] = t[3] ^ t[4]
        t[14] = t[6] ^ t[11]
        t[15] = t[5] ^ t[11]
        t[16] = t[5] ^ t[12]
        t[17] = t[9] ^ t[16]
        t[18] = input[3] ^ input[7]
        t[19] = t[7] ^ t[18]
        t[20] = t[1] ^ t[19]
        t[21] = input[6] ^ input[7]
        t[22] = t[7] ^ t[21]
        t[23] = t[2] ^ t[22]
        t[24] = t[2] ^ t[10]
        t[25] = t[20]^ t[17]
        t[26] = t[3] ^ t[16]
        t[27] = t[1] ^ t[12]

        # Middle non-linear
        m[1] = AND(t[13], t[6], size)
        m[2] = AND(t[23], t[8], size)
        m[4] = AND(t[19], input[7], size)
        m[6] = AND(t[3], t[16], size)
        m[7] = AND(t[22], t[9], size)
        m[9] = AND(t[20], t[17], size)
        m[11] = AND(t[1], t[15], size)
        m[12] = AND(t[4], t[27], size)
        m[14] = AND(t[2], t[10], size)
        m[3] = t[14] ^ m[1]
        m[5] = m[4] ^ m[1]
        m[8] = t[26] ^ m[6]
        m[10] = m[9] ^ m[6]
        m[13] = m[12] ^ m[11]
        m[15] = m[14] ^ m[11]
        m[16] = m[3] ^ m[2]
        m[17] = m[5] ^ t[24]
        m[18] = m[8] ^ m[7]
        m[19] = m[10] ^ m[15]
        m[20] = m[16] ^ m[13]
        m[21] = m[17] ^ m[15]
        m[22] = m[18] ^ m[13]
        m[23] = m[19] ^ t[25]
        m[24] = m[22] ^ m[23]
        m[27] = m[20] ^ m[21]
  
        # depth 1 till here
        m[25] = AND(m[22], m[20], size)
        m[31] = AND(m[20], m[23], size)
        m[34] = AND(m[21], m[22], size)
        m[26] = m[21] ^ m[25]
        m[28] = m[23] ^ m[25]
        m[33] = m[27] ^ m[25]
        m[36] = m[24] ^ m[25]

        # depth 3 start
        m[29] = AND(m[28], m[27], size)
        m[30] = AND(m[26], m[24], size)
        m[32] = AND(m[27], m[31], size)
        m[35] = AND(m[24], m[34], size)
        m[37] = m[21] ^ m[29]
        m[38] = m[32] ^ m[33]
        m[39] = m[23] ^ m[30] 
        m[40] = m[35] ^ m[36] 
        m[41] = m[38] ^ m[40]
        m[42] = m[37] ^ m[39]
        m[43] = m[37] ^ m[38]
        m[44] = m[39] ^ m[40] 
        m[45] = m[42] ^ m[41]

        M[0] = AND1(m[44], t[6], size)
        M[1] = AND1(m[40], t[8], size)
        M[2] = AND1(m[39], input[7], size)
        M[3] = AND1(m[43], t[16], size)
        M[4] = AND1(m[38], t[9], size)
        M[5] = AND1(m[37], t[17], size)
        M[6] = AND1(m[42], t[15], size)
        M[7] = AND1(m[45], t[27], size)
        M[8] = AND1(m[41], t[10], size)
        M[9] = AND1(m[44], t[13], size)
        M[10] = AND1(m[40], t[23], size)
        M[11] = AND1(m[39], t[19], size)
        M[12] = AND1(m[43], t[3], size)
        M[13] = AND1(m[38], t[22], size)
        M[14] = AND1(m[37], t[20], size)
        M[15] = AND1(m[42], t[1], size)
        M[16] = AND1(m[45], t[4], size)
        M[17] = AND1(m[41], t[2], size)

        # Bottom linear
        L[0] = OR(M[15], M[16])
        L[1] = OR(M[4], M[10])
        L[2] = OR(M[0], M[2])
        L[3] = OR(M[1], M[9])
        L[4] = OR(M[8], M[12])
        L[5] = OR(M[3], M[15])
        L[6] = OR(M[16], L[5])
        L[7] = OR(M[0], L[3])
        L[8] = OR(M[5], M[13])
        L[9] = OR(M[6], M[7])
        L[10] = OR(M[7], L[4])
        L[11] = OR(M[14], L[2])
        L[12] = OR(M[2], M[5])
        L[13] = OR(M[4], L[0])
        L[14] = OR(M[6], M[15])
        L[15] = OR(M[9], L[1])
        L[16] = OR(M[10], L[0])
        L[17] = OR(M[11], L[1])
        L[18] = OR(M[12], L[8])
        L[19] = OR(M[17], L[4])
        L[20] = OR(L[0], L[1])
        L[21] = OR(L[1], L[7])
        L[22] = OR(L[3], L[12])
        L[23] = OR(L[18], L[2])
        L[24] = OR(L[15], L[9])
        L[25] = OR(L[6], L[10])
        L[26] = OR(L[7], L[9])
        L[27] = OR(L[8], L[10])
        L[28] = OR(L[11], L[14])
        L[29] = OR(L[11], L[17])
        S[0] = OR(L[6], L[24])
        S[1] = OR(L[16], L[26])
        S[2] = OR(L[19], L[28])
        S[3] = OR(L[6], L[21])
        S[4] = OR(L[20], L[22])
        S[5] = OR(L[25], L[29])
        S[6] = OR(L[13], L[27])
        S[7] = OR(L[6], L[23])
        S[1] = OR(S[1], (bitarray("1"*size), bitarray("1"*size)))
        S[2] = OR(S[2], (bitarray("1"*size), bitarray("1"*size)))
        S[6] = OR(S[6], (bitarray("1"*size), bitarray("1"*size)))
        S[7] = OR(S[7], (bitarray("1"*size), bitarray("1"*size)))

        for i in range(8):
            output[i] = S[i]
            if(len(S[i]) == 1):  
                out1[i] = output[i][0]
            else:
                out1[i] = output[i][0]
                out2[i] = output[i][1]

        Output1 = []
        for i in range(f):
            Output1.append(bitarray(128))
        for i in range(8):
            l = 0
            for k in range(f):
                for j in range(16):
                    Output1[k][8*j+i] = out1[i][l]
                    l += 1
            for k in range(4):
                keyout1[8*k + i] = out1[i][l]
                l += 1
                    
            
    
        if(len(S[0]) == 1):
            return Output1, keyout1
        else:
            Output2 = []
            for i in range(f):
                Output2.append(bitarray(128))
            for i in range(8):
                l = 0
                for k in range(f):
                    for j in range(16):
                        Output2[k][8*j+i] = out2[i][l]
                        l += 1
                for k in range(4):
                    keyout2[8*k + i] = out2[i][l]
                    l += 1
            return [Output1, Output2], [keyout1, keyout2]

    def SBox_offline(self, input: bitarray(8), AND, AND1, OR) -> bitarray(8):

        t = bitarray(28)
        m = bitarray(64)
        L = [[]]*30
        S = [[]]*8
        M = [[]]*18

        output = [[]]*8
        out1 = bitarray(8)
        out2 = bitarray(8)

        # Top linear layer
        t[1] = input[0] ^ input[3] 
        t[2] = input[0] ^ input[5]
        t[3] = input[0] ^ input[6]
        t[4] = input[3] ^ input[5]
        t[5] = input[4] ^ input[6]
        t[6] = t[1] ^ t[5]
        t[7] = input[1] ^ input[2]
        t[8] = input[7] ^ t[6]
        t[9] = input[7] ^ t[7]
        t[10] = t[6] ^ t[7]
        t[11] = input[1] ^ input[5]
        t[12] = input[2] ^ input[5]
        t[13] = t[3] ^ t[4]
        t[14] = t[6] ^ t[11]
        t[15] = t[5] ^ t[11]
        t[16] = t[5] ^ t[12]
        t[17] = t[9] ^ t[16]
        t[18] = input[3] ^ input[7]
        t[19] = t[7] ^ t[18]
        t[20] = t[1] ^ t[19]
        t[21] = input[6] ^ input[7]
        t[22] = t[7] ^ t[21]
        t[23] = t[2] ^ t[22]
        t[24] = t[2] ^ t[10]
        t[25] = t[20]^ t[17]
        t[26] = t[3] ^ t[16]
        t[27] = t[1] ^ t[12]

        # Middle non-linear
        m[1] = ba2int(AND(t[13], t[6]))
        m[2] = ba2int(AND(t[23], t[8]))
        m[4] = ba2int(AND(t[19], input[7]))
        m[6] = ba2int(AND(t[3], t[16]))
        m[7] = ba2int(AND(t[22], t[9]))
        m[9] = ba2int(AND(t[20], t[17]))
        m[11] = ba2int(AND(t[1], t[15]))
        m[12] = ba2int(AND(t[4], t[27]))
        m[14] = ba2int(AND(t[2], t[10]))
        m[3] = t[14] ^ m[1]
        m[5] = m[4] ^ m[1]
        m[8] = t[26] ^ m[6]
        m[10] = m[9] ^ m[6]
        m[13] = m[12] ^ m[11]
        m[15] = m[14] ^ m[11]
        m[16] = m[3] ^ m[2]
        m[17] = m[5] ^ t[24]
        m[18] = m[8] ^ m[7]
        m[19] = m[10] ^ m[15]
        m[20] = m[16] ^ m[13]
        m[21] = m[17] ^ m[15]
        m[22] = m[18] ^ m[13]
        m[23] = m[19] ^ t[25]
        m[24] = m[22] ^ m[23]
        m[27] = m[20] ^ m[21]
  
        # depth 1 till here
        m[25] = ba2int(AND(m[22], m[20]))
        m[31] = ba2int(AND(m[20], m[23]))
        m[34] = ba2int(AND(m[21], m[22]))
        m[26] = m[21] ^ m[25]
        m[28] = m[23] ^ m[25]
        m[33] = m[27] ^ m[25]
        m[36] = m[24] ^ m[25]

        # depth 3 start
        m[29] = ba2int(AND(m[28], m[27]))
        m[30] = ba2int(AND(m[26], m[24]))
        m[32] = ba2int(AND(m[27], m[31]))
        m[35] = ba2int(AND(m[24], m[34]))
        m[37] = m[21] ^ m[29]
        m[38] = m[32] ^ m[33]
        m[39] = m[23] ^ m[30] 
        m[40] = m[35] ^ m[36] 
        m[41] = m[38] ^ m[40]
        m[42] = m[37] ^ m[39]
        m[43] = m[37] ^ m[38]
        m[44] = m[39] ^ m[40] 
        m[45] = m[42] ^ m[41]

        M[0] = AND1(m[44], t[6])
        M[1] = AND1(m[40], t[8])
        M[2] = AND1(m[39], input[7])
        M[3] = AND1(m[43], t[16])
        M[4] = AND1(m[38], t[9])
        M[5] = AND1(m[37], t[17])
        M[6] = AND1(m[42], t[15])
        M[7] = AND1(m[45], t[27])
        M[8] = AND1(m[41], t[10])
        M[9] = AND1(m[44], t[13])
        M[10] = AND1(m[40], t[23])
        M[11] = AND1(m[39], t[19])
        M[12] = AND1(m[43], t[3])
        M[13] = AND1(m[38], t[22])
        M[14] = AND1(m[37], t[20])
        M[15] = AND1(m[42], t[1])
        M[16] = AND1(m[45], t[4])
        M[17] = AND1(m[41], t[2])

        # Bottom linear
        L[0] = OR(M[15], M[16])
        L[1] = OR(M[4], M[10])
        L[2] = OR(M[0], M[2])
        L[3] = OR(M[1], M[9])
        L[4] = OR(M[8], M[12])
        L[5] = OR(M[3], M[15])
        L[6] = OR(M[16], L[5])
        L[7] = OR(M[0], L[3])
        L[8] = OR(M[5], M[13])
        L[9] = OR(M[6], M[7])
        L[10] = OR(M[7], L[4])
        L[11] = OR(M[14], L[2])
        L[12] = OR(M[2], M[5])
        L[13] = OR(M[4], L[0])
        L[14] = OR(M[6], M[15])
        L[15] = OR(M[9], L[1])
        L[16] = OR(M[10], L[0])
        L[17] = OR(M[11], L[1])
        L[18] = OR(M[12], L[8])
        L[19] = OR(M[17], L[4])
        L[20] = OR(L[0], L[1])
        L[21] = OR(L[1], L[7])
        L[22] = OR(L[3], L[12])
        L[23] = OR(L[18], L[2])
        L[24] = OR(L[15], L[9])
        L[25] = OR(L[6], L[10])
        L[26] = OR(L[7], L[9])
        L[27] = OR(L[8], L[10])
        L[28] = OR(L[11], L[14])
        L[29] = OR(L[11], L[17])
        S[0] = OR(L[6], L[24])
        S[1] = OR(L[16], L[26])
        S[2] = OR(L[19], L[28])
        S[3] = OR(L[6], L[21])
        S[4] = OR(L[20], L[22])
        S[5] = OR(L[25], L[29])
        S[6] = OR(L[13], L[27])
        S[7] = OR(L[6], L[23])
        S[1] = OR(S[1], (bitarray("1"), bitarray("1")))
        S[2] = OR(S[2], (bitarray("1"), bitarray("1")))
        S[6] = OR(S[6], (bitarray("1"), bitarray("1")))
        S[7] = OR(S[7], (bitarray("1"), bitarray("1")))

        for i in range(8):
            output[i] = S[i]
            if(len(S[i]) == 1):  
                out1[i] = ba2int(output[i][0])
            else:
                out1[i] = ba2int(output[i][0])
                out2[i] = ba2int(output[i][1])
        
        if(len(S[0]) == 1):
            return out1
        else:
            return [out1, out2]

    def SBox_online(self, input: bitarray(8), AND, AND1, OR, Serv: Server1 | Server2) -> bitarray(8):

        t = bitarray(28)
        m = bitarray(64)
        L = [[]]*30
        S = [[]]*8
        M = [[]]*18

        output = [[]]*8
        out1 = bitarray(8)
        out2 = bitarray(8)

        # Top linear layer
        t[1] = input[0] ^ input[3] 
        t[2] = input[0] ^ input[5]
        t[3] = input[0] ^ input[6]
        t[4] = input[3] ^ input[5]
        t[5] = input[4] ^ input[6]
        t[6] = t[1] ^ t[5]
        t[7] = input[1] ^ input[2]
        t[8] = input[7] ^ t[6]
        t[9] = input[7] ^ t[7]
        t[10] = t[6] ^ t[7]
        t[11] = input[1] ^ input[5]
        t[12] = input[2] ^ input[5]
        t[13] = t[3] ^ t[4]
        t[14] = t[6] ^ t[11]
        t[15] = t[5] ^ t[11]
        t[16] = t[5] ^ t[12]
        t[17] = t[9] ^ t[16]
        t[18] = input[3] ^ input[7]
        t[19] = t[7] ^ t[18]
        t[20] = t[1] ^ t[19]
        t[21] = input[6] ^ input[7]
        t[22] = t[7] ^ t[21]
        t[23] = t[2] ^ t[22]
        t[24] = t[2] ^ t[10]
        t[25] = t[20]^ t[17]
        t[26] = t[3] ^ t[16]
        t[27] = t[1] ^ t[12]

        # Middle non-linear - depth 1 start
        temp = [AND(t[13], t[6]),
        AND(t[23], t[8]),
        AND(t[19], input[7]),
        AND(t[3], t[16]),
        AND(t[22], t[9]),
        AND(t[20], t[17]),
        AND(t[1], t[15]),
        AND(t[4], t[27]),
        AND(t[2], t[10])]
        temp2 = Serv.complete_optimised_online(temp)
        m[1] = ba2int(temp[0] ^ temp2[0])
        m[2] = ba2int(temp[1] ^ temp2[1])
        m[4] = ba2int(temp[2] ^ temp2[2])
        m[6] = ba2int(temp[3] ^ temp2[3])
        m[7] = ba2int(temp[4] ^ temp2[4])
        m[9] = ba2int(temp[5] ^ temp2[5])
        m[11] = ba2int(temp[6] ^ temp2[6])
        m[12] = ba2int(temp[7] ^ temp2[7])
        m[14] = ba2int(temp[8] ^ temp2[8])

        m[3] = t[14] ^ m[1]
        m[5] = m[4] ^ m[1]
        m[8] = t[26] ^ m[6]
        m[10] = m[9] ^ m[6]
        m[13] = m[12] ^ m[11]
        m[15] = m[14] ^ m[11]
        m[16] = m[3] ^ m[2]
        m[17] = m[5] ^ t[24]
        m[18] = m[8] ^ m[7]
        m[19] = m[10] ^ m[15]
        m[20] = m[16] ^ m[13]
        m[21] = m[17] ^ m[15]
        m[22] = m[18] ^ m[13]
        m[23] = m[19] ^ t[25]
        m[24] = m[22] ^ m[23]
        m[27] = m[20] ^ m[21]
  
        # depth 2 starts here
        temp = [
        AND(m[22], m[20]),
        AND(m[20], m[23]),
        AND(m[21], m[22])]
        temp2 = Serv.complete_optimised_online(temp)
        m[25] = ba2int(temp[0] ^ temp2[0])
        m[31] = ba2int(temp[1] ^ temp2[1])
        m[34] = ba2int(temp[2] ^ temp2[2])

        m[26] = m[21] ^ m[25]
        m[28] = m[23] ^ m[25]
        m[33] = m[27] ^ m[25]
        m[36] = m[24] ^ m[25]

        # depth 3 start
        temp = [AND(m[28], m[27]),
        AND(m[26], m[24]),
        AND(m[27], m[31]),
        AND(m[24], m[34])]
        temp2 = Serv.complete_optimised_online(temp)
        m[29] = ba2int(temp[0] ^ temp2[0])
        m[30] = ba2int(temp[1] ^ temp2[1])
        m[32] = ba2int(temp[2] ^ temp2[2])
        m[35] = ba2int(temp[3] ^ temp2[3])
        m[37] = m[21] ^ m[29]
        m[38] = m[32] ^ m[33]
        m[39] = m[23] ^ m[30] 
        m[40] = m[35] ^ m[36] 
        m[41] = m[38] ^ m[40]
        m[42] = m[37] ^ m[39]
        m[43] = m[37] ^ m[38]
        m[44] = m[39] ^ m[40] 
        m[45] = m[42] ^ m[41]

        # depth 4 start

        temp = [AND1(m[44], t[6]),
        AND1(m[40], t[8]),
        AND1(m[39], input[7]),
        AND1(m[43], t[16]),
        AND1(m[38], t[9]),
        AND1(m[37], t[17]),
        AND1(m[42], t[15]),
        AND1(m[45], t[27]),
        AND1(m[41], t[10]),
        AND1(m[44], t[13]),
        AND1(m[40], t[23]),
        AND1(m[39], t[19]),
        AND1(m[43], t[3]),
        AND1(m[38], t[22]),
        AND1(m[37], t[20]),
        AND1(m[42], t[1]),
        AND1(m[45], t[4]),
        AND1(m[41], t[2])]
        temp2 = Serv.complete_optimised_online(temp)
        M[0] = OR(temp[0], temp2[0])
        M[1] = OR(temp[1], temp2[1])
        M[2] = OR(temp[2], temp2[2])
        M[3] = OR(temp[3], temp2[3])
        M[4] = OR(temp[4], temp2[4])
        M[5] = OR(temp[5], temp2[5])
        M[6] = OR(temp[6], temp2[6])
        M[7] = OR(temp[7], temp2[7])
        M[8] = OR(temp[8], temp2[8])
        M[9] = OR(temp[9], temp2[9])
        M[10] = OR(temp[10], temp2[10])
        M[11] = OR(temp[11], temp2[11])
        M[12] = OR(temp[12], temp2[12])
        M[13] = OR(temp[13], temp2[13])
        M[14] = OR(temp[14], temp2[14])
        M[15] = OR(temp[15], temp2[15])
        M[16] = OR(temp[16], temp2[16])
        M[17] = OR(temp[17], temp2[17])

        # Bottom linear
        L[0] = OR(M[15], M[16])
        L[1] = OR(M[4], M[10])
        L[2] = OR(M[0], M[2])
        L[3] = OR(M[1], M[9])
        L[4] = OR(M[8], M[12])
        L[5] = OR(M[3], M[15])
        L[6] = OR(M[16], L[5])
        L[7] = OR(M[0], L[3])
        L[8] = OR(M[5], M[13])
        L[9] = OR(M[6], M[7])
        L[10] = OR(M[7], L[4])
        L[11] = OR(M[14], L[2])
        L[12] = OR(M[2], M[5])
        L[13] = OR(M[4], L[0])
        L[14] = OR(M[6], M[15])
        L[15] = OR(M[9], L[1])
        L[16] = OR(M[10], L[0])
        L[17] = OR(M[11], L[1])
        L[18] = OR(M[12], L[8])
        L[19] = OR(M[17], L[4])
        L[20] = OR(L[0], L[1])
        L[21] = OR(L[1], L[7])
        L[22] = OR(L[3], L[12])
        L[23] = OR(L[18], L[2])
        L[24] = OR(L[15], L[9])
        L[25] = OR(L[6], L[10])
        L[26] = OR(L[7], L[9])
        L[27] = OR(L[8], L[10])
        L[28] = OR(L[11], L[14])
        L[29] = OR(L[11], L[17])
        S[0] = OR(L[6], L[24])
        S[1] = OR(L[16], L[26])
        S[2] = OR(L[19], L[28])
        S[3] = OR(L[6], L[21])
        S[4] = OR(L[20], L[22])
        S[5] = OR(L[25], L[29])
        S[6] = OR(L[13], L[27])
        S[7] = OR(L[6], L[23])
        S[1] = OR(S[1], (bitarray("1"), bitarray("1")))
        S[2] = OR(S[2], (bitarray("1"), bitarray("1")))
        S[6] = OR(S[6], (bitarray("1"), bitarray("1")))
        S[7] = OR(S[7], (bitarray("1"), bitarray("1")))

        for i in range(8):
            output[i] = S[i]
            if(len(S[i]) == 1):  
                out1[i] = ba2int(output[i][0])
            else:
                out1[i] = ba2int(output[i][0])
                out2[i] = ba2int(output[i][1])
        
        if(len(S[0]) == 1):
            return out1
        else:
            return [out1, out2]
    
    def Optimized_SBox_online(self, fingerprints: list[bitarray], keyinput: bitarray, AND, AND1, OR, Serv: Server1 | Server2):

        f = len(fingerprints)

        size = 16 * f + 4

        input = []
        for i in range(8):
            l = 0
            temp = bitarray(size)
            for j in range(f):
                for k in range(16):
                    temp[l] = fingerprints[j][8*k + i]
                    l += 1
            # input.append(temp)
            for j in range(4):
                temp[l] = keyinput[8*j + i]
                l += 1
            input.append(temp)
        
        t = []
        m = []
        out1 = []
        keyout1 = bitarray(32)

        for i in range(28):
            t.append(bitarray(size))
        for i in range(64):
            m.append(bitarray(size))
        for i in range(8):
            out1.append(bitarray(size))

        L = [[]]*30
        S = [[]]*8
        M = [[]]*18

        # Top linear layer
        t[1] = input[0] ^ input[3] 
        t[2] = input[0] ^ input[5]
        t[3] = input[0] ^ input[6]
        t[4] = input[3] ^ input[5]
        t[5] = input[4] ^ input[6]
        t[6] = t[1] ^ t[5]
        t[7] = input[1] ^ input[2]
        t[8] = input[7] ^ t[6]
        t[9] = input[7] ^ t[7]
        t[10] = t[6] ^ t[7]
        t[11] = input[1] ^ input[5]
        t[12] = input[2] ^ input[5]
        t[13] = t[3] ^ t[4]
        t[14] = t[6] ^ t[11]
        t[15] = t[5] ^ t[11]
        t[16] = t[5] ^ t[12]
        t[17] = t[9] ^ t[16]
        t[18] = input[3] ^ input[7]
        t[19] = t[7] ^ t[18]
        t[20] = t[1] ^ t[19]
        t[21] = input[6] ^ input[7]
        t[22] = t[7] ^ t[21]
        t[23] = t[2] ^ t[22]
        t[24] = t[2] ^ t[10]
        t[25] = t[20]^ t[17]
        t[26] = t[3] ^ t[16]
        t[27] = t[1] ^ t[12]

        # Middle non-linear - depth 1 start
        temp = [AND(t[13], t[6]),
        AND(t[23], t[8]),
        AND(t[19], input[7]),
        AND(t[3], t[16]),
        AND(t[22], t[9]),
        AND(t[20], t[17]),
        AND(t[1], t[15]),
        AND(t[4], t[27]),
        AND(t[2], t[10])]
        temp2 = Serv.complete_optimised_online(temp)
        m[1] = temp[0] ^ temp2[0]
        m[2] = temp[1] ^ temp2[1]
        m[4] = temp[2] ^ temp2[2]
        m[6] = temp[3] ^ temp2[3]
        m[7] = temp[4] ^ temp2[4]
        m[9] = temp[5] ^ temp2[5]
        m[11] = temp[6] ^ temp2[6]
        m[12] = temp[7] ^ temp2[7]
        m[14] = temp[8] ^ temp2[8]

        m[3] = t[14] ^ m[1]
        m[5] = m[4] ^ m[1]
        m[8] = t[26] ^ m[6]
        m[10] = m[9] ^ m[6]
        m[13] = m[12] ^ m[11]
        m[15] = m[14] ^ m[11]
        m[16] = m[3] ^ m[2]
        m[17] = m[5] ^ t[24]
        m[18] = m[8] ^ m[7]
        m[19] = m[10] ^ m[15]
        m[20] = m[16] ^ m[13]
        m[21] = m[17] ^ m[15]
        m[22] = m[18] ^ m[13]
        m[23] = m[19] ^ t[25]
        m[24] = m[22] ^ m[23]
        m[27] = m[20] ^ m[21]
  
        # depth 2 starts here
        temp = [
        AND(m[22], m[20]),
        AND(m[20], m[23]),
        AND(m[21], m[22])]
        temp2 = Serv.complete_optimised_online(temp)
        m[25] = temp[0] ^ temp2[0]
        m[31] = temp[1] ^ temp2[1]
        m[34] = temp[2] ^ temp2[2]

        m[26] = m[21] ^ m[25]
        m[28] = m[23] ^ m[25]
        m[33] = m[27] ^ m[25]
        m[36] = m[24] ^ m[25]

        # depth 3 start
        temp = [AND(m[28], m[27]),
        AND(m[26], m[24]),
        AND(m[27], m[31]),
        AND(m[24], m[34])]
        temp2 = Serv.complete_optimised_online(temp)
        m[29] = temp[0] ^ temp2[0]
        m[30] = temp[1] ^ temp2[1]
        m[32] = temp[2] ^ temp2[2]
        m[35] = temp[3] ^ temp2[3]
        m[37] = m[21] ^ m[29]
        m[38] = m[32] ^ m[33]
        m[39] = m[23] ^ m[30] 
        m[40] = m[35] ^ m[36] 
        m[41] = m[38] ^ m[40]
        m[42] = m[37] ^ m[39]
        m[43] = m[37] ^ m[38]
        m[44] = m[39] ^ m[40] 
        m[45] = m[42] ^ m[41]

        # depth 4 start

        temp = [AND1(m[44], t[6]),
        AND1(m[40], t[8]),
        AND1(m[39], input[7]),
        AND1(m[43], t[16]),
        AND1(m[38], t[9]),
        AND1(m[37], t[17]),
        AND1(m[42], t[15]),
        AND1(m[45], t[27]),
        AND1(m[41], t[10]),
        AND1(m[44], t[13]),
        AND1(m[40], t[23]),
        AND1(m[39], t[19]),
        AND1(m[43], t[3]),
        AND1(m[38], t[22]),
        AND1(m[37], t[20]),
        AND1(m[42], t[1]),
        AND1(m[45], t[4]),
        AND1(m[41], t[2])]
        temp2 = Serv.complete_optimised_online(temp)
        M[0] = OR(temp[0], temp2[0])
        M[1] = OR(temp[1], temp2[1])
        M[2] = OR(temp[2], temp2[2])
        M[3] = OR(temp[3], temp2[3])
        M[4] = OR(temp[4], temp2[4])
        M[5] = OR(temp[5], temp2[5])
        M[6] = OR(temp[6], temp2[6])
        M[7] = OR(temp[7], temp2[7])
        M[8] = OR(temp[8], temp2[8])
        M[9] = OR(temp[9], temp2[9])
        M[10] = OR(temp[10], temp2[10])
        M[11] = OR(temp[11], temp2[11])
        M[12] = OR(temp[12], temp2[12])
        M[13] = OR(temp[13], temp2[13])
        M[14] = OR(temp[14], temp2[14])
        M[15] = OR(temp[15], temp2[15])
        M[16] = OR(temp[16], temp2[16])
        M[17] = OR(temp[17], temp2[17])

        # Bottom linear
        L[0] = OR(M[15], M[16])
        L[1] = OR(M[4], M[10])
        L[2] = OR(M[0], M[2])
        L[3] = OR(M[1], M[9])
        L[4] = OR(M[8], M[12])
        L[5] = OR(M[3], M[15])
        L[6] = OR(M[16], L[5])
        L[7] = OR(M[0], L[3])
        L[8] = OR(M[5], M[13])
        L[9] = OR(M[6], M[7])
        L[10] = OR(M[7], L[4])
        L[11] = OR(M[14], L[2])
        L[12] = OR(M[2], M[5])
        L[13] = OR(M[4], L[0])
        L[14] = OR(M[6], M[15])
        L[15] = OR(M[9], L[1])
        L[16] = OR(M[10], L[0])
        L[17] = OR(M[11], L[1])
        L[18] = OR(M[12], L[8])
        L[19] = OR(M[17], L[4])
        L[20] = OR(L[0], L[1])
        L[21] = OR(L[1], L[7])
        L[22] = OR(L[3], L[12])
        L[23] = OR(L[18], L[2])
        L[24] = OR(L[15], L[9])
        L[25] = OR(L[6], L[10])
        L[26] = OR(L[7], L[9])
        L[27] = OR(L[8], L[10])
        L[28] = OR(L[11], L[14])
        L[29] = OR(L[11], L[17])
        S[0] = OR(L[6], L[24])
        S[1] = OR(L[16], L[26])
        S[2] = OR(L[19], L[28])
        S[3] = OR(L[6], L[21])
        S[4] = OR(L[20], L[22])
        S[5] = OR(L[25], L[29])
        S[6] = OR(L[13], L[27])
        S[7] = OR(L[6], L[23])
        S[1] = OR(S[1], (bitarray("1"*size), bitarray("1"*size)))
        S[2] = OR(S[2], (bitarray("1"*size), bitarray("1"*size)))
        S[6] = OR(S[6], (bitarray("1"*size), bitarray("1"*size)))
        S[7] = OR(S[7], (bitarray("1"*size), bitarray("1"*size)))

        for i in range(8):
            out1[i] = S[i][0]

        Output1 = []
        for i in range(f):
            Output1.append(bitarray(128))
        
        for i in range(8):
            l = 0
            for k in range(f):
                for j in range(16):
                    Output1[k][8*j+i] = out1[i][l]
                    l += 1
            for k in range(4):
                keyout1[8*k + i] = out1[i][l]
                l += 1
    
        if(len(S[0]) == 1):
            return Output1, keyout1
    
    def R(self, round):
        a = []
        temp = bitarray("00000001")
        a.append(temp)

        for i in range(9):
            a.append(self.times(a[i]))

        return a[round]

    def g_offline(self, sboxoutput: bitarray, round, S: Server0 | Server1 | Server2) -> bitarray:
        output = []

        if S.id() == 0:
            sboxoutput1 = sboxoutput[0]
            sboxoutput2 = sboxoutput[1]
            v0 = sboxoutput1[0:8]
            v1 = sboxoutput1[8:16]
            v2 = sboxoutput1[16:24]
            v3 = sboxoutput1[24:32]

            sboxoutput1[0:8] = v1 ^ self.R(round - 1)
            sboxoutput1[8:16] = v2
            sboxoutput1[16:24] = v3
            sboxoutput1[24:32] = v0

            v0 = sboxoutput2[0:8]
            v1 = sboxoutput2[8:16]
            v2 = sboxoutput2[16:24]
            v3 = sboxoutput2[24:32]

            sboxoutput2[0:8] = v1 ^ self.R(round - 1)
            sboxoutput2[8:16] = v2
            sboxoutput2[16:24] = v3
            sboxoutput2[24:32] = v0
            output.append(sboxoutput1)
            output.append(sboxoutput2)

        else:
            v0 = sboxoutput[0:8]
            v1 = sboxoutput[8:16]
            v2 = sboxoutput[16:24]
            v3 = sboxoutput[24:32]

            sboxoutput[0:8] = v1 ^ self.R(round - 1)
            sboxoutput[8:16] = v2
            sboxoutput[16:24] = v3
            sboxoutput[24:32] = v0
            
            output.append(sboxoutput)
        
        return output
    
    def g_online(self, sboxoutput: bitarray, round, S: Server1 | Server2) -> bitarray:
        v0 = sboxoutput[0:8]
        v1 = sboxoutput[8:16]
        v2 = sboxoutput[16:24]
        v3 = sboxoutput[24:32]

        sboxoutput[0:8] = v1 ^ self.R(round - 1)
        sboxoutput[8:16] = v2
        sboxoutput[16:24] = v3
        sboxoutput[24:32] = v0

        output = []
        output.append(sboxoutput)
        return output

    def KeyGen_offline(self, key: bitarray | list[bitarray], sboxoutput: bitarray, round, S: Server0 | Server1 | Server2) -> bitarray:
        output = []
        if(S.id() == 0):
            key1 = key[0]
            key2 = key[1]

            w01 = key1[0:32]
            w11 = key1[32:64]
            w21 = key1[64:96]
            w1 = key1[96:128]
            w31 = key1[96:128]

            w02 = key2[0:32]
            w12 = key2[32:64]
            w22 = key2[64:96]
            w2 = key2[96:128]
            w32 = key2[96:128]

            temp = self.g_offline(sboxoutput, round, S)
            w01 = w01 ^ temp[0]
            w02 = w02 ^ temp[1]
            
            w11 = w01 ^ w11
            w21 = w11 ^ w21
            w31 = w21 ^ w31

            w12 = w02 ^ w12
            w22 = w12 ^ w22
            w32 = w22 ^ w32

            key1 = bitarray(128)
            key2 = bitarray(128)
            
            key1[0:32] = w01
            key1[32:64] = w11
            key1[64:96] = w21
            key1[96:128] = w31

            key2[0:32] = w02
            key2[32:64] = w12
            key2[64:96] = w22
            key2[96:128] = w32

            output.append(key1)
            output.append(key2)
            return output
        
        else:
            w0 = key[0:32]
            w1 = key[32:64]
            w2 = key[64:96]
            w = key[96:128]
            w3 = key[96:128]
            temp = self.g_offline(sboxoutput, round, S)
            w0 = w0 ^ temp[0]
            w1 = w0 ^ w1
            w2 = w1 ^ w2
            w3 = w2 ^ w3

            key[0:32] = w0
            key[32:64] = w1
            key[64:96] = w2 
            key[96:128] = w3

            output.append(key)
            return output
        
    def KeyGen_online(self, key: bitarray, sboxoutput: bitarray, round, S: Server1 | Server2) -> bitarray:
        output = []
        w0 = key[0:32]
        w1 = key[32:64]
        w2 = key[64:96]
        w = key[96:128]
        w3 = key[96:128]
        temp = self.g_online(sboxoutput, round, S)
        w0 = w0 ^ temp[0]
        w1 = w0 ^ w1
        w2 = w1 ^ w2
        w3 = w2 ^ w3

        key[0:32] = w0
        key[32:64] = w1
        key[64:96] = w2 
        key[96:128] = w3

        output.append(key)
        return output
        
    def circuit_offline(self, k: list[bitarray], m: list[list[bitarray]], S: Server0 | Server1 | Server2, output: list[Share]):
        
        # For Server 0
        if S.id() == 0:
        
        #Offline begins
            key = k.copy()
            states = []

            f = len(m[0])
            
            for i in range(f):
                message1 = m[0][i].copy()   
                message2 = m[1][i].copy()              
                states.append(message1 ^ message2 ^ key[0] ^ key[1]) # Key Addition
            

            
            for i in range(9):
                keysboxinp = key[0] ^ key[1]
                keysboxinp = keysboxinp[96:]
                temp, keytemp = self.Optimized_SBox_offline(states, keysboxinp, S.multibit_optimised_offline_AND, S.multibit_optimised_offline_AND1, S.OR, S)
                for j in range(f):
                    states[j] = temp[0][j] ^ temp[1][j]

                    states[j] = self.ShiftRow(states[j]) # Shift Row
                    states[j] = self.MixColumn(states[j]) # Mix Columns
                
                temp = self.KeyGen_offline([key[0], key[1]], keytemp, i + 1, S) # Key Generation
                if i == 0:
                    print()
                key[0] = temp[0]
                key[1] = temp[1]

                for j in range(f):
                    states[j] = states[j] ^ key[0] ^ key[1] # Key Addition

            state1 = []
            state2 = []

            for j in range(f):
                state1.append(bitarray(128))
                state2.append(bitarray(128))

            keysboxinp = key[0] ^ key[1]
            keysboxinp = keysboxinp[96:]
            
            temp, keytemp = self.Optimized_SBox_offline(states, keysboxinp, S.multibit_optimised_offline_AND, S.multibit_optimised_offline_AND1, S.OR, S)
            
            for j in range(f):
                state1[j] = temp[0][j]
                state2[j] = temp[1][j]
            
                state1[j] = self.ShiftRow(state1[j]) # Shift Row
                state2[j] = self.ShiftRow(state2[j])

            temp = self.KeyGen_offline([key[0], key[1]], keytemp, 10, S) # Final round key generation
            key[0] = temp[0]
            key[1] = temp[1] 
            
            for j in range(f):
                state1[j] = state1[j] ^ key[0] # Key Addition
                state2[j] = state2[j] ^ key[1]

            for j in range(f):
                output[j].add(state1[j])
                output[j].add(state2[j])
            # S.complete_optimised_offline()
        #Offline ends


        # For Server 1
        else:

        #Offline begins
            key = k[0].copy()
            states = []

            f = len(m[0])
            for i in range(f):
                message = m[0][i].copy()              
                states.append(message ^ key) # Key Addition
                   
            for i in range(9):
                keysboxinp = key[96:]
                states, keysboxout = self.Optimized_SBox_offline(states, keysboxinp, S.multibit_optimised_offline_AND, S.multibit_optimised_offline_AND1, S.OR, S)

                for j in range(f):
                    states[j] = self.ShiftRow(states[j]) # Shift Row
                    states[j] = self.MixColumn(states[j]) # Mix Columns

                temp = self.KeyGen_offline(key, keysboxout, i + 1, S) # Key Generation
                key = temp[0]

                for j in range(f):
                    states[j] = states[j] ^ key # Key Addition

            keysboxinp = key[96:]
            temp, keysboxout = self.Optimized_SBox_offline(states, keysboxinp, S.multibit_optimised_offline_AND, S.multibit_optimised_offline_AND1, S.OR, S)

            for j in range(f):
                states[j] = self.ShiftRow(temp[j]) # Shift Row

            
            temp = self.KeyGen_offline(key, keysboxout, 10, S) # Final round key generation
            key = temp[0]

            for j in range(f):
                states[j] = states[j] ^ key # Key Addition

            for j in range(f):
                output[j].add(states[j])
        #Offline ends

        # # For Server 2
        # if S.id() == 2:

        # #Offline begins
        #     key = k[0].copy()
        #     states = []

        #     f = len(m[0])
        #     for i in range(f):
        #         message = m[0][i].copy()              
        #         states.append(message ^ key) # Key Addition
        
        #     for i in range(9):
        #         states = self.Optimized_SBox_offline(states, S.multibit_optimised_offline_AND, S.multibit_optimised_offline_AND1, S.OR, S)

        #         for j in range(f):  
        #             states[j] = self.ShiftRow(states[j]) # Shift Row
        #             states[j] = self.MixColumn(states[j]) # Mix Columns

        #         temp = self.KeyGen_offline(key, i + 1, S) # Key Generation
        #         key = temp[0]

        #         for j in range(f):
        #             states[j] = states[j] ^ key # Key Addition
                
        #     temp = self.Optimized_SBox_offline(states, S.multibit_optimised_offline_AND, S.multibit_optimised_offline_AND1, S.OR, S)

        #     for j in range(f):
        #         states[j] = self.ShiftRow(temp[j]) # Shift Row

        #     temp = self.KeyGen_offline(key, 10, S) # Final round key generation
        #     key = temp[0]

        #     for j in range(f):
        #         states[j] = states[j] ^ key # Key Addition
        
        #     for j in range(f):
        #         output[j].add(states[j])
        # # Offline ends
        
    def circuit_online(self, k: list[bitarray], m: list[list[bitarray]], S: Server1 | Server2, output: list[Share]):
        
        state = None
        # For Server 1
        if S.id() != 0:
        #Online begins
            key = k[1].copy()
            states = []

            f = len(m[0])
            for i in range(f):
                message = m[1][i].copy()              
                states.append(message ^ key) # Key Addition
        
            for i in range(9):
                keysboxinp = key[96:]
                states, keysboxout = self.Optimized_SBox_online(states, keysboxinp, S.multibit_optimised_online_AND, S.multibit_optimised_online_AND1, S.OR, S) # Byte Substitution

                for j in range(f):
                    states[j] = self.ShiftRow(states[j]) # Shift Row
                    states[j] = self.MixColumn(states[j]) # Mix Columns

                temp = self.KeyGen_online(key, keysboxout, i + 1, S) # Key Generation
                key = temp[0]

                for j in range(f):
                    states[j] = states[j] ^ key # Key Addition

            keysboxinp = key[96:]
            states, keysboxinp = self.Optimized_SBox_online(states, keysboxinp, S.multibit_optimised_online_AND, S.multibit_optimised_online_AND1, S.OR, S) # Byte Substitution
            
            for j in range(f):
                states[j] = self.ShiftRow(states[j]) # Shift Row

            temp = self.KeyGen_online(key, keysboxinp, 10, S) # Final round key generation
            key = temp[0]

            for j in range(f):
                states[j] = states[j] ^ key # Key Addition

            for j in range(f):
                output[j].add(states[j])
        #Online ends

def RunAES(k: list[bitarray], m: list[bitarray], S:Server):
    aes = AES()
    if S.id() == 0:
        output = Share()
        aes.circuit_offline(k, [[m[0]], [m[1]]], S, [output])
        S.complete_optimised_offline()
        o = output.get()
        # print(ba2hex(o[0]), ba2hex(o[1]))
        p = S.online_reconstruction(o[0], o[1])
        print(ba2hex(p))
    elif S.id() == 1:
        output = Share()
        aes.circuit_offline(k, [[m[0]], [m[1]]], S, [output])
        aes.circuit_online(k, [[m[0]], [m[1]]], S, [output])
        o = output.get()
        # print(ba2hex(o[0]), ba2hex(o[1]))
        S.online_reconstruction(o[0], o[1])
    else:
        output = Share()
        aes.circuit_offline(k, [[m[0]], [m[1]]], S, [output])
        S.complete_optimised_offline()
        aes.circuit_online(k, [[m[0]], [m[1]]], S, [output])
        o = output.get()
        # print(ba2hex(o[0]), ba2hex(o[1]))
        S.online_reconstruction(o[0], o[1])

if __name__=='__main__':
    # message = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    message = bitarray("01010100011101110110111100100000010011110110111001100101001000000100111001101001011011100110010100100000010101000111011101101111")
    print("Message: ", ba2hex(message))
    l1 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    l2 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    m = l1 ^ l2 ^ message

    # key = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    key = bitarray("01010100011010000110000101110100011100110010000001101101011110010010000001001011011101010110111001100111001000000100011001110101")
    print("Key: ", ba2hex(key))
    k1 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    k2 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    mk = k1 ^ k2 ^ key


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

    aes = AES()
    o0 = Share()
    o1 = Share()
    o2 = Share()

    p0 = multiprocessing.Process(target=RunAES, args=([k1, k2], [l1, l2], S0))
    p1 = multiprocessing.Process(target=RunAES, args=([k1, mk], [l1, m], S1))
    p2 = multiprocessing.Process(target=RunAES, args=([k2, mk], [l2, m], S2))

    p0.start()
    p1.start()
    p2.start()

    p0.join()
    p1.join()
    p2.join()

    # p0 = multiprocessing.Process(target=aes.circuit_online, args=([k1, k2], [l1, l2], S0, o0))
    # p1 = multiprocessing.Process(target=aes.circuit_online, args=([k1, mk], [l1, m], S1, o1))
    # p2 = multiprocessing.Process(target=aes.circuit_online, args=([k2, mk], [l2, m], S2, o2))

    # p0.start()
    # p1.start()
    # p2.start()

    # p0.join()
    # p1.join()
    # p2.join()

    # o0 = o0.get()
    # o2 = o2.get()
    # print(ba2hex(o0[0] ^ o0[1] ^ o2[1]))