function solution(citations) {
  var answer = 0;

  citations.sort((a, b) => {
    return b - a;
  });

  const n = citations.length;

  for (let i = 0; i < n; i++) {
    if (citations[i] > i) {
      answer++;
    } else break;
  }

  return answer;
}
