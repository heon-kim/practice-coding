let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim();
input = input.split(" ");
let num = 0;
const A = input[0];
const B = input[1];
const C = input[2];

num = Math.floor(A / (C - B)) + 1;
C - B > 0 ? console.log(num) : console.log(-1);
