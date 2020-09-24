// 자물쇠와 열쇠 (완전탐색)
const key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
const lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

function solution(key, lock) {
  const background = new Array(lock.length + (key.length -1) * 2)
  // 처음 lock 위치
  background[key.length -1, key.length -1] = lock[0,0]

  // 처음 background에 lock 세팅
  initBackground(background, key, lock)

  return sum(background, key, lock)
  // var answer = true;
  // return answer;
}

function initBackground(background, key, lock) {
  const start = key.length - 1;
  const end = lock.length + key.length - 1;
  const flatLock = lock.flat()
  let index = 0;

  for (let i = start; i < end; i ++) {
    for (let j = start; j < end; j++) {
      console.log('i, j', i, j)
      background[i, j] = flatLock[index]
      index++
    }
  }
}

// 오른쪽이동 왼쪽 이동 함수

// 90도 4번 회전 함수

function sum(background, key, lock) {
  const start = key.length - 1;
  const end = lock.length + key.length - 1;

  for(let i = start; i < end; i++ ) {
    for (let j = start; j < end; j++) {
      if (background[i, j] === 0) {
        // return false
      }
    }
  }
}
console.log(solution(key, lock))
// lock의 배열중 1이 없을 경우 리턴
// 1. key의 M*M의 마지막 배열의 값을 Lock의 첫번째 값이랑 더한 후 lock의 모든 배열에 1이 있는지 없는지 확인