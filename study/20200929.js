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

// 1. key의 M*M의 마지막 배열의 값을 Lock의 첫번째 값이랑 더한 후 lock의 모든 배열에 1이 있는지 없는지 확인.
