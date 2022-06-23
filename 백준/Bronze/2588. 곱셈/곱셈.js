var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split("\n");

const a = parseInt(input[0]);
const b = input[1];

const c = parseInt(b[2]);
const d = parseInt(b[1]);
const e = parseInt(b[0]);

console.log(a*c);
console.log(a*d);
console.log(a*e);
console.log(a*c+(a*d*10)+(a*e*100))
