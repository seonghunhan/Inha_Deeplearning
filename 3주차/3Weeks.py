import numpy as np

def AND (x1, x2) : # AND 연산자 함수
    x= np.array([x1, x2])
    w = np.array([10, 10])
    b = -15

    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else :
        return 1

def OR(x1, x2) : # OR 연산자 함수
    x = np.array([x1,x2])
    w = np.array([9, 9])
    b = -4

    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1,x2) : # NAND 연산자 함수
    x = np.array([x1,x2])
    w = np.array([-8, -8])
    b = 10

    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else :
        return 1

def NAND_OR(x1, x2) : # NAND연산자를 이용하여 OR연산자 구현함수
    NAND1 = (NAND(x1,x1))
    NAND2 = (NAND(x2,x2))

    result = NAND(NAND1, NAND2)

    return result 



print("OR")
print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))
print("-------------------------------")
print("AND연산자")
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))
print("-------------------------------")
print("NAND연산자")
print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))
print("-------------------------------")
print("2번과제")
print(NAND_OR(0,0))
print(NAND_OR(0,1))
print(NAND_OR(1,0))
print(NAND_OR(1,1))
print("-------------------------------")