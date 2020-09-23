// 자물쇠와 열쇠
const key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
const lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

function solution(key, lock) {
  lock[0,0][0] = key[key.length -1, key.length -1][key.length - 1] + lock[0,0][0]
  console.log(lock)
  var answer = true;
  return answer;
}

solution(key, lock)

// lock의 배열중 1이 없을 경우 리턴
