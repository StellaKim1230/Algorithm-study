from collections import deque


def isMatch(user, bann):
    result = False
    if len(bann.split('*')) - 1 == len(user):
        return True

    if len(user) == len(bann):
        result = False
        count = 0
        for i in range(0, len(user)):
            if user[i] != bann[i] and bann[i] != '*':
                result = False
                break
            if user[i] == bann[i] or bann[i] == '*':
                count += 1
                if count == len(bann):
                    result = True
                    break

    return result


def solution(user_id, banned_id):
    answer = 0

    while len(user_id) >= len(banned_id):
        check = [0] * len(banned_id)

        for i in range(0, len(banned_id)):
            for j in range(0, len(user_id)):

                if isMatch(user_id[j], banned_id[i]):
                    check[i] = 1

                    if check[i] == 1 and i == len(banned_id) - 1:
                        del user_id[0]
                        answer += 1
                        break
                    if check[i] == 1:
                        break

    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
               ["*rodo", "*rodo", "******"]))
