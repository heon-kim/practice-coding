const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let scores = input[1].split(" ");
  let sum = 0;

  let maxScore = Math.max(...scores);
  for (const score of scores) {
    sum += (score / maxScore) * 100;
  }
  console.log(sum / input[0]);
  process.exit();
});
