// https://school.programmers.co.kr/learn/courses/30/lessons/140108

function solution(s) {
  var answer = 0;
  let mainChar;
  let mainCharNum = 0;
  let charNum = 0;
  for (let i = 0; i < s.length; i++) {
    if (mainCharNum === 0) {
      mainChar = s[i];
    } // 초기화 되어있는 상태라면

    mainChar === s[i] ? mainCharNum++ : charNum++;
    // 개수체크

    if (mainCharNum !== 0 && mainCharNum === charNum) {
      // 같아진다면
      answer++;
      mainCharNum = 0;
      charNum = 0;
    }
  }

  if (mainCharNum !== 0) answer++;

  console.log(answer);
  return answer;
}

// 'abcaccad'3
// 'abcaccade'4
let a = "aass";

solution("abracadabra");

// 1. 첫째문자 기억
// 2. 개수들 기억
// 3.
