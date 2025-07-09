const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const stdin = [];

rl.on('line', (line) => {
  stdin.push(Number(line.trim()));
});

rl.on('close', () => {
  const arr = stdin;
  const choose = [];
  let flag = false;

  function comb(index, level) {
    if (flag) return;

    if (level === 7) {
      const sum = choose.reduce((a, b) => a + b, 0);
      if (sum === 100) {
        choose
          .slice()
          .sort((a, b) => a - b)
          .forEach((item) => console.log(item));
        flag = true;
      }
      return;
    }

    for (let i = index; i < arr.length; i++) {
      choose.push(arr[i]);
      comb(i + 1, level + 1);
      choose.pop();
    }
  }

  comb(0, 0);
});
