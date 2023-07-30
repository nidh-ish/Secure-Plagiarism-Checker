from server import *
import math
import struct

class FPVShare:
    def __init__(self, significand: Share, exponent: Share, zero: Share, sign: Share,) -> None:
        self.significand = significand
        self.exponent = exponent
        self.sign = sign
        self.zero = zero
        self.l = 24
    
    def setShare(self, significand: Share, exponent: Share, sign: Share, zero: Share):
        if significand != None:
            self.significand = significand
        if exponent != None:
            self.exponent = exponent
        if sign != None:
            self.sign = sign
        if zero != None:
            self.zero = zero
    
    def getShare(self) -> tuple[Share, Share, Share, Share]:
        return self.significand, self.exponent, self.zero, self.sign
    
    def getl(self):
        return self.l



avs0 = Share()
avs0.add(bitarray("0"))
avs0.add(bitarray("0"))
aps0 = Share()
aps0.add(bitarray("0"))
aps0.add(bitarray("0"))
azs0 = Share()
azs0.add(bitarray("0"))
azs0.add(bitarray("0"))
ass0 = Share()
ass0.add(bitarray("0"))
ass0.add(bitarray("0"))
bvs0 = Share()
bvs0.add(bitarray("0"))
bvs0.add(bitarray("0"))
bps0 = Share()
bps0.add(bitarray("0"))
bps0.add(bitarray("0"))
bzs0 = Share()
bzs0.add(bitarray("0"))
bzs0.add(bitarray("0"))
bss0 = Share()
bss0.add(bitarray("0"))
bss0.add(bitarray("0"))

avs1 = Share()
avs1.add(bitarray("0"))
avs1.add(bitarray("101000000000000000000000"))
aps1 = Share()
aps1.add(bitarray("0"))
aps1.add(bitarray("10000000"))
azs1 = Share()
azs1.add(bitarray("0"))
azs1.add(bitarray("0"))
ass1 = Share()
ass1.add(bitarray("0"))
ass1.add(bitarray("0"))
bvs1 = Share()
bvs1.add(bitarray("0"))
bvs1.add(bitarray("111000000000000000000000"))
bps1 = Share()
bps1.add(bitarray("0"))
bps1.add(bitarray("10000000"))
bzs1 = Share()
bzs1.add(bitarray("0"))
bzs1.add(bitarray("0"))
bss1 = Share()
bss1.add(bitarray("0"))
bss1.add(bitarray("0"))

avs2 = Share()
avs2.add(bitarray("0"))
avs2.add(bitarray("101000000000000000000000"))
aps2 = Share()
aps2.add(bitarray("0"))
aps2.add(bitarray("10000000"))
azs2 = Share()
azs2.add(bitarray("0"))
azs2.add(bitarray("0"))
ass2 = Share()
ass2.add(bitarray("0"))
ass2.add(bitarray("0"))
bvs2 = Share()
bvs2.add(bitarray("0"))
bvs2.add(bitarray("111000000000000000000000"))
bps2 = Share()
bps2.add(bitarray("0"))
bps2.add(bitarray("10000000"))
bzs2 = Share()
bzs2.add(bitarray("0"))
bzs2.add(bitarray("0"))
bss2 = Share()
bss2.add(bitarray("0"))
bss2.add(bitarray("0"))

a0 = FPVShare(avs0, aps0, azs0, ass0)
a1 = FPVShare(avs1, aps1, azs1, ass1)
a2 = FPVShare(avs2, aps2, azs2, ass2)

b0 = FPVShare(bvs0, bps0, bzs0, bss0)
b1 = FPVShare(bvs1, bps1, bzs1, bss1)
b2 = FPVShare(bvs2, bps2, bzs2, bss2)




