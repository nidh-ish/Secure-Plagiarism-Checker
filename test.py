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

f0 = open("Client2_Server0_v2.dat", "w+")
f1 = open("Client2_Server1_v2.dat", "w+")
f2 = open("Client2_Server2_v2.dat", "w+")

# for i in range(10):
#     l1 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
#     l2 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
#     m = l1 ^ l2 ^ inp 
#     f0.write(f"{ba2base(2, l1)} {ba2base(2, l2)}\n")
#     f1.write(f"{ba2base(2, l1)} {ba2base(2, m)}\n")
#     f2.write(f"{ba2base(2, l2)} {ba2base(2, m)}\n")
#     inp = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
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

import struct
from bitarray import bitarray

def float_to_binary128(value):
    # Pack the floating-point value into 16 bytes (128 bits)
    binary = struct.pack('>Q', struct.unpack('>Q', struct.pack('>d', value))[0])

    # Extract the sign, exponent, and significand from the packed binary
    sign = (binary[0] >> 7) & 0x01
    exponent = ((binary[0] & 0x7F) << 8) | (binary[1])
    significand = int.from_bytes(binary[2:], 'big')

    # Convert each component to binary strings
    sign_str = format(sign, '01b')
    exponent_str = format(exponent, '015b')
    significand_str = format(significand, '0112b')

    # Combine the binary strings
    binary128 = sign_str + exponent_str + significand_str

    return binary128

# Example usage
# value = 3.14159
# binary128 = float_to_binary128(value)
# print(binary128)

# Example usage
value = 3.14159
binary128 = float_to_binary128(value)
print(ba2hex(bitarray(binary128)))
