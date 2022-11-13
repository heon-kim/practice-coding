const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  for (let line = 1; line <= input[0]; line++) {
    const testcase = input[line].split(" ");
    const numberOfScores = testcase.shift();
    const sum = testcase.reduce((a, b) => +a + +b);
    const avg = sum / numberOfScores;
    const count = testcase.filter((score) => score > avg).length;
    const answer = (count / numberOfScores) * 100;
    console.log(answer.toFixed(3) + "%");
  }
  process.exit();
});
