def solution(angle):
    answer = 0
    if 0<angle<90:
         angle= 1
    elif angle == 90:
         angle= 2
    elif 90<angle<180:
         angle= 3
    elif angle == 180:
         angle= 4
    return angle