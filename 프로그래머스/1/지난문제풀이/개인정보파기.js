// https://school.programmers.co.kr/learn/courses/30/lessons/150370

function solution(today, terms, privacies) {
  var answer = [];
  const [todayYear, todayMonth, todayDay] = today.split(".").map(Number);

  let promise = {};
  terms.forEach((i) => {
    let [name, deadline] = i.split(" ");
    promise[name] = Number(deadline);
  });

  privacies.forEach((i, idx) => {
    let [deadLine, name] = i.split(" ");
    let [year, month, day] = deadLine.split(".").map(Number);
    month += promise[name];
    if (month >= 12) {
      year++;
      month -= 12;
    }

    if (todayYear > year) {
      answer.push(idx + 1);
    }

    if (todayYear === year) {
      if (todayMonth > month) {
        answer.push(idx + 1);
      }

      if (todayMonth === month) {
        if (todayDay >= day) {
          answer.push(idx + 1);
        }
      }
    }
  });

  return answer;
}

solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]);

// 정답코드

// 1. privacies를 순회하며 비교를 위해 '일자'와 '약관 종류' 분리
// 2. terms를 순회하며 privacies의 '약관 종류'와 terms의 '약관 종류' 매칭
// 3. terms의 '약관 종류'에 따른 개인정보 보관 일자 계산
// 4. 개인정보 보관 일자와 오늘 일자 비교
// 5. 조건에 따른 결론 도출

/*------------------------------------------
*  1 달은 28일
*  month_count = 12월이 넘어가면 year에 + 1
*  Day_count = 28일이 넘어가면 month에 + 1
------------------------------------------*/
function solution(today, terms, privacies) {
  var answer = [];

  // 1)
  // privacies '일자'와 '약관 종류' 분리
  privacies.forEach((e, i) => {
    let privacies_split = e.split(" ");

    // 2)
    // terms를 순회하며 privacies의 약관 종류와 같은 유형 매칭
    terms.forEach((e) => {
      let terms_split = e.split(" ");

      // privacies의 약관 종류와 terms 약관 종류가 같다면
      if (terms_split[0] == privacies_split[1]) {
        // 3)
        // 날짜 계산하기 매개변수 넘기기 (개인정보 수집 일자, 약관 종류에 따른 유효기간)
        let modified_date = dateCalculator(privacies_split[0], terms_split[1]);

        // 4)
        // 보관날짜와 오늘 날짜를 비교
        let modify_compare = new Date(modified_date);
        let today_compare = new Date(today);
        modify_compare.setDate(modify_compare.getDate() + 1); // new Date로 하면 일수가 하루 차이가 난다. 일수 +1 해주기
        today_compare.setDate(today_compare.getDate() + 1); // new Date로 하면 일수가 하루 차이가 난다. 일수 +1 해주기

        // 5)
        // 보관날짜가 개인정보 오늘 날짜를 지났다면 폐기
        if (today_compare > modify_compare) {
          answer.push(i + 1);
        }
      }
    });
  });

  return answer;
}

// 3)
// 일수 계산 함수
function dateCalculator(privacy, term) {
  // (개인정보 수집 일자, 약관 종류에 따른 유효기간)
  let split_privacy;
  let year = 0;
  let month = 0;
  let day = 0;
  let term_day = 28 * term; // 한 달을 28일만 있다고 가정
  let result = "";

  // 개인정보 수집 일자를 각각 분리
  split_privacy = privacy.split(".");

  // 연, 월, 일 각자 저장
  year = Number(split_privacy[0]);
  month = Number(split_privacy[1]);
  day = Number(split_privacy[2]);

  // 유효기간에 따른 일수 더해주기 (28일 초과 시 월+1 / 12월 초과 시 연+1)
  let count = 1;
  while (term_day > count) {
    day += 1;
    if (day == 29) {
      day = 1;
      month += 1;

      if (month > 12) {
        year += 1;
        month = 1;
      }
    }
    count++;
  }

  // MM이 한 자릿수인 경우 앞에 0이 붙습니다. DD가 한 자릿수인 경우 앞에 0이 붙습니다. 조건 생각하기
  year = String(year);
  month = String(month);
  day = String(day);

  if (month.length == 1) {
    month = "0" + month;
  }

  if (day.length == 1) {
    day = "0" + day;
  }

  // 비교를 위해 처음 형태와 똑같이 리턴
  result = year + "." + month + "." + day;

  return result;
}
