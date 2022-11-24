let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
let arr = [];
for (num of input) {
  let reversed = 0;
  let pow = 1;
  for (char of num) {
    reversed += char * pow;
    pow *= 10;
  }
  arr.push(reversed);
}

console.log(Math.max(...arr));
