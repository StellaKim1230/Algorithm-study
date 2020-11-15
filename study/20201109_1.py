def solution(routes):
    sortedRoutes = sorted(routes, reverse=True)
    check = [0] * len(routes)
    answer = 0

    for index in range(len(routes)):
        if check[index] == 1:
            continue
        camera = sortedRoutes[index][0]
        answer += 1
        for i in range(index, len(routes)):
            if sortedRoutes[i][0] <= camera and camera <= sortedRoutes[i][1]:
                check[i] = 1
    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))

# [[-5, -3], [-14, -5], [-18, -13], [-20, 15]]
# [0, 0, 0, 0]
# [1, 0, 0, 0]
# [1, 1, 0, 0]
# [1, 1, 0, 1]
# [1, 1, 0, 1] answer = 1
# [1, 1, 1, 1] answer = 2
