let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString();

let num = parseInt(input);
let sum = 0;
let count = 0;
while (1) {
  sum = Math.floor(num / 10) + (num % 10);
  num = (num % 10) * 10 + (sum % 10);
  count++;
  if (input == num) {
    break;
  }
}

console.log(count);