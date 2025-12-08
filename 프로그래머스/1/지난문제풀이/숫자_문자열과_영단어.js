// https://school.programmers.co.kr/learn/courses/30/lessons/81301

function solution(s) {
  const dict = {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
  };

  for (const i in dict) {
    s = s.replaceAll(i, dict[i]);
  }
  return Number(s);
}
solution("onetwothreefourfivesix");

// const a = { a: 34 };
// let b = "gaggee";
// console.log(typeof a.a);
// b = b.replace("a", a.a);
// console.log(typeof b);
