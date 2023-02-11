def solution(age):
    li=['a','b','c','d','e','f','g','h','i','j'] #배열로 선언
    a=''    #빈 공간 할당
    for i in str(age):  #str로 해야 나이를 구할 수 있음
         a+= li[int(i)] #  i가 int여야 값 계산이 된다
    return a