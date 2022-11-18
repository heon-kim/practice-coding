const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  input.shift();
  for (const item of input) {
    let str = "";
    const testcase = item.split(" ");
    for (let char of testcase[1]) {
      for (let i = 0; i < testcase[0]; i++) {
        str += char;
      }
    }
    console.log(str);
  }
  process.exit();
});
