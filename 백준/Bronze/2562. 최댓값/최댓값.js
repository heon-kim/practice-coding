const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let max = Math.max(...input);
  for (let i = 0; i < input.length; i++) {
    if (input[i] == max) {
      console.log(max);
      console.log(i + 1);
    }
  }
  process.exit();
});