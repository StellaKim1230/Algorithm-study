// 문자열 압축
function solution(s) {
  let answer = s.length
  for (let compareCount = 1; compareCount <= s.length / 2; compareCount++) {
    let count = 1
    let prev = ''
    var compress = ''

    for (let j = 0; j < s.length / compareCount; j++) {
      var current = s.substring(
        compareCount * j,
        compareCount * j + compareCount,
      )

      if (prev === current) {
        count++
        continue
      }

      if (count > 1) {
        compress += count.toString() + prev
      } else {
        compress += prev
      }

      prev = current
      count = 1
    }

    if (count > 1) {
      compress += count.toString() + prev
    } else {
      compress += prev
    }

    answer = Math.min(compress.length, answer)
  }
  return answer
}

// 정수삼각형 (다이나믹 프로그래밍) : 이전결과를 토대로 현재값 구하기 : n2
// 보석쇼핑 (특정 범위 내에서 뭔가를 골라야 할때) : 2 pointer 알고리즘 100,000 -> nlogn, O(n) : 결론 ㅒ(ㅜ)
// - 부분 집합을 구해야하는데 순차적일때 사용한다.
// - 포인터 : 두개의 선택자
// - 구간의 합 : 해시테이블로 구현