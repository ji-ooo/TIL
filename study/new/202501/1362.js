const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on('line', function (line) {
  input.push(line);
}).on('close', function () {
  let index = 0;
  let scenario = 1;

  while (index < input.length) {
    let [o, w] = input[index].split(' ').map(Number);
    if (o === 0 && w === 0) break;
    index++;
    let isDead = false;

    while (index < input.length) {
      let [action, value] = input[index].split(' ');
      let n = Number(value);
      if (action === '#' && n === 0) break;

      if (!isDead) {
        if (action === 'F') {
          w += n;
        } else if (action === 'E') {
          w -= n;
        }
      }

      if (w <= 0) isDead = true;
      index++;
    }

    if (w <= 0) {
      console.log(`${scenario} RIP`);
    } else if (w > o / 2 && w < o * 2) {
      console.log(`${scenario} :-)`);
    } else {
      console.log(`${scenario} :-(`);
    }
    scenario++;
    index++;
  }
  process.exit();
});
