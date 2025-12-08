// https://school.programmers.co.kr/learn/courses/30/lessons/340213

// video_len	pos	op_start	op_end	commands	result
// "34:33"	"13:00"	"00:55"	"02:55"	["next", "prev"]	"13:00"
// "10:55"	"00:05"	"00:15"	"06:55"	["prev", "next", "next"]	"06:55"
// "07:22"	"04:05"	"00:15"	"04:07"	["next"]	"04:17"

function solution(video_len, pos, op_start, op_end, commands) {
  // pos 를 현재시간에 넣는다.
  // 비디오 길이, pos, op start, op end를 초로 바꾼다.
  // 작업을 실행하고 현재위치가 op_start end 사이에 있다면 op_end로 이동한다.
  // 만약 pos가 음수가 나오면 0 op_end보다 크면 op_end를 할당한다.

  video_len = timeStringToSecond(video_len);
  pos = timeStringToSecond(pos);
  op_start = timeStringToSecond(op_start);
  op_end = timeStringToSecond(op_end);

  if (pos >= op_start && pos <= op_end) pos = op_end;
  for (let command of commands) {
    if (command === "prev") {
      pos -= 10;
    } else if (command === "next") {
      pos += 10;
    }

    if (pos < 0) pos = 0;
    if (pos > video_len) pos = video_len;
    if (pos >= op_start && pos <= op_end) pos = op_end;

    console.log(pos);
  }
  let minute = String(Math.floor(pos / 60));
  let second = String(pos % 60);

  if (minute.length === 1) minute = "0" + minute;
  if (second.length === 1) second = "0" + second;

  return minute + ":" + second;
}

function timeStringToSecond(str) {
  let result;
  str = str.split(":");
  result = +str[0] * 60 + +str[1];
  return result;
}
console.time();
console.log(solution("34:33", "00:32", "00:55", "02:55", ["next"]));
console.timeEnd();
