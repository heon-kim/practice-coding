let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

input == "" ? console.log("0") : console.log(input.length);
