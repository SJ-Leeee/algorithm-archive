// https://school.programmers.co.kr/learn/courses/30/lessons/64061

function recur(stack) {
  let result = 0;
  console.log(stack);
  for (let i = 0; i < stack.length; i++) {
    if (stack[i] === stack[i + 1]) {
      stack.splice(i, 2);
      result = result + 2;
      result = result + recur(stack);
    }
  }

  return result;
}

function solution(board, moves) {
  // 만약 moves가 1이라면 각 0번째 인덱스 순회
  let stack = [];
  for (let i = 0; i < moves.length; i++) {
    let line = moves[i] - 1;
    for (let j = 0; j < board.length; j++) {
      if (board[j][line] !== 0) {
        stack.push(board[j][line]);
        board[j][line] = 0;
        break;
      }
    }
  }

  return recur(stack);
}

// [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4
// solution(
//   [
//     [0, 0, 0, 0, 0],
//     [0, 0, 1, 0, 3],
//     [0, 2, 5, 0, 1],
//     [4, 2, 4, 4, 2],
//     [3, 5, 1, 3, 1],
//   ],
//   [1, 5, 3, 5, 1, 2, 1, 4]
// );

recur([4, 3, 1, 1, 3, 2, 4]);
