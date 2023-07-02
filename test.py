from server import *
from aes import *



# que = multiprocessing.Queue()

# p1 = Process(target = getmethod, args = [que])
# p2 = Process(target = putmethod, args = [que])


# p1.start()
# p2.start()

# p1.join()
# p2.join()
inp = bitarray("01010100011101110110111100100000010011110110111001100101001000000100111001101001011011100110010100100000010101000111011101101111")
print("or", ba2hex(inp))

# f0 = open("Client0_Server0.dat", "w+")
# f1 = open("Client0_Server1.dat", "w+")
# f2 = open("Client0_Server2.dat", "w+")

# for i in range(10):
#     l1 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
#     l2 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
#     m = l1 ^ l2 ^ inp 
#     f0.write(f"{ba2base(2, l1)} {ba2base(2, l2)}\n")
#     f1.write(f"{ba2base(2, l1)} {ba2base(2, m)}\n")
#     f2.write(f"{ba2base(2, l2)} {ba2base(2, m)}\n")

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