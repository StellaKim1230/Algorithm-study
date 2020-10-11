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
                    visited[i] = 1
                    convert_deque.append(words[i])
        answer +=1
    return answer


# review
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    convert_deque = deque([(begin, 0)])
    visited = [False for i in words]
    answer = 0

    while convert_deque:
        word, count = convert_deque.popleft()
        if word == target:
            return count

        for i in range(len(words)):
            is_change = len([j for j in range(len(words[i])) if words[i][j] != word[j]])
            if is_change == 1 and not visited[i]:
                visited[i] = True
                convert_deque.append((words[i], count + 1))
        answer += 1
        
    return answer