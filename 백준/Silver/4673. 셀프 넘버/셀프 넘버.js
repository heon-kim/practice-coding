let sum = 0;
let arr = Array(10000).fill(0);

function d(n) {
  const strN = n.toString();
  sum = n;
  for (let i = 0; i < strN.length; i++) {
    sum += parseInt(strN[i]);
  }
  arr[sum] = 1;
}

for (let j = 0; j < 10000; j++) {
  d(j);
}

for (let k = 0; k < 10000; k++) {
  if (arr[k] === 0) console.log(k);
}