def solution(n, times):
    left = 1 
    right = n * max(times)
    answer = 0

    while left <= right:
        people = 0
        mid = (left + right ) // 2

        for time in times:
            people += mid // time
            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid - 1

        elif people < n:
            left = mid + 1
    return answer

print(solution(6, [7, 10]))