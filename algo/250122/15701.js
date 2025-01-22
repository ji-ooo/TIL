const solution = input => {
  const n = input;
  let ans = 0;

  for (let i = 1; i <= n ** (1 / 2); i++) {
    if (n % i === 0) {
      if (i * i === n) {
        ans += 1;
        continue;
      }
      ans += 2;
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

let input;

rl.on('line', function (line) {
  input = parseInt(line);
  rl.close();
}).on('close', function () {
  solution(input);
  process.exit();
});
