const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  for (let i = 1; i <= input[0]; i++) {
    let total = 0;
    let score = 1;
    for (const result of input[i]) {
      if (result === "X") {
        score = 1;
      } else {
        total += score;
        score++;
      }
    }
    console.log(total);
  }
  process.exit();
});
