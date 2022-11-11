const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let checkArray = Array.from({ length: 30 }, () => 0);

  input.forEach((element) => {
    checkArray[element - 1] = 1;
  });

  let index = 0;
  let count = 0;
  checkArray.forEach((element) => {
    ++index;
    count++;
    if (element === 0) console.log(index);
    if (count === 2) return;
  });
  process.exit();
});