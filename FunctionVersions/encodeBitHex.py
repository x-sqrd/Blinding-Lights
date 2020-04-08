# Blinding Lights Image to Cartesian Coordinates [Python 3.8.2]
if __name__ == "__main__": print('Module encodeBitHex.py')
# Created by Ayush Nayak in 2020

import re
import sys
import binascii
import base64

# Stack Overflow Stuff
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



global output
output = [] # output list

#8 Bit Color Matrix
global Colors
Colors = [
    ('#FFFFFF', '0000'), #white
    ('#00FFFF', '0100'), #aqua
    ('#FF00FF', '0110'), #brightpink
    ('#FFFF00', '0111'), #yellow
    ('#C0C0C0', '0011'), #lightgrey
    ('#FF0000', '0001'), #red
    ('#00FF00', '0101'), #brightgreen
    ('#0000FF', '0010'),  #blue
    ('#808080', '1000'), #darkgrey
    ('#008080', '1100'), #turquoise
    ('#FF5005', '1110'), #orange
    ('#FFCC99', '1111'), #tan
    ('#993F00', '1011'), #darkorange
    ('#4C005C', '1001'), #darkpurple
    ('#94FFB5', '1101'), #lightmintgreen
    ('#FFA8BB', '1010')] #lightpink

def texttohex(string): # Callable Function
    binaryinput = text_to_bits(string)

    split = re.findall('.{1,4}', binaryinput)

    for z in range(0, len(split)):
        for x in range(0,16):
            if split[z] == Colors[x][1]:
                output.append(Colors[x][0])
    o = " "
    stroutput = o.join(output)
    return stroutput

if __name__ == "__main__": print("Imported Successfuly") # import message