# All the elements on which operations take place are from F_{2**P-1}, which implies P-bit bitarrays
class FPVArithmetic:
    def __init__(self):
        self.P = 61

    def convertToInt(self, mantissa_str):
        power_count = -1
        mantissa_int = 0
        for i in mantissa_str:
            mantissa_int += (int(i) * pow(2, power_count))
            power_count -= 1
        return (mantissa_int + 1)
    
    def converttofloat(self, ieee_32: str):
        signstr = ieee_32[0]
        expstr = ieee_32[1:9]
        manstr = ieee_32[9:]
        ieee_32 = signstr + "|" + expstr + "|" + manstr
        sign_bit = int(ieee_32[0])
        exponent_bias = int(ieee_32[2 : 10], 2)
        exponent_unbias = exponent_bias - 127
        mantissa_str = ieee_32[11 : ]
        mantissa_int = self.convertToInt(mantissa_str)
        real_no = pow(-1, sign_bit) * mantissa_int * pow(2, exponent_unbias)
        return real_no

    def float_to_bin(self, num):
        bits, = struct.unpack('!I', struct.pack('!f', num))
        return "{:032b}".format(bits)

    # Offline XOR of bits A and B
    def XOR_offline(self, A: list[bitarray], B: list[bitarray], S: Server0 | Server1 | Server2):
        if S.id() == 0:
            # temp21 = S.offline_AND1(ba2int(A[0] ^ A[1]), ba2int(B[0] ^ B[1]))
            a0 = ba2int(A[0])
            a1 = ba2int(A[1])
            b0 = ba2int(B[0])
            b1 = ba2int(B[1])
            return [int2ba((a0 + b0 - 2*a0*b0)%(2**self.P), length=self.P), int2ba((a1 + b1 - 2*a1*b1)%(2**self.P), length=self.P)]
        
        else:
            a0 = ba2int(A[0])
            b0 = ba2int(B[0])
            return [int2ba((a0 + b0 - 2*a0*b0)%(2**self.P), length=self.P)]

    # Online XOR of bits A and B
    def XOR_online(self, A: bitarray, B: bitarray, S: Server0 | Server1 | Server2):
        a = ba2int(A)
        b = ba2int(B)
        return [int2ba((a + b - 2*a*b)%(2**self.P), length=self.P)]

    # Offline XOR of Field elements A and B
    def XOR_offlineF(self, A: list[bitarray], B: list[bitarray], S: Server0 | Server1 | Server2):
        if S.id() == 0:
            temp00 = S.addF(self.P, A[0], B[0])
            temp01 = S.addF(self.P, A[1], B[1])
            temp1, temp10, temp11 = S.offline_ANDF(self.P, S.addF(self.P, A[0], A[1]), S.addF(self.P, B[0], B[1]))
            temp20 = S.multiplyF(self.P, int2ba(2), temp10)
            temp21 = S.multiplyF(self.P, int2ba(2), temp11)
            return S.subtractF(self.P, temp20, temp00), S.subtractF(self.P, temp21, temp01)
        
        else:
            temp0 = S.addF(self.P, A[0], B[0])
            temp1 = S.offline_ANDF(self.P, A[0], B[0])
            temp2 = S.multiplyF(self.P, int2ba(2), temp1)
            return S.subtractF(self.P, temp2, temp0)

    # Online XOR of Field elements A and B
    def XOR_onlineF(self, A: bitarray, B: bitarray, S: Server0 | Server1 | Server2):
        temp0 = S.addF(self.P, A, B)
        temp1 = S.online_ANDF(self.P, A, B)
        temp2 = S.multiplyF(self.P, int2ba(2), temp1)
        return S.subtractF(self.P, temp2, temp0)
    
    def XORShareConst_offline(self, A: list[bitarray], B: bitarray, S: Server0 | Server1 | Server2):
        if S.id() == 0:
            temp00 = A[0]
            temp01 = A[1]
            temp20 = S.multiplyF(self.P, int2ba(2), S.multiplyF(self.P, A[0], B))
            temp21 = S.multiplyF(self.P, int2ba(2), S.multiplyF(self.P, A[1], B))
            return S.subtractF(self.P, temp20, temp00), S.subtractF(self.P, temp21, temp01)
        
        else:
            temp0 = A[0]
            temp2 = S.multiplyF(self.P, int2ba(2), S.multiplyF(self.P, A[0], B))
            return S.subtractF(self.P, temp2, temp0)
        
    def XORShareConst_online(self, A: bitarray, B: bitarray, S: Server0 | Server1 | Server2):
        temp0 = S.addF(self.P, A, B)
        temp2 = S.multiplyF(self.P, int2ba(2), S.multiplyF(self.P, A, B))
        return S.subtractF(self.P, temp2, temp0)

    def RandBitFD(self, S: Server0 | Server1 | Server2):
        if S.id() == 0:
            temp0 ,temp1 = S.offline_generateRandomShare(1)

        elif S.id() == 1:
            temp_off = S.offline_generateRandomShare(1)

        else:
            temp_off = S.offline_generateRandomShare(1)

    # Offline OR of A and B
    def OR_offline(self, A: list[bitarray], B: list[bitarray], S: Server0 | Server1 | Server2):
        if S.id() == 0:
            a0 = ba2int(A[0])
            a1 = ba2int(A[1])
            b0 = ba2int(B[0])
            b1 = ba2int(B[1])
            temp21 = S.offline_AND1(ba2int(A[0] ^ A[1]), ba2int(B[0] ^ B[1]))
            return [int2ba(a0 ^ b0 ^ ba2int(temp21[0]), length=1), int2ba(a1 ^ b1 ^ ba2int(temp21[1]), length=1)]
        else:
            a0 = ba2int(A[0])
            b0 = ba2int(B[0])
            temp21 = S.offline_AND1(ba2int(A[0]), ba2int(B[0]))
            return [int2ba(a0 ^ b0 ^ ba2int(temp21[0]), length=1)]
    
    # Online OR of A and B
    def OR_online(self, A: bitarray, B: bitarray, S: Server0 | Server1 | Server2):
        a = ba2int(A)
        b = ba2int(B)
        temp21 = S.online_AND1(ba2int(A), ba2int(B))
        return [int2ba(a ^ b ^ ba2int(temp21[0]), length=1)]
    
    # Offline OR of A and B
    def OR_offlineF(self, A: list[bitarray], B: list[bitarray], S: Server0 | Server1 | Server2):
        if S.id() == 0:
            temp00 = S.addF(self.P, A[0], B[0])
            temp01 = S.addF(self.P, A[1], B[1])
            temp2 = S.offline_ANDF(self.P, S.addF(self.P, A[0], A[1]), S.addF(self.P, B[0], B[1]))
            return S.subtractF(self.P, temp2[1], temp00), S.subtractF(self.P, temp2[2], temp01)
        else:
            temp0 = S.addF(self.P, A[0], B[0])
            temp2 = S.offline_ANDF(self.P, A[0], B[0])
            return S.subtractF(self.P, temp2, temp0)
    
    # Online OR of A and B
    def OR_onlineF(self, A: bitarray, B: bitarray, S: Server0 | Server1 | Server2):
            temp0 = S.addF(self.P, A, B)
            temp2 = S.online_ANDF(self.P, A, B)
            return S.subtractF(self.P, temp2, temp0)

    def Inverse(self,  A: list[bitarray], S: Server0 | Server1 | Server2):
        if S.id() == 0:
            r1, r2 = S.offline_generateRandomShareF(self.P, self.P)
            a1 = A[0]
            a2 = A[1]
            c = S.offline_ANDF(self.P, S.addF(self.P, a1, a2), S.addF(self.P, r1, r2))  
            Reconc = S.online_reconstructionF(self.P, c[1], c[2])
            InvC = S.find_multiplicative_inverse(self.P, Reconc)
            return S.multiplyF(self.P, InvC, r1), S.multiplyF(self.P, InvC, r2)
        else: 
            r1 = S.offline_generateRandomShareF(self.P, self.P)
            a1 = A[0]
            lambdac = S.offline_ANDF(self.P, a1, r1)
            r2 = S.online_generateRandomShareF(self.P, self.P)
            a2 = A[1]
            mc = S.online_ANDF(self.P, a2, r2)
            Reconc = S.online_reconstructionF(self.P, lambdac, mc)
            InvC = S.find_multiplicative_inverse(self.P, Reconc)
            return S.multiplyF(self.P, InvC, r1), S.multiplyF(self.P, InvC, r2)
    
    def PreMul_offline(self, A: list[list[bitarray]], S: Server0 | Server1 | Server2) -> list[list[bitarray]]:
        output = []
        if S.id() == 0:
            temp = [None, None]
            flag = True
            for a in A:
                if flag:
                    temp[0] = a[0]
                    temp[1] = a[1]
                    flag = False
                else:
                    out = S.offline_ANDF(self.P, S.addF(self.P, a[0], a[1]), S.addF(self.P, temp[0], temp[1]))
                    temp[0] = out[1]
                    temp[1] = out[2]
                output.append([temp[0], temp[1]])
        else:
            temp = None
            flag = True
            for a in A:
                if flag:
                    temp = a[0]
                    flag = False
                else:
                    out = S.offline_ANDF(self.P, a[0], temp)
                    temp = out
                output.append([temp])
        return output
    
    def PreMul_online(self, A: list[list[bitarray]], S: Server0 | Server1 | Server2) -> list[list[bitarray]]:
        output = []
        temp = None
        flag = True
        for a in A:
            if flag:
                temp = a[0]
                flag = False
            else:
                out = S.online_ANDF(self.P, a[0], temp)
                temp = out
            output.append([temp])
        return output
    
    def PreOR_offline(self, A: list[list[bitarray]], S: Server0 | Server1 | Server2) -> list[list[bitarray]]:
        output = []
        if S.id() == 0:
            temp = [None, None]
            flag = True
            for a in A:
                if flag:
                    temp[0] = a[0]
                    temp[1] = a[1]
                    flag = False
                else:
                    out = self.OR_offlineF(a, temp, S)
                    temp[0] = out[0]
                    temp[1] = out[1]
                output.append([temp[0], temp[1]])
        else:
            temp = None
            flag = True
            for a in A:
                if flag:
                    temp = a[0]
                    flag = False
                else:
                    out = self.OR_offlineF(a, [temp], S)
                    temp = out
                output.append([temp])
        return output
    
    def PreOR_online(self, A: list[list[bitarray]], S: Server0 | Server1 | Server2) -> list[list[bitarray]]:
        output = []
        temp = None
        flag = True
        for a in A:
            if flag:
                temp = a[0]
                flag = False
            else:
                out = self.OR_onlineF(a[0], temp, S)
                temp = out
            output.append([temp])
        return output

    def GenerateRandomSharesFD(self, S: Server0 | Server1 | Server2) -> tuple[bitarray, bitarray, bitarray, bitarray]:
        if S.id() == 0:
            l1, l2 = S.offline_generateRandomShare(1)
            l1l1, l1l2 = S.offline_shareF(self.P, 0)
            l1m = S.online_shareF(self.P, 0, l1l1, l1l2, l1)
            l2l1, l2l2 = S.offline_shareF(self.P, 0)
            l2m = S.online_shareF(self.P, 0, l2l1, l2l2, l2)
            ml1, ml2 = S.offline_shareF(self.P, 1)
            temp00, temp01 = self.XOR_offlineF([l1l1, l1l2], [l2l1, l2l2], S)
            l1F, l2F = self.XOR_offlineF([temp00, temp01], [ml1, ml2], S)
            return l1, l2, l1F, l2F

        elif S.id() ==1:
            l1= S.offline_generateRandomShare(1)
            m = S.online_generateRandomShare(1)
            l1l1 = S.offline_shareF(self.P, 0)
            l1m = S.online_shareF(self.P, 0, None, None, None)
            l2l1 = S.offline_shareF(self.P, 0)
            l2m = S.online_shareF(self.P, 0, None, None, None)
            ml1, ml2 = S.offline_shareF(self.P, 1)
            mm = S.online_shareF(self.P, 1, ml1, ml2, m)
            temp0 = self.XOR_offlineF([l1l1], [l2l1], S)
            l1F = self.XOR_offlineF([temp0], [ml1], S)
            temp1 = self.XOR_onlineF(l1m, l2m, S)
            mF = self.XOR_onlineF(temp1, mm, S)
            return l1, m, l1F, mF
            
        else:
            l2 = S.offline_generateRandomShare(1)
            m = S.online_generateRandomShare(1)
            l1l2 = S.offline_shareF(self.P, 0)
            l1m = S.online_shareF(self.P, 0, None, None, None)
            l2l2 = S.offline_shareF(self.P, 0)
            l2m = S.online_shareF(self.P, 0, None, None, None)
            ml2 = S.offline_shareF(self.P, 1)
            mm = S.online_shareF(self.P, 1, None, None, None)
            temp0 = self.XOR_offlineF([l1l2], [l2l2], S)
            l2F = self.XOR_offlineF([temp0], [ml2], S)
            temp1 = self.XOR_onlineF(l1m, l2m, S)
            mF = self.XOR_onlineF(temp1, mm, S)
            return l2, m, l2F, mF

    def BitDec(self, A: list[bitarray], k: int, m: int, S: Server0 | Server1 | Server2) -> list[list[bitarray]]:
        if S.id() == 0:
            rtempbit0 = []
            rtempbit1 = []
            rtemp0 = []
            rtemp1 = []
            Output = []
            for i in range(m):
                temp = self.GenerateRandomSharesFD(S)
                rtempbit0.append(temp[0])
                rtempbit1.append(temp[1])
                rtemp0.append(temp[2])
                rtemp1.append(temp[3])
            r10 = bitarray('0')
            r11 = bitarray('0')
            for i in range(m):
                revi = m - 1 - i
                r10 = S.addF(self.P, r10, S.multiplyF(self.P, int2ba(2**revi, length=self.P), rtemp0[i]))
                r11 = S.addF(self.P, r11, S.multiplyF(self.P, int2ba(2**revi, length=self.P), rtemp1[i]))
            r20 = bitarray('0')
            r21 = bitarray('0')
            for i in range(1 + k - m):
                revi = 1 + k - m - 1 - i
                temp = self.GenerateRandomSharesFD(S)
                r20 = S.addF(self.P, r20, S.multiplyF(self.P, int2ba(2**revi, length=self.P), temp[2]))
                r21 = S.addF(self.P, r21, S.multiplyF(self.P, int2ba(2**revi, length=self.P), temp[3]))
            r0 = S.addF(self.P, r10, S.multiplyF(self.P, int2ba(2**m, length=self.P), r20))
            r1 = S.addF(self.P, r11, S.multiplyF(self.P, int2ba(2**m, length=self.P), r21))
            ctemp0 = A[0]
            ctemp1 = A[1]
            c0 = S.subtractF(self.P, r0, ctemp0)
            c1 = S.subtractF(self.P, r1, ctemp1)
            c = S.online_reconstructionF(self.P, c0, c1)
            for i in range(m):
                Output.append([rtempbit0[i] ^ c[self.P - m + i: self.P - m + i + 1], rtempbit1[i] ^ c[self.P - m + i: self.P - m + i + 1]])
            carry0 = bitarray("0")
            carry1 = bitarray("0")
            for i in range(m):
                revi = m - i - 1
                Output[revi] = [rtempbit0[revi] ^ c[self.P - m + revi: self.P - m + revi + 1] ^ carry0, rtempbit1[revi] ^ c[self.P - m + revi: self.P - m + revi + 1] ^ carry1]
                tempc = S.offline_AND1(rtempbit0[revi][0] ^ rtempbit1[revi][0], carry0[0] ^ carry1[0])
                carry0 = tempc[0] ^ rtempbit0[revi] & c[self.P - m + revi: self.P - m + revi + 1] ^ c[self.P - m + revi: self.P - m + revi + 1] & carry0
                carry1 = tempc[1] ^ rtempbit1[revi] & c[self.P - m + revi: self.P - m + revi + 1] ^ c[self.P - m + revi: self.P - m + revi + 1] & carry1
            return Output
            
        else: 
            rtempbit_off = []
            rtemp_off = []
            rtempbit_on = []
            rtemp_on = []
            Output = []
            for i in range(m):
                temp = self.GenerateRandomSharesFD(S)
                rtempbit_off.append(temp[0])
                rtempbit_on.append(temp[1])
                rtemp_off.append(temp[2])
                rtemp_on.append(temp[3])
            r1_off = bitarray('0')
            r1_on = bitarray('0')
            for i in range(m):
                revi = m - 1 - i
                r1_off = S.addF(self.P, r1_off, S.multiplyF(self.P, int2ba(2**revi, length=self.P), rtemp_off[i]))
                r1_on = S.addF(self.P, r1_on, S.multiplyF(self.P, int2ba(2**revi, length=self.P), rtemp_on[i]))
            r2_off = bitarray('0') 
            r2_on = bitarray('0')
            for i in range(1 + k - m):
                revi = 1 + k - m - 1 - i
                temp = self.GenerateRandomSharesFD(S)
                r2_off = S.addF(self.P, r2_off, S.multiplyF(self.P, int2ba(2**revi, length=self.P), temp[2]))
                r2_on = S.addF(self.P, r2_on, S.multiplyF(self.P, int2ba(2**revi, length=self.P), temp[3]))
            r_off = S.addF(self.P, r1_off, S.multiplyF(self.P, int2ba(2**m, length=self.P), r2_off))
            r_on = S.addF(self.P, r1_on, S.multiplyF(self.P, int2ba(2**m, length=self.P), r2_on))
            ctemp_off = A[0]
            ctemp_on = S.addF(self.P, S.addF(self.P, int2ba(2**(self.P - 2)), int2ba(2**k)), A[1])
            c_off = S.subtractF(self.P, r_off, ctemp_off)
            c_on = S.subtractF(self.P, r_on, ctemp_on)
            c = S.online_reconstructionF(self.P, c_off, c_on)
            for i in range(m):
                Output.append([rtempbit_off[i] ^ c[self.P - m + i: self.P - m + i + 1], rtempbit_on[i] ^ c[self.P - m + i: self.P - m + i + 1]])
            carry0 = bitarray("0")
            carry1 = bitarray("0")
            for i in range(m):
                revi = m - i - 1
                Output[revi] = [rtempbit_off[revi] ^ c[self.P - m + revi: self.P - m + revi + 1] ^ carry0, rtempbit_on[revi] ^ c[self.P - m + revi: self.P - m + revi + 1] ^ carry1]
                tempc = S.offline_AND1(rtempbit_off[revi][0], carry0[0])
                tempc.append(S.online_AND(rtempbit_on[revi][0], carry1[0]))
                carry0 = tempc[0] ^ rtempbit_off[revi] & c[self.P - m + revi: self.P - m + revi + 1] ^ c[self.P - m + revi: self.P - m + revi + 1] & carry0
                carry1 = tempc[1] ^ rtempbit_on[revi] & c[self.P - m + revi: self.P - m + revi + 1] ^ c[self.P - m + revi: self.P - m + revi + 1] & carry1
            return Output
        
    def BittoField(self, A: list[list[bitarray]], S: Server0 | Server1 | Server2) -> list[list[bitarray]]:   
        if S.id() == 0:
            Output = []
            for i in range(len(A)):
                l1, l2 = A[i][0], A[i][1]
                l1l1, l1l2 = S.offline_shareF(self.P, 0)
                l1m = S.online_shareF(self.P, 0, l1l1, l1l2, l1)
                l2l1, l2l2 = S.offline_shareF(self.P, 0)
                l2m = S.online_shareF(self.P, 0, l2l1, l2l2, l2)
                ml1, ml2 = S.offline_shareF(self.P, 1)
                temp00, temp01 = self.XOR_offlineF([l1l1, l1l2], [l2l1, l2l2], S)
                l1F, l2F = self.XOR_offlineF([temp00, temp01], [ml1, ml2], S)
                Output.append([l1F, l2F])
            return Output

        elif S.id() ==1:
            Output = []
            for i in range(len(A)):
                l1, m = A[i][0], A[i][1]
                l1l1 = S.offline_shareF(self.P, 0)
                l1m = S.online_shareF(self.P, 0, None, None, None)
                l2l1 = S.offline_shareF(self.P, 0)
                l2m = S.online_shareF(self.P, 0, None, None, None)
                ml1, ml2 = S.offline_shareF(self.P, 1)
                mm = S.online_shareF(self.P, 1, ml1, ml2, m)
                temp0 = self.XOR_offlineF([l1l1], [l2l1], S)
                l1F = self.XOR_offlineF([temp0], [ml1], S)
                temp1 = self.XOR_onlineF(l1m, l2m, S)
                mF = self.XOR_onlineF(temp1, mm, S)
                Output.append([l1F, mF])
            return Output
            
        else:
            Output = []
            for i in range(len(A)):
                l2, m = A[i][0], A[i][1]
                l1l2 = S.offline_shareF(self.P, 0)
                l1m = S.online_shareF(self.P, 0, None, None, None)
                l2l2 = S.offline_shareF(self.P, 0)
                l2m = S.online_shareF(self.P, 0, None, None, None)
                ml2 = S.offline_shareF(self.P, 1)
                mm = S.online_shareF(self.P, 1, None, None, None)
                temp0 = self.XOR_offlineF([l1l2], [l2l2], S)
                l2F = self.XOR_offlineF([temp0], [ml2], S)
                temp1 = self.XOR_onlineF(l1m, l2m, S)
                mF = self.XOR_onlineF(temp1, mm, S)
                Output.append([l2F, mF])
            return Output

    def Pow2(self, A: list[bitarray], l: int, S: Server0 | Server1 | Server2) -> tuple[bitarray, bitarray]:
        if S.id() == 0:
            m = math.ceil(math.log(l, 2))
            ADecBit = self.BitDec(A, m, m, S)
            ADec = self.BittoField(ADecBit, S)
            InvMullist = []
            for i in range(len(ADec)-1, -1 , -1):
                Invcount = len(ADec) - 1 - i
                temp00 = S.multiplyF(self.P, ADec[i][0], int2ba(2**(2**Invcount), length=self.P))
                temp10 = S.multiplyF(self.P, ADec[i][1], int2ba(2**(2**Invcount), length=self.P))
                temp01 = temp00
                temp11 = temp10
                temp02 = S.subtractF(self.P, ADec[i][0], temp01)
                temp12 = S.subtractF(self.P, ADec[i][1], temp11)
                InvMullist.append([temp02, temp12])
            MulValues = self.PreMul_offline(InvMullist, S)
            return MulValues[-1][0], MulValues[-1][1]
        else:
            m = math.ceil(math.log(l, 2))
            ADecBit = self.BitDec(A, m, m, S)
            ADec = self.BittoField(ADecBit, S)
            InvMullist_off = []
            InvMullist_on = []
            for i in range(len(ADec)-1, -1 , -1):
                Invcount = len(ADec) - 1 - i
                temp0_off = S.multiplyF(self.P, ADec[i][0], int2ba(2**(2**Invcount), length=self.P))
                temp0_on = S.multiplyF(self.P, ADec[i][1], int2ba(2**(2**Invcount), length=self.P))
                temp1_off = temp0_off
                temp1_on = S.addF(self.P, temp0_on, bitarray("1"))
                temp2_off = S.subtractF(self.P, ADec[i][0], temp1_off)
                temp2_on = S.subtractF(self.P, ADec[i][1], temp1_on)
                InvMullist_off.append([temp2_off])
                InvMullist_on.append([temp2_on])
            MulValues_off = self.PreMul_offline(InvMullist_off, S)
            MulValues_on = self.PreMul_online(InvMullist_on, S)
            return MulValues_off[-1][0], MulValues_on[-1][0]

    def B2U(self, A: list[bitarray], l: int, S: Server0 | Server1 | Server2) -> list[list[bitarray]]:
        if S.id() == 0:
            pow2 = self.Pow2(A, l, S)
            Randbits = []
            ctemp00 = bitarray("0")
            ctemp01 = bitarray("0")
            for i in range(l):
                invi = l - 1 - i
                temp = self.GenerateRandomSharesFD(S)
                Randbits.append([temp[2], temp[3]])
                ctemp00 = S.addF(self.P, ctemp00, S.multiplyF(self.P, int2ba(2**invi), temp[2]))
                ctemp01 = S.addF(self.P, ctemp01, S.multiplyF(self.P, int2ba(2**invi), temp[3]))
            ranint0 = bitarray("0")
            ranint1 = bitarray("0")
            for i in range(5):
                invi = 4 - i
                temp = self.GenerateRandomSharesFD(S)
                ranint0 = S.addF(self.P, ranint0, S.multiplyF(self.P, int2ba(2**invi), temp[2]))
                ranint1 = S.addF(self.P, ranint1, S.multiplyF(self.P, int2ba(2**invi), temp[3]))
            ranint0 = S.multiplyF(self.P, ranint0, int2ba(2**l))
            ranint1 = S.multiplyF(self.P, ranint1, int2ba(2**l))
            c0 = S.addF(self.P, S.addF(self.P, pow2[0], ctemp00), ranint0)
            c1 = S.addF(self.P, S.addF(self.P, pow2[1], ctemp01), ranint1)
            c = S.online_reconstructionF(self.P, c0, c1)
            x = []
            for i in range(self.P - l, self.P):
                starti = i - self.P + l
                temp0 = S.subtractF(self.P, S.multiplyF(self.P, int2ba(2*c[i]), Randbits[starti][0]), Randbits[starti][0])
                temp1 = S.subtractF(self.P, S.multiplyF(self.P, int2ba(2*c[i]), Randbits[starti][1]), Randbits[starti][1])
                x.append([temp0, temp1])
            x.reverse()
            y = self.PreOR_offline(x, S)
            output = []
            for i in range(len(y)):
                temp1 = S.find_additive_inverse(self.P, y[i][0])
                temp2 = S.find_additive_inverse(self.P, y[i][1])
                output.append([temp1, temp2])
            return output

        else:
            pow2 = self.Pow2(A, l, S)
            Randbits = []
            ctemp0_off = bitarray("0")
            ctemp0_on = bitarray("0")
            for i in range(l):
                invi = l - 1 - i
                temp = self.GenerateRandomSharesFD(S)
                Randbits.append([temp[2], temp[3]])
                ctemp0_off = S.addF(self.P, ctemp0_off, S.multiplyF(self.P, int2ba(2**invi), temp[2]))
                ctemp0_on = S.addF(self.P, ctemp0_on, S.multiplyF(self.P, int2ba(2**invi), temp[3]))
            ranint_off = bitarray("0")
            ranint_on = bitarray("0")
            for i in range(5):
                invi = 4 - i
                temp = self.GenerateRandomSharesFD(S)
                ranint_off = S.addF(self.P, ranint_off, S.multiplyF(self.P, int2ba(2**invi), temp[2]))
                ranint_on = S.addF(self.P, ranint_on, S.multiplyF(self.P, int2ba(2**invi), temp[3]))
            ranint_off = S.multiplyF(self.P, ranint_off, int2ba(2**l))
            ranint_on = S.multiplyF(self.P, ranint_on, int2ba(2**l))
            c_off = S.addF(self.P, S.addF(self.P, pow2[0], ctemp0_off), ranint_off)
            c_on = S.addF(self.P, S.addF(self.P, pow2[1], ctemp0_on), ranint_on)
            c = S.online_reconstructionF(self.P, c_off, c_on)
            x_off = []
            x_on = []
            for i in range(self.P - l, self.P):
                starti = i - self.P + l
                temp0 = S.subtractF(self.P, S.multiplyF(self.P, int2ba(2*c[i]), Randbits[starti][0]), Randbits[starti][0])
                temp1 = S.addF(self.P, S.subtractF(self.P, S.multiplyF(self.P, int2ba(2*c[i]), Randbits[starti][1]), Randbits[starti][1]), c[i:i+1])
                x_off.append([temp0])
                x_on.append([temp1])
            x_off.reverse()
            x_on.reverse()
            y_off = self.PreOR_offline(x_off, S)
            y_on = self.PreOR_online(x_on, S)
            output = []
            for i in range(len(y_off)):
                temp1 = S.find_additive_inverse(self.P, y_off[i][0])
                temp2 = S.subtractF(self.P, y_on[i][0], int2ba(1))
                output.append([temp1, temp2])
            return output

    def CarryOutbitConstShare(self, A: bitarray, B: list[list[bitarray]], S: Server0 | Server1 | Server2) -> tuple[bitarray, bitarray]:
        if S.id() == 0:    
            k = len(A)
            carry0 = bitarray("0")
            carry1 = bitarray("0")
            for i in range(k):
                invi = k - 1 - i
                temp00 = S.multiplyF(self.P, A[invi:invi+1], B[invi][0])
                temp01 = S.multiplyF(self.P, A[invi:invi+1], B[invi][1])
                temp10 = S.multiplyF(self.P, A[invi:invi+1], carry0)
                temp11 = S.multiplyF(self.P, A[invi:invi+1], carry1)
                temp2, temp20, temp21 = S.offline_ANDF(self.P, S.addF(self.P, B[invi][0], B[invi][1]), S.addF(self.P, carry0, carry1))
                temp = self.XOR_offlineF([temp00, temp01], [temp10, temp11], S)
                carry = self.XOR_offlineF([temp[0], temp[1]], [temp20, temp21], S)
                carry0 = carry[0]
                carry1 = carry[1]
            return carry0, carry1
        else: 
            k = len(A)
            carry_off = bitarray("0")
            carry_on = bitarray("0")
            for i in range(k):
                invi = k - 1 - i
                temp0_off = S.multiplyF(self.P, A[invi:invi+1], B[invi][0])
                temp0_on = S.multiplyF(self.P, A[invi:invi+1], B[invi][1])
                temp1_off = S.multiplyF(self.P, A[invi:invi+1], carry_off)
                temp1_on = S.multiplyF(self.P, A[invi:invi+1], carry_on)
                temp2_off = S.offline_ANDF(self.P, B[invi][0], carry_off)
                temp2_on = S.online_ANDF(self.P, B[invi][1], carry_on)
                temp_off = self.XOR_offlineF([temp0_off], [temp1_off], S)
                temp_on = self.XOR_onlineF(temp0_on, temp1_on, S)
                carry_off = self.XOR_offlineF([temp_off], [temp2_off], S)
                carry_on = self.XOR_onlineF(temp_on, temp2_on, S)
            return carry_off, carry_on

    def EQZ(self, A: list[bitarray], l: int, S: Server0 | Server1 | Server2):
        if S.id() == 0:
            Randbits = []
            r10 = bitarray("0")
            r11 = bitarray("0")
            for i in range(l):
                invi = l - 1 - i
                temp = self.GenerateRandomSharesFD(S)
                Randbits.append([temp[2], temp[3]])
                r10 = S.addF(self.P, r10, S.multiplyF(self.P, int2ba(2**invi), temp[2]))
                r11 = S.addF(self.P, r11, S.multiplyF(self.P, int2ba(2**invi), temp[3]))
            r20 = bitarray("0")
            r21 = bitarray("0")
            for i in range(5):
                invi = 5 - 1 - i
                temp = self.GenerateRandomSharesFD(S)
                r20 = S.addF(self.P, r20, S.multiplyF(self.P, int2ba(2**invi), temp[2]))
                r21 = S.addF(self.P, r21, S.multiplyF(self.P, int2ba(2**invi), temp[3]))
            ctemp00 = S.addF(self.P, S.multiplyF(self.P, int2ba(2**l), r20), r10)
            ctemp01 = S.addF(self.P, S.multiplyF(self.P, int2ba(2**l), r21), r11)
            ctemp10 = S.addF(self.P, A[0], ctemp00)
            ctemp11 = S.addF(self.P, A[1], ctemp01)
            c = S.online_reconstructionF(self.P, ctemp10, ctemp11)
            c = c[self.P-l:self.P]
            dlist = []
            dor0 = None
            dor1 = None
            for i in range(l):
                dtemp0 = S.subtractF(self.P, S.multiplyF(self.P, int2ba(2), S.multiplyF(self.P, c[i:i+1], Randbits[i][0])), Randbits[i][0])
                dtemp1 = S.subtractF(self.P, S.multiplyF(self.P, int2ba(2), S.multiplyF(self.P, c[i:i+1], Randbits[i][1])), Randbits[i][1])
                dlist.append([dtemp0, dtemp1])
                if dor0 == None:
                    dor0 = dtemp0
                    dor1 = dtemp1
                else:
                    dortemp = self.OR_offlineF([dor0, dor1], [dtemp0, dtemp1], S)
                    dor0 = dortemp[0]
                    dor1 = dortemp[1]
            return S.find_additive_inverse(self.P, dor0), S.find_additive_inverse(self.P, dor1)   

        else: 
            Randbits = []
            r1_off = bitarray("0")
            r1_on = bitarray("0")
            for i in range(l):
                invi = l - 1 - i
                temp = self.GenerateRandomSharesFD(S)
                Randbits.append([temp[2], temp[3]])
                r1_off = S.addF(self.P, r1_off, S.multiplyF(self.P, int2ba(2**invi), temp[2]))
                r1_on = S.addF(self.P, r1_on, S.multiplyF(self.P, int2ba(2**invi), temp[3]))
            r2_off = bitarray("0")
            r2_on = bitarray("0")
            for i in range(5):
                invi = 5 - 1 - i
                temp = self.GenerateRandomSharesFD(S)
                r2_off = S.addF(self.P, r2_off, S.multiplyF(self.P, int2ba(2**invi), temp[2]))
                r2_on = S.addF(self.P, r2_on, S.multiplyF(self.P, int2ba(2**invi), temp[3]))
            ctemp0_off = S.addF(self.P, S.multiplyF(self.P, int2ba(2**l), r2_off), r1_off)
            ctemp0_on = S.addF(self.P, S.multiplyF(self.P, int2ba(2**l), r2_on), r1_on)
            ctemp1_off = S.addF(self.P, A[0], ctemp0_off)
            ctemp1_on = S.addF(self.P, A[1], ctemp0_on)
            c = S.online_reconstructionF(self.P, ctemp1_off, ctemp1_on)
            c = c[self.P-l:self.P]
            dlist = []
            dor_off = None
            dor_on = None
            for i in range(l):
                dtemp_off = S.subtractF(self.P, S.multiplyF(self.P, int2ba(2), S.multiplyF(self.P, c[i:i+1], Randbits[i][0])), Randbits[i][0])
                dtemp_on = S.subtractF(self.P, S.multiplyF(self.P, int2ba(2), S.multiplyF(self.P, c[i:i+1], Randbits[i][1])), Randbits[i][1])
                dtemp_on = S.addF(self.P, dtemp_on, c[i:i+1])
                dlist.append([dtemp_off, dtemp_on])
                if dor_off == None:
                    dor_off = dtemp_off
                    dor_on = dtemp_on
                else:
                    dor_off = self.OR_offlineF([dor_off], [dtemp_off], S)
                    dor_on = self.OR_onlineF(dor_on, dtemp_on, S)
            return S.find_additive_inverse(self.P, dor_off), S.subtractF(self.P, dor_on, int2ba(1))

    def BitLT(self, A: bitarray, B: list[list[bitarray]], S: Server0 | Server1 | Server2):
        if S.id() == 0:
            k = len(A)
            bprime = []
            for i in range(k):
                temp1 = S.find_additive_inverse(self.P, B[i][0])
                temp2 = S.find_additive_inverse(self.P, B[i][1])
                bprime.append([temp1, temp2])
            b0 =  bitarray("0")
            b1 = bitarray("0")
            for i in range(k):
                invi = k - 1 - i
                b0 = S.addF(self.P, b0, S.multiplyF(self.P, B[i][0], int2ba(2**invi)))
                b1 = S.addF(self.P, b1, S.multiplyF(self.P, B[i][1], int2ba(2**invi)))
            eq = self.EQZ([b0, b1], k, S)
            carrybit = self.CarryOutbitConstShare(A, bprime, S)
            outbitl1 = S.find_additive_inverse(self.P, carrybit[0])
            outbitl2 = S.find_additive_inverse(self.P, carrybit[1])
            outbit = self.XOR_offlineF([outbitl1, outbitl2], [eq[0], eq[1]], S)
            return outbit[0], outbit[1]
        
        else: 
            k = len(A)
            bprime = []
            for i in range(k):
                temp1 = S.find_additive_inverse(self.P, B[i][0])
                temp2 = S.subtractF(self.P, B[i][1], int2ba(1))
                bprime.append([temp1, temp2])
            b_off =  bitarray("0")
            b_on = bitarray("0")
            for i in range(k):
                invi = k - 1 - i
                b_off = S.addF(self.P, b_off, S.multiplyF(self.P, B[i][0], int2ba(2**invi)))
                b_on = S.addF(self.P, b_on, S.multiplyF(self.P, B[i][1], int2ba(2**invi)))
            b_on = S.subtractF(self.P, A, b_on)
            eq = self.EQZ([b_off, b_on], k, S)
            carrybit = self.CarryOutbitConstShare(A, bprime, S)
            outbitl = S.find_additive_inverse(self.P, carrybit[0])
            outbitm = S.subtractF(self.P, carrybit[1], int2ba(1))
            outbit_off = self.XOR_offlineF([outbitl], [eq[0]], S)
            outbit_on = self.XOR_onlineF(outbitm, eq[1], S)
            return outbit_off, outbit_on

    def Mod2m(self, A: list[bitarray], k: int, m: int, S: Server0 | Server1 | Server2):
        if S.id() == 0:
            Randbits = []
            r10 = bitarray("0")
            r11 = bitarray("0")
            for i in range(m):
                invi = m - 1 - i
                temp = self.GenerateRandomSharesFD(S)
                Randbits.append([temp[2], temp[3]])
                r10 = S.addF(self.P, r10, S.multiplyF(self.P, int2ba(2**invi), temp[2]))
                r11 = S.addF(self.P, r11, S.multiplyF(self.P, int2ba(2**invi), temp[3]))
            r20 = bitarray("0")
            r21 = bitarray("0")
            for i in range(5 + k - m):
                invi = 5 + k - m - 1 - i
                temp = self.GenerateRandomSharesFD(S)
                r20 = S.addF(self.P, r20, S.multiplyF(self.P, int2ba(2**invi), temp[2]))
                r21 = S.addF(self.P, r21, S.multiplyF(self.P, int2ba(2**invi), temp[3]))
            ctemp00 = S.addF(self.P, S.multiplyF(self.P, int2ba(2**m), r20), r10)
            ctemp01 = S.addF(self.P, S.multiplyF(self.P, int2ba(2**m), r21), r11)
            ctemp10 = S.addF(self.P, A[0], ctemp00)
            ctemp11 = S.addF(self.P, A[1], ctemp01)
            c = S.online_reconstructionF(self.P, ctemp10, ctemp11)
            cp = int2ba(ba2int(c) % 2**m, length=m)
            u0, u1 = self.BitLT(cp, Randbits, S)
            atemp0 = S.subtractF(self.P, r10, S.multiplyF(self.P, int2ba(2**m), u0))
            atemp1 = S.subtractF(self.P, r11, S.multiplyF(self.P, int2ba(2**m), u1))
            a0 = atemp0
            a1 = atemp1
            return a0, a1
                
        else:
            Randbits = []
            r1_off = bitarray("0")
            r1_on = bitarray("0")
            for i in range(m):
                invi = m - 1 - i
                temp = self.GenerateRandomSharesFD(S)
                Randbits.append([temp[2], temp[3]])
                r1_off = S.addF(self.P, r1_off, S.multiplyF(self.P, int2ba(2**invi), temp[2]))
                r1_on = S.addF(self.P, r1_on, S.multiplyF(self.P, int2ba(2**invi), temp[3]))   
            r2_off = bitarray("0")
            r2_on = bitarray("0")
            for i in range(5 + k - m):
                invi = 5 + k - m - 1 - i
                temp = self.GenerateRandomSharesFD(S)
                r2_off = S.addF(self.P, r2_off, S.multiplyF(self.P, int2ba(2**invi), temp[2]))
                r2_on = S.addF(self.P, r2_on, S.multiplyF(self.P, int2ba(2**invi), temp[3]))
            ctemp0_off = S.addF(self.P, S.multiplyF(self.P, int2ba(2**m), r2_off), r1_off)
            ctemp0_on = S.addF(self.P, S.multiplyF(self.P, int2ba(2**m), r2_on), r1_on)
            ctemp1_off = S.addF(self.P, A[0], ctemp0_off)
            ctemp1_on = S.addF(self.P, S.addF(self.P, A[1], ctemp0_on), int2ba(2**(k-1)))
            c = S.online_reconstructionF(self.P, ctemp1_off, ctemp1_on)
            cp = int2ba(ba2int(c) % 2**m, length=m)
            u_off, u_on = self.BitLT(cp, Randbits, S)
            atemp_off = S.subtractF(self.P, r1_off, S.multiplyF(self.P, int2ba(2**m), u_off))
            atemp_on = S.subtractF(self.P, r1_on, S.multiplyF(self.P, int2ba(2**m), u_on))
            a_off = atemp_off
            a_on = S.addF(self.P, atemp_on, cp)
            return a_off, a_on
    
    def SimpleTrunc(self, A: list[bitarray], k: int, m: int, S: Server0 | Server1 | Server2):
        if S.id() == 0:
            ap = self.Mod2m(A, k, m, S)
            dtemp0 = S.subtractF(self.P, ap[0], A[0])
            dtemp1 = S.subtractF(self.P, ap[1], A[1])
            q = S.find_multiplicative_inverse(self.P, int2ba(2**m))
            d0 = S.multiplyF(self.P, dtemp0, q)
            d1 = S.multiplyF(self.P, dtemp1, q)
            return d0, d1
        else:
            ap = self.Mod2m(A, k, m, S)
            dtemp_off = S.subtractF(self.P, ap[0], A[0])
            dtemp_on = S.subtractF(self.P, ap[1], A[1])
            q = S.find_multiplicative_inverse(self.P, int2ba(2**m))
            d_off = S.multiplyF(self.P, dtemp_off, q)
            d_on = S.multiplyF(self.P, dtemp_on, q)
            return d_off, d_on

    def CarryOutbitShareShare(self, A: list[list[bitarray]], B: list[list[bitarray]], S: Server0 | Server1 | Server2) -> tuple[bitarray, bitarray]:
        if S.id() == 0:    
            k = len(A)
            B = B
            carry0 = bitarray("0")
            carry1 = bitarray("0")
            for i in range(k):
                invi = k - 1 - i
                temp0, temp00, temp01 = S.offline_ANDF(self.P, S.addF(self.P, A[invi][0], A[invi][1]), S.addF(self.P, B[invi][0], B[invi][1]))
                temp0, temp10, temp11 = S.offline_ANDF(self.P, S.addF(self.P, A[invi][0], A[invi][1]), S.addF(self.P, carry0, carry1))
                temp2, temp20, temp21 = S.offline_ANDF(self.P, S.addF(self.P, B[invi][0], B[invi][1]), S.addF(self.P, carry0, carry1))
                temp = self.XOR_offlineF([temp00, temp01], [temp10, temp11], S)
                carry = self.XOR_offlineF([temp[0], temp[1]], [temp20, temp21], S)
                carry0 = carry[0]
                carry1 = carry[1]
            return carry0, carry1
        else: 
            k = len(A)
            B = B
            carry_off = bitarray("0")
            carry_on = bitarray("0")
            for i in range(k):
                invi = k - 1 - i
                temp0_off = S.offline_ANDF(self.P, A[invi][0], B[invi][0])
                temp1_off = S.offline_ANDF(self.P, A[invi][0], carry_off)
                temp2_off = S.offline_ANDF(self.P, B[invi][0], carry_off)
                temp_off = self.XOR_offlineF([temp0_off], [temp1_off], S)
                carry_off = self.XOR_offlineF([temp_off], [temp2_off], S)
                temp0_on = S.online_ANDF(self.P, A[invi][1], B[invi][1])
                temp1_on = S.online_ANDF(self.P, A[invi][1], carry_on)
                temp2_on = S.online_ANDF(self.P, B[invi][1], carry_on)
                temp_on = self.XOR_onlineF(temp0_on, temp1_on, S)
                carry_on = self.XOR_onlineF(temp_on, temp2_on, S)
            return carry_off, carry_on
    
    def LT(self, A: list[bitarray], B: list[bitarray], l: int, S: Server0 | Server1 | Server2):
        if S.id() == 0:
            adec = self.BitDec(A, l, l, S)
            bdec = self.BitDec(B, l, l, S)
            a = self.BittoField(adec, S)
            b = self.BittoField(bdec, S)
            bprime = []
            for i in range(l):
                b0 = S.find_additive_inverse(self.P, b[i][0])
                b1 = S.find_additive_inverse(self.P, b[i][1])
                bprime.append([b0, b1])
            carry = self.CarryOutbitShareShare(a, bprime, S)
            return S.find_additive_inverse(self.P, carry[0]), S.find_additive_inverse(self.P, carry[1])
        else:
            adec = self.BitDec(A, l, l, S)
            bdec = self.BitDec(B, l, l, S)
            a = self.BittoField(adec, S)
            b = self.BittoField(bdec, S)
            bprime = []
            for i in range(l):
                b0 = S.find_additive_inverse(self.P, b[i][0])
                b1 = S.subtractF(self.P, b[i][1], int2ba(1))
                bprime.append([b0, b1])
            carry = self.CarryOutbitShareShare(a, bprime, S)
            return S.find_additive_inverse(self.P, carry[0]), S.subtractF(self.P, carry[1], int2ba(1))

    def Truncate(self, A:list[bitarray], l: int, m: list[bitarray], S: Server0 | Server1 | Server2):
        if S.id() == 0:
            x = self.B2U(m, l, S)
            powm = self.Pow2(m, l, S)
            invpowm = self.Inverse(powm, S)
            rbit = []
            for i in range(l):
                temp = self.GenerateRandomSharesFD(S)
                rbit.append([temp[2], temp[3]])
            rp0 = bitarray("0")
            rp1 = bitarray("0")
            for i in range(l):
                temp, temp0, temp1 = S.offline_ANDF(self.P, S.addF(self.P, x[i][0], x[i][1]), S.addF(self.P, rbit[i][0], rbit[i][1]))
                rp0 = S.addF(self.P, rp0, S.multiplyF(self.P, int2ba(2**i), temp0))
                rp1 = S.addF(self.P, rp1, S.multiplyF(self.P, int2ba(2**i), temp1))
            randint = self.GenerateRandomSharesFD(S)
            r2p0 = S.multiplyF(self.P, int2ba(2**l), randint[2])
            r2p1 = S.multiplyF(self.P, int2ba(2**l), randint[3])
            for i in range(l):
                invx0 = S.find_additive_inverse(self.P, x[i][0])
                invx1 = S.find_additive_inverse(self.P, x[i][1])
                temp, temp0, temp1 = S.offline_ANDF(self.P, S.addF(self.P, invx0, invx1), S.addF(self.P, rbit[i][0], rbit[i][1]))
                r2p0 = S.addF(self.P, r2p0, S.multiplyF(self.P, int2ba(2**i), temp0))
                r2p1 = S.addF(self.P, r2p1, S.multiplyF(self.P, int2ba(2**i), temp1))
            c0 = S.addF(self.P, S.addF(self.P, rp0, r2p0), A[0])
            c1 = S.addF(self.P, S.addF(self.P, rp1, r2p1), A[1])
            c = S.online_reconstructionF(self.P, c0, c1)
            cp = [None]
            for i in range(1, l):
                cptemp = int2ba((ba2int(c) % 2**i)%(2**self.P - 1), length=self.P)
                cp.append(cptemp)
            c2p0 = bitarray("0")
            c2p1 = bitarray("0")
            for i in range(1, l):
                temp0 = S.subtractF(self.P, x[i][0], x[i-1][0])
                temp1 = S.subtractF(self.P, x[i][1], x[i-1][1])
                c2p0 = S.addF(self.P, c2p0, S.multiplyF(self.P, cp[i], temp0))
                c2p1 = S.addF(self.P, c2p1, S.multiplyF(self.P, cp[i], temp1))
            d = self.LT([c2p0, c2p1], [rp0, rp1], l, S)
            btemp00 = S.addF(self.P, S.subtractF(self.P, c2p0, A[0]), rp0)
            btemp01 = S.addF(self.P, S.subtractF(self.P, c2p1, A[1]), rp1)
            btemp1 = S.offline_ANDF(self.P, S.addF(self.P, btemp00, btemp01), S.addF(self.P, invpowm[0], invpowm[1]))
            b0 = S.subtractF(self.P, d[0], btemp1[1])
            b1 = S.subtractF(self.P, d[1], btemp1[2])
            return b0, b1

        else:
            x = self.B2U(m, l, S)
            powm = self.Pow2(m, l, S)
            invpowm = self.Inverse(powm, S)
            rbit = []
            for i in range(l):
                temp = self.GenerateRandomSharesFD(S)
                rbit.append([temp[2], temp[3]])
            rp_off = bitarray("0")
            rp_on = bitarray("0")
            for i in range(l):
                temp_off = S.offline_ANDF(self.P, x[i][0], rbit[i][0])
                temp_on = S.online_ANDF(self.P, x[i][1], rbit[i][1])
                rp_off = S.addF(self.P, rp_off, S.multiplyF(self.P, int2ba(2**i), temp_off))
                rp_on = S.addF(self.P, rp_on, S.multiplyF(self.P, int2ba(2**i), temp_on))
            randint = self.GenerateRandomSharesFD(S)
            r2p_off = S.multiplyF(self.P, int2ba(2**l), randint[2])
            r2p_on = S.multiplyF(self.P, int2ba(2**l), randint[3])
            for i in range(l):
                invx_off = S.find_additive_inverse(self.P, x[i][0])
                invx_on = S.subtractF(self.P, x[i][1], int2ba(1))
                temp_off = S.offline_ANDF(self.P, invx_off, rbit[i][0])
                temp_on = S.online_ANDF(self.P, invx_on, rbit[i][1])
                r2p_off = S.addF(self.P, r2p_off, S.multiplyF(self.P, int2ba(2**i), temp_off))
                r2p_on = S.addF(self.P, r2p_on, S.multiplyF(self.P, int2ba(2**i), temp_on))
            c_off = S.addF(self.P, S.addF(self.P, rp_off, r2p_off), A[0])
            c_on = S.addF(self.P, S.addF(self.P, rp_on, r2p_on), A[1])
            c = S.online_reconstructionF(self.P, c_off, c_on)
            cp = [None]
            for i in range(1, l):
                cptemp = int2ba((ba2int(c) % 2**i)%(2**self.P - 1), length=self.P)
                cp.append(cptemp)
            c2p_off = bitarray("0")
            c2p_on = bitarray("0")
            for i in range(1, l):
                temp_off = S.subtractF(self.P, x[i][0], x[i-1][0])
                temp_on = S.subtractF(self.P, x[i][1], x[i-1][1])
                c2p_off = S.addF(self.P, c2p_off, S.multiplyF(self.P, cp[i], temp_off))
                c2p_on = S.addF(self.P, c2p_on, S.multiplyF(self.P, cp[i], temp_on))
            d = self.LT([c2p_off, c2p_on], [rp_off, rp_on], l, S)
            btemp0_off = S.addF(self.P, S.subtractF(self.P, c2p_off, A[0]), rp_off)
            btemp0_on = S.addF(self.P, S.subtractF(self.P, c2p_on, A[1]), rp_on)
            btemp1_off = S.offline_ANDF(self.P, btemp0_off, invpowm[0])
            btemp1_on = S.online_ANDF(self.P, btemp0_on, invpowm[1])
            b_off = S.subtractF(self.P, d[0], btemp1_off)
            b_on = S.subtractF(self.P, d[1], btemp1_on)
            return b_off, b_on

    def FPVMultiply(self, A: FPVShare, B: FPVShare, S: Server0 | Server1 | Server2):
        sharesa = A.getShare()
        sharesb = B.getShare()
        v1 = sharesa[0].get()
        v2 = sharesb[0].get()
        p1 = sharesa[1].get()
        p2 = sharesb[1].get()
        z1 = sharesa[2].get()
        z2 = sharesb[2].get()
        s1 = sharesa[3].get()
        s2 = sharesb[3].get()
        l = A.getl()
        if S.id() == 0:
            v = S.offline_ANDF(self.P, S.addF(self.P, v1[0], v1[1]), S.addF(self.P, v2[0], v2[1]))
            v = self.SimpleTrunc([v[1], v[2]], 2*l, l - 1, S)
            b = self.LT(v, [bitarray('0'), bitarray('0')], l + 1, S)
            temptrunc0 = S.offline_ANDF(self.P, S.addF(self.P, v[0], v[1]), S.addF(self.P, b[0], b[1]))
            temptrunc1 = [S.multiplyF(self.P, temptrunc0[1], int2ba(2)), S.multiplyF(self.P, temptrunc0[2], int2ba(2))]
            temptrunc2 = [S.find_additive_inverse(self.P, b[0]), S.find_additive_inverse(self.P, b[1])]
            temptrunc3 = S.offline_ANDF(self.P, S.addF(self.P, temptrunc2[0], temptrunc2[1]), S.addF(self.P, v[0], v[1]))
            temptrunc = [S.addF(self.P, temptrunc1[0], temptrunc3[1]), S.addF(self.P, temptrunc1[1], temptrunc3[2])]
            v = self.SimpleTrunc([temptrunc[0], temptrunc[1]], l + 1, 1, S)
            z = self.OR_offlineF(z1, z2, S)
            s = self.XOR_offlineF(s1, s2, S)
            ptemp0 = S.subtractF(self.P, b[0], S.addF(self.P, p1[0], p2[0]))
            ptemp1 = S.subtractF(self.P, b[1], S.addF(self.P, p1[1], p2[1]))
            ztemp = [S.find_additive_inverse(self.P, z[0]), S.find_additive_inverse(self.P, z[1])]
            p, pl0, pl1 = S.offline_ANDF(self.P, S.addF(self.P, ptemp0, ptemp1), S.addF(self.P, ztemp[0], ztemp[1]))
            vshare = Share()
            vshare.add(v[0])
            vshare.add(v[1])
            pshare = Share()
            pshare.add(pl0)
            pshare.add(pl1)
            zshare = Share()
            zshare.add(z[0])
            zshare.add(z[1])
            sshare = Share()
            sshare.add(s[0])
            sshare.add(s[1])
            output = FPVShare(vshare, pshare, zshare, sshare)
            return output
        else:
            v_off = S.offline_ANDF(self.P, v1[0], v2[0])
            v_on = S.online_ANDF(self.P, v1[1], v2[1])
            v = self.SimpleTrunc([v_off, v_on], 2*l, l - 1, S)
            b = self.LT(v, [bitarray('0'), int2ba(2**l)], l + 1, S)
            temptrunc0_off = S.offline_ANDF(self.P, v[0], b[0])
            temptrunc0_on = S.online_ANDF(self.P, v[1], b[1])
            temptrunc1 = [S.multiplyF(self.P, temptrunc0_off, int2ba(2)), S.multiplyF(self.P, temptrunc0_on, int2ba(2))]
            temptrunc2 = [S.find_additive_inverse(self.P, b[0]), S.subtractF(self.P, b[1], int2ba(1))]
            temptrunc3_off = S.offline_ANDF(self.P, temptrunc2[0], v[0])
            temptrunc3_on = S.online_ANDF(self.P, temptrunc2[1], v[1])
            temptrunc = [S.addF(self.P, temptrunc1[0], temptrunc3_off), S.addF(self.P, temptrunc1[1], temptrunc3_on)]
            v = self.SimpleTrunc([temptrunc[0], temptrunc[1]], l + 1, 1, S)
            z_off = self.OR_offlineF([z1[0]], [z2[0]], S)
            z_on = self.OR_onlineF(z1[1], z2[1], S)
            s_off = self.XOR_offlineF([s1[0]], [s2[0]], S)
            s_on = self.XOR_onlineF(s1[1], s2[1], S)
            ptemp_off = S.subtractF(self.P, b[0], S.addF(self.P, p1[0], p2[0]))
            ptemp_on = S.subtractF(self.P, int2ba(126), S.subtractF(self.P, b[1], S.addF(self.P, p1[1], p2[1])))
            ztemp = [S.find_additive_inverse(self.P, z_off), S.subtractF(self.P, z_on, int2ba(1))]
            p_off = S.offline_ANDF(self.P, ptemp_off, ztemp[0])
            p_on = S.online_ANDF(self.P, ptemp_on, ztemp[1])
            vshare = Share()
            vshare.add(v[0])
            vshare.add(v[1])
            pshare = Share()
            pshare.add(p_off)
            pshare.add(p_on)
            zshare = Share()
            zshare.add(z_off)
            zshare.add(z_on)
            sshare = Share()
            sshare.add(s_off)
            sshare.add(s_on)
            output = FPVShare(vshare, pshare, zshare, sshare)
            return output

    def FPVonline_reconstruction2Float(self, A: FPVShare, S: Server0 | Server1 | Server2):
        sharesa = A.getShare()
        v1 = sharesa[0].get()
        p1 = sharesa[1].get()
        z1 = sharesa[2].get()
        s1 = sharesa[3].get()
        
        v = S.online_reconstructionF(61, v1[0], v1[1])
        p = S.online_reconstructionF(61, p1[0], p1[1])
        z = S.online_reconstructionF(61, z1[0], z1[1])
        s = S.online_reconstructionF(61, s1[0], s1[1])
        # p = S.addF(self.P, int2ba(127), p)

        v = ba2base(2, v[self.P - 23 : self.P])
        p = ba2base(2, p[self.P - 8 : self.P])
        s = ba2base(2, s[self.P - 1 : self.P])

        z = ba2int(z)
        if z == 1:
            return 0.0
        
        f = self.converttofloat(s + p + v)
        return f

    def FPVoffline_shareFloat(self, sharingserver: int, S: Server0 | Server1 | Server2):
        if S.id() == 0:
            vl1, vl2 = S.offline_shareF(self.P, sharingserver)
            pl1, pl2 = S.offline_shareF(self.P, sharingserver)
            zl1, zl2 = S.offline_shareF(self.P, sharingserver)
            sl1, sl2 = S.offline_shareF(self.P, sharingserver)
            return [vl1, vl2, pl1, pl2, zl1, zl2, sl1, sl2]
        
        elif S.id() == 1:
            if sharingserver == 1:
                vl1, vl2 = S.offline_shareF(self.P, sharingserver)
                pl1, pl2 = S.offline_shareF(self.P, sharingserver)
                zl1, zl2 = S.offline_shareF(self.P, sharingserver)
                sl1, sl2 = S.offline_shareF(self.P, sharingserver)
                return [vl1, vl2, pl1, pl2, zl1, zl2, sl1, sl2]
            else:
                vl1 = S.offline_shareF(self.P, sharingserver)
                pl1 = S.offline_shareF(self.P, sharingserver)
                zl1 = S.offline_shareF(self.P, sharingserver)
                sl1 = S.offline_shareF(self.P, sharingserver)
                return [vl1, pl1, zl1, sl1]
        else:
            if sharingserver == 2:
                vl1, vl2 = S.offline_shareF(self.P, sharingserver)
                pl1, pl2 = S.offline_shareF(self.P, sharingserver)
                zl1, zl2 = S.offline_shareF(self.P, sharingserver)
                sl1, sl2 = S.offline_shareF(self.P, sharingserver)
                return [vl1, vl2, pl1, pl2, zl1, zl2, sl1, sl2]
            else:
                vl2 = S.offline_shareF(self.P, sharingserver)
                pl2 = S.offline_shareF(self.P, sharingserver)
                zl2 = S.offline_shareF(self.P, sharingserver)
                sl2 = S.offline_shareF(self.P, sharingserver)
                return [vl2, pl2, zl2, sl2]
    
    def FPVonline_shareFloat(self, sharingserver: int, offlineData: list[bitarray], message: float | None, S: Server0 | Server1 | Server2):
        vshare = Share()
        pshare = Share()
        zshare = Share()
        sshare = Share()
        if S.id() == 0:
            if S.id() == sharingserver:
                if message == 0.0:
                    zmessage = bitarray("1")
                else:
                    zmessage = bitarray("0")
                m = self.float_to_bin(message)
                smessage = bitarray(m[0:1])
                pmessage = bitarray(m[1:9])
                vmessage = bitarray("1" + m[9:])
                S.online_shareF(self.P, sharingserver, offlineData[0], offlineData[1], vmessage)
                S.online_shareF(self.P, sharingserver, offlineData[2], offlineData[3], pmessage)
                S.online_shareF(self.P, sharingserver, offlineData[4], offlineData[5], zmessage)
                S.online_shareF(self.P, sharingserver, offlineData[6], offlineData[7], smessage)
            vshare.add(offlineData[0])
            vshare.add(offlineData[1])
            pshare.add(offlineData[2])
            pshare.add(offlineData[3])
            zshare.add(offlineData[4])
            zshare.add(offlineData[5])
            sshare.add(offlineData[6])
            sshare.add(offlineData[7])
        elif S.id() == 1:
            vm, pm, zm, sm = None, None, None, None
            if sharingserver == 1:
                if message == 0.0:
                    zmessage = bitarray("1")
                else:
                    zmessage = bitarray("0")
                m = self.float_to_bin(message)
                smessage = bitarray(m[0:1])
                pmessage = bitarray(m[1:9])
                vmessage = bitarray("1" + m[9:])
                vm = S.online_shareF(self.P, sharingserver, offlineData[0], offlineData[1], vmessage)
                pm = S.online_shareF(self.P, sharingserver, offlineData[2], offlineData[3], pmessage)
                zm = S.online_shareF(self.P, sharingserver, offlineData[4], offlineData[5], zmessage)
                sm = S.online_shareF(self.P, sharingserver, offlineData[6], offlineData[7], smessage)
                vshare.add(offlineData[0])
                vshare.add(vm)
                pshare.add(offlineData[2])
                pshare.add(pm)
                zshare.add(offlineData[4])
                zshare.add(zm)
                sshare.add(offlineData[6])
                sshare.add(sm)
            else:
                vm = S.online_shareF(self.P, sharingserver, None, None, None)
                pm = S.online_shareF(self.P, sharingserver, None, None, None)
                zm = S.online_shareF(self.P, sharingserver, None, None, None)
                sm = S.online_shareF(self.P, sharingserver, None, None, None)
                vshare.add(offlineData[0])
                vshare.add(vm)
                pshare.add(offlineData[1])
                pshare.add(pm)
                zshare.add(offlineData[2])
                zshare.add(zm)
                sshare.add(offlineData[3])
                sshare.add(sm)
        else:
            vm, pm, zm, sm = None, None, None, None
            if sharingserver == 2:
                if message == 0.0:
                    zmessage = bitarray("1")
                else:
                    zmessage = bitarray("0")
                m = self.float_to_bin(message)
                smessage = bitarray(m[0:1])
                pmessage = bitarray(m[1:9])
                vmessage = bitarray("1" + m[9:])
                vm = S.online_shareF(self.P, sharingserver, offlineData[0], offlineData[1], vmessage)
                pm = S.online_shareF(self.P, sharingserver, offlineData[2], offlineData[3], pmessage)
                zm = S.online_shareF(self.P, sharingserver, offlineData[4], offlineData[5], zmessage)
                sm = S.online_shareF(self.P, sharingserver, offlineData[6], offlineData[7], smessage)
                vshare.add(offlineData[1])
                vshare.add(vm)
                pshare.add(offlineData[3])
                pshare.add(pm)
                zshare.add(offlineData[5])
                zshare.add(zm)
                sshare.add(offlineData[7])
                sshare.add(sm)
            else:
                vm = S.online_shareF(self.P, sharingserver, None, None, None)
                pm = S.online_shareF(self.P, sharingserver, None, None, None)
                zm = S.online_shareF(self.P, sharingserver, None, None, None)
                sm = S.online_shareF(self.P, sharingserver, None, None, None)
                vshare.add(offlineData[0])
                vshare.add(vm)
                pshare.add(offlineData[1])
                pshare.add(pm)
                zshare.add(offlineData[2])
                zshare.add(zm)
                sshare.add(offlineData[3])
                sshare.add(sm)
        Output = FPVShare(vshare, pshare, zshare, sshare)
        return Output

