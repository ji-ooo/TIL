function solution(players, m, k) {
  var answer = 0;

  const len = players.length;
  let serverCount = 1;
  const returnQueue = [];

  for (let i = 0; i < len; i++) {
    nowPlay = players[i];

    if (returnQueue.length && i == returnQueue[0][0]) {
      const [_, returnCount] = returnQueue.shift();
      serverCount -= returnCount;
    }

    if (serverCount * m <= nowPlay) {
      const target = Math.floor(nowPlay / m) + 1;
      const diff = target - serverCount;

      answer += diff;
      serverCount += diff;

      returnQueue.push([i + k, diff]);
    }
  }

  return answer;
}
