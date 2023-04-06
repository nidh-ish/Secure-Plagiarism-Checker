from server import *
import threading
from aes import *

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

    input_fin0 = [[l1], [l2]]
    input_fin1 = [[l1], [m]]
    input_fin2 = [[l2], [m]]

    k1 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    k2 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
    sk = bitarray("01010100011010000110000101110100011100110010000001101101011110010010000001001011011101010110111001100111001000000100011001110101")
    mk = k1 ^ k2 ^ sk

    key_0 = [[k1], [k2]]
    key_1 = [[k1], [mk]]
    key_2 = [[k2], [mk]]

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

    p0 = multiprocessing.Process(target=aes.circuit, args=([k1 , k2], [l1 , l2], S0, s0))
    p1 = multiprocessing.Process(target=aes.circuit, args=([k1, mk], [l1, m], S1, s1))
    p2 = multiprocessing.Process(target=aes.circuit, args=([k2, mk], [l2, m], S2, s2))

    p0.start()
    p1.start()
    p2.start()

    p0.join()
    p1.join()
    p2.join()

    o0 = s0.get()
    o1 = s1.get()
    o2 = s2.get()

    print("0: ", ba2hex(o0[0]), ba2hex(o0[1]) )
    print("1: ", ba2hex(o1[0]), ba2hex(o1[1]) )
    print("2: ", ba2hex(o2[0]), ba2hex(o2[1]) )

    print("AES input: ", ba2hex(inp))
    print("AES key: ", ba2hex(sk))
    print("AES output: ", ba2hex(o0[0] ^ o0[1] ^ o1[1]))
    # Run the online phase 