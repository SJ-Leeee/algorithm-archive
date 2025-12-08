function solution(fees, records) {
    const [basicTime, basicFee, addTime, addFee] = [...fees]


    const parkDict = {}

    for (let i = 0; i < records.length; i++) {
        let line = records[i].split(' ')
        let [hour, minute] = line[0].split(':').map((i) => Number(i))
        const time = line[2] === 'OUT' ? hour * 60 + minute : -(hour * 60 + minute)
        // 나갈때는 +
        // 들어올때는 -

        if (parkDict[line[1]]) {
            parkDict[line[1]].time += time
            parkDict[line[1]].out = time > 0 ? true : false
        } else {
            let out = time > 0 ? true : false
            parkDict[line[1]] = { time, out, cost: 0, num: Number(line[1]) }

        }
    }
    let b = Object.values(parkDict).sort((a, b) => a.num - b.num)

    var answer = [];

    b.forEach((i, idx) => {
        if (!i.out) i.time += 1439

        if (i.time - basicTime > 0) {
            i.cost = basicFee + Math.ceil((i.time - basicTime) / addTime) * addFee
        } else {
            i.cost = basicFee
        }
        answer.push(i.cost)
    })
    return answer;
}

// solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
//     "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
// solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"])
solution([1, 461, 1, 10], ["00:00 1234 IN"])