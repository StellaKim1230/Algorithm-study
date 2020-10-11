from collections import deque

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]



def solution(maps):
    visited = [[0 for col in maps] for row in maps]
    answer = 0
    bfs_queue = deque()
    bfs_queue += [[0,0]]

    while bfs_queue:
        queue = bfs_queue.popleft()
        start = queue[0]
        end = queue[1]

        for n in range(len(maps)):
            for m in range(len(maps[n])):

                if start+1 == len(maps[n]) and end+1 == len(maps): return answer+1

                if end+1 < len(maps) and maps[start][end+1] == 1:
                    if visited[start][end+1] != 0:
                        continue
                    else:
                        visited[start][end+1] = 1
                        bfs_queue.append([start,end+1])
                        answer +=1

                if end+1 == len(maps) and maps[start][end] == 1 and maps[start+1][end] == 0:
                    return -1

                if start+1 < len(maps[n]) and maps[start+1][end] == 1:
                    if visited[start+1][end] != 0:
                        continue
                    else:
                        visited[start+1][end] = 1
                        bfs_queue.append([start+1,end])
                        answer +=1

                if start+1 == len(maps[n]) and maps[start][end] == 1 and maps[start][end+1] == 0:
                    return -1

                if end+1 < len(maps) and maps[start][end+1] == 0 and start+1 < len(maps[n]) and maps[start+1][end] == 0:
                    if maps[start-1][end] == 1:
                        if visited[start-1][end] != 0:
                            continue
                        else:
                            visited[start-1][end] = 1
                            bfs_queue.append([start-1,end])
                            answer +=1
                    else: return -1
    return answer +1

# review
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    bfs_queue = deque([(0, 0, 1)])
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    maps[0][0] = 0
    while bfs_queue:
        y, x, count = bfs_queue.popleft()
        
        if y == n - 1 and x == m - 1:
            return count
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                bfs_queue.append((ny, nx, count + 1))

    return -1