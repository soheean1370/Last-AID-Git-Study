def pow(a, b):
    return a**b
#pow 함수 구현

def abs(a):
    if a < 0 :
        return a*(-1)
    else :
        return a
#abs 함수 구현

def mod(a, b):
    if b == 0 :
        print("can't devide to 0!!")
    else :
        return divmod(a, b)
#mod 함수 구현