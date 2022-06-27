const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");

const a = parseInt(input[0]);
const b = parseInt(input[1]);
const c = parseInt(input[2]);
let result = 0;

if (a == b && a == c && b == c) {
  result = 10000 + a * 1000;
} else if (a != b && a != c && b != c) {
  result = Math.max(a, b, c) * 100;
} else {
  if (a == b) {
    result = 1000 + a * 100;
  } else if (a == c) {
    result = 1000 + a * 100;
  } else {
    result = 1000 + b * 100;
  }
}

console.log(result);