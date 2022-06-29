let fs = require("fs");
let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

let T = parseInt(input[0]);

for (var i = 1; i <= T; i++) {
  let arr = input[i].split(" ");
  a = parseInt(arr[0]);
  b = parseInt(arr[1]);
  sum = a + b;
  console.log(`Case #${i}: ${a} + ${b} = ${sum}`);
}