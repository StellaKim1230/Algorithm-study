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
  return n - visit.length
}

// [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [3, 4], [3, 6]]

// hashmap
// 1: 2, 3
// 2: 1, 3, 4, 5
// 3: 1, 2, 4, 6
// 4: 2, 3
// 5: 2


// queue
// queue : 2, 3, 1, 3, 4, 5, 1, 2, 4, 6, 2, 3, 2

