// https://school.programmers.co.kr/learn/courses/30/lessons/133499
// aya, ye, woo, ma
function solution(babbling) {
  let answer = 0;
  for (let word of babbling) {
    word = word.replaceAll("aya", "1");
    word = word.replaceAll("ye", "2");
    word = word.replaceAll("woo", "3");
    word = word.replaceAll("ma", "4");

    if (Number.isNaN(+word)) continue;
    if (
      word.includes("11") ||
      word.includes("22") ||
      word.includes("33") ||
      word.includes("44")
    )
      continue;

    answer++;
  }
  console.log(answer);
  return answer;
}

console.time();
solution(["aya", "yee", "u", "maa"]);
solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]);
console.timeEnd();

// aya, ye, ma woo 인지 체크하고 커트 그리고 최근단어에 저장

// best
function bestSolution1(babbling) {
  const babblables = ["aya", "ye", "woo", "ma"];

  return babbling.reduce((possible, babbl, index) => {
    for (let i = 0; i < babblables.length; i += 1) {
      if (babbl.includes(babblables[i].repeat(2))) return possible;
    }

    for (let i = 0; i < babblables.length; i += 1) {
      babbl = babbl.split(babblables[i]).join(" ").trim();
    }

    if (babbl) return possible;

    return (possible += 1);
  }, 0);
}

function bestSolution2(babbling) {
  let answer = 0;

  babbling.forEach((word) => {
    word = word.replaceAll("ayaaya", "*");
    word = word.replaceAll("yeye", "*");
    word = word.replaceAll("woowoo", "*");
    word = word.replaceAll("mama", "*");

    word = word.replaceAll("aya", " ");
    word = word.replaceAll("ye", " ");
    word = word.replaceAll("woo", " ");
    word = word.replaceAll("ma", " ");

    if (word.replaceAll(" ", "").length === 0) answer++;
  });

  return answer;
}
