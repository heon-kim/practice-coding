let fs = require("fs");
let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

let N = parseInt(input[0]);
let answer = "";

for (var i = 1; i <= N; i++) {
  let arr = input[i].split(" ");
  answer += parseInt(arr[0]) + parseInt(arr[1]) + "\n";
}

console.log(answer);