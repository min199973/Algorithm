def solution(n, k):
    answer = 12000*n + 2000*k
    sale = 2000*(int(n//10))
    if n>=10:
        return answer-sale
    else:
        return answer
