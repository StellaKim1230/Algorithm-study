def hanoi(answer, n, from_hanoi, to_hanoi, middle_hanoi):
    print(n, from_hanoi, to_hanoi, middle_hanoi)
    if n == 1:
        answer.append([from_hanoi, to_hanoi])
        return answer
    
    hanoi(answer, n-1, from_hanoi, middle_hanoi, to_hanoi)
    answer.append([from_hanoi, to_hanoi])

    hanoi(answer, n-1, middle_hanoi, to_hanoi, from_hanoi)

def solution(n):
    answer = [[]]
    hanoi(answer, n, 1, 3, 2)

    del answer[0]
    return answer

solution(3)
