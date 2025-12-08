// https://school.programmers.co.kr/learn/courses/30/lessons/118666

const score = {
  1: 3,
  2: 2,
  3: 1,
  5: 1,
  6: 2,
  7: 3,
};

function solution(survey, choices) {
  let resultObj = { R: 0, T: 0, C: 0, F: 0, J: 0, M: 0, A: 0, N: 0 };
  let answer = "";
  for (let i = 0; i < choices.length; i++) {
    if (choices[i] > 4) {
      resultObj[survey[i][1]] += score[choices[i]];
    } else if (choices[i] < 4) {
      resultObj[survey[i][0]] += score[choices[i]];
    }
  }

  answer += resultObj.R >= resultObj.T ? "R" : "T";
  answer += resultObj.C >= resultObj.F ? "C" : "F";
  answer += resultObj.J >= resultObj.M ? "J" : "M";
  answer += resultObj.A >= resultObj.N ? "A" : "N";

  return answer;
}

const sur = ["AN", "CF", "MJ", "RT", "NA"];
const choices = [5, 3, 2, 7, 5];
const result = "TCMA";

solution(sur, choices);
