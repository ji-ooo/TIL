const solution = () => {
  const n = input;
  const ans = Array(n).fill(1);

  for (let i = 0; i < n; i++) {
    if (i % 2 !== 0) {
      ans[i] = 2;
    }
  }

  if (n % 2 !== 0) {
    ans[n - 1] = 3;
  }

  console.log(ans.join(' '));
};

const fs = require('fs');
const path = './input.txt';
const readline = require('readline');
const rl = readline.createInterface({
  input: fs.createReadStream(path),
  output: process.stdout,
});

let input = [];

rl.on('line', function (line) {
  input = parseInt(line);
  rl.close();
}).on('close', function () {
  solution(input);
  process.exit();
});
