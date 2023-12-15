def solution(sides):
    answer = 0
    a = max(sides)
    sides.remove(a)
    answer = sum(sides)
    return 1 if answer>a else 2