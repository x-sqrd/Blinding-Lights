#
# //     //  //             //  //                      //  //          //
# //     //                 //                          //              //        //
# /////  //  //  //////  /////  //  /////// //////      //  //  //////  //////  //////    //////
# //  // //  //  //  // //  //  //  //   // //  //      //  //  //  //  //  //    //     //
# /////  //  //  //  //  /////  //  //   // //////      //  //  //////  //  //    // /////
#                                               //                  //
#                                           //////              //////
# created by Shad0w7

# Blinding Encode NOCOMPRESSION v0.0.1a
''' [Input]: String fixed or with input()
    [Output]: ColorMatrix on 10x10 grid to encode and send (with binary 0's afterward)
    [Description]: This script will take in any string, and output the colormatrix that needs to be sent, if it needs to take up more than one frame, it will send out multiple blocks of different colors'''

import re
import sys
import binascii
import base64
# -- Bootflags --
FlexibleInput = False # ONLY IN ALPHA
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


# Input
global inputstr
if FlexibleInput == False: inputstr = "Hello World"
if FlexibleInput: inputstr = input('InputStr: ') # Use Custom Input

# Converting String to Binary
binaryinput = text_to_bits(inputstr) #! TODO NEED TO CREATE ENCODE/DECODE METHOD!!!!

#8 Bit Color Matrix
Colors = [
    ('#FFFFFF', '0000'), #white
    ('#00FFFF', '0100'), #aqua
    ('#FF00FF', '0110'), #brightpink
    ('#FFFF00', '0111'), #yellow
    ('#C0C0C0', '0011'), #lightgrey
    ('#FF0000', '0001'), #red
    ('#00FF00', '0101'), #brightgreen
    ('#0000FF', '0010'),  #blue
    ('#808080', '1000'), #darkgre7
    ('#008080', '1100'), #turquoise
    ('#FF5005', '1110'), #orange
    ('#FFCC99', '1111'), #tan
    ('#993F00', '1011'), #darkorange
    ('#4C005C', '1001'), #darkpurple
    ('#94FFB5', '1101'), #lightmintgreen
    ('#FFA8BB', '1010')] #lightpink

output = [] # output list

# Parsing Color To List
split = re.findall('.{1,4}', binaryinput)   # may need to use re.finditer() instead of findall because of stringsize
                                            # has issue where needs exactly 3 on each i think or else will output 000
for z in range(0, len(split)):
    block = split[z]
    for x in range(0,16):
        if block == Colors[x][1]:
            output.append(Colors[x][0])     # at this point there is an exaustive list of colors created to represent the different code peices, but it is not rationalized into small peices

cnt = 0 # Ew i prefer //konnie
matrisizedoutput = []
while cnt < len(output):
    templist = []
    if cnt+100 >= len(output):
        for a in range(cnt, len(output)):
            templist.append(output[a])

    else:
        for a in range(cnt, cnt+100):
            templist.append(output[a])

    cnt+=100

    matrisizedoutput.append(tuple(templist))
    templist.clear()

sys.exit(matrisizedoutput)
