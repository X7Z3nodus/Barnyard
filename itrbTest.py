def findMinAndMax(L):
    #if len(L)<0:
    #if L==[]:
    if L:
        min = max = L[0]
        for num in L:
            if num > max:
                max = num
            elif num < min:
                min = num
        return (min, max)
    else:
        return (None, None)

if findMinAndMax([]) != (None, None):
    print('ERROR!')
elif findMinAndMax([7]) != (7, 7):
    print('ERROR!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('ERROR!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('ERROR!')
else:
    print('SUCEESS!')
