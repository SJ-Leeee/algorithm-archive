// https://school.programmers.co.kr/learn/courses/30/lessons/42746

function solution(numbers) {
  const numbersToString = numbers.map(String);

  numbersToString.sort((a, b) => {
    if (a[0] < b[0]) return 1;
    // a가 b보다 크다면 1, 3 자리바꿈
    else if (a[0] > b[0]) return -1;
    else {
      // 길이가 같으면 그냥 큰 게 앞으로
      if (a.length === b.length) return b - a;

      let length = a.length > b.length ? a.length : b.length;

      let sameLengthA = a.padEnd(length, a[0]);
      let sameLengthB = b.padEnd(length, b[0]);

      if (sameLengthA === sameLengthB) {
        // 만약 채운수가 같다면
        let originShort = a.length === length ? b : a;

        // 짧은 숫자의 앞뒤를 비교하여 뒤가 크면 길이가 짧은것이 앞으로 오는 것이 맞다
        if (originShort[0] < originShort[originShort.length - 1])
          return a.length - b.length;
        else return b.length - a.length;
      }

      if (sameLengthA > sameLengthB) return -1;
      else return 1;
    }
  });

  let result = numbersToString.join("");
  result = result.replace(/^0+/, "") || "0";
  return result;
}
/// 일단은 내림차순인데
/// 만약에 3과 33이 붙었어
// solution([3, 33, 32, 34, 333, 3555]);
// solution([3, 30, 34, 5, 9]);
// solution([6, 2, 10]);
solution([232, 23]);
solution([212, 21]);
solution([0, 0, 0, 0, 0]);

// const solution = (numbers) =>
//   numbers
//     .sort((a, b) => {
//       const ab = a.toString() + b.toString();
//       const ba = b.toString() + a.toString();
//       if (ab < ba) return -1;
//       if (ba > ab) return 1;
//     })
//     .reverse()
//     .join("");
