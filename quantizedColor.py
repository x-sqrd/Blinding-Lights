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




def quantize(hexValue):
    rgb = rgb_to_hex
    