// 자물쇠와 열쇠 (완전탐색)
const key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
const lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
function solution(key, lock) {
  const background = new Array(lock.length + (key.length -1) * 2)
  // 처음 lock 위치
  background[key.length -1, key.length -1] = lock[0,0][0]
  // lock[0,0][0] = key[key.length -1, key.length -1][key.length - 1] + lock[0,0][0]
  sum(background, key, lock)
  var answer = true;
  return answer;
}
function sum(background, key, lock) {
  const start = key.length - 1;
  const end = lock.length + key.length - 1;
  for(let i = start; i < end; i++ ) {
    for (let j = start; j < end; j++) {
      if (background[i, j] === 0) return false
      return true
    }
  }
}
solution(key, lock)
// lock의 배열중 1이 없을 경우 리턴
// 1. key의 M*M의 마지막 배열의 값을 Lock의 첫번째 값이랑 더한 후 lock의 모든 배열에 1이 있는지 없는지 확인