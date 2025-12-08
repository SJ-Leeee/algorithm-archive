// https://school.programmers.co.kr/learn/courses/30/lessons/155652

function solution(s, skip, index) {
  let answer = "";
  let alphabat = "abcdefghijklmnopqrstuvwxyz";
  const skipStr = [...skip];
  for (skip of skipStr) {
    alphabat = alphabat.replace(skip, "");
  }

  let sArr = [...s];
  for (let i = 0; i < sArr.length; i++) {
    let beforeIndex = alphabat.indexOf(sArr[i]);
    let afterIndex = beforeIndex + index;
    while (afterIndex >= alphabat.length) {
      afterIndex -= alphabat.length;
    }
    answer += alphabat[afterIndex];
  }

  console.log(answer);
  return answer;
}

solution("aukks", "wbqd", 5);

// 스킵이 10개 인덱스가 20개라고 치자
// 26개 - 10 = 16개 여기서 20개면
// z
