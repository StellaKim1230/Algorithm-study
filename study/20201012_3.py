def make_trie(words):
    root = {}
    for word in words:
        current = root
        for letter in word:
            current.setdefault(letter, [0, {}])
            current[letter][0] += 1
            print(current[letter])
            current = current[letter][1]
    return root

def solution(words):
    answer = 0
    trie = make_trie(words)
    for word in words:
        cur_Trie = trie
        for i in range(len(word)):
            if cur_Trie[word[i]][0] == 1 :
                break
            cur_Trie = cur_Trie[word[i]][1]
        answer += i+1
    return answer

solution(['word','war','warrior', 'world'])