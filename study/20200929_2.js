function solution(n, edge) {
  const arr = Array.from(Array(n + 1).fill([]))
  const queue = [[1, 0]]
  const visit = new Set()
}

console.log(
  solution(6, [
    [3, 6],
    [4, 3],
    [3, 2],
    [1, 3],
    [1, 2],
    [2, 4],
    [5, 2],
  ]),
)
