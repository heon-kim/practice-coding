const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

const stdin = [];

const input = (() => {
  let i = -1;

  return () => stdin[++i];
})();

rl.on('line', (line) => {
  stdin.push(line.trim());
});

rl.on('close', () => {
  const [a, b] = input().split(' ').map(Number);
  console.log(cds(a, b))
  console.log(css(a, b))

  function cds(a, b){
    let max = Math.min(a, b)
    for (let i = max; i > 0; i--){
      if(a % i == 0 && b % i == 0){
        return i
      }
    }
    return -1
  }

  function css(a, b) {
    let min = Math.max(a, b)
    if(min % a == 0 && min % b == 0){
      return min
    }
    let i = 1;
    while (true) {
      const mutipleMin = min*i
      if(mutipleMin % a == 0 && mutipleMin % b == 0){
        return mutipleMin
      }
      i++
    }
    return -1
  }
})
