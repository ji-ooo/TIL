const solution = (n, nums) => {
  nums.sort((a, b) => {
    return b - a;
  });

  let ans = 0;
  for (let i = 0; i < n; i++) {
    if (nums[i] > i) {
      ans++;
    } else break;
  }

  console.log(ans);
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
  input.push(line);
}).on('close', function () {
  const n = Number(input[0]);
  const numbers = input[1].split(' ').map(el => parseInt(el));

  solution(n, numbers);

  process.exit();
});
