from bitarray import bitarray
from bitarray.util import *

# Function for converting decimal to binary
# def float_bin(my_number, places = 3):
#     my_whole, my_dec = str(my_number).split(".")
#     my_whole = int(my_whole)
#     res = (str(bin(my_whole))+".").replace('0b','')
 
#     for x in range(places):
#         my_dec = str('0.')+str(my_dec)
#         temp = '%1.20f' %(float(my_dec)*2)
#         my_whole, my_dec = temp.split(".")
#         res += my_whole
#     return res
 
# def float2IEEE754(n) :
#     # identifying whether the number
#     # is positive or negative
#     sign = 0
#     if n < 0 :
#         sign = 1
#         n = n * (-1)
#     p = 30
#     # convert float to binary
#     dec = float_bin (n, places = p)
 
#     dotPlace = dec.find('.')
#     onePlace = dec.find('1')
#     # finding the mantissa
#     if onePlace > dotPlace:
#         dec = dec.replace(".","")
#         onePlace -= 1
#         dotPlace -= 1
#     elif onePlace < dotPlace:
#         dec = dec.replace(".","")
#         dotPlace -= 1
#     mantissa = dec[onePlace+1:]
 
#     # calculating the exponent(E)
#     exponent = dotPlace - onePlace
#     exponent_bits = exponent + 127
 
#     # converting the exponent from
#     # decimal to binary
#     exponent_bits = bin(exponent_bits).replace("0b",'')
 
#     mantissa = mantissa[0:23]
 
#     # the IEEE754 notation in binary    
#     final = str(sign) + exponent_bits.zfill(8) + mantissa
 
#     # convert the binary to hexadecimal
#     hstr = '0x%0*X' %((len(final) + 3) // 4, int(final, 2))
#     return bitarray(final)

def binaryOfFraction(fraction):
    binary = str()
    while (fraction):
        fraction *= 2
        if (fraction >= 1):
            int_part = 1
            fraction -= 1
        else:
            int_part = 0
        binary += str(int_part)
    return binary
 
def floatingPoint(real_no):
    sign_bit = 0
    if(real_no < 0):
        sign_bit = 1
    real_no = abs(real_no)
    int_str = bin(int(real_no))[2 : ]
    fraction_str = binaryOfFraction(real_no - int(real_no))
    ind = int_str.index('1')
    exp_str = bin((len(int_str) - ind - 1) + 127)[2 : ]
    mant_str = int_str[ind + 1 : ] + fraction_str
    mant_str = mant_str + ('0' * (23 - len(mant_str)))
    return bitarray(str(sign_bit)+ exp_str+ mant_str[0:23])

def convertToInt(mantissa_str):
    power_count = -1
    mantissa_int = 0
    for i in mantissa_str:
        mantissa_int += (int(i) * pow(2, power_count))
        power_count -= 1
    return (mantissa_int + 1)

def converttofloat(ieee_32: bitarray):
    signstr = str(ieee_32[0])
    expstr = ba2base(2, ieee_32[1:9])
    manstr = ba2base(2, ieee_32[9:])
    ieee_32 = signstr + "|" + expstr + "|" + manstr
    sign_bit = int(ieee_32[0])
    exponent_bias = int(ieee_32[2 : 10], 2)
    exponent_unbias = exponent_bias - 127
    mantissa_str = ieee_32[11 : ]
    mantissa_int = convertToInt(mantissa_str)
    real_no = pow(-1, sign_bit) * mantissa_int * pow(2, exponent_unbias)
    return real_no

# Driver Code
if __name__ == "__main__" :
    element = 16  # The element for which we want to find the inverse
    prime_l = 7  # The value of 'l', a small prime number
    f1 = floatingPoint(8.75)
    print(f1)
    print(converttofloat(f1))