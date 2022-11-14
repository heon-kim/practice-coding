let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString();
input = input.split("\n");
let sum = 0;
for (let element of input[1]) {
  sum += +element;
}
console.log(sum);