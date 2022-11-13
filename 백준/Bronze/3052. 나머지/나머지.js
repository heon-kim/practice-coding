const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let remainders = [];

  for (const n of input) {
    let remainder = n % 42;
    if (!remainders.includes(remainder)) remainders.push(n % 42);
  }

  console.log(remainders.length);
  process.exit();
});
