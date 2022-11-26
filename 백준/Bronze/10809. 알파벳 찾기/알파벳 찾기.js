let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim();
input = input.split("");
let alphabet = [
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
];

var answer = [...alphabet].fill(-1);
alphabet.forEach((el, index) => {
  answer[index] = input.findIndex((element) => element === el);
});

console.log(answer.join(" "));
