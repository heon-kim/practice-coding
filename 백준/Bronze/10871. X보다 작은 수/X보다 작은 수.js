let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let NX = input[0].split(" ");
let N = parseInt(NX[0]);
let X = parseInt(NX[1]);
let A = input[1].split(" ");

let result = "";

for (i = 0; i < N; i++) {
  if (A[i] < X) {
    result = result + A[i] + " ";
  }
}

result.slice(0, -1);

console.log(result);