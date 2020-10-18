def solution(words, queries):
    answer = []
    for query in queries:
        count = 0
        length = len(query)

        if query[0] == "?":
            suffix = query.split("?")
            prefixLen = len(suffix) - 1
            end_check = suffix[prefixLen]

            for word in words:
                if prefixLen == 0 and len(word) == length:
                    count += 1
                elif word.endswith(end_check) and len(word) == length:
                    count += 1
            answer.append(count)
        else:
            prefix = query.split("?")[0]
            for word in words:
                if len(prefix) == 0 and len(word) == length:
                    count += 1
                elif word.startswith(prefix) and len(word) == length:
                    count += 1
            answer.append(count)
    return answer



solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])