let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let result = "";

for (let i = 0; i < input.length - 1; i++) {
  let a = Number(input[i].split(" ")[0]);
  let b = Number(input[i].split(" ")[1]);
  let sum = a + b;

  if (sum === 0) {
    break;
  } else {
    result += sum + "\n";
  }
}

console.log(result.slice(0, -1));