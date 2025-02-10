const solution = (n, m, arr) => {
  let start, end;
  start = 0;
  end = m;

  let ans;
  let now = 0;

  for (let i = start; i < end; i++) {
    now += arr[i];
  }

  ans = now;
  while (end < n) {
    now -= arr[start];
    now += arr[end];
    ans = Math.max(ans, now);
    start++;
    end++;
  }
  console.log(ans);
};

// const readline = require('readline');
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

const fs = require('fs');
const path = './input.txt';
const readline = require('readline');
const rl = readline.createInterface({
  input: fs.createReadStream(path),
  output: process.stdout,
});

let input = [];

rl.on('line', function (line) {
  input.push(line);
}).on('close', function () {
  const nm = input[0].split(' ').map(el => Number(el));
  const n = nm[0];
  const m = nm[1];

  const arr = input[1].split(' ').map(el => Number(el));

  solution(n, m, arr);

  process.exit();
});
