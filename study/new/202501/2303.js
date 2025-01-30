const solution = (n, input) => {
  let max = 0;
  let ans = 0;

  for (let i = 0; i < n; i++) {
    let sum = 0;

    for (let a = 0; a < 5; a++) {
      for (let b = a + 1; b < 5; b++) {
        for (let c = b + 1; c < 5; c++) {
          let k = input[i][a] + input[i][b] + input[i][c];
          if (k % 10 > sum) {
            sum = k % 10;
          }
        }
      }
    }

    if (sum >= max) {
      max = sum;
      ans = i + 1;
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
  // input = parseInt(line);
  input.push(line);
  // rl.close();
}).on('close', function () {
  let n = parseInt(input[0]);
  let list = [];
  for (let i = 1; i <= n; i++) {
    list.push(input[i].split(' ').map(el => parseInt(el)));
  }
  solution(n, list);
  process.exit();
});
