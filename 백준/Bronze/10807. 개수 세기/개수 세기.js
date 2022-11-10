const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let N = input[0];
  let nums = input[1].split(" ");
  let v = input[2];

  let count = 0;

  for (let i = 0; i < N; i++) {
    if (nums[i] == v) count++;
  }

  console.log(count);
  process.exit();
});