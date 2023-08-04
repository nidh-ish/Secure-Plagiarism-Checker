from server import *
from aes import *
from fpv import *
import math

def Write2File(f0, f1, f2, inp1, v1):
    f0.write(f"3\n")
    f1.write(f"3\n")
    f2.write(f"3\n")
    for i in range(3):
        l1 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
        l2 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
        m = l1 ^ l2 ^ inp1[i] 
        f0.write(f"{ba2base(2, l1)} {ba2base(2, l2)}\n")
        f1.write(f"{ba2base(2, l1)} {ba2base(2, m)}\n")
        f2.write(f"{ba2base(2, l2)} {ba2base(2, m)}\n")

    for i in range(3):
        l1 = int2ba(random.randint(0, 2**61 - 2), length=61)
        l2 = int2ba(random.randint(0, 2**61 - 2), length=61)
        m = int2ba((ba2int(l1) + ba2int(l2) + v1[i])%(2**61-1), length=61) 
        f0.write(f"{ba2base(2, l1)} {ba2base(2, l2)}\n")
        f1.write(f"{ba2base(2, l1)} {ba2base(2, m)}\n")
        f2.write(f"{ba2base(2, l2)} {ba2base(2, m)}\n")
    s = 0
    for i in v1:
        s += i**2
    s = math.sqrt(s)
    s = 1/s
    fpv = FPVArithmetic()
    zmessage = None
    if s == 0.0:
        zmessage = bitarray("1")
    else:
        zmessage = bitarray("0")
    m = fpv.float_to_bin(s)
    smessage = bitarray(m[0:1])
    pmessage = bitarray(m[1:9])
    vmessage = bitarray("1" + m[9:])
    s = [vmessage, pmessage, zmessage, smessage]
    for i in s:
        l1 = int2ba(random.randint(0, 2**61 - 2), length=61)
        l2 = int2ba(random.randint(0, 2**61 - 2), length=61)
        m = int2ba((ba2int(l1) + ba2int(l2) + ba2int(i))%(2**61-1), length=61) 
        f0.write(f"{ba2base(2, l1)} {ba2base(2, l2)}\n")
        f1.write(f"{ba2base(2, l1)} {ba2base(2, m)}\n")
        f2.write(f"{ba2base(2, l2)} {ba2base(2, m)}\n")




# que = multiprocessing.Queue()

# p1 = Process(target = getmethod, args = [que])
# p2 = Process(target = putmethod, args = [que])


# p1.start()
# p2.start()

# p1.join()
# p2.join()
# inp = bitarray("01010100011101110110111100100000010011110110111001100101001000000100111001101001011011100110010100100000010101000111011101101111")
# print("or", ba2hex(inp))

f0 = open("Client1_Server0_v2.dat", "w+")
f1 = open("Client1_Server1_v2.dat", "w+")
f2 = open("Client1_Server2_v2.dat", "w+")
inp1 = [bitarray("01010100011101110110111100100000010011110110111001100101001000000100111001101001011011100110010100100000010101000111011101101111"), bitarray("00000010100001001100111000111011111000010110100100000000111110101101110011101010010011000001111110000001010100101111110110010001"), bitarray("10100111010110011100100101111000001000110110101100000110111011011100010000101001101100010011100100101111110100101110100100011100")]
inp2 = [bitarray("11001111101111011111001011100100010111000100001000111001111011111110100110010111101100110111001100101101000110100110001000110100"), bitarray("10100111010110011100100101111000001000110110101100000110111011011100010000101001101100010011100100101111110100101110100100011100"), bitarray("01010100011101110110111100100000010011110110111001100101001000000100111001101001011011100110010100100000010101000111011101101111")]
v1 = [1, 2, 3]
v2 = [2, 4, 5]

Write2File(f0, f1, f2, inp1, v1)
# for i in range(3):
#     l1 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
#     l2 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
#     m = l1 ^ l2 ^ inp1[i] 
#     f0.write(f"{ba2base(2, l1)} {ba2base(2, l2)}\n")
#     f1.write(f"{ba2base(2, l1)} {ba2base(2, m)}\n")
#     f2.write(f"{ba2base(2, l2)} {ba2base(2, m)}\n")

# for i in range(3):
#     l1 = int2ba(random.randint(0, 2**61 - 2), length=61)
#     l2 = int2ba(random.randint(0, 2**61 - 2), length=61)
#     m = int2ba((ba2int(l1) + ba2int(l2) + v1[i])%(2**61-1), length=61) 
#     f0.write(f"{ba2base(2, l1)} {ba2base(2, l2)}\n")
#     f1.write(f"{ba2base(2, l1)} {ba2base(2, m)}\n")
#     f2.write(f"{ba2base(2, l2)} {ba2base(2, m)}\n")
# s = 0
# for i in v1:
#     s += i**2
# s = math.sqrt(s)
# s = 1/s
# fpv = FPVArithmetic()
# zmessage = None
# if s == 0.0:
#     zmessage = bitarray("1")
# else:
#     zmessage = bitarray("0")
# m = fpv.float_to_bin(s)
# smessage = bitarray(m[0:1])
# pmessage = bitarray(m[1:9])
# vmessage = bitarray("1" + m[9:])
# s = [vmessage, pmessage, zmessage, smessage]
# for i in s:
#     l1 = int2ba(random.randint(0, 2**61 - 2), length=61)
#     l2 = int2ba(random.randint(0, 2**61 - 2), length=61)
#     m = int2ba((ba2int(l1) + ba2int(l2) + ba2int(i))%(2**61-1), length=61) 
#     f0.write(f"{ba2base(2, l1)} {ba2base(2, l2)}\n")
#     f1.write(f"{ba2base(2, l1)} {ba2base(2, m)}\n")
#     f2.write(f"{ba2base(2, l2)} {ba2base(2, m)}\n")


f0.close()
f1.close()
f2.close()

# def getSharesfromFile(f) -> list[Share]:
#     line = f.readline()
#     shares = []
#     while line:
#         s = Share()
#         x = line.split(" ")
#         s.add(bitarray(x[0]))
#         s.add(bitarray(x[1]))
#         shares.append(s)
#         line = f.readline()
#     return shares

# f0 = open("Client0_Server0.dat", "r")
# s0 = getSharesfromFile(f0)
# f0.close()
# f1 = open("Client0_Server1.dat", "r")
# s1 = getSharesfromFile(f1)
# f1.close()
# f2 = open("Client0_Server2.dat", "r")
# s2 = getSharesfromFile(f2)
# f2.close()

# for i in range(len(s0)):
#     l10, l20 = s0[i].get()
#     l11, m1 = s1[i].get()
#     l22, m2 = s2[i].get()
#     print(ba2int(l10) == ba2int(l11), ba2int(l20) == ba2int(l22), ba2int(m1) == ba2int(m2))
#     print(ba2hex(l11 ^ l22 ^ m2))