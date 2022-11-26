let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
input.shift();
let arr = [];
let answer = 0;
let isGroup = true;

for (line of input) {
  arr = [];
  isGroup = true;
  for (let i = 0; i < line.length; i++) {
    if (!arr.includes(line[i])) arr.push(line[i]);
    else {
      if (line[i - 1] != line[i]) isGroup = false;
    }
  }
  if (isGroup == true) answer++;
}

console.log(answer);