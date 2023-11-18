function solution(X) {
  const N = X.length
  
  let total_score = 0
  let tmp_score = 1

  for (let i = 0; i < N; i++) {
    if (i === 0) {
      if (A[i] === 'O') {
        total_score++
        tmp_score++
      }
    } else {
      if (A[i] === 'O') {
        total_score = total_score + tmp_score
        tmp_score++
      } else {
        tmp_score = 1
      }
    }
  }

  return total_score
}

const A = 'OXXOOXXXOOOXO'
console.log(solution(A))