const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let nums = input[1].split(" ");
  console.log(Math.min(...nums), Math.max(...nums));
  process.exit();
});