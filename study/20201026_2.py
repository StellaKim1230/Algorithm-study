input = '7 4 '+'\n'+'0 7 1 7 6 7 6 '+'\n'+'4 1 9 7'
list = input.split()
A = list[2 : int(list[0]) + 2]
B = list[2 + int(list[0]) : len(list)]

def move(A, B):
    N, M = len(A) - 1, len(B) - 1

    row, col = 0, 0
    total = 0

    while row != N or col != M:
        print(row, col, A[row], B[col])
        total += int(A[row]) * 1000000000 + int(B[col])

        if row < N:
            row += 1
        elif col < M:
            col += 1

    print(row, col, A[row], B[col])
    total += int(A[row]) * 1000000000 + int(B[col])
    print(total)

move(A,B)