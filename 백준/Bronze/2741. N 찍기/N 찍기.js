let fs = require("fs");
let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

let N = parseInt(input[0]);
let answer = "";

for (var i = 1; i <= N; i++) {
  answer += i + "\n";
}

console.log(answer);