#            |
# SHEBANG - <^> -
#            |

# Utilites
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

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


def quantize(hexValue):
    rgb = rgb_to_hex

    # white

    if abs(rgb[1] - rgb[0]) < 10 and abs(rgb[1] - rgb[3]) < 10 and abs(rgb[1] - rgb[2]) < 10 and rgb[1] > 240:
        return "#FFFFFF"

    # black

    if rgb[0] < 25 and rgb[1] < 25 and rgb[2] <25:
        return '#000000'

    # aqua

    if abs(rgb[1] - rgb[2]) < 30 and rgb[0] > 75 and rgb[2] > 210:
        return '#00FFFF'

    # brightpink

    if abs(rgb[0] - rgb[2]) < 40 and rgb[1] > 75 and rgb[2] > 210:
        return '#FF00FF'

    #yellow

    if abs(rgb[0] - rgb[1]) < 30 and rgb[2] > 75 and rgb[2] > 210:
        return '#FFFF00'

    #lightgrey

    if abs(rgb[1] - rgb[0]) < 10 and abs(rgb[1] - rgb[3]) < 10 and abs(rgb[1] - rgb[2]) < 10 and rgb[1] > 190 and rgb[1] < 240:
        return "#C0C0C0"
