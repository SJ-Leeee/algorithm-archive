// https://school.programmers.co.kr/learn/courses/30/lessons/159994

function solution(cards1, cards2, goal) {
  for (let i = 0; i < goal.length; i++) {
    let temp = goal[i];
    if (temp === cards1[0]) cards1.shift();
    else if (temp === cards2[0]) cards2.shift();
    else return "No";
  }

  return "Yes";
}

// 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.
// 한 번 사용한 카드는 다시 사용할 수 없습니다.
// 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.
// 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.

solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]);
// if (goal[0] === cards1[0]) {
//     // 카드1과 같다면
//     for (let i = 0; i < goal.length; i++) {
//       // 짝수일때는
//       if (i % 2 == 0) {
//         // i가 짝수일 때
//         if (cards1.shift() !== goal[i]) return "No";
//       } else {
//         // i가 홀수일 때
//         if (cards2.shift() !== goal[i]) return "No";
//       }
//     }
//   } else if (goal[0] === cards2[0]) {
//     for (let i = 0; i < goal.length; i++) {
//       if (i % 2 == 0) {
//         // i가 짝수일 때
//         if (cards2.shift() !== goal[i]) return "No";
//       } else {
//         // i가 홀수일 때
//         if (cards1.shift() !== goal[i]) return "No";
//       }
//     }
//   } else {
//     return "No";
//   }
