from collections import deque

def solution(begin, target, words):
    convert_deque = deque()
    convert_deque += [begin]
    answer = 0

    visited = [0 for i in words]
    while convert_deque:
        queue = convert_deque.popleft()
        if (queue == target):
            return answer
        
        if target not in words:
            return 0

        for i in range(0, len(words)):
            if len([j for j in range(0, len(words[i])) if words[i][j] != queue[j]]) == 1:
                if len(convert_deque) > 0:
                    convert_deque.popleft()
                if visited[i] != 0:
                    continue
                else:
                    if len(convert_deque) > 0:
                        convert_deque.popleft()
                    visited[i] = 1
                    convert_deque.append(words[i])
        answer +=1
    return answer

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))