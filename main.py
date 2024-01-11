



def F(INPUT_LIST):
    ResultList=[]
    for Number in INPUT_LIST:
        if Number < 0:
            break
        A = Number * Number
        if Number % 2 == 0 :
            ResultList.append(A)
        else:
            B=1
            for I in range(1,Number+1):
                B = B * I

            ResultList.append(B)
    return ResultList

INPUT_LIST =[3, -2, 4, 1, 5]
RESULT = F(INPUT_LIST)
print(RESULT)