let fs = require("fs");
let input = require("fs").readFileSync("/dev/stdin");

let star = "";

for (var i = 1; i <= input; i++) {
  for (var j = 0; j < i; j++) {
    star += "*";
  }
  star += "\n";
}
star = star.slice(0, -1);
console.log(star);