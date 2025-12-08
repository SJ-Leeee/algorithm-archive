//https://school.programmers.co.kr/learn/courses/30/lessons/42577

function solution(phone_book) {
  console.log(phone_book);
  let arr = [...phone_book];
  console.log(arr);
  arr = arr.sort();
  console.log(arr);
  for (let i = 0; i < phone_book.length - 1; i++) {
    for (let y = i + 1; y < phone_book.length; y++) {
      if (phone_book[i].length >= phone_book[y].length) {
        if (phone_book[i].startsWith(phone_book[y])) {
          return false;
        }
      } else {
        if (phone_book[y].startsWith(phone_book[i])) {
          return false;
        }
      }
    }
  }
  return true;
}
// 1번은 복잡도에서 탈락

// 정답

function solution(phone_book) {
  let answer = true;
  let arr = [...phone_book];

  arr = arr.sort();

  for (let i = 0; i < arr.length - 1; i++) {
    let nextString = arr[i + 1].substr(0, arr[i].length);
    if (arr[i] === nextString) {
      return false;
    }
  }

  return answer;
}

console.log(solution(["119", "97674223", "1195524421"]));
// ["119", "97674223", "1195524421"]	false
