let fs = require("fs");
let input = require("fs").readFileSync("/dev/stdin").toString();

let N = parseInt(input);
for (var i = 1; i < 10; i++) {
  console.log(`${N} * ${i} = ${N * i}`);
}
