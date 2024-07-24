#import special_functions.py

def add(a, b):
    return a + b 
# 덧셈 기능 구현


def subtract(a, b):
	return a - b
# 뺄셈 기능 구현

def multiply(a, b):
    return a * b
# 곱셈 기능 구현

def divide(a, b):
    if b == 0 :
        print("can't devide to 0!!")
    return a/b

# hotfix 대상 함수
def testPrint(): # a-z까지 출력하는 함수
    print('abcdefghijklmnopqrstuvwxyz')

 

if __name__ == "__main__":
    testPrint()
    a = 10
    b = 20
    print('a + b =', add(a,b))
    print('a - b =', subtract(a,b))
    print('a * b =', multiply(a,b))
    print('a / b =', divide(a,b))
    # print('a ^ b =', pow(a,b))
    # print('|a| =', abs(a,b))
    # print('a % b =', mod(a,b))
    

