const solution = (n, numbers) => {
  const arr = Array(n).fill(false);

  for (let i = 1; i < n; i++) {
    const num = numbers[i];
    const prev = numbers[i - 1];

    const diff = Math.abs(num - prev);

    if (diff <= 0 || diff >= n) return console.log('Not jolly');
    if (arr[diff]) return console.log('Not jolly');
    arr[diff] = true;
  }

  return console.log('Jolly');
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
  for (let i = 0; i < input.length; i++) {
    const line = input[i].split(' ');
    const n = Number(line[0]);
    const numbers = line.slice(1, n + 1).map(el => parseInt(el));

    solution(n, numbers);
  }
  process.exit();
});
