const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  input = input[0].toUpperCase();
  let obj = {};

  for (let i = 0; i < input.length; i++) {
    if (!obj[input[i]]) obj[input[i]] = 1;
    else obj[input[i]] += 1;
  }

  let max = 0;
  let answer = "";

  for (char in obj) {
    if (obj[char] > max) {
      max = obj[char];
      answer = char;
    } else if (obj[char] === max) {
      answer = "?";
    }
  }
  console.log(answer);
  process.exit();
});
