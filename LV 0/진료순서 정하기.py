def solution(emergency):
    se = sorted(emergency ,reverse=True)
    return [se.index(i)+1 for i in emergency]