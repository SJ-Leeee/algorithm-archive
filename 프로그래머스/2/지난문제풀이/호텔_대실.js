// https://school.programmers.co.kr/learn/courses/30/lessons/155651

function solution(book_time) {
  var answer = 0;

  const timeStrToNumber = book_time.map(function (timeArray) {
    return timeArray.map(function (timeString) {
      // 시간과 분을 추출
      const [hours, minutes] = timeString.split(":").map(Number);
      // 시간을 24시간 형식으로 변환하여 숫자로 합치기
      const numericTime = hours * 60 + minutes;
      return numericTime;
    });
  });
  timeStrToNumber.sort((a, b) => a[0] - b[0]);

  console.log(timeStrToNumber);

  let finishTimeArr = [];
  timeStrToNumber.forEach(([start_time, end_time]) => {
    if (Math.min(...finishTimeArr) + 10 > start_time) {
      finishTimeArr.push(end_time);
    } else {
      let minIdx = finishTimeArr.indexOf(Math.min(...finishTimeArr));
      finishTimeArr.splice(minIdx, 1, end_time);
    }
  });

  console.log(finishTimeArr.length);
  return finishTimeArr.length;
}

solution([
  ["10:00", "10:20"],
  ["09:00", "09:20"],
  ["09:20", "09:40"],
  ["09:40", "10:00"],
]);

// 나온시간+10 1420 다음손님의 입실시간 1430
// 만약에 된다 그럼
//

// let finishTimeArr = [];
//   timeStrToNumber.forEach((i) => {
//     finishTimeArr.push(i[1]);
//     // 1920 넣고
//     finishTimeArr.sort((a, b) => a - b);
//     // 정렬하고
//     if (finishTimeArr[0] + 10 <= i[0]) {
//       // 만약 들어갈 수 있다면
//       finishTimeArr.shift();
//       // 앞에 것을 잘라
//     } else {
//       // 아니라면
//       answer++;
//     }
//   });
