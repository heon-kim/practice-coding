let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim();
const croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="];
for (alphabet of croatia) {
  input = input.split(alphabet).join("a");
}
console.log(input.length);
