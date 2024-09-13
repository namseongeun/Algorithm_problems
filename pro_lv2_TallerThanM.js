// 머쓱이 보다 키 큰 사람 찾기
// array는 반 친구들의 키 리스트, height는 머쓱이의 키

function solution(array, height) {
  let answer = 0;
  
  for (let i = 0; i < array.lenth; i++) {
      if (array[i] > height) {
          answer++
      }
  }
  return answer;
}