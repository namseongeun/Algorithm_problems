
function solution(Arr) {
  const maxNum = Math.max(...Arr)
  const cntArr = new Array(maxNum + 1)
  cntArr.fill(0)
  
  const answer = new Array()

  for (elem of Arr) {
    cntArr[elem]++
  }

  for (let i = 0; i < maxNum + 1; i++) {
    if (cntArr[i] === 1) {
      answer.push(i)
    }
  }
  return(answer)
}

let A = [1,4,23,5,6]
console.log(solution(A))