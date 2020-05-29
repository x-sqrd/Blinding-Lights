# -- Core Packages --

import base64
import re
import sys
import binascii

# ASCII to Bits

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

# File to ASCII

def grabfile(path): # WORKS
    with open(path, "rb") as f:
        encodedZip = base64.b64encode(f.read())
        rawoutput = encodedZip.decode()
        while True:
            if rawoutput[-1] == "=": 
                rawoutput = rawoutput[:-1]
                continue
            else: 
                break
        return rawoutput

# Color Array

global Colors
Colors = [
    ('0', '0000', '#FFFFFF'), #white
    ('1', '0100', '#00FFFF'), #aqua
    ('2', '0110', '#FF00FF'), #brightpink
    ('3', '0111', '#FFFF00'), #yellow
    ('4', '0011', '#C0C0C0'), #lightgrey
    ('5', '0001', '#FF0000'), #red
    ('6', '0101', '#00FF00'), #brightgreen
    ('7', '0010', '#0000FF'),  #blue
    ('8', '1000', '#808080'), #darkgrey
    ('9', '1100', '#008080'), #turquoise
    ('A', '1110', '#FF5005'), #orange
    ('B', '1111', '#FFCC99'), #tan
    ('C', '1011', '#993F00'), #darkorange
    ('D', '1001', '#4C005C'), #darkpurple
    ('E', '1101', '#94FFB5'), #lightmintgreen
    ('F', '1010', '#FFA8BB')] #lightpink

# Bit to Colors

def textToHex(string): # Callable Function
    output = []
    binaryinput = text_to_bits(string)

    split = re.findall('.{1,4}', binaryinput)

    for z in range(0, len(split)):
        for x in range(0,16):
            if split[z] == Colors[x][1]:
                output.append(Colors[x][0])
    return output

    





# -- CLI -- 
print("""

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|         BlindingLightsCLIInterface        |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

v0.0.0
Ayush Nayak et al.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



""")
input("Press Enter to Continue...")