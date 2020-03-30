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
# -- Bootflags --
FlexibleInput = False # ONLY IN ALPHA

# Input
global inputstr
if FlexibleInput == False:inputstr = "THIS IS AN AMAZINGLY AMAZING TEST! LOREM IPSUM DOLOR SIT AMET CORSUCATME YAY I LOVE MY LIFE ANEESH IS SUCKY LIFE IS GOOD (FUTURE FEAT DRAKE) ALTHOUGH IN REALITY IT WAS LIFE IS GOOD DRAKE AND WHOO FUTURE CAUSE THATS A YOUTUBE COMMENT I SAW ALSO I LOVE BLOODDD"
if FlexibleInput: inputstr = input('InputStr: ') # Use Custom Input

# Converting String to Binary 
binaryinput = ''.join(format(ord(i), 'b') for i in inputstr) 

#8 Bit Color Matrix
Colors = [
    ('#FFFFFF', '000'), #white
    ('#FF0000', '100'), #red
    ('#00FF00', '110'), #lime (green)
    ('#0000FF', '111'), #blue
    ('#FFFF00', '011'), #yellow
    ('#00FFFF', '001'), #cyan/aqua
    ('#FF00FF', '101'), #magenta/fuschia
    ('#808080', '010')] #gray

output = [] # output list

# Parsing Color To List
split = re.findall('.{1,3}', binaryinput)   # may need to use re.finditer() instead of findall because of stringsize
                                            # has issue where needs exactly 3 on each i think or else will output 000
for z in range(0, len(split)):
    block = split[z]
    for x in range(0,8):
        if block == Colors[x][1]:
            output.append(Colors[x][0])     # at this point there is an exaustive list of colors created to represent the different code peices, but it is not rationalized into small peices

cnt = 0
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
    

    


    

