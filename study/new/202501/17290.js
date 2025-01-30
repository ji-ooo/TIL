const solution = (n, m, list) => {
  const row = new Array(10).fill(true);
  const col = new Array(10).fill(true);

  for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 10; j++) {
      if (list[i][j] === 'o') {
        row[i] = false;
        col[j] = false;
      }
    }
  }

  let ans = 21;

  for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 10; j++) {
      if (row[i] && col[j]) {
        const dist = Math.abs(n - i) + Math.abs(m - j);
        if (ans > dist) {
          ans = dist;
        }
      }
    }
  }

  console.log(ans);
};

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// const fs = require('fs');
// const path = './input.txt';
// const readline = require('readline');
// const rl = readline.createInterface({
//   input: fs.createReadStream(path),
//   output: process.stdout,
// });

let input = [];

rl.on('line', function (line) {
  input.push(line);
}).on('close', function () {
  let n, m;
  n = parseInt(input[0].split(' ')[0]) - 1;
  m = parseInt(input[0].split(' ')[1]) - 1;
  let list = [];
  for (let i = 1; i <= 10; i++) {
    list.push(input[i].split(''));
  }
  solution(n, m, list);
  process.exit();
});
