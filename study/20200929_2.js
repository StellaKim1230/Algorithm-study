function solution(n, edge) {
  const queue = [1]

  for (let i = 0; i < edge.length; i++) {
    for (let j = 0; j < edge.length; j++) {
      if (edge[i][0] === 1) {
        queue.push(edge[i][1])
      }

      if (edge[0][j] === 1) {
        queue.push(edge[i][0])
      }
    }
  }

  const visit = [...new Set(queue)]
  return visit.length
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
