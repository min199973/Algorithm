import math
def solution(balls, share):
    result = math.factorial(balls)//(math.factorial((balls-share)) *math.factorial(share))
    return result
    
 