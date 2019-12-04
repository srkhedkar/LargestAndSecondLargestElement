

def printTopandSecondTop(l1):
    top = l1[0]
    secondTop = l1[0]
    isSecondTopSet = False

    for i in l1:
        if ( i >= top):
            if ( i > top):
                secondTop = top
                top = i
        elif(i > secondTop):
            secondTop = i
        elif(isSecondTopSet == False):
            secondTop = i
            isSecondTopSet = True

    print(top, secondTop)


l1 = [-6,-6,-6,-3,100,100,100,100,1,2,3,4,10,1, 10,10,99]
printTopandSecondTop(l1)

l2 = [10,10,10,9]
printTopandSecondTop(l2)


l3 = [-1,-1,-1,-1,0]
printTopandSecondTop(l3)

            