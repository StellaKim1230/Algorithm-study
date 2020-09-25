// 자물쇠와 열쇠 (완전탐색)
const key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
const lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

function solution(key, lock) {
  let answer = true;
  const len = lock.length;
  const arr = Array.from(Array(len * 3), () => Array(len * 3).fill(null));
  // const background = initBackground(new Array(lock.length + (key.length -1) * 2), key, lock)

  // return sum(background, key, lock)
}

// function initBackground(background, key, lock) {
//   const start = key.length - 1;
//   const end = lock.length + key.length - 1;
//   const flatLock = lock.flat()
//   let index = 0;

//   for (let i = start; i < end; i ++) {
//     for (let j = start; j < end; j++) {
//       background[i, j] = flatLock[index]
//       index++
//     }
//   }
//   return background
// }

// 오른쪽이동 왼쪽 이동 함수

// 회전하는 함수

// function sum(background, key, lock) {
//   const start = key.length - 1;
//   const end = lock.length + key.length - 1;

//   for(let i = start; i < end; i++ ) {
//     for (let j = start; j < end; j++) {
//       if (background[i, j] === 0) {
//         // return false
//       }
//     }
//   }
// }

solution(key, lock)