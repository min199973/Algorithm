def solution(hp):
    x = int(hp // 5) 
    y = int((hp-(x*5))//3)
    z = int(hp - 5*x - y*3 // 1)
    return x+y+z