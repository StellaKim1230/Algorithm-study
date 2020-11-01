def make_trie(words):
    root = {}
    for word in words:
        current = root
        for letter in word:
            current.setdefault(letter, [0, {}])
            current[letter][0] += 1
            current = current[letter][1]
    return root

def solution(phone_book):
    phone_book.sort()
    trie = make_trie(phone_book)
    current = trie

    for index, phone in enumerate(phone_book[0]):
        if current[phone][0] == 1:
            return True
        current = current[phone][1]
    return False

print(solution(['119', '97674223', '1195524421']))