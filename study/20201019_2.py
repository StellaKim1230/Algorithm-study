def solution(operations):
    answer = []
    heap_list = []

    for oper in operations:
        if oper.find("I") == 0:
            heap_list.append(int(oper.replace('I ', '')))

        if oper.find("D -1") == 0 and len(heap_list) > 0:
            heap_list.remove(min(heap_list))

        if oper.find("D 1") == 0 and len(heap_list) > 0:
            heap_list.remove(max(heap_list))

    if len(heap_list) == 0:
        return [0, 0]

    answer.append(max(heap_list))
    answer.append(min(heap_list))

    return answer

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])