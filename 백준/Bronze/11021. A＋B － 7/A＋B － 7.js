let fs = require("fs");
let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

let T = parseInt(input[0]);

for (var i = 1; i <= T; i++) {
  let arr = input[i].split(" ");
  sum = parseInt(arr[0]) + parseInt(arr[1]);
  console.log(`Case #${i}: ${sum}`);
}