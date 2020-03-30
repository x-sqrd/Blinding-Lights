#
# //     //  //             //  //                      //  //          //
# //     //                 //                          //              //        //
# /////  //  //  //////  /////  //  /////// //////      //  //  //////  //////  //////    //////
# //  // //  //  //  // //  //  //  //   // //  //      //  //  //  //  //  //    //     //
# /////  //  //  //  //  /////  //  //   // //////      //  //  //////  //  //    // /////
#                                               //                  //
#                                           //////              //////
# created by Shad0w7

# Blinding Decode NOCOMPRESSION v0.0.1a
''' [Input]: Colordata
    [Output]: String (ASCII)
    [Description]:  '''

import re
import sys
import binascii
FlexibleInput = False
# encoding/decoding function from stackexchange thread
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



#Input Stuff
if FlexibleInput == False: inputstr = "[('#00FFFF', '#808080', '#FF00FF', '#00FF00', '#FF00FF', '#008080', '#FF00FF', '#008080', '#FF00FF', '#FFCC99', '#0000FF', '#FFFFFF', '#00FF00', '#FFFF00', '#FF00FF', '#FFCC99', '#FFFF00', '#0000FF', '#FF00FF', '#008080', '#FF00FF', '#00FFFF')]"
if FlexibleInput: inputstr = input('InputHexData: ') # Use Custom Input

#Removing All Tuples and Text Stuff and Converting to an easy text
hexstr = inputstr + '~~~' #know where the end is
data = hexstr.split("'")
rawhex = []

counter = 0
data[counter]

for z in range(0, len(data)):
    if '#' in str(data[z]):
        rawhex.append(data[z])
    else: continue


#8 Bit Color Matrix
Colors = [
    ('#FFFFFF', '0000'), #white
    ('#00FFFF', '0100'), #aqua
    ('#FF00FF', '0110'), #brightpink
    ('#FFFF00', '0111'), #yellow
    ('#C0C0C0', '0011'), #lightgrey
    ('#FF0000', '0001'), #red
    ('#00FF00', '0101'), #brightgreen
    ('#0000FF', '0010'), #blue
    ('#808080', '1000'), #darkgrey
    ('#008080', '1100'), #turquoise
    ('#FF5005', '1110'), #orange
    ('#FFCC99', '1111'), #tan
    ('#993F00', '1011'), #darkorange
    ('#4C005C', '1001'), #darkpurple
    ('#94FFB5', '1101'), #lightmintgreen
    ('#FFA8BB', '1010')] #lightpink

binarylist = []
for x in range(0, len(rawhex)):
    for y in range(0, 16):
        if rawhex[x] == Colors[y][0]:
            binarylist.append(Colors[y][1])


binarystring = ''.join(map(str, binarylist))

originalstring = text_from_bits(binarystring)

sys.exit(originalstring)
