let fs = require("fs");
let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

let N = parseInt(input[0]);

for (var i = 1; i <= N; i++) {
  let arr = input[i].split(" ");
  console.log(parseInt(arr[0]) + parseInt(arr[1]));
}