def check(answer):
    for x, y, pillar_bo in answer:
        if pillar_bo == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                print(x, y, pillar_bo)
                continue
            else:
                return False
        elif pillar_bo == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []

    for bf in build_frame:
        x, y, pillar_bo, add_del = bf
        
        if add_del == 1:
            # 일단 넣고, 조건에 안맞으면 제거
            answer.append([x, y, pillar_bo])
            if not check(answer):
                answer.remove([x, y, pillar_bo])
        else:
            # 일단 제거하고, 조건에 안맞으면 다시 넣기
            answer.remove([x, y, pillar_bo])
            if not check(answer):
                answer.append([x, y, pillar_bo])
    return sorted(answer)
