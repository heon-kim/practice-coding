var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim();

var year = parseInt(input)-543;
console.log(year);