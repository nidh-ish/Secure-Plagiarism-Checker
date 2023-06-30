import random
from typing import List
import numpy as np
from server import * 
from bitarray import bitarray
from bitarray.util import *

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

    def SBox(self, input: bitarray(8), AND, AND1, OR) -> bitarray(8):

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

    def R(self, round):
        a = []
        temp = bitarray("00000001")
        a.append(temp)

        for i in range(9):
            a.append(self.times(a[i]))

        return a[round]

    def g_offline(self, input: bitarray, round, S: Server) -> bitarray:
        v0 = input[0:8]
        v1 = input[8:16]
        v2 = input[16:24]
        v3 = input[24:32]

        input[0:8] = v1
        input[8:16] = v2
        input[16:24] = v3
        input[24:32] = v0

        output = []

        if S.id() == 0:
            input1 = bitarray(32)
            input2 = bitarray(32)
            for i in range(4):
                temp = self.SBox(input[8*i:8*i + 8], S.offline_AND, S.offline_AND1, S.OR) # Byte Substitution
                input1[8*i:8*i + 8] = temp[0]
                input2[8*i:8*i + 8] = temp[1]
            v01 = input1[0:8]
            v02 = input2[0:8]
            v01 = v01 ^ self.R(round - 1)
            v02 = v02 ^ self.R(round - 1)
            input1[0:8] = v01
            input2[0:8] = v02
            output.append(input1)
            output.append(input2)

        else:
            for i in range(4):
                input[8*i:8*i + 8] = self.SBox(input[8*i:8*i + 8], S.offline_AND, S.offline_AND1, S.OR) # Byte Substitution
            v0 = input[0:8]
            v0 = v0 ^ self.R(round - 1)
            input[0:8] = v0
            output.append(input)
        
        return output
    
    def g_online(self, input: bitarray, round, S: Server) -> bitarray:
        v0 = input[0:8]
        v1 = input[8:16]
        v2 = input[16:24]
        v3 = input[24:32]

        input[0:8] = v1
        input[8:16] = v2
        input[16:24] = v3
        input[24:32] = v0

        output = []
        for i in range(4):
            input[8*i:8*i + 8] = self.SBox(input[8*i:8*i + 8], S.online_AND, S.online_AND1, S.OR) # Byte Substitution
        v0 = input[0:8]
        v0 = v0 ^ self.R(round - 1)
        input[0:8] = v0
        output.append(input)
    
        return output

    def KeyGen_offline(self, key: bitarray, round, S: Server) -> bitarray:
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

            temp = self.g_offline(w1 ^ w2, round, S)
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
            temp = self.g_offline(w, round, S)
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
        
    def KeyGen_online(self, key: bitarray, round, S: Server) -> bitarray:
        output = []
        w0 = key[0:32]
        w1 = key[32:64]
        w2 = key[64:96]
        w = key[96:128]
        w3 = key[96:128]
        temp = self.g_online(w, round, S)
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
        

    def circuit(self, k: List[bitarray], m: List[bitarray], S:Server, output: Share) -> bitarray:
        
        state = None

        # For Server 0
        if S.id() == 0:

        #Offline begins
            message = m
            key = k
            state = message[0] ^ message[1] ^ key[0] ^ key[1] # Key Addition
        
            for i in range(9):
                for j in range(16):
                    temp = self.SBox(state[8*j:8*(j+1)], S.offline_AND, S.offline_AND1, S.OR) # Byte Substitution
                    state[8*j:8*(j+1)] = temp[0] ^ temp[1]
                state = self.ShiftRow(state) # Shift Row
                state = self.MixColumn(state) # Mix Columns
                
                temp = self.KeyGen_offline([key[0], key[1]], i + 1, S) # Key Generation
                key[0] = temp[0]
                key[1] = temp[1]

                state = state ^ key[0] ^ key[1] # Key Addition

            state1 = bitarray(128)
            state2 = bitarray(128)

            for i in range(16):
                temp = self.SBox(state[8*i:8*i + 8], S.offline_AND, S.offline_AND1, S.OR) # Byte Substitution
                state1[8*i:8*i + 8] = temp[0]
                state2[8*i:8*i + 8] = temp[1]

            state1 = self.ShiftRow(state1) # Shift Row
            state2 = self.ShiftRow(state2)

            temp = self.KeyGen_offline([key[0], key[1]], 10, S) # Final round key generation
            key[0] = temp[0]
            key[1] = temp[1] 
            
            state1 = state1 ^ key[0] # Key Addition
            state2 = state2 ^ key[1]
            output.add(state1)
            output.add(state2)
        #Offline ends


        # For Server 1
        if S.id() == 1:

        #Offline begins
            message = m[0]
            key = k[0]
            state = message ^ key # Key Addition

            for i in range(9):
                for j in range(16):
                    state[8*j:8*(j+1)] = self.SBox(state[8*j:8*(j+1)], S.offline_AND, S.offline_AND1, S.OR) # Byte Substitution

                state = self.ShiftRow(state) # Shift Row
                state = self.MixColumn(state) # Mix Columns

                temp = self.KeyGen_offline(key, i + 1, S) # Key Generation
                key = temp[0]

                state = state ^ key # Key Addition

            for i in range(16):
                state[8*i:8*i + 8] = self.SBox(state[8*i:8*i + 8], S.offline_AND, S.offline_AND1, S.OR) # Byte Substitution            

            state = self.ShiftRow(state) # Shift Row

            temp = self.KeyGen_offline(key, 10, S) # Final round key generation
            key = temp[0]

            state = state ^ key # Key Addition

            offline_output = state
            output.add(offline_output)
        #Offline ends

        #Online begins
            message = m[1]
            key = k[1]
            state = message ^ key # Key Addition
        
            for i in range(9):
                for j in range(16):
                    state[8*j:8*(j+1)] = self.SBox(state[8*j:8*(j+1)], S.online_AND, S.online_AND1, S.OR) # Byte Substitution

                state = self.ShiftRow(state) # Shift Row
                state = self.MixColumn(state) # Mix Columns

                temp = self.KeyGen_online(key, i + 1, S) # Key Generation
                key = temp[0]

                state = state ^ key # Key Addition

            for i in range(16):
                state[8*i:8*i + 8] = self.SBox(state[8*i:8*i + 8], S.online_AND, S.online_AND1, S.OR) # Byte Substitution

            state = self.ShiftRow(state) # Shift Row

            temp = self.KeyGen_online(key, 10, S) # Final round key generation
            key = temp[0]

            state = state ^ key # Key Addition

            online_output = state
            output.add(online_output)
        #Online ends

        # For Server 2
        if S.id() == 2:

        #Offline begins
            message = m[0]
            key = k[0]
            state = message ^ key # Key Addition
        
            for i in range(9):
                for j in range(16):
                    state[8*j:8*(j+1)] = self.SBox(state[8*j:8*(j+1)], S.offline_AND, S.offline_AND1, S.OR) # Byte Substitution
                
                state = self.ShiftRow(state) # Shift Row
                state = self.MixColumn(state) # Mix Columns

                temp = self.KeyGen_offline(key, i + 1, S) # Key Generation
                key = temp[0]

                state = state ^ key # Key Addition
                
            for i in range(16):
                state[8*i:8*i + 8] = self.SBox(state[8*i:8*i + 8], S.offline_AND, S.offline_AND1, S.OR) # Byte Substitution
            
            state = self.ShiftRow(state) # Shift Row

            temp = self.KeyGen_offline(key, 10, S) # Final round key generation
            key = temp[0]

            state = state ^ key # Key Addition
        
            offline_output = state
            output.add(offline_output)
        # Offline ends

        #Online begins
            message = m[1]
            key = k[1]
            state = message ^ key # Key Addition
        
            for i in range(9):

                for j in range(16):
                    state[8*j:8*(j+1)] = self.SBox(state[8*j:8*(j+1)], S.online_AND, S.online_AND1, S.OR) # Byte Substitution
                
                state = self.ShiftRow(state) # Shift Row
                state = self.MixColumn(state) # Mix Columns

                temp = self.KeyGen_online(key, i + 1, S) # Key Generation
                key = temp[0]

                state = state ^ key # Key Addition

            for i in range(16):
                state[8*i:8*i + 8] = self.SBox(state[8*i:8*i + 8], S.online_AND, S.online_AND1, S.OR) # Byte Substitution
            
            state = self.ShiftRow(state) # Shift Row
            
            temp = self.KeyGen_online(key, 10, S) # Final round key generation
            key = temp[0]

            state = state ^ key # Key Addition
        
            online_output = state        
            output.add(online_output)
        #Online ends
        

# if __name__=='__main__':
#     # message = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
#     message = bitarray("01010100011101110110111100100000010011110110111001100101001000000100111001101001011011100110010100100000010101000111011101101111")
#     print("Message: ", ba2hex(message))

#     # key = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
#     key = bitarray("01010100011010000110000101110100011100110010000001101101011110010010000001001011011101010110111001100111001000000100011001110101")
#     print("Key: ", ba2hex(key))

#     aes = AES()
#     ciphertext = aes.circuit(key, message)
#     print("Ciphertext: ", ba2hex(ciphertext))