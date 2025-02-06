const solution = (A, B, m, nums) => {
  let ans = [];
  let n = 0;
  
  for (let i = 0; i < m; i++) {
    let num = nums[i];
    n += num * (A ** (m - i - 1));
  }
  
  if (n === 0) {
    console.log(0);
    return;
  }
  
  while (n > 0) {
    ans.unshift(n % B);
    n = Math.floor(n / B);
  }
  console.log(ans.join(' '));
};
              
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', function (line) {
  input.push(line);
}).on('close', function () {
  const jin = input[0].split(' ').map(el => parseInt(el));
  const A = jin[0];
  const B = jin[1];
  const m = Number(input[1]);
  const nums = input[2].split(' ').map(el => parseInt(el));
  solution(A, B, m, nums);
  process.exit();
});
