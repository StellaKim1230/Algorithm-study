// 자물쇠와 열쇠 (완전탐색)
const key = [
  [0, 0, 0],
  [1, 0, 0],
  [0, 1, 1],
]
const lock = [
  [1, 1, 1],
  [1, 1, 0],
  [1, 0, 1],
]

function rotation(key) {
  const length = key.length
  const rotationKey = Array.from(Array(length), () => Array(length).fill(null))

  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length; j++) {
      rotationKey[i][j] = key[length - j - 1][i]
    }
  }

  return rotationKey
}

function isAnswer(newLock, length) {
  for (let i = length; i < length * 2; i++) {
    for (let j = length; j < length * 2; j++) {
      if (newLock[i][j] !== 1) return false
    }
  }

  return true
}

function solution(key, lock) {
  let newKey = key
  const length = lock.length

  // 백그라운드 배열 초기 null로 세팅
  const background = Array.from(Array(length * 3), () =>
    Array(length * 3).fill(null),
  )
  // 백그라운드 가운데에 lock 세팅
  for (let i = length; i < length * 2; i++) {
    for (let j = length; j < length * 2; j++) {
      background[i][j] = lock[i - length][j - length]
    }
  }

  for (let i = 0; i < 4; i++) {
    newKey = rotation(newKey)

    // key를 background 길이에서 한칸식 이동하면서 answer 인지 판단
    // 오른쪽으로 한칸씩 이동이 끝나면 아래로 한칸 이동
    for (let j = 0; j <= background.length - newKey.length; j++) {
      // 오른쪽으로 한칸씩 이동
      for (let k = 0; k <= background.length - newKey.length; k++) {
        let newLock = background.map(function (b) {
          return b.slice()
        })
        for (let m = 0; m < newKey.length; m++) {
          for (let n = 0; n < newKey.length; n++) {
            if (newLock[j + m][k + n] === 1 && newKey[m][n] === 1) {
              newLock[j + m][k + n] = 2
            } else if (newLock[j + m][k + n] === 1 && newKey[m][n] === 0) {
              newLock[j + m][k + n] = 1
            } else {
              newLock[j + m][k + n] = newKey[m][n]
            }
          }
        }
        if (isAnswer(newLock, length)) {
          return true
        }
      }
    }
  }
  return false
}

console.log(solution(key, lock))
