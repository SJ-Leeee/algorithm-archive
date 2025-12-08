// https://school.programmers.co.kr/learn/courses/30/lessons/172928

function solution(park, routes) {
  const N = park.length;
  const M = park[0].length;

  // 시작 좌표 설정
  let start;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (park[i][j] == "S") start = [i, j];
    }
  }
  // 방향 객체
  const directions = {
    E: [0, 1],
    W: [0, -1],
    S: [1, 0],
    N: [-1, 0],
  };
  // 주어진 이동정보 배열에 담기
  for (const route of routes) {
    const [dir, distanceStr] = route.split(" ");
    let distance = parseInt(distanceStr);
    let [nx, ny] = start;
    // 주어진 걸음수 만큼 한칸씩 이동
    let step = 0;
    while (step < distance) {
      nx += directions[dir][0];
      ny += directions[dir][1];
      // 만약 밖에 나가게 되거나 X를 만나게 된다면 종료
      if (nx < 0 || N <= nx || ny < 0 || M <= ny || park[nx][ny] === "X") break;
      step++;
    }
    // 원하는 걸음수를 채우면 start는 마지막 위치로 바꿈
    if (step === distance) start = [nx, ny];
  }

  return start;
}

console.log(solution(["SOO", "OOO", "OOO"], ["E 1", "E 1"]));
// for (let i = 0; i < routes.length; i++) {
//   let [direct, distance] = routes[i].split(" ");
//   // 방향 거리
//   let row = location[0];
//   // 현재 행
//   let column = location[1];
//   // 현재 열

//   if (direct === "E" && park[row][column + +distance]) {
//     if (!park[row].slice(column, column + +distance + 1).includes("X")) {
//       location = [row, column + +distance];
//     }
//   } else if (direct === "W" && park[row][column - +distance]) {
//     if (!park[row].slice(column - +distance, column).includes("X")) {
//       location = [row, column - +distance];
//     }
//   } else if (direct === "S" && park[row + +distance]) {
//   } else if (direct === "N" && park[row - +distance]) {
//     for (let i = row - +distance; i <= row; i++) {
//       if (park[i][column] === "X") break;

//       if (i === row) location = [row - distance, column];
//     }
//   }
// }

const directions = {
  E: [0, 1],
  W: [0, -1],
  S: [1, 0],
  N: [-1, 0],
};

console.log(directions["E"][0], directions["E"][1]);
