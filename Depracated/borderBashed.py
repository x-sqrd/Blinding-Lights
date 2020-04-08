# The AYUSH Framework !!!! YAY!

# Shad0w7

def borderBashed(coordinates): #Part of @bashingit
    blacklist = []
    height = len(coordinates)
    width = len(coordinates[0])
    x = 0
    y = 0
    while y < height:
        while x < width:
            if hexIsBlack(coordinates[y][x]):
                blacklist.append((x, y))
            x += 1
        x = 0
        y += 1
    return blacklist

def bashSkew(blacklist):
    output = 0
    vertical = False
    #find corners
    topCorner = blacklist[0] # top corner is first encountered by blacklist which goes by y downwards
    bottomCorner = blacklist[len(blacklist) - 1] # same principle for bottom corner
    # NOTE: if the image is perfect, the entire function will output a slope of -1 which is 45 degrees anyways so the function works no matter what
    if topCorner[0] > bottomCorner[0]:
        x1 = bottomCorner[0]
        y1 = bottomCorner[1]
        x2 = topCorner[0]
        y2 = topCorner[1]
    elif topCorner[0] < bottomCorner[0]:
        x2 = bottomCorner[0]
        y2 = bottomCorner[1]
        x1 = topCorner[0]
        y1 = topCorner[1]
    elif topCorner[0] == bottomCorner[0]:
        vertical = True
    else:
        print('This print message will never print... Odd...')

    if vertical: output = 'Vertical'

    if not vertical: slope = (y2 - y1)/(x2 - x1) #rise/run

    degrees = math.degrees(math.atan(slope))
    # TODO Still have to play with degree's to find out how well it works, and what it represents, however no debugging needed, as reliably will spit out a degree value.
    if slope < 0:
        newdeg = degrees + 45 #this is if it is tilted from the right side
    else:
        newdeg = degrees - 45
    newslope = math.degrees(math.tan(math.radians(newdeg)))
    output = newslope
    return output





    # New Framework!!! Not based at all!!!

    def searchup(initialpoint, coordinates, searchmetric, color="#000000"):
        initialpoint = list(initialpoint)
        if searchmetric == 'y':
            down = initialpoint.copy()
            up = initialpoint.copy()
            while True:
                #go up
                down[1] -= 1
                if coordinates[down[1]][down[0]] == color:
                    point1 = down
                    break
                up[1] += 1
                if coordinates[up[1]][down[0]] == color:
                    point1 = up
                    break

        elif searchmetric == 'x':
            left = initialpoint.copy()
            right = initialpoint.copy()
            while True:
                #go up
                left[0] -= 1
                if coordinates[left[1]][left[0]] == color:
                    point1 = left
                    break
                right[0] += 1
                if coordinates[right[1]][right[0]] == color:
                    point1 = right
                    break
        else:
            print("Error, incorrect searchmetric value! \n  exiting...")
            exit(1)

        return point1


    def borderFindSlope(coordinates, borderPoint=(-1,-1)):
        # assumes nonperfect dataset, and a dataset that is not rotated exactly 45 degrees (slope of two points is either 0 or undefined based on the way you look at it)
        #go down and up
        if borderPoint == [-1, -1]:
            borderPoint = findBorderStart(coordinates)
        point1 = searchup(borderPoint, coordinates, searchmetric="y", color="#000000")
        point2 = searchup(point1, coordinates, searchmetric="x", color="#000000")
        point3 = searchup(point2, coordinates, searchmetric="y", color="#000000")
        point4 = searchup(point3, coordinates, searchmetric="x", color="#000000")

        print(point1, point2, point3, point4)





    def bashFlatten(coordinates, blacklist, corners):
        # Do Later!
        pass
