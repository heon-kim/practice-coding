const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let clock = [];

clock = input[0].split(" ");

let curHour = parseInt(clock[0]);
let curMin = parseInt(clock[1]);
let cookTime = parseInt(input[1]);

let sumMin = curMin + cookTime;

let finHour = parseInt(curHour + sumMin / 60);
let finMin = sumMin % 60;

finHour %= 24;

console.log(`${finHour} ${finMin}`);