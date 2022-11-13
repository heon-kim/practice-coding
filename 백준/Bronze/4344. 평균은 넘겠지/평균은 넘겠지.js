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
    const numberOfScores = testcase[0];
    let sum = 0;
    let count = 0;
    for (let score = 1; score <= numberOfScores; score++) {
      sum += Number(testcase[score]);
    }
    let avg = sum / numberOfScores;
    for (let score = 1; score <= numberOfScores; score++) {
      if (testcase[score] > avg) count++;
    }
    let answer = (count / numberOfScores) * 100;

    console.log(answer.toFixed(3) + "%");
  }
  process.exit();
});