def TestFunctions(A: list[bitarray], B: list[bitarray], C :list[bitarray], S: Server0 | Server1 | Server2):
    fpv = FPVArithmetic()
    if S.id() == 0:
        x = 0.57
        offlinedata = fpv.FPVoffline_shareFloat(0, S)
        sharex = fpv.FPVonline_shareFloat(0, offlinedata, x, S)
        offlinedata = fpv.FPVoffline_shareFloat(1, S)
        sharey = fpv.FPVonline_shareFloat(1, offlinedata, None, S)
        offlinedata = fpv.FPVoffline_shareFloat(2, S)
        sharez = fpv.FPVonline_shareFloat(2, offlinedata, None, S)
        outoff = fpv.FPVMultiply(sharex, sharey, S)
        v = fpv.FPVonline_reconstruction2Float(outoff, S)
        print(v)
        output = fpv.FPVMultiply(outoff, sharez, S)
        v = fpv.FPVonline_reconstruction2Float(output, S)
        print(v)
        
    elif S.id() == 1:
        offlinedata = fpv.FPVoffline_shareFloat(0, S)
        sharex = fpv.FPVonline_shareFloat(0, offlinedata, None, S)
        y = 0.047
        offlinedata = fpv.FPVoffline_shareFloat(1, S)
        sharey = fpv.FPVonline_shareFloat(1, offlinedata, y, S)
        offlinedata = fpv.FPVoffline_shareFloat(2, S)
        sharez = fpv.FPVonline_shareFloat(2, offlinedata, None, S)
        outoff = fpv.FPVMultiply(sharex, sharey, S)
        v = fpv.FPVonline_reconstruction2Float(outoff, S)
        output = fpv.FPVMultiply(outoff, sharez, S)
        v = fpv.FPVonline_reconstruction2Float(output, S)

    else:
        offlinedata = fpv.FPVoffline_shareFloat(0, S) 
        sharex = fpv.FPVonline_shareFloat(0, offlinedata, None, S)
        offlinedata = fpv.FPVoffline_shareFloat(1, S)
        sharey = fpv.FPVonline_shareFloat(1, offlinedata, None, S)
        z = 0.945
        offlinedata = fpv.FPVoffline_shareFloat(2, S)
        sharez = fpv.FPVonline_shareFloat(2, offlinedata, z, S)
        outoff = fpv.FPVMultiply(sharex, sharey, S)
        v = fpv.FPVonline_reconstruction2Float(outoff, S)
        output = fpv.FPVMultiply(outoff, sharez, S)
        v = fpv.FPVonline_reconstruction2Float(output, S)


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

    l1 = bitarray(bin(random.getrandbits(61))[2:].zfill(61))
    l2 = bitarray(bin(random.getrandbits(61))[2:].zfill(61))
    inp = bitarray("001")
    m = int2ba((ba2int(inp) + ba2int(l1) + ba2int(l2))%(2**61-1), length=61)
    # inp = bitarray("0")
    # m = inp ^ l1 ^ l2   

    k1 = bitarray(bin(random.getrandbits(61))[2:].zfill(61))
    k2 = bitarray(bin(random.getrandbits(61))[2:].zfill(61))
    sk = bitarray("000")
    mk = int2ba((ba2int(sk) + ba2int(k1) + ba2int(k2))%(2**61-1), length=61)
    # sk = bitarray("0")
    # mk = sk ^ k1 ^ k2   
    
    x1 = bitarray(bin(random.getrandbits(61))[2:].zfill(61))
    x2 = bitarray(bin(random.getrandbits(61))[2:].zfill(61))
    x = bitarray("0")
    mx = int2ba((ba2int(x) + ba2int(x1) + ba2int(x2))%(2**61-1), length=61)
    # mx = x ^ x1 ^ x2   
    # 2.5 = 0 10000000 01000000000000000000000
    # 3.5 = 0 10000000 11000000000000000000000
    



    manager = multiprocessing.Manager()
    d = manager.dict()

    s0 = Share()
    s1 = Share()
    s2 = Share()

    p0 = multiprocessing.Process(target=TestFunctions, args=([l1, l2], [k1, k2], [x1, x2], S0))
    p1 = multiprocessing.Process(target=TestFunctions, args=([l1, m], [k1, mk], [x1, mx], S1))
    p2 = multiprocessing.Process(target=TestFunctions, args=([l2, m], [k2, mk], [x2, mx], S2))

    p0.start()
    p1.start()
    p2.start()

    p0.join()
    p1.join()
    p2.join()

