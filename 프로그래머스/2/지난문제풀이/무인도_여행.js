// https://school.programmers.co.kr/learn/courses/30/lessons/154540

// 문제 설명
// 메리는 여름을 맞아 무인도로 여행을 가기 위해 지도를 보고 있습니다.
// 지도에는 바다와 무인도들에 대한 정보가 표시돼 있습니다. 지도는 1 x 1크기의 사각형들로 이루어진 직사각형 격자 형태이며,
// 격자의 각 칸에는 'X' 또는 1에서 9 사이의 자연수가 적혀있습니다. 지도의 'X'는 바다를 나타내며, 숫자는 무인도를 나타냅니다.
// 이때, 상, 하, 좌, 우로 연결되는 땅들은 하나의 무인도를 이룹니다. 지도의 각 칸에 적힌 숫자는 식량을 나타내는데,
// 상, 하, 좌, 우로 연결되는 칸에 적힌 숫자를 모두 합한 값은 해당 무인도에서 최대 며칠동안 머물 수 있는지를 나타냅니다.
// 어떤 섬으로 놀러 갈지 못 정한 메리는 우선 각 섬에서 최대 며칠씩 머물 수 있는지 알아본 후 놀러갈 섬을 결정하려 합니다.

// 지도를 나타내는 문자열 배열 maps가 매개변수로 주어질 때, 각 섬에서 최대 며칠씩 머무를 수 있는지
// 배열에 오름차순으로 담아 return 하는 solution 함수를 완성해주세요.
// 만약 지낼 수 있는 무인도가 없다면 -1을 배열에 담아 return 해주세요.
let island = 0;
let rowLength;
let columnLength;
let visited;
let mapsCopy;

// 변수 공유

function search(y, x) {
  // 재귀함수부분
  if (y + 1 < rowLength && visited[y + 1][x] === false && mapsCopy[y + 1][x] !== "X") {
    //상
    island += parseInt(mapsCopy[y + 1][x]);
    visited[y + 1][x] = true;
    search(y + 1, x);
  }
  if (y - 1 >= 0 && visited[y - 1][x] === false && mapsCopy[y - 1][x] !== "X") {
    //하5
    island += parseInt(mapsCopy[y - 1][x]);
    visited[y - 1][x] = true;
    search(y - 1, x);
  }
  if (x + 1 < columnLength && visited[y][x + 1] === false && mapsCopy[y][x + 1] !== "X") {
    // 좌
    island += parseInt(mapsCopy[y][x + 1]);
    visited[y][x + 1] = true;
    search(y, x + 1);
  }
  if (x - 1 >= 0 && visited[y][x - 1] === false && mapsCopy[y][x - 1] !== "X") {
    // 우
    island += parseInt(mapsCopy[y][x - 1]);
    visited[y][x - 1] = true;
    search(y, x - 1);
  }
}

function solution(maps) {
  const answer = [];

  rowLength = maps.length;
  columnLength = maps[0].length;
  visited = Array.from({ length: rowLength }, () => Array(columnLength).fill(false));
  mapsCopy = maps.map((map) => map.split(""));

  for (let y = 0; y < maps.length; y++) {
    for (let x = 0; x < maps[0].length; x++) {
      if (visited[y][x] === false && mapsCopy[y][x] !== "X") {
        // 방문한적이 없고 X가 아닌경우
        visited[y][x] = true;
        island += parseInt(mapsCopy[y][x]);
        search(y, x);
        answer.push(island);
        island = 0;
      }
    }
  }
  return answer.length === 0 ? [-1] : answer.sort((a, b) => a - b);
}
let maps = ["X591X", "X1X5X", "X231X", "1XXX1"];
console.log(solution(maps));

// maps = ["X591X","X1X5X","X231X", "1XXX1"],	result = [1, 1, 27]
// 첫번째 줄에서 숫자가 있을시 새로운 변수생성
// 만약 합쳐있다면 하나의 변수로
// 다음줄도 같은 인덱스에 X가 아니라면 합치기 아니면 새로 생성하기
